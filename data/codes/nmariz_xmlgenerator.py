#!/usr/bin/env python# -*- coding: utf-8 -*-
__author__ = 'Nuno Mariz'__url__ = 'http://mariz.org'__license__ = 'BSD'
import codecs
from datetime import datetime, date, timefrom decimal import Decimalfrom types import NoneTypefrom xml.sax.saxutils import escape

class Xml(object): """    XML generator class    Usage: >>> root = Element('root') >>> xml = Xml(root)  # root is a root <Element> object >>> xml.render()    u'<?xml version="1.0" encoding="utf-8"?>\\n<root />'    Writing contents to a file or a writer: >>> import cStringIO >>> output = cStringIO.StringIO() >>> xml = Xml(root)  # root is a root <Element> object >>> xml.render(output) """
    encoding = 'utf-8'
 def __init__(self, element): self._element = element
 def __repr__(self): return '<Xml: "Element: {0}">'.format(str(self._element))
 def __unicode__(self): return (u'<?xml version="1.0" encoding="{0}"?>\n{1}' u''.format(Xml.encoding, self._element.render()))
 @staticmethod def set_encoding(encoding):        Xml.encoding = encoding
 def render(self, writer=None): if writer is None: return unicode(self)        writer.write(unicode(self))
 def write(self, filename):        writer = codecs.open(filename, 'w', Xml.encoding) self.render(writer)        writer.close()

class Element(object): """    Element element class    Usage:    Element creation: >>> root = Element('root') >>> records = Element('blog', 'http://mariz.org', \        dict(author='Nuno Mariz', title='Nuno Mariz Weblog'))    Append a child element: >>> root.append(records)    or inline: >>> root.append_as_element('blog', 'http://mariz.org', \        dict(author='Nuno Mariz', title='Nuno Mariz Weblog')) """
 def __init__(self, name, contents=None, attributes=None, cdata=False): self._name = name self._contents = contents self._attributes = attributes or dict() self._cdata = cdata self._elements = []
 def __repr__(self): return '<Element: "%s">' % self._name
 def __str__(self): return self._name
 def __unicode__(self):        attributes = u''.join([' {0}="{1}"'.format(key, Element.escape(value)) for key, value in self._attributes.items()])        contents = None if self._contents is not None:            contents = Element.escape(self._contents, self._cdata) elif self._elements:            contents = u''.join(                [unicode(element) for element in self._elements]            ) if contents is not None: return u'<{0}{1}>{2}</{3}>'.format(self._name, attributes,                                               contents, self._name) return u'<{0}{1} />'.format(self._name, attributes)
 def __len__(self): return len(self._elements)
 def __getitem__(self, key): return self._attributes.get(key)
 def __setitem__(self, key, value): self._attributes[key] = value
 def __delitem__(self, key): del self._attributes[key]
 @property def elements(self): return self._elements
 @property def contents(self): return self._contents
 @property def has_contents(self): return self._contents is None
 @property def has_elements(self): return bool(self._elements)
 @property def is_cdata(self): return self._cdata
 @staticmethod def escape(value, cdata=False): if isinstance(value, NoneType): return u'' if isinstance(value, (bool, int, long, datetime, date, time, float,                              Decimal)): return value if cdata:            value = u'<![CDATA[%s]]>' % value else:            value = escape(value) if isinstance(value, basestring): if not isinstance(value, unicode):                value = unicode(value, Xml.encoding) return value
 def append(self, element): assert isinstance(element, Element), \ '"element" is not a Element instance' self._elements.append(element)
 def append_as_element(self, *args, **kargs): self._elements.append(Element(*args, **kargs))
 def render(self): return unicode(self)

class Node(Element): """    Element class clone for back compatibility """
 @property def nodes(self): return self._elements
 @property def has_nodes(self): return bool(self._elements)
 def append_as_node(self, *args, **kargs): self._elements.append(Node(*args, **kargs))

if __name__ == "__main__": import doctest    doctest.testmod()