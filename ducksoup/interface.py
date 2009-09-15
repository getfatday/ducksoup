#!/usr/bin/env python
# encoding: utf-8
"""
interface.py

Created by Ian Anderson on 2009-07-08.

Derived from:
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/204349
http://svn.pythonfr.org/public/pythonfr/plugin_framework/framework
"""

import inspect

class interface_type(type):
  """
  Validates the presence of required attributes
  """
  
  def __new__(cls, classname, bases, classdict):
    obj = type.__new__(cls, classname, bases, classdict)
    interface = classdict.get('__implements__')
    
    if interface:
      defined = set(dir(obj))
      required = set(dir(interface))
      if not required.issubset(defined):
        missing = list(required - defined)
        error = "Not implemented methods from %s : %r"
        raise KeyError, error % (interface.__name__, missing)
      
    return obj
      

class interface(object):
  __metaclass__ = interface_type
  __implements__ = None