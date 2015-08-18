# encoding: utf-8
# module _billiard
# from /usr/local/lib/python2.7/site-packages/_billiard.so
# by generator 1.136
# no doc
# no imports

# functions

def address_of_buffer(obj): # real signature unknown; restored from __doc__
    """
    address_of_buffer(obj) -> int
    
    Return address of obj assuming obj supports buffer inteface
    """
    return 0

def read(fd, buffer): # real signature unknown; restored from __doc__
    """
    read(fd, buffer) -> bytes
    
    Read from file descriptor into buffer.
    """
    return ""

def recvfd(sockfd): # real signature unknown; restored from __doc__
    """
    recvfd(sockfd) -> fd
    
    Receive a file descriptor over a unix domain socket
    whose file decriptor is sockfd
    """
    pass

def sendfd(sockfd, fd): # real signature unknown; restored from __doc__
    """
    sendfd(sockfd, fd) -> None
    
    Send file descriptor given by fd over the unix domain socket
    whose file decriptor is sockfd
    """
    pass

# classes

class Connection(object):
    """
    Connection type whose constructor signature is
    
        Connection(handle, readable=True, writable=True).
    
    The constructor does *not* duplicate the handle.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """ close the connection """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ file descriptor or handle of the connection """
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        """ whether there is any input available to be read """
        pass

    def recv(self, *args, **kwargs): # real signature unknown
        """ receive a (picklable) object """
        pass

    def recv_bytes(self, *args, **kwargs): # real signature unknown
        """ receive byte data as a string """
        pass

    def recv_bytes_into(self, *args, **kwargs): # real signature unknown
        """
        receive byte data into a writeable buffer-like object
        returns the number of bytes read
        """
        pass

    def recv_payload(self, *args, **kwargs): # real signature unknown
        """ receive raw payload (not unpickled) """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """ send a (picklable) object """
        pass

    def send_bytes(self, *args, **kwargs): # real signature unknown
        """ send the byte data from a readable buffer-like object """
        pass

    def send_offset(self, *args, **kwargs): # real signature unknown
        """ send string/buffer (non-blocking) """
        pass

    def setblocking(self, *args, **kwargs): # real signature unknown
        """ set socket blocking/non-blocking """
        pass

    def __init__(self, handle, readable=True, writable=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is closed"""

    readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is readable"""

    writable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is writable"""



class SemLock(object):
    """ Semaphore/Mutex type """
    def acquire(self, *args, **kwargs): # real signature unknown
        """ acquire the semaphore/lock """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """ release the semaphore/lock """
        pass

    def sem_unlink(self): # real signature unknown; restored from __doc__
        """ unlink the named semaphore using sem_unlink() """
        pass

    def _after_fork(self, *args, **kwargs): # real signature unknown
        """ rezero the net acquisition count after fork() """
        pass

    def _count(self, *args, **kwargs): # real signature unknown
        """ num of `acquire()`s minus num of `release()`s for this process """
        pass

    def _get_value(self, *args, **kwargs): # real signature unknown
        """ get the value of the semaphore """
        pass

    def _is_mine(self, *args, **kwargs): # real signature unknown
        """ whether the lock is owned by this thread """
        pass

    def _is_zero(self, *args, **kwargs): # real signature unknown
        """ returns whether semaphore has value zero """
        pass

    @classmethod
    def _rebuild(cls, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ enter the semaphore/lock """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ exit the semaphore/lock """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxvalue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    SEM_VALUE_MAX = 2147483647


# variables with complex values

flags = {
    'HAVE_FD_TRANSFER': 1,
    'HAVE_SEM_OPEN': 1,
    'HAVE_SEM_TIMEDWAIT': 1,
}

