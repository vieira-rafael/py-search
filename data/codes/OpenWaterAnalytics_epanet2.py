'''Wrapper for epanet2.hGenerated with:/home/mau/ctypesgen-0.r125/ctypesgen.py epanet2.h -lepanet2 -o epanet2.pyDo not modify this file.'''
__docformat__ = 'restructuredtext'
# Begin preamble
import ctypes, os, sysfrom ctypes import *
_int_types = (c_int16, c_int32)if hasattr(ctypes, 'c_int64'): # Some builds of ctypes apparently do not have c_int64 # defined; it's a pretty good bet that these builds do not # have 64-bit pointers.    _int_types += (c_int64,)for t in _int_types: if sizeof(t) == sizeof(c_size_t):        c_ptrdiff_t = tdel tdel _int_types
class c_void(Structure): # c_void_p is a buggy return type, converting to int, so # POINTER(None) == c_void_p is actually written as # POINTER(c_void), so it can be treated as a real pointer.    _fields_ = [('dummy', c_int)]
def POINTER(obj):    p = ctypes.POINTER(obj)
 # Convert None to a real NULL pointer to work around bugs # in how ctypes handles None on 64-bit platforms if not isinstance(p.from_param, classmethod): def from_param(cls, x): if x is None: return cls() else: return x        p.from_param = classmethod(from_param)
 return p
class UserString: def __init__(self, seq): if isinstance(seq, basestring): self.data = seq elif isinstance(seq, UserString): self.data = seq.data[:] else: self.data = str(seq) def __str__(self): return str(self.data) def __repr__(self): return repr(self.data) def __int__(self): return int(self.data) def __long__(self): return long(self.data) def __float__(self): return float(self.data) def __complex__(self): return complex(self.data) def __hash__(self): return hash(self.data)
 def __cmp__(self, string): if isinstance(string, UserString): return cmp(self.data, string.data) else: return cmp(self.data, string) def __contains__(self, char): return char in self.data
 def __len__(self): return len(self.data) def __getitem__(self, index): return self.__class__(self.data[index]) def __getslice__(self, start, end):        start = max(start, 0); end = max(end, 0) return self.__class__(self.data[start:end])
 def __add__(self, other): if isinstance(other, UserString): return self.__class__(self.data + other.data) elif isinstance(other, basestring): return self.__class__(self.data + other) else: return self.__class__(self.data + str(other)) def __radd__(self, other): if isinstance(other, basestring): return self.__class__(other + self.data) else: return self.__class__(str(other) + self.data) def __mul__(self, n): return self.__class__(self.data*n) __rmul__ = __mul__ def __mod__(self, args): return self.__class__(self.data % args)
 # the following methods are defined in alphabetical order: def capitalize(self): return self.__class__(self.data.capitalize()) def center(self, width, *args): return self.__class__(self.data.center(width, *args)) def count(self, sub, start=0, end=sys.maxint): return self.data.count(sub, start, end) def decode(self, encoding=None, errors=None): # XXX improve this? if encoding: if errors: return self.__class__(self.data.decode(encoding, errors)) else: return self.__class__(self.data.decode(encoding)) else: return self.__class__(self.data.decode()) def encode(self, encoding=None, errors=None): # XXX improve this? if encoding: if errors: return self.__class__(self.data.encode(encoding, errors)) else: return self.__class__(self.data.encode(encoding)) else: return self.__class__(self.data.encode()) def endswith(self, suffix, start=0, end=sys.maxint): return self.data.endswith(suffix, start, end) def expandtabs(self, tabsize=8): return self.__class__(self.data.expandtabs(tabsize)) def find(self, sub, start=0, end=sys.maxint): return self.data.find(sub, start, end) def index(self, sub, start=0, end=sys.maxint): return self.data.index(sub, start, end) def isalpha(self): return self.data.isalpha() def isalnum(self): return self.data.isalnum() def isdecimal(self): return self.data.isdecimal() def isdigit(self): return self.data.isdigit() def islower(self): return self.data.islower() def isnumeric(self): return self.data.isnumeric() def isspace(self): return self.data.isspace() def istitle(self): return self.data.istitle() def isupper(self): return self.data.isupper() def join(self, seq): return self.data.join(seq) def ljust(self, width, *args): return self.__class__(self.data.ljust(width, *args)) def lower(self): return self.__class__(self.data.lower()) def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars)) def partition(self, sep): return self.data.partition(sep) def replace(self, old, new, maxsplit=-1): return self.__class__(self.data.replace(old, new, maxsplit)) def rfind(self, sub, start=0, end=sys.maxint): return self.data.rfind(sub, start, end) def rindex(self, sub, start=0, end=sys.maxint): return self.data.rindex(sub, start, end) def rjust(self, width, *args): return self.__class__(self.data.rjust(width, *args)) def rpartition(self, sep): return self.data.rpartition(sep) def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars)) def split(self, sep=None, maxsplit=-1): return self.data.split(sep, maxsplit) def rsplit(self, sep=None, maxsplit=-1): return self.data.rsplit(sep, maxsplit) def splitlines(self, keepends=0): return self.data.splitlines(keepends) def startswith(self, prefix, start=0, end=sys.maxint): return self.data.startswith(prefix, start, end) def strip(self, chars=None): return self.__class__(self.data.strip(chars)) def swapcase(self): return self.__class__(self.data.swapcase()) def title(self): return self.__class__(self.data.title()) def translate(self, *args): return self.__class__(self.data.translate(*args)) def upper(self): return self.__class__(self.data.upper()) def zfill(self, width): return self.__class__(self.data.zfill(width))
