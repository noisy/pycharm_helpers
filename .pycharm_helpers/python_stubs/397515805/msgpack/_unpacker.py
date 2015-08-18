# encoding: utf-8
# module msgpack._unpacker
# from /usr/local/lib/python2.7/site-packages/msgpack/_unpacker.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import msgpack as __msgpack
import msgpack.exceptions as __msgpack_exceptions


# functions

def default_read_extended_type(typecode, data): # real signature unknown; restored from __doc__
    """ default_read_extended_type(typecode, data) """
    pass

def unpack(stream, object_hook=None, list_hook=None, bool_use_list=1, encoding=None, unicode_errors='strict', object_pairs_hook=None): # real signature unknown; restored from __doc__
    """
    unpack(stream, object_hook=None, list_hook=None, bool use_list=1, encoding=None, unicode_errors='strict', object_pairs_hook=None)
    
        Unpack an object from `stream`.
    
        Raises `ValueError` when `stream` has extra bytes.
    
        See :class:`Unpacker` for options.
    """
    pass

def unpackb(packed, object_hook=None, list_hook=None, bool_use_list=1, encoding=None, unicode_errors='strict', object_pairs_hook=None, ext_hook=None, Py_ssize_t_max_str_len=2147483647, Py_ssize_t_max_bin_len=2147483647, Py_ssize_t_max_array_len=2147483647, Py_ssize_t_max_map_len=2147483647, Py_ssize_t_max_ext_len=2147483647): # real signature unknown; restored from __doc__
    """
    unpackb(packed, object_hook=None, list_hook=None, bool use_list=1, encoding=None, unicode_errors='strict', object_pairs_hook=None, ext_hook=ExtType, Py_ssize_t max_str_len=2147483647, Py_ssize_t max_bin_len=2147483647, Py_ssize_t max_array_len=2147483647, Py_ssize_t max_map_len=2147483647, Py_ssize_t max_ext_len=2147483647)
    
        Unpack packed_bytes to object. Returns an unpacked object.
    
        Raises `ValueError` when `packed` contains extra bytes.
    
        See :class:`Unpacker` for options.
    """
    pass

# classes

class BufferFull(__msgpack_exceptions.UnpackException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ExtraData(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ExtType(__msgpack.ExtType):
    """ ExtType represents ext type in msgpack. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, code, data): # reliably restored by inspect
        # no doc
        pass

    __dict__ = None # (!) real value is ''


class OutOfData(__msgpack_exceptions.UnpackException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Unpacker(object):
    """
    Unpacker(file_like=None, Py_ssize_t read_size=0, bool use_list=1, object_hook=None, object_pairs_hook=None, list_hook=None, encoding=None, unicode_errors='strict', int max_buffer_size=0, ext_hook=ExtType, Py_ssize_t max_str_len=2147483647, Py_ssize_t max_bin_len=2147483647, Py_ssize_t max_array_len=2147483647, Py_ssize_t max_map_len=2147483647, Py_ssize_t max_ext_len=2147483647)
    Streaming unpacker.
    
        arguments:
    
        :param file_like:
            File-like object having `.read(n)` method.
            If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.
    
        :param int read_size:
            Used as `file_like.read(read_size)`. (default: `min(1024**2, max_buffer_size)`)
    
        :param bool use_list:
            If true, unpack msgpack array to Python list.
            Otherwise, unpack to Python tuple. (default: True)
    
        :param callable object_hook:
            When specified, it should be callable.
            Unpacker calls it with a dict argument after unpacking msgpack map.
            (See also simplejson)
    
        :param callable object_pairs_hook:
            When specified, it should be callable.
            Unpacker calls it with a list of key-value pairs after unpacking msgpack map.
            (See also simplejson)
    
        :param str encoding:
            Encoding used for decoding msgpack raw.
            If it is None (default), msgpack raw is deserialized to Python bytes.
    
        :param str unicode_errors:
            Used for decoding msgpack raw with *encoding*.
            (default: `'strict'`)
    
        :param int max_buffer_size:
            Limits size of data waiting unpacked.  0 means system's INT_MAX (default).
            Raises `BufferFull` exception when it is insufficient.
            You shoud set this parameter when unpacking data from untrasted source.
    
        :param int max_str_len:
            Limits max length of str. (default: 2**31-1)
    
        :param int max_bin_len:
            Limits max length of bin. (default: 2**31-1)
    
        :param int max_array_len:
            Limits max length of array. (default: 2**31-1)
    
        :param int max_map_len:
            Limits max length of map. (default: 2**31-1)
    
    
        example of streaming deserialize from file-like object::
    
            unpacker = Unpacker(file_like)
            for o in unpacker:
                process(o)
    
        example of streaming deserialize from socket::
    
            unpacker = Unpacker()
            while True:
                buf = sock.recv(1024**2)
                if not buf:
                    break
                unpacker.feed(buf)
                for o in unpacker:
                    process(o)
    """
    def feed(self, next_bytes): # real signature unknown; restored from __doc__
        """
        Unpacker.feed(self, next_bytes)
        Append `next_bytes` to internal buffer.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read_array_header(self, write_bytes=None): # real signature unknown; restored from __doc__
        """
        Unpacker.read_array_header(self, write_bytes=None)
        assuming the next object is an array, return its size n, such that
                the next n unpack() calls will iterate over its contents.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def read_bytes(self, Py_ssize_t_nbytes): # real signature unknown; restored from __doc__
        """
        Unpacker.read_bytes(self, Py_ssize_t nbytes)
        Read a specified number of raw bytes from the stream
        """
        pass

    def read_map_header(self, write_bytes=None): # real signature unknown; restored from __doc__
        """
        Unpacker.read_map_header(self, write_bytes=None)
        assuming the next object is a map, return its size n, such that the
                next n * 2 unpack() calls will iterate over its key-value pairs.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def skip(self, write_bytes=None): # real signature unknown; restored from __doc__
        """
        Unpacker.skip(self, write_bytes=None)
        Read and ignore one object, returning None
        
                If write_bytes is not None, it will be called with parts of the raw
                message as it is unpacked.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def unpack(self, write_bytes=None): # real signature unknown; restored from __doc__
        """
        Unpacker.unpack(self, write_bytes=None)
        Unpack one object
        
                If write_bytes is not None, it will be called with parts of the raw
                message as it is unpacked.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def __init__(self, file_like=None, Py_ssize_t_read_size=0, bool_use_list=1, object_hook=None, object_pairs_hook=None, list_hook=None, encoding=None, unicode_errors='strict', int_max_buffer_size=0, ext_hook=None, Py_ssize_t_max_str_len=2147483647, Py_ssize_t_max_bin_len=2147483647, Py_ssize_t_max_array_len=2147483647, Py_ssize_t_max_map_len=2147483647, Py_ssize_t_max_ext_len=2147483647): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class UnpackValueError(__msgpack_exceptions.UnpackException, ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__test__ = {}

