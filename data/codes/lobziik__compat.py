# coding: utf-8import sys

PY2 = sys.version_info[0] == 2PY3 = sys.version_info[0] == 3PYPY = hasattr(sys, 'pypy_translation_info')

if PY2:    text_type = unicodeelse:    text_type = str
try: from unittest.mock import patch, Mockexcept ImportError: from mock import patch, Mock
try: import ujson as jsonexcept ImportError: import json