class MutableString(UserString): """mutable string objects    Python strings are immutable objects.  This has the advantage, that    strings may be used as dictionary keys.  If this property isn't needed    and you insist on changing string values in place instead, you may cheat    and use MutableString.    But the purpose of this class is an educational one: to prevent    people from inventing their own mutable string class derived    from UserString and than forget thereby to remove (override) the    __hash__ method inherited from UserString.  This would lead to    errors that would be very hard to track down.    A faster and better solution is to rewrite your program using lists.""" def __init__(self, string=""): self.data = string def __hash__(self): raise TypeError("unhashable type (it is mutable)") def __setitem__(self, index, sub): if index < 0:            index += len(self.data) if index < 0 or index >= len(self.data): raise IndexError self.data = self.data[:index] + sub + self.data[index+1:] def __delitem__(self, index): if index < 0:            index += len(self.data) if index < 0 or index >= len(self.data): raise IndexError self.data = self.data[:index] + self.data[index+1:] def __setslice__(self, start, end, sub):        start = max(start, 0); end = max(end, 0) if isinstance(sub, UserString): self.data = self.data[:start]+sub.data+self.data[end:] elif isinstance(sub, basestring): self.data = self.data[:start]+sub+self.data[end:] else: self.data = self.data[:start]+str(sub)+self.data[end:] def __delslice__(self, start, end):        start = max(start, 0); end = max(end, 0) self.data = self.data[:start] + self.data[end:] def immutable(self): return UserString(self.data) def __iadd__(self, other): if isinstance(other, UserString): self.data += other.data elif isinstance(other, basestring): self.data += other else: self.data += str(other) return self def __imul__(self, n): self.data *= n return self
class String(MutableString, Union):
    _fields_ = [('raw', POINTER(c_char)),                ('data', c_char_p)]
 def __init__(self, obj=""): if isinstance(obj, (str, unicode, UserString)): self.data = str(obj) else: self.raw = obj
 def __len__(self): return self.data and len(self.data) or 0
 def from_param(cls, obj): # Convert None or 0 if obj is None or obj == 0: return cls(POINTER(c_char)())
 # Convert from String elif isinstance(obj, String): return obj
 # Convert from str elif isinstance(obj, str): return cls(obj)
 # Convert from c_char_p elif isinstance(obj, c_char_p): return obj
 # Convert from POINTER(c_char) elif isinstance(obj, POINTER(c_char)): return obj
 # Convert from raw pointer elif isinstance(obj, int): return cls(cast(obj, POINTER(c_char)))
 # Convert from object else: return String.from_param(obj._as_parameter_)    from_param = classmethod(from_param)
