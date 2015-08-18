# encoding: utf-8
# module gevent._semaphore
# from /usr/local/lib/python2.7/site-packages/gevent/_semaphore.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
from greenlet import getcurrent


# functions

def get_hub(*args, **kwargs): # reliably restored by inspect
    """
    Return the hub for the current thread.
    
        If a hub does not exist in the current thread, a new one is
        created of the type returned by :func:`get_hub_class`.
    """
    pass

# classes

class Semaphore(object):
    """
    A semaphore manages a counter representing the number of release()
        calls minus the number of acquire() calls, plus an initial value.
        The acquire() method blocks if necessary until it can return
        without making the counter negative.
    
        If not given, ``value`` defaults to 1.
    
        This Semaphore's ``__exit__`` method does not call the trace function.
    """
    def acquire(self, *args, **kwargs): # real signature unknown
        """
        Acquire the semaphore.
        
                .. warning:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned.
        """
        pass

    def locked(self, *args, **kwargs): # real signature unknown
        """
        Return a boolean indicating whether the semaphore can be acquired.
                Most useful with binary semaphores.
        """
        pass

    def rawlink(self, *args, **kwargs): # real signature unknown
        """
        Register a callback to call when a counter is more than zero.
        
                *callback* will be called in the :class:`Hub <gevent.hub.Hub>`, so it must not use blocking gevent API.
                *callback* will be passed one argument: this instance.
        """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def unlink(self, *args, **kwargs): # real signature unknown
        """ Remove the callback set by :meth:`rawlink` """
        pass

    def wait(self, *args, **kwargs): # real signature unknown
        """
        Wait until it is possible to acquire this semaphore, or until the optional
                *timeout* elapses.
        
                .. warning:: If this semaphore was initialized with a size of 0,
                   this method will block forever if no timeout is given.
        
                :param float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A number indicating how many times the semaphore can be acquired
                    before blocking.
        """
        pass

    def _notify_links(self, *args, **kwargs): # real signature unknown
        pass

    def _py3k_acquire(self, *args, **kwargs): # real signature unknown
        """
        Acquire the semaphore.
        
                .. warning:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned.
        """
        pass

    def _start_notify(self, *args, **kwargs): # real signature unknown
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

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _notifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class BoundedSemaphore(Semaphore):
    """
    A bounded semaphore checks to make sure its current value doesn't
        exceed its initial value. If it does, :class:`ValueError` is
        raised. In most situations semaphores are used to guard resources
        with limited capacity. If the semaphore is released too many times
        it's a sign of a bug.
    
        If not given, *value* defaults to 1.
    """
    def release(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    _initial_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _OVER_RELEASE_ERROR = ValueError
    __pyx_vtable__ = None # (!) real value is ''


class Timeout(BaseException):
    """
    Raise *exception* in the current greenlet after given time period::
    
            timeout = Timeout(seconds, exception)
            timeout.start()
            try:
                ...  # exception will be raised here, after *seconds* passed since start() call
            finally:
                timeout.cancel()
    
        .. note:: If the code that the timeout was protecting finishes
           executing before the timeout elapses, be sure to ``cancel`` the timeout
           so it is not unexpectedly raised in the future. Even if it is raised, it is a best
           practice to cancel it. This ``try/finally`` construct is a recommended pattern.
    
        When *exception* is omitted or ``None``, the :class:`Timeout` instance itself is raised:
    
            >>> import gevent
            >>> gevent.Timeout(0.1).start()
            >>> gevent.sleep(0.2)  #doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            Timeout: 0.1 seconds
    
        To simplify starting and canceling timeouts, the ``with`` statement can be used::
    
            with gevent.Timeout(seconds, exception) as timeout:
                pass  # ... code block ...
    
        This is equivalent to the try/finally block above with one additional feature:
        if *exception* is ``False``, the timeout is still raised, but the context manager
        suppresses it, so the code outside the with-block won't see it.
    
        This is handy for adding a timeout to the functions that don't
        support a *timeout* parameter themselves::
    
            data = None
            with gevent.Timeout(5, False):
                data = mysock.makefile().readline()
            if data is None:
                ...  # 5 seconds passed without reading a line
            else:
                ...  # a line was read within 5 seconds
    
        .. caution:: If ``readline()`` above catches and doesn't re-raise :class:`BaseException`
           (for example, with a bare ``except:``), then your timeout will fail to function and control
           won't be returned to you when you expect.
    
        When catching timeouts, keep in mind that the one you catch may
        not be the one you have set (a calling function may have set its
        own timeout); if you going to silence a timeout, always check that
        it's the instance you need::
    
            timeout = Timeout(1)
            timeout.start()
            try:
                ...
            except Timeout as t:
                if t is not timeout:
                    raise # not my timeout
    
        If the *seconds* argument is not given or is ``None`` (e.g.,
        ``Timeout()``), then the timeout will never expire and never raise
        *exception*. This is convenient for creating functions which take
        an optional timeout parameter of their own.
    
        .. versionchanged:: 1.1b2
           If *seconds* is not given or is ``None``, no longer allocate a libev
           timer that will never be started.
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        """ If the timeout is pending, cancel it. Otherwise, do nothing. """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """ Schedule the timeout. """
        pass

    @classmethod
    def start_new(cls, *args, **kwargs): # real signature unknown
        """
        Create a started :class:`Timeout`.
        
                This is a shortcut, the exact action depends on *timeout*'s type:
        
                * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
                  if it's not already begun.
                * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
                  arguments, then call its :meth:`start` method.
        
                Returns the :class:`Timeout` instance.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """
        >>> raise Timeout #doctest: +IGNORE_EXCEPTION_DETAIL
                Traceback (most recent call last):
                    ...
                Timeout
        """
        pass

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if the timeout is scheduled to be raised."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'Semaphore',
    'BoundedSemaphore',
]

__test__ = {}

