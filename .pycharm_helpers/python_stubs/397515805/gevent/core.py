# encoding: utf-8
# module gevent.core
# from /usr/local/lib/python2.7/site-packages/gevent/core.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import traceback as traceback # /usr/local/lib/python2.7/traceback.pyc
import signal as signalmodule # <module 'signal' (built-in)>
import os as os # /usr/local/lib/python2.7/os.pyc

# Variables with simple values

ASYNC = 524288

BACKEND_EPOLL = 4
BACKEND_KQUEUE = 8
BACKEND_POLL = 2
BACKEND_PORT = 32
BACKEND_SELECT = 1

CHECK = 32768
CHILD = 2048

CLEANUP = 262144

CUSTOM = 16777216

EMBED = 65536

ERROR = -2147483648

EV_USE_4HEAP = 2

EV_USE_CLOCK_SYSCALL = 0

EV_USE_EVENTFD = 64
EV_USE_FLOOR = 1
EV_USE_INOTIFY = 64
EV_USE_MONOTONIC = 1
EV_USE_NANOSLEEP = 64
EV_USE_REALTIME = 0
EV_USE_SIGNALFD = 64

FORK = 131072
FORKCHECK = 33554432

IDLE = 8192

LIBEV_EMBED = True

MAXPRI = 2

MINPRI = -2

NOINOTIFY = 1048576
NONE = 0
NOSIGMASK = 4194304

PERIODIC = 512

PREPARE = 16384

READ = 1
READWRITE = 3

SIGNAL = 1024
SIGNALFD = 2097152

STAT = 4096

TIMER = 256

UNDEF = -1

WRITE = 2

__SYSERR_CALLBACK = None

# functions

def embeddable_backends(*args, **kwargs): # real signature unknown
    pass

def get_header_version(*args, **kwargs): # real signature unknown
    pass

def get_version(*args, **kwargs): # real signature unknown
    pass

def recommended_backends(*args, **kwargs): # real signature unknown
    pass

def set_syserr_cb(*args, **kwargs): # real signature unknown
    pass

def supported_backends(*args, **kwargs): # real signature unknown
    pass

def time(*args, **kwargs): # real signature unknown
    pass

def _check_flags(*args, **kwargs): # real signature unknown
    pass

def _events_to_str(*args, **kwargs): # real signature unknown
    pass

def _flags_to_int(*args, **kwargs): # real signature unknown
    pass

def _flags_to_list(*args, **kwargs): # real signature unknown
    pass

# classes

class watcher(object):
    """ Abstract base class for all the watchers """
    def _format(self, *args, **kwargs): # real signature unknown
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


class async(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def send(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class basestring(object):
    """ Type basestring cannot be instantiated; it is the base for str and unicode. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class callback(object):
    # no doc
    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class check(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class child(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rpid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rstatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class fork(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class idle(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class io(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    events_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class loop(object):
    # no doc
    def async(self, *args, **kwargs): # real signature unknown
        pass

    def break_(self, *args, **kwargs): # real signature unknown
        pass

    def check(self, *args, **kwargs): # real signature unknown
        pass

    def child(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def fork(self, *args, **kwargs): # real signature unknown
        pass

    def handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def idle(self, *args, **kwargs): # real signature unknown
        pass

    def install_sigchld(self, *args, **kwargs): # real signature unknown
        pass

    def io(self, *args, **kwargs): # real signature unknown
        pass

    def now(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def reinit(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def run_callback(self, *args, **kwargs): # real signature unknown
        pass

    def signal(self, *args, **kwargs): # real signature unknown
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        pass

    def timer(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        pass

    def _default_handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def _format_details(self, *args, **kwargs): # real signature unknown
        pass

    def _handle_syserr(self, *args, **kwargs): # real signature unknown
        pass

    def _stop_watchers(self, *args, **kwargs): # real signature unknown
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

    activecnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iteration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MAXPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MINPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pendingcnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sigfd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sig_pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    WatcherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _callbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class prepare(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class signal(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class stat(watcher):
    # no doc
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    attr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class timer(watcher):
    # no doc
    def again(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

EVENTS = None # (!) real value is ''

_events = [
    (
        1,
        'READ',
    ),
    (
        2,
        'WRITE',
    ),
    (
        128,
        '_IOFDSET',
    ),
    (
        512,
        'PERIODIC',
    ),
    (
        1024,
        'SIGNAL',
    ),
    (
        2048,
        'CHILD',
    ),
    (
        4096,
        'STAT',
    ),
    (
        8192,
        'IDLE',
    ),
    (
        16384,
        'PREPARE',
    ),
    (
        32768,
        'CHECK',
    ),
    (
        65536,
        'EMBED',
    ),
    (
        131072,
        'FORK',
    ),
    (
        262144,
        'CLEANUP',
    ),
    (
        524288,
        'ASYNC',
    ),
    (
        16777216,
        'CUSTOM',
    ),
    (
        -2147483648,
        'ERROR',
    ),
]

_flags = [
    (
        32,
        'port',
    ),
    (
        8,
        'kqueue',
    ),
    (
        4,
        'epoll',
    ),
    (
        2,
        'poll',
    ),
    (
        1,
        'select',
    ),
    (
        16777216,
        'noenv',
    ),
    (
        33554432,
        'forkcheck',
    ),
    (
        1048576,
        'noinotify',
    ),
    (
        2097152,
        'signalfd',
    ),
    (
        4194304,
        'nosigmask',
    ),
]

_flags_str2int = {
    'epoll': 4,
    'forkcheck': 33554432,
    'kqueue': 8,
    'noenv': 16777216,
    'noinotify': 1048576,
    'nosigmask': 4194304,
    'poll': 2,
    'port': 32,
    'select': 1,
    'signalfd': 2097152,
}

__all__ = [
    'get_version',
    'get_header_version',
    'supported_backends',
    'recommended_backends',
    'embeddable_backends',
    'time',
    'loop',
]

__test__ = {}