def ReturnString(obj, func=None, arguments=None): return String.from_param(obj)
# As of ctypes 1.0, ctypes does not support custom error-checking# functions on callbacks, nor does it support custom datatypes on# callbacks, so we must ensure that all callbacks return# primitive datatypes.## Non-primitive return values wrapped with UNCHECKED won't be# typechecked, and will be converted to c_void_p.def UNCHECKED(type): if (hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P"): return type else: return c_void_p
# ctypes doesn't have direct support for variadic functions, so we have to write# our own wrapper classclass _variadic_function(object): def __init__(self,func,restype,argtypes): self.func=func self.func.restype=restype self.argtypes=argtypes def _as_parameter_(self): # So we can pass this variadic function as a function pointer return self.func def __call__(self,*args):        fixed_args=[]        i=0 for argtype in self.argtypes: # Typecheck what we can            fixed_args.append(argtype.from_param(args[i]))            i+=1 return self.func(*fixed_args+list(args[i:]))
# End preamble
_libs = {}_libdirs = []
# Begin loader
# ----------------------------------------------------------------------------# Copyright (c) 2008 David James# Copyright (c) 2006-2008 Alex Holkner# All rights reserved.## Redistribution and use in source and binary forms, with or without# modification, are permitted provided that the following conditions# are met:##  * Redistributions of source code must retain the above copyright#    notice, this list of conditions and the following disclaimer.#  * Redistributions in binary form must reproduce the above copyright#    notice, this list of conditions and the following disclaimer in#    the documentation and/or other materials provided with the#    distribution.#  * Neither the name of pyglet nor the names of its#    contributors may be used to endorse or promote products#    derived from this software without specific prior written#    permission.## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE# POSSIBILITY OF SUCH DAMAGE.# ----------------------------------------------------------------------------
import os.path, re, sys, globimport ctypesimport ctypes.util
def _environ_path(name): if name in os.environ: return os.environ[name].split(":") else: return []
class LibraryLoader(object): def __init__(self): self.other_dirs=[]
 def load_library(self,libname): """Given the name of a library, load it."""        paths = self.getpaths(libname)
 for path in paths: if os.path.exists(path): return self.load(path)
 raise ImportError("%s not found." % libname)
 def load(self,path): """Given a path to a library, load it.""" try: # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead # of the default RTLD_LOCAL.  Without this, you end up with # libraries not being loadable, resulting in "Symbol not found" # errors if sys.platform == 'darwin': return ctypes.CDLL(path, ctypes.RTLD_GLOBAL) else: return ctypes.cdll.LoadLibrary(path) except OSError,e: raise ImportError(e)
 def getpaths(self,libname): """Return a list of paths where the library might be found.""" if os.path.isabs(libname): yield libname
 else: for path in self.getplatformpaths(libname): yield path
            path = ctypes.util.find_library(libname) if path: yield path
 def getplatformpaths(self, libname): return []
# Darwin (Mac OS X)
class DarwinLibraryLoader(LibraryLoader):    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib", "%s.so", "%s.bundle", "%s"]
 def getplatformpaths(self,libname): if os.path.pathsep in libname:            names = [libname] else:            names = [format % libname for format in self.name_formats]
 for dir in self.getdirs(libname): for name in names: yield os.path.join(dir,name)
 def getdirs(self,libname): '''Implements the dylib search as specified in Apple documentation:        http://developer.apple.com/documentation/DeveloperTools/Conceptual/            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html        Before commencing the standard search, the method first checks        the bundle's ``Frameworks`` directory if the application is running        within a bundle (OS X .app). '''
        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH") if not dyld_fallback_library_path:            dyld_fallback_library_path = [os.path.expanduser('~/lib'), '/usr/local/lib', '/usr/lib']
        dirs = []
 if '/' in libname:            dirs.extend(_environ_path("DYLD_LIBRARY_PATH")) else:            dirs.extend(_environ_path("LD_LIBRARY_PATH"))            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        dirs.extend(self.other_dirs)        dirs.append(".")
 if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':            dirs.append(os.path.join(                os.environ['RESOURCEPATH'], '..', 'Frameworks'))
        dirs.extend(dyld_fallback_library_path)
 return dirs
# Posix
class PosixLibraryLoader(LibraryLoader):    _ld_so_cache = None
 def _create_ld_so_cache(self): # Recreate search path followed by ld.so.  This is going to be # slow to build, and incorrect (ld.so uses ld.so.cache, which may # not be up-to-date).  Used only as fallback for distros without # /sbin/ldconfig. # # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.
        directories = [] for name in ("LD_LIBRARY_PATH", "SHLIB_PATH", # HPUX "LIBPATH", # OS/2, AIX "LIBRARY_PATH", # BE/OS                    ): if name in os.environ:                directories.extend(os.environ[name].split(os.pathsep))        directories.extend(self.other_dirs)        directories.append(".")
 try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')]) except IOError: pass
        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])
        cache = {}        lib_re = re.compile(r'lib(.*)\.s[ol]')        ext_re = re.compile(r'\.s[ol]$') for dir in directories: try: for path in glob.glob("%s/*.s[ol]*" % dir): file = os.path.basename(path)
 # Index by filename if file not in cache:                        cache[file] = path
 # Index by library name                    match = lib_re.match(file) if match:                        library = match.group(1) if library not in cache:                            cache[library] = path except OSError: pass
 self._ld_so_cache = cache
 def getplatformpaths(self, libname): if self._ld_so_cache is None: self._create_ld_so_cache()
        result = self._ld_so_cache.get(libname) if result: yield result
        path = ctypes.util.find_library(libname) if path: yield os.path.join("/lib",path)
