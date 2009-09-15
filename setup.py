#!/usr/bin/env python
# encoding: utf-8

"""
Created by Ian Anderson on 2009-09-15.
"""

from setuptools import setup
from ducksoup import __version__ as version
from ducksoup import __doc__ as long_description

setup(name = "ducksoup",
    version = version,
    description = "A ducktype plugin library for python",
    author = "Ian Anderson",
    author_email = "getfatday@gmail.com",
    url = "http://github.com/getfatday/ducksoup",
    packages = ['ducksoup',],
    long_description = long_description
)