# -*- coding: utf-8 -*-from glr import GLRParser
dictionaries = { u"CLOTHES": [u"", u"", u""]}
grammar = u"""    S = adj<agr-gnc=1> CLOTHES"""
glr = GLRParser(grammar, dictionaries=dictionaries, debug=False)
text = u" "for parsed in glr.parse(text): print "FOUND:", parsed