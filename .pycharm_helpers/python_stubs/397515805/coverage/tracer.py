# encoding: utf-8
# module coverage.tracer
# from /usr/local/lib/python2.7/site-packages/coverage/tracer.so
# by generator 1.136
""" Fast coverage tracer. """
# no imports

# no functions
# classes

class CTracer(object):
    """ CTracer objects """
    def get_stats(self, *args, **kwargs): # real signature unknown
        """ Get statistics about the tracing """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """ Start the tracer """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        """ Stop the tracer """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    arcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should we trace arcs, or just lines?"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw dictionary of trace data."""

    should_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function indicating whether to trace a file."""

    should_trace_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary caching should_trace results."""

    warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for issuing warnings."""



