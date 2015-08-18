# encoding: utf-8
# module gevent.ares
# from /usr/local/lib/python2.7/site-packages/gevent/ares.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import socket as __socket


# Variables with simple values

ARES_EADDRGETNETWORKPARAMS = 23
ARES_EBADFAMILY = 9
ARES_EBADFLAGS = 18
ARES_EBADHINTS = 20
ARES_EBADNAME = 8
ARES_EBADQUERY = 7
ARES_EBADRESP = 10
ARES_EBADSTR = 17
ARES_ECANCELLED = 24
ARES_ECONNREFUSED = 11
ARES_EDESTRUCTION = 16
ARES_EFILE = 14
ARES_EFORMERR = 2
ARES_ELOADIPHLPAPI = 22
ARES_ENODATA = 1
ARES_ENOMEM = 15
ARES_ENONAME = 19
ARES_ENOTFOUND = 4
ARES_ENOTIMP = 5
ARES_ENOTINITIALIZED = 21
ARES_EOF = 13
ARES_EREFUSED = 6
ARES_ESERVFAIL = 3
ARES_ETIMEOUT = 12

ARES_FLAG_IGNTC = 4
ARES_FLAG_NOALIASES = 64
ARES_FLAG_NOCHECKRESP = 128
ARES_FLAG_NORECURSE = 8
ARES_FLAG_NOSEARCH = 32
ARES_FLAG_PRIMARY = 2
ARES_FLAG_STAYOPEN = 16
ARES_FLAG_USEVC = 1

ARES_SUCCESS = 0

TIMEOUT = 1

_cares_flag_map = None

# functions

def strerror(*args, **kwargs): # real signature unknown
    pass

def _convert_cares_flags(*args, **kwargs): # real signature unknown
    pass

# classes

class ares_host_result(tuple):
    # no doc
    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is ''
    __qualname__ = 'ares_host_result'


class channel(object):
    # no doc
    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def gethostbyaddr(self, *args, **kwargs): # real signature unknown
        pass

    def gethostbyname(self, *args, **kwargs): # real signature unknown
        pass

    def getnameinfo(self, *args, **kwargs): # real signature unknown
        pass

    def set_servers(self, *args, **kwargs): # real signature unknown
        pass

    def _getnameinfo(self, *args, **kwargs): # real signature unknown
        pass

    def _on_timer(self, *args, **kwargs): # real signature unknown
        pass

    def _process_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _timer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _watchers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class gaierror(__socket.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InvalidIP(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'InvalidIP'


class result(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        pass

    def successful(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

_ares_errors = {
    0: 'ARES_SUCCESS',
    1: 'ARES_ENODATA',
    2: 'ARES_EFORMERR',
    3: 'ARES_ESERVFAIL',
    4: 'ARES_ENOTFOUND',
    5: 'ARES_ENOTIMP',
    6: 'ARES_EREFUSED',
    7: 'ARES_EBADQUERY',
    8: 'ARES_EBADNAME',
    9: 'ARES_EBADFAMILY',
    10: 'ARES_EBADRESP',
    11: 'ARES_ECONNREFUSED',
    12: 'ARES_ETIMEOUT',
    13: 'ARES_EOF',
    14: 'ARES_EFILE',
    15: 'ARES_ENOMEM',
    16: 'ARES_EDESTRUCTION',
    17: 'ARES_EBADSTR',
    18: 'ARES_EBADFLAGS',
    19: 'ARES_ENONAME',
    20: 'ARES_EBADHINTS',
    21: 'ARES_ENOTINITIALIZED',
    22: 'ARES_ELOADIPHLPAPI',
    23: 'ARES_EADDRGETNETWORKPARAMS',
    24: 'ARES_ECANCELLED',
}

__all__ = [
    'channel',
]

__test__ = {}

