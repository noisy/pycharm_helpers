# encoding: utf-8
# module scss.grammar._scanner
# from /usr/local/lib/python2.7/site-packages/scss/grammar/_scanner.so
# by generator 1.136
# no doc
# no imports

# functions

def locate_blocks(*args, **kwargs): # real signature unknown
    """ Locate Scss blocks. """
    pass

# classes

class NoMoreTokens(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Scanner(object):
    """ Scanner object. """
    def reset(self, *args, **kwargs): # real signature unknown
        """ Scan the next token """
        pass

    def rewind(self, *args, **kwargs): # real signature unknown
        """ Rewind scanner """
        pass

    def setup_patterns(self, *args, **kwargs): # real signature unknown
        """ Initialize patterns. """
        pass

    def token(self, *args, **kwargs): # real signature unknown
        """ Get the nth token """
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


class _BlockLocator(object):
    """ Internal BlockLocator iterator object. """
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