# Windows
class _WindowsLibrary(object): def __init__(self, path): self.cdll = ctypes.cdll.LoadLibrary(path) self.windll = ctypes.windll.LoadLibrary(path)
 def __getattr__(self, name): try: return getattr(self.cdll,name) except AttributeError: try: return getattr(self.windll,name) except AttributeError: raise
class WindowsLibraryLoader(LibraryLoader):    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]
 def load_library(self, libname): try:            result = LibraryLoader.load_library(self, libname) except ImportError:            result = None if os.path.sep not in libname: for name in self.name_formats: try:                        result = getattr(ctypes.cdll, name % libname) if result: break except WindowsError:                        result = None if result is None: try:                    result = getattr(ctypes.cdll, libname) except WindowsError:                    result = None if result is None: raise ImportError("%s not found." % libname) return result
 def load(self, path): return _WindowsLibrary(path)
 def getplatformpaths(self, libname): if os.path.sep not in libname: for name in self.name_formats:                dll_in_current_dir = os.path.abspath(name % libname) if os.path.exists(dll_in_current_dir): yield dll_in_current_dir                path = ctypes.util.find_library(name % libname) if path: yield path
# Platform switching
# If your value of sys.platform does not appear in this dict, please contact# the Ctypesgen maintainers.
loaderclass = { "darwin":   DarwinLibraryLoader, "cygwin":   WindowsLibraryLoader, "win32":    WindowsLibraryLoader}
loader = loaderclass.get(sys.platform, PosixLibraryLoader)()
def add_library_search_dirs(other_dirs):    loader.other_dirs = other_dirs
load_library = loader.load_library
del loaderclass
# End loader
add_library_search_dirs([])
# Begin libraries
_libs["epanet2"] = load_library("epanet2")
# 1 libraries# End libraries
# No modules
# /home/mau/github/EPANET/include/epanet2.h: 200for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENepanet'): continue    ENepanet = _lib.ENepanet    ENepanet.argtypes = [String, String, String, CFUNCTYPE(UNCHECKED(None), String)]    ENepanet.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 202for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENopen'): continue    ENopen = _lib.ENopen    ENopen.argtypes = [String, String, String]    ENopen.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 203for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsaveinpfile'): continue    ENsaveinpfile = _lib.ENsaveinpfile    ENsaveinpfile.argtypes = [String]    ENsaveinpfile.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 204for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENclose'): continue    ENclose = _lib.ENclose    ENclose.argtypes = []    ENclose.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 206for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsolveH'): continue    ENsolveH = _lib.ENsolveH    ENsolveH.argtypes = []    ENsolveH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 207for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsaveH'): continue    ENsaveH = _lib.ENsaveH    ENsaveH.argtypes = []    ENsaveH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 208for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENopenH'): continue    ENopenH = _lib.ENopenH    ENopenH.argtypes = []    ENopenH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 209for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENinitH'): continue    ENinitH = _lib.ENinitH    ENinitH.argtypes = [c_int]    ENinitH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 210for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENrunH'): continue    ENrunH = _lib.ENrunH    ENrunH.argtypes = [POINTER(c_long)]    ENrunH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 211for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENnextH'): continue    ENnextH = _lib.ENnextH    ENnextH.argtypes = [POINTER(c_long)]    ENnextH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 212for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENcloseH'): continue    ENcloseH = _lib.ENcloseH    ENcloseH.argtypes = []    ENcloseH.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 213for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsavehydfile'): continue    ENsavehydfile = _lib.ENsavehydfile    ENsavehydfile.argtypes = [String]    ENsavehydfile.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 214for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENusehydfile'): continue    ENusehydfile = _lib.ENusehydfile    ENusehydfile.argtypes = [String]    ENusehydfile.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 216for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsolveQ'): continue    ENsolveQ = _lib.ENsolveQ    ENsolveQ.argtypes = []    ENsolveQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 217for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENopenQ'): continue    ENopenQ = _lib.ENopenQ    ENopenQ.argtypes = []    ENopenQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 218for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENinitQ'): continue    ENinitQ = _lib.ENinitQ    ENinitQ.argtypes = [c_int]    ENinitQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 219for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENrunQ'): continue    ENrunQ = _lib.ENrunQ    ENrunQ.argtypes = [POINTER(c_long)]    ENrunQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 220for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENnextQ'): continue    ENnextQ = _lib.ENnextQ    ENnextQ.argtypes = [POINTER(c_long)]    ENnextQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 221for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENstepQ'): continue    ENstepQ = _lib.ENstepQ    ENstepQ.argtypes = [POINTER(c_long)]    ENstepQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 222for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENcloseQ'): continue    ENcloseQ = _lib.ENcloseQ    ENcloseQ.argtypes = []    ENcloseQ.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 224for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENwriteline'): continue    ENwriteline = _lib.ENwriteline    ENwriteline.argtypes = [String]    ENwriteline.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 225for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENreport'): continue    ENreport = _lib.ENreport    ENreport.argtypes = []    ENreport.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 226for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENresetreport'): continue    ENresetreport = _lib.ENresetreport    ENresetreport.argtypes = []    ENresetreport.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 227for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetreport'): continue    ENsetreport = _lib.ENsetreport    ENsetreport.argtypes = [String]    ENsetreport.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 229for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcontrol'): continue    ENgetcontrol = _lib.ENgetcontrol    ENgetcontrol.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_float), POINTER(c_int), POINTER(c_float)]    ENgetcontrol.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 230for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcount'): continue    ENgetcount = _lib.ENgetcount    ENgetcount.argtypes = [c_int, POINTER(c_int)]    ENgetcount.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 231for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetoption'): continue    ENgetoption = _lib.ENgetoption    ENgetoption.argtypes = [c_int, POINTER(c_float)]    ENgetoption.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 232for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgettimeparam'): continue    ENgettimeparam = _lib.ENgettimeparam    ENgettimeparam.argtypes = [c_int, POINTER(c_long)]    ENgettimeparam.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 233for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetflowunits'): continue    ENgetflowunits = _lib.ENgetflowunits    ENgetflowunits.argtypes = [POINTER(c_int)]    ENgetflowunits.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 234for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetpatternindex'): continue    ENgetpatternindex = _lib.ENgetpatternindex    ENgetpatternindex.argtypes = [String, POINTER(c_int)]    ENgetpatternindex.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 235for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetpatternid'): continue    ENgetpatternid = _lib.ENgetpatternid    ENgetpatternid.argtypes = [c_int, String]    ENgetpatternid.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 236for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetpatternlen'): continue    ENgetpatternlen = _lib.ENgetpatternlen    ENgetpatternlen.argtypes = [c_int, POINTER(c_int)]    ENgetpatternlen.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 237for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetpatternvalue'): continue    ENgetpatternvalue = _lib.ENgetpatternvalue    ENgetpatternvalue.argtypes = [c_int, c_int, POINTER(c_float)]    ENgetpatternvalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 238for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetaveragepatternvalue'): continue    ENgetaveragepatternvalue = _lib.ENgetaveragepatternvalue    ENgetaveragepatternvalue.argtypes = [c_int, POINTER(c_float)]    ENgetaveragepatternvalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 239for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetqualtype'): continue    ENgetqualtype = _lib.ENgetqualtype    ENgetqualtype.argtypes = [POINTER(c_int), POINTER(c_int)]    ENgetqualtype.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 240for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgeterror'): continue    ENgeterror = _lib.ENgeterror    ENgeterror.argtypes = [c_int, String, c_int]    ENgeterror.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 241for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetstatistic'): continue    ENgetstatistic = _lib.ENgetstatistic    ENgetstatistic.argtypes = [c_int, POINTER(c_float)]    ENgetstatistic.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 243for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetnodeindex'): continue    ENgetnodeindex = _lib.ENgetnodeindex    ENgetnodeindex.argtypes = [String, POINTER(c_int)]    ENgetnodeindex.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 244for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetnodeid'): continue    ENgetnodeid = _lib.ENgetnodeid    ENgetnodeid.argtypes = [c_int, String]    ENgetnodeid.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 245for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetnodetype'): continue    ENgetnodetype = _lib.ENgetnodetype    ENgetnodetype.argtypes = [c_int, POINTER(c_int)]    ENgetnodetype.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 246for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetnodevalue'): continue    ENgetnodevalue = _lib.ENgetnodevalue    ENgetnodevalue.argtypes = [c_int, c_int, POINTER(c_float)]    ENgetnodevalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 247for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcoord'): continue    ENgetcoord = _lib.ENgetcoord    ENgetcoord.argtypes = [c_int, POINTER(c_float), POINTER(c_float)]    ENgetcoord.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 248for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetcoord'): continue    ENsetcoord = _lib.ENsetcoord    ENsetcoord.argtypes = [c_int, c_float, c_float]    ENsetcoord.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 250for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetnumdemands'): continue    ENgetnumdemands = _lib.ENgetnumdemands    ENgetnumdemands.argtypes = [c_int, POINTER(c_int)]    ENgetnumdemands.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 251for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetbasedemand'): continue    ENgetbasedemand = _lib.ENgetbasedemand    ENgetbasedemand.argtypes = [c_int, c_int, POINTER(c_float)]    ENgetbasedemand.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 252for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetdemandpattern'): continue    ENgetdemandpattern = _lib.ENgetdemandpattern    ENgetdemandpattern.argtypes = [c_int, c_int, POINTER(c_int)]    ENgetdemandpattern.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 254for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetlinkindex'): continue    ENgetlinkindex = _lib.ENgetlinkindex    ENgetlinkindex.argtypes = [String, POINTER(c_int)]    ENgetlinkindex.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 255for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetlinkid'): continue    ENgetlinkid = _lib.ENgetlinkid    ENgetlinkid.argtypes = [c_int, String]    ENgetlinkid.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 256for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetlinktype'): continue    ENgetlinktype = _lib.ENgetlinktype    ENgetlinktype.argtypes = [c_int, POINTER(c_int)]    ENgetlinktype.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 257for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetlinknodes'): continue    ENgetlinknodes = _lib.ENgetlinknodes    ENgetlinknodes.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]    ENgetlinknodes.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 258for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetlinkvalue'): continue    ENgetlinkvalue = _lib.ENgetlinkvalue    ENgetlinkvalue.argtypes = [c_int, c_int, POINTER(c_float)]    ENgetlinkvalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 260for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcurve'): continue    ENgetcurve = _lib.ENgetcurve    ENgetcurve.argtypes = [c_int, String, POINTER(c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]    ENgetcurve.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 261for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetheadcurveindex'): continue    ENgetheadcurveindex = _lib.ENgetheadcurveindex    ENgetheadcurveindex.argtypes = [c_int, POINTER(c_int)]    ENgetheadcurveindex.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 262for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetpumptype'): continue    ENgetpumptype = _lib.ENgetpumptype    ENgetpumptype.argtypes = [c_int, POINTER(c_int)]    ENgetpumptype.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 264for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetversion'): continue    ENgetversion = _lib.ENgetversion    ENgetversion.argtypes = [POINTER(c_int)]    ENgetversion.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 266for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetcontrol'): continue    ENsetcontrol = _lib.ENsetcontrol    ENsetcontrol.argtypes = [c_int, c_int, c_int, c_float, c_int, c_float]    ENsetcontrol.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 267for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetnodevalue'): continue    ENsetnodevalue = _lib.ENsetnodevalue    ENsetnodevalue.argtypes = [c_int, c_int, c_float]    ENsetnodevalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 268for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetlinkvalue'): continue    ENsetlinkvalue = _lib.ENsetlinkvalue    ENsetlinkvalue.argtypes = [c_int, c_int, c_float]    ENsetlinkvalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 269for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENaddpattern'): continue    ENaddpattern = _lib.ENaddpattern    ENaddpattern.argtypes = [String]    ENaddpattern.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 270for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetpattern'): continue    ENsetpattern = _lib.ENsetpattern    ENsetpattern.argtypes = [c_int, POINTER(c_float), c_int]    ENsetpattern.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 271for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetpatternvalue'): continue    ENsetpatternvalue = _lib.ENsetpatternvalue    ENsetpatternvalue.argtypes = [c_int, c_int, c_float]    ENsetpatternvalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 272for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsettimeparam'): continue    ENsettimeparam = _lib.ENsettimeparam    ENsettimeparam.argtypes = [c_int, c_long]    ENsettimeparam.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 273for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetoption'): continue    ENsetoption = _lib.ENsetoption    ENsetoption.argtypes = [c_int, c_float]    ENsetoption.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 274for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetstatusreport'): continue    ENsetstatusreport = _lib.ENsetstatusreport    ENsetstatusreport.argtypes = [c_int]    ENsetstatusreport.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 275for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetqualtype'): continue    ENsetqualtype = _lib.ENsetqualtype    ENsetqualtype.argtypes = [c_int, String, String, String]    ENsetqualtype.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 276for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetqualinfo'): continue    ENgetqualinfo = _lib.ENgetqualinfo    ENgetqualinfo.argtypes = [POINTER(c_int), String, String, POINTER(c_int)]    ENgetqualinfo.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 277for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetbasedemand'): continue    ENsetbasedemand = _lib.ENsetbasedemand    ENsetbasedemand.argtypes = [c_int, c_int, c_float]    ENsetbasedemand.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 279for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcurveindex'): continue    ENgetcurveindex = _lib.ENgetcurveindex    ENgetcurveindex.argtypes = [String, POINTER(c_int)]    ENgetcurveindex.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 280for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcurveid'): continue    ENgetcurveid = _lib.ENgetcurveid    ENgetcurveid.argtypes = [c_int, String]    ENgetcurveid.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 281for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcurvelen'): continue    ENgetcurvelen = _lib.ENgetcurvelen    ENgetcurvelen.argtypes = [c_int, POINTER(c_int)]    ENgetcurvelen.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 282for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENgetcurvevalue'): continue    ENgetcurvevalue = _lib.ENgetcurvevalue    ENgetcurvevalue.argtypes = [c_int, c_int, POINTER(c_float), POINTER(c_float)]    ENgetcurvevalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 283for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetcurvevalue'): continue    ENsetcurvevalue = _lib.ENsetcurvevalue    ENsetcurvevalue.argtypes = [c_int, c_int, c_float, c_float]    ENsetcurvevalue.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 284for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENsetcurve'): continue    ENsetcurve = _lib.ENsetcurve    ENsetcurve.argtypes = [c_int, POINTER(c_float), POINTER(c_float), c_int]    ENsetcurve.restype = c_int break
# /home/mau/github/EPANET/include/epanet2.h: 285for _lib in _libs.itervalues(): if not hasattr(_lib, 'ENaddcurve'): continue    ENaddcurve = _lib.ENaddcurve    ENaddcurve.argtypes = [String]    ENaddcurve.restype = c_int break
EN_API_FLOAT_TYPE = c_float # /home/mau/github/EPANET/include/epanet2.h: 24
# /home/mau/github/EPANET/include/epanet2.h: 60try: EN_ELEVATION = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 61try: EN_BASEDEMAND = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 62try: EN_PATTERN = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 63try: EN_EMITTER = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 64try: EN_INITQUAL = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 65try: EN_SOURCEQUAL = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 66try: EN_SOURCEPAT = 6except: pass
# /home/mau/github/EPANET/include/epanet2.h: 67try: EN_SOURCETYPE = 7except: pass
# /home/mau/github/EPANET/include/epanet2.h: 68try: EN_TANKLEVEL = 8except: pass
# /home/mau/github/EPANET/include/epanet2.h: 69try: EN_DEMAND = 9except: pass
# /home/mau/github/EPANET/include/epanet2.h: 70try: EN_HEAD = 10except: pass
# /home/mau/github/EPANET/include/epanet2.h: 71try: EN_PRESSURE = 11except: pass
# /home/mau/github/EPANET/include/epanet2.h: 72try: EN_QUALITY = 12except: pass
# /home/mau/github/EPANET/include/epanet2.h: 73try: EN_SOURCEMASS = 13except: pass
# /home/mau/github/EPANET/include/epanet2.h: 74try: EN_INITVOLUME = 14except: pass
# /home/mau/github/EPANET/include/epanet2.h: 75try: EN_MIXMODEL = 15except: pass
# /home/mau/github/EPANET/include/epanet2.h: 76try: EN_MIXZONEVOL = 16except: pass
# /home/mau/github/EPANET/include/epanet2.h: 78try: EN_TANKDIAM = 17except: pass
# /home/mau/github/EPANET/include/epanet2.h: 79try: EN_MINVOLUME = 18except: pass
# /home/mau/github/EPANET/include/epanet2.h: 80try: EN_VOLCURVE = 19except: pass
# /home/mau/github/EPANET/include/epanet2.h: 81try: EN_MINLEVEL = 20except: pass
# /home/mau/github/EPANET/include/epanet2.h: 82try: EN_MAXLEVEL = 21except: pass
# /home/mau/github/EPANET/include/epanet2.h: 83try: EN_MIXFRACTION = 22except: pass
# /home/mau/github/EPANET/include/epanet2.h: 84try: EN_TANK_KBULK = 23except: pass
# /home/mau/github/EPANET/include/epanet2.h: 85try: EN_TANKVOLUME = 24except: pass
# /home/mau/github/EPANET/include/epanet2.h: 86try: EN_MAXVOLUME = 25except: pass
# /home/mau/github/EPANET/include/epanet2.h: 88try: EN_DIAMETER = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 89try: EN_LENGTH = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 90try: EN_ROUGHNESS = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 91try: EN_MINORLOSS = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 92try: EN_INITSTATUS = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 93try: EN_INITSETTING = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 94try: EN_KBULK = 6except: pass
# /home/mau/github/EPANET/include/epanet2.h: 95try: EN_KWALL = 7except: pass
# /home/mau/github/EPANET/include/epanet2.h: 96try: EN_FLOW = 8except: pass
# /home/mau/github/EPANET/include/epanet2.h: 97try: EN_VELOCITY = 9except: pass
# /home/mau/github/EPANET/include/epanet2.h: 98try: EN_HEADLOSS = 10except: pass
# /home/mau/github/EPANET/include/epanet2.h: 99try: EN_STATUS = 11except: pass
# /home/mau/github/EPANET/include/epanet2.h: 100try: EN_SETTING = 12except: pass
# /home/mau/github/EPANET/include/epanet2.h: 101try: EN_ENERGY = 13except: pass
# /home/mau/github/EPANET/include/epanet2.h: 102try: EN_LINKQUAL = 14except: pass
# /home/mau/github/EPANET/include/epanet2.h: 103try: EN_LINKPATTERN = 15except: pass
# /home/mau/github/EPANET/include/epanet2.h: 105try: EN_DURATION = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 106try: EN_HYDSTEP = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 107try: EN_QUALSTEP = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 108try: EN_PATTERNSTEP = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 109try: EN_PATTERNSTART = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 110try: EN_REPORTSTEP = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 111try: EN_REPORTSTART = 6except: pass
# /home/mau/github/EPANET/include/epanet2.h: 112try: EN_RULESTEP = 7except: pass
# /home/mau/github/EPANET/include/epanet2.h: 113try: EN_STATISTIC = 8except: pass
# /home/mau/github/EPANET/include/epanet2.h: 114try: EN_PERIODS = 9except: pass
# /home/mau/github/EPANET/include/epanet2.h: 115try: EN_STARTTIME = 10except: pass
# /home/mau/github/EPANET/include/epanet2.h: 116try: EN_HTIME = 11except: pass
# /home/mau/github/EPANET/include/epanet2.h: 117try: EN_QTIME = 12except: pass
# /home/mau/github/EPANET/include/epanet2.h: 118try: EN_HALTFLAG = 13except: pass
# /home/mau/github/EPANET/include/epanet2.h: 119try: EN_NEXTEVENT = 14except: pass
# /home/mau/github/EPANET/include/epanet2.h: 121try: EN_ITERATIONS = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 122try: EN_RELATIVEERROR = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 124try: EN_NODECOUNT = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 125try: EN_TANKCOUNT = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 126try: EN_LINKCOUNT = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 127try: EN_PATCOUNT = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 128try: EN_CURVECOUNT = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 129try: EN_CONTROLCOUNT = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 131try: EN_JUNCTION = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 132try: EN_RESERVOIR = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 133try: EN_TANK = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 135try: EN_CVPIPE = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 136try: EN_PIPE = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 137try: EN_PUMP = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 138try: EN_PRV = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 139try: EN_PSV = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 140try: EN_PBV = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 141try: EN_FCV = 6except: pass
# /home/mau/github/EPANET/include/epanet2.h: 142try: EN_TCV = 7except: pass
# /home/mau/github/EPANET/include/epanet2.h: 143try: EN_GPV = 8except: pass
# /home/mau/github/EPANET/include/epanet2.h: 145try: EN_NONE = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 146try: EN_CHEM = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 147try: EN_AGE = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 148try: EN_TRACE = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 150try: EN_CONCEN = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 151try: EN_MASS = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 152try: EN_SETPOINT = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 153try: EN_FLOWPACED = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 155try: EN_CFS = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 156try: EN_GPM = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 157try: EN_MGD = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 158try: EN_IMGD = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 159try: EN_AFD = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 160try: EN_LPS = 5except: pass
# /home/mau/github/EPANET/include/epanet2.h: 161try: EN_LPM = 6except: pass
# /home/mau/github/EPANET/include/epanet2.h: 162try: EN_MLD = 7except: pass
# /home/mau/github/EPANET/include/epanet2.h: 163try: EN_CMH = 8except: pass
# /home/mau/github/EPANET/include/epanet2.h: 164try: EN_CMD = 9except: pass
# /home/mau/github/EPANET/include/epanet2.h: 166try: EN_TRIALS = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 167try: EN_ACCURACY = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 168try: EN_TOLERANCE = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 169try: EN_EMITEXPON = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 170try: EN_DEMANDMULT = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 172try: EN_LOWLEVEL = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 173try: EN_HILEVEL = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 174try: EN_TIMER = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 175try: EN_TIMEOFDAY = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 177try: EN_AVERAGE = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 178try: EN_MINIMUM = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 179try: EN_MAXIMUM = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 180try: EN_RANGE = 4except: pass
# /home/mau/github/EPANET/include/epanet2.h: 182try: EN_MIX1 = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 183try: EN_MIX2 = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 184try: EN_FIFO = 2except: pass
# /home/mau/github/EPANET/include/epanet2.h: 185try: EN_LIFO = 3except: pass
# /home/mau/github/EPANET/include/epanet2.h: 187try: EN_NOSAVE = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 188try: EN_SAVE = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 190try: EN_INITFLOW = 10except: pass
# /home/mau/github/EPANET/include/epanet2.h: 192try: EN_CONST_HP = 0except: pass
# /home/mau/github/EPANET/include/epanet2.h: 193try: EN_POWER_FUNC = 1except: pass
# /home/mau/github/EPANET/include/epanet2.h: 194try: EN_CUSTOM = 2except: pass
# No inserted files
