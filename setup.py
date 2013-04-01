#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(
  name='simple-stopwatch',
  version='1.2.0',
  description='Simple ncurses based terminal stopwatch',
  author='Christoph Göttschkes',
  author_email='just.mychris@googlemail.com',
  url='https://github.com/mychris/simple-stopwatch',
  download_url='https://github.com/mychris/simple-stopwatch/tarball/master',
  packages = [],
  scripts = ['simple-stopwatch'],
  classifiers = [
    'Programming Language :: Python :: 3',
    'Operating System :: POSIX',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console :: Curses'
  ],
  license = 'GPL v3 or later',
  data_files = [('share/doc/simple-stopwatch', ['README.md', 'LICENSE'])]
)

# vim: ft=python ts=2 sts=2 sw=2 et:
