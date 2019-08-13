#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
This is a setup.py script generated by py2applet

Usage:
    python py2app_setup.py py2app
"""
import sys
from setuptools import setup

app_name = 'K40 Whisperer'
app_version = "0.34"
app_copyright = u'Copyright © 2017-2019, Scorch Works, GNU General Public License'
main_script = 'k40_whisperer.py'
url = 'https://github.com/rsre/K40-Whisperer-macOS'

if sys.platform == 'darwin':
     extra_options = dict(
        setup_requires=['py2app'],
        #python_requires='>=2.7, <3',
        options=dict(py2app = {
            'iconfile': 'emblem.icns',
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
            'resources': ['right.png','left.png','up.png','down.png',
                          'UL.png','UR.png','LR.png','LL.png','CC.png'],
            'plist': {
                'CFBundleName': app_name,
                'CFBundleDisplayName': app_name,
                'CFBundleGetInfoString': "Scorch Works",
                'CFBundleIdentifier': "com.scorchworks.osx.k40-whisperer",
                'CFBundleVersion': app_version,
                'CFBundleShortVersionString': app_version,
                'NSHumanReadableCopyright': app_copyright,
                'NSHighResolutionCapable': True
                }
            })
     )
else:
     extra_options = dict(
         # Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
         scripts=[mainscript],
     )

setup(
    name=app_name,
    app=[main_script],
    version=app_version,
    url=url,
    **extra_options
    )
