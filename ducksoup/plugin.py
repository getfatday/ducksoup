#!/usr/bin/env python
# encoding: utf-8
"""
plugin.py

Created by Ian Anderson on 2009-07-08.
"""

from interface import interface
from pkg_resources import iter_entry_points

class IPlugin():
  # Returns true if plugin is enabled
  def enabled(self): pass

class plugin_type(type):
  
  def __init__(cls, classname, bases, classdict):
    super(plugin_type, cls).__init__(classname, bases, classdict)
    setattr(cls, '__entries__', None)
    setattr(cls, '__invalid__', None)

class plugin(object):

  __metaclass__ = plugin_type
  __entry_point__ = "ducksoup.plugin"
  __interface__ = IPlugin
    
  @classmethod
  def enabled(cls):
    return True
    
  @property
  def entries(self):
    if self.__entries__ == None:
      self.__getentries__()
    return self.__entries__

  @property
  def invalid_entries(self):
    if self.__invalid__ == None:
      self.__getentries__()
    return self.__invalid__
  
  def __getentries__(self):
    """Returns plugin classes avialable"""
    
    self.__entries__ = []
    self.__invalid__ = []
    
    for e in iter_entry_points(group=self.__entry_point__):
      cls = e.load()
      defined = set(dir(cls))
      required = set(dir(self.__interface__))
      if not required.issubset(defined):
        self.__invalid__.append(cls)
        missing = list(required - defined)
        error = "Plug-in '%s' missing implementations of '%s' required for '%s'"
        print error % (cls.__name__, ", ".join(missing), self.__entry_point__)
      else:
        if cls.enabled():
          self.__entries__.append(cls)