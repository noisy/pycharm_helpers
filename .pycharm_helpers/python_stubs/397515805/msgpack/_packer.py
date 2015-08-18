# encoding: utf-8
# module msgpack._packer
# from /usr/local/lib/python2.7/site-packages/msgpack/_packer.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import msgpack as __msgpack
import msgpack.exceptions as __msgpack_exceptions


# no functions
# classes

class ExtType(__msgpack.ExtType):
    """ ExtType represents ext type in msgpack. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, code, data): # reliably restored by inspect
        # no doc
        pass

    __dict__ = None # (!) real value is ''


class Packer(object):
    """
    Packer(default=None, encoding='utf-8', unicode_errors='strict', use_single_float=False, bool autoreset=1, bool use_bin_type=0)
    
        MessagePack Packer
    
        usage::
    
            packer = Packer()
            astream.write(packer.pack(a))
            astream.write(packer.pack(b))
    
        Packer's constructor has some keyword arguments:
    
        :param callable default:
            Convert user type to builtin type that Packer supports.
            See also simplejson's document.
        :param str encoding:
            Convert unicode to bytes with this encoding. (default: 'utf-8')
        :param str unicode_errors:
            Error handler for encoding unicode. (default: 'strict')
        :param bool use_single_float:
            Use single precision float type for float. (default: False)
        :param bool autoreset:
            Reset buffer after each pack and return it's content as `bytes`. (default: True).
            If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.
        :param bool use_bin_type:
            Use bin type introduced in msgpack spec 2.0 for bytes.
            It also enable str8 type for unicode.
    """
    def bytes(self): # real signature unknown; restored from __doc__
        """
        Packer.bytes(self)
        Return buffer content.
        """
        pass

    def pack(self, obj): # real signature unknown; restored from __doc__
        """ Packer.pack(self, obj) """
        pass

    def pack_array_header(self, size_t_size): # real signature unknown; restored from __doc__
        """ Packer.pack_array_header(self, size_t size) """
        pass

    def pack_ext_type(self, typecode, data): # real signature unknown; restored from __doc__
        """ Packer.pack_ext_type(self, typecode, data) """
        pass

    def pack_map_header(self, size_t_size): # real signature unknown; restored from __doc__
        """ Packer.pack_map_header(self, size_t size) """
        pass

    def pack_map_pairs(self, pairs): # real signature unknown; restored from __doc__
        """
        Packer.pack_map_pairs(self, pairs)
        
                Pack *pairs* as msgpack map type.
        
                *pairs* should sequence of pair.
                (`len(pairs)` and `for k, v in pairs:` should be supported.)
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        Packer.reset(self)
        Clear internal buffer.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class PackValueError(__msgpack_exceptions.PackException, ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__test__ = {}

