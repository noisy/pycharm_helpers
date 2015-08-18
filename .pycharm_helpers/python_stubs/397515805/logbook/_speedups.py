# encoding: utf-8
# module logbook._speedups
# from /usr/local/lib/python2.7/site-packages/logbook/_speedups.so
# by generator 1.136
"""
logbook._speedups
    ~~~~~~~~~~~~~~~~~

    Cython implementation of some core objects.

    :copyright: (c) 2010 by Armin Ronacher, Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import platform as platform # /usr/local/lib/python2.7/platform.pyc
from thread import thread_get_ident, thread_local


# functions

def greenlet_get_ident(gr=None): # reliably restored by inspect
    # no doc
    pass

def is_gevent_enabled(): # reliably restored by inspect
    # no doc
    pass

# classes

class ContextStackManager(object):
    # no doc
    def iter_context_objects(self, *args, **kwargs): # real signature unknown
        pass

    def pop_application(self, *args, **kwargs): # real signature unknown
        pass

    def pop_greenlet(self, *args, **kwargs): # real signature unknown
        pass

    def pop_thread(self, *args, **kwargs): # real signature unknown
        pass

    def push_application(self, *args, **kwargs): # real signature unknown
        pass

    def push_greenlet(self, *args, **kwargs): # real signature unknown
        pass

    def push_thread(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class GreenletRLock(object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def _get_greenlet_lock(self, *args, **kwargs): # real signature unknown
        pass

    def _is_owned(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class greenlet_local(object):
    # no doc
    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, *args, **kw): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    _local__impl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''
    __slots__ = (
        '_local__impl',
        '__dict__',
    )


class group_reflected_property(object):
    # no doc
    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass


class StackedObject(object):
    """
    Baseclass for all objects that provide stack manipulation
        operations.
    """
    def applicationbound(self, *args, **kwargs): # real signature unknown
        """
        Can be used in combination with the `with` statement to
                execute code while the object is bound to the application.
        """
        pass

    def greenletbound(self, *args, **kwargs): # real signature unknown
        """
        Can be used in combination with the `with` statement to
                execute code while the object is bound to the greenlet.
        """
        pass

    def pop_application(self, *args, **kwargs): # real signature unknown
        """ Pops the stacked object from the application stack. """
        pass

    def pop_greenlet(self, *args, **kwargs): # real signature unknown
        """ Pops the stacked object from the greenlet stack. """
        pass

    def pop_thread(self, *args, **kwargs): # real signature unknown
        """ Pops the stacked object from the thread stack. """
        pass

    def push_application(self, *args, **kwargs): # real signature unknown
        """ Pushes the stacked object to the application stack. """
        pass

    def push_greenlet(self, *args, **kwargs): # real signature unknown
        """ Pushes the stacked object to the greenlet stack. """
        pass

    def push_thread(self, *args, **kwargs): # real signature unknown
        """ Pushes the stacked object to the thread stack. """
        pass

    def threadbound(self, *args, **kwargs): # real signature unknown
        """
        Can be used in combination with the `with` statement to
                execute code while the object is bound to the thread.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class _StackBound(object):
    # no doc
    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class _StackItem(object):
    # no doc
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    val = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__test__ = {}

