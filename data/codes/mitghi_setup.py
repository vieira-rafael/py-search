from distutils.core import setupfrom distutils.extension import Extensionfrom Cython.Build import cythonize
setup( ext_modules = cythonize([Extension("cyj", ["cyj.pyx","./cJSON/cJSON.c"])]))