# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python2.7/site-packages/psycopg2/_psycopg.so
# by generator 1.136
""" psycopg PostgreSQL driver """

# imports
import psycopg2 as __psycopg2


# Variables with simple values

apilevel = '2.0'

paramstyle = 'pyformat'

threadsafety = 2

__version__ = '2.6.1 (dt dec pq3 ext lo64)'

# functions

def adapt(obj, protocol, alternate): # real signature unknown; restored from __doc__
    """ adapt(obj, protocol, alternate) -> object -- adapt obj to given protocol """
    return object()

def BINARY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BINARYARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BOOLEAN(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BOOLEANARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def Date(year, month, day): # real signature unknown; restored from __doc__
    """
    Date(year, month, day) -> new date
    
    Build an object holding a date value.
    """
    pass

def DATEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DateFromPy(datetime_date): # real signature unknown; restored from __doc__
    """ DateFromPy(datetime.date) -> new wrapper """
    pass

def DateFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    DateFromTicks(ticks) -> new date
    
    Build an object holding a date value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def DATETIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATETIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DECIMAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DECIMALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def FLOAT(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def FLOATARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def get_wait_callback(*args, **kwargs): # real signature unknown
    """
    Return the currently registered wait callback.
    
    Return `!None` if no callback is currently registered.
    """
    pass

def INTEGER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTEGERARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTERVAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTERVALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def IntervalFromPy(datetime_timedelta): # real signature unknown; restored from __doc__
    """ IntervalFromPy(datetime.timedelta) -> new wrapper """
    pass

def LONGINTEGER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def LONGINTEGERARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def new_array_type(oids, name, baseobj): # real signature unknown; restored from __doc__
    """
    new_array_type(oids, name, baseobj) -> new type object
    
    Create a new binding object to parse an array.
    
    The object can be used with `register_type()`.
    
    :Parameters:
      * `oids`: Tuple of ``oid`` of the PostgreSQL types to convert.
      * `name`: Name for the new type
      * `baseobj`: Adapter to perform type conversion of a single array item.
    """
    pass

def new_type(oids, name, castobj): # real signature unknown; restored from __doc__
    """
    new_type(oids, name, castobj) -> new type object
    
    Create a new binding object. The object can be used with the
    `register_type()` function to bind PostgreSQL objects to python objects.
    
    :Parameters:
      * `oids`: Tuple of ``oid`` of the PostgreSQL types to convert.
      * `name`: Name for the new type
      * `adapter`: Callable to perform type conversion.
        It must have the signature ``fun(value, cur)`` where ``value`` is
        the string representation returned by PostgreSQL (`!None` if ``NULL``)
        and ``cur`` is the cursor from which data are read.
    """
    pass

def NUMBER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYINTERVAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYINTERVALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYTIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYTIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def register_type(obj, conn_or_curs): # real signature unknown; restored from __doc__
    """
    register_type(obj, conn_or_curs) -> None -- register obj with psycopg type system
    
    :Parameters:
      * `obj`: A type adapter created by `new_type()`
      * `conn_or_curs`: A connection, cursor or None
    """
    pass

def ROWID(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def ROWIDARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def set_wait_callback(None): # real signature unknown; restored from __doc__
    """
    Register a callback function to block waiting for data.
    
    The callback should have signature :samp:`fun({conn})` and
    is called to wait for data available whenever a blocking function from the
    libpq is called.  Use `!set_wait_callback(None)` to revert to the
    original behaviour (i.e. using blocking libpq functions).
    
    The function is an hook to allow coroutine-based libraries (such as
    Eventlet_ or gevent_) to switch when Psycopg is blocked, allowing
    other coroutines to run concurrently.
    
    See `~psycopg2.extras.wait_select()` for an example of a wait callback
    implementation.
    
    .. _Eventlet: http://eventlet.net/
    .. _gevent: http://www.gevent.org/
    """
    pass

def STRING(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def STRINGARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def TIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def Time(hour, minutes, seconds, tzinfo=None): # real signature unknown; restored from __doc__
    """
    Time(hour, minutes, seconds, tzinfo=None) -> new time
    
    Build an object holding a time value.
    """
    pass

def TIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def TimeFromPy(datetime_time): # real signature unknown; restored from __doc__
    """ TimeFromPy(datetime.time) -> new wrapper """
    pass

def TimeFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimeFromTicks(ticks) -> new time
    
    Build an object holding a time value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def Timestamp(year, month, day, hour, minutes, seconds, tzinfo=None): # real signature unknown; restored from __doc__
    """
    Timestamp(year, month, day, hour, minutes, seconds, tzinfo=None) -> new timestamp
    
    Build an object holding a timestamp value.
    """
    pass

def TimestampFromPy(datetime_datetime): # real signature unknown; restored from __doc__
    """ TimestampFromPy(datetime.datetime) -> new wrapper """
    pass

def TimestampFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimestampFromTicks(ticks) -> new timestamp
    
    Build an object holding a timestamp value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def UNICODE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def UNICODEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def UNKNOWN(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def _connect(dsn, connection_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _connect(dsn, [connection_factory], [async]) -- New database connection. """
    pass

# classes

class AsIs(object):
    """ AsIs(str) -> new AsIs adapter object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Binary(object):
    """ Binary(buffer) -> new binary object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted binary string """
        pass

    def prepare(self, conn): # real signature unknown; restored from __doc__
        """ prepare(conn) -> prepare for binary encoding using conn """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, buffer): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Boolean(object):
    """ Boolean(str) -> new Boolean adapter object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Column(tuple):
    """ Column(name, type_code, display_size, internal_size, precision, scale, null_ok) """
    def _asdict(self, *args, **kwargs): # real signature unknown
        """ Return a new OrderedDict which maps field names to their values """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Column object from a sequence or iterable """
        pass

    def _replace(self, *args, **kwargs): # real signature unknown
        """ Return a new Column object replacing specified fields with new values """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Exclude the OrderedDict from pickling """
        pass

    def __init__(self, name, type_code, display_size, internal_size, precision, scale, null_ok): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, name, type_code, display_size, internal_size, precision, scale, null_ok): # reliably restored by inspect
        """ Create new instance of Column(name, type_code, display_size, internal_size, precision, scale, null_ok) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return a nicely formatted representation string """
        pass

    display_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    internal_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    null_ok = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 6"""

    precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    type_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'name',
        'type_code',
        'display_size',
        'internal_size',
        'precision',
        'scale',
        'null_ok',
    )
    __dict__ = None # (!) real value is ''
    __slots__ = ()


class connection(object):
    """
    connection(dsn, ...) -> new connection object
    
    :Groups:
      * `DBAPI-2.0 errors`: Error, Warning, InterfaceError,
        DatabaseError, InternalError, OperationalError,
        ProgrammingError, IntegrityError, DataError, NotSupportedError
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel() -- cancel the current operation """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close() -- Close the connection. """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit() -- Commit all changes to database. """
        pass

    def cursor(self, name=None, cursor_factory=None, withhold=False): # real signature unknown; restored from __doc__
        """
        cursor(name=None, cursor_factory=extensions.cursor, withhold=False) -- new cursor
        
        Return a new cursor.
        
        The ``cursor_factory`` argument can be used to
        create non-standard cursors by passing a class different from the
        default. Note that the new class *should* be a sub-class of
        `extensions.cursor`.
        
        :rtype: `extensions.cursor`
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """ fileno() -> int -- Return file descriptor associated to database connection. """
        return 0

    def get_backend_pid(self): # real signature unknown; restored from __doc__
        """ get_backend_pid() -- Get backend process id. """
        pass

    def get_parameter_status(self, parameter): # real signature unknown; restored from __doc__
        """
        get_parameter_status(parameter) -- Get backend parameter status.
        
        Potential values for ``parameter``:
          server_version, server_encoding, client_encoding, is_superuser,
          session_authorization, DateStyle, TimeZone, integer_datetimes,
          and standard_conforming_strings
        If server did not report requested parameter, None is returned.
        
        See libpq docs for PQparameterStatus() for further details.
        """
        pass

    def get_transaction_status(self): # real signature unknown; restored from __doc__
        """ get_transaction_status() -- Get backend transaction status. """
        pass

    def isexecuting(self): # real signature unknown; restored from __doc__
        """ isexecuting() -> bool -- Return True if the connection is executing an asynchronous operation. """
        return False

    def lobject(self, oid=0, mode=0, new_oid=0, new_file=None, lobject_factory=None): # real signature unknown; restored from __doc__
        """
        lobject(oid=0, mode=0, new_oid=0, new_file=None,
               lobject_factory=extensions.lobject) -- new lobject
        
        Return a new lobject.
        
        The ``lobject_factory`` argument can be used
        to create non-standard lobjects by passing a class different from the
        default. Note that the new class *should* be a sub-class of
        `extensions.lobject`.
        
        :rtype: `extensions.lobject`
        """
        pass

    def poll(self): # real signature unknown; restored from __doc__
        """ poll() -> int -- Advance the connection or query process without blocking. """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset() -- Reset current connection to defaults. """
        pass

    def rollback(self): # real signature unknown; restored from __doc__
        """ rollback() -- Roll back all changes done to database. """
        pass

    def set_client_encoding(self, encoding): # real signature unknown; restored from __doc__
        """ set_client_encoding(encoding) -- Set client encoding to ``encoding``. """
        pass

    def set_isolation_level(self, level): # real signature unknown; restored from __doc__
        """ set_isolation_level(level) -- Switch isolation level to ``level``. """
        pass

    def set_session(self, *more): # real signature unknown; restored from __doc__
        """
        set_session(...) -- Set one or more parameters for the next transactions.
        
        Accepted arguments are 'isolation_level', 'readonly', 'deferrable', 'autocommit'.
        """
        pass

    def tpc_begin(self, xid): # real signature unknown; restored from __doc__
        """ tpc_begin(xid) -- begin a TPC transaction with given transaction ID xid. """
        pass

    def tpc_commit(self, xid=None): # real signature unknown; restored from __doc__
        """ tpc_commit([xid]) -- commit a transaction previously prepared. """
        pass

    def tpc_prepare(self): # real signature unknown; restored from __doc__
        """ tpc_prepare() -- perform the first phase of a two-phase transaction. """
        pass

    def tpc_recover(self): # real signature unknown; restored from __doc__
        """ tpc_recover() -- returns a list of pending transaction IDs. """
        pass

    def tpc_rollback(self, xid=None): # real signature unknown; restored from __doc__
        """ tpc_rollback([xid]) -- abort a transaction previously prepared. """
        pass

    def xid(self, format_id, gtrid, bqual): # real signature unknown; restored from __doc__
        """ xid(format_id, gtrid, bqual) -- create a transaction identifier. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ __enter__ -> self """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ __exit__ -- commit if no exception, else roll back """
        pass

    def __init__(self, dsn, *more): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is asynchronous."""

    autocommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set or return the autocommit status."""

    binary_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A set of typecasters to convert binary values."""

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is closed."""

    cursor_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default cursor_factory for cursor()."""

    DatabaseError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to the database engine."""

    DataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to problems with the processed data."""

    dsn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current connection string."""

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current client encoding."""

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Base class for error exceptions."""

    IntegrityError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to database integrity."""

    InterfaceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to the database interface."""

    InternalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The database encountered an internal error."""

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current isolation level."""

    notices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notifies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NotSupportedError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A method or database API was used which is not supported by the database."""

    OperationalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to database operation (disconnect, memory allocation etc)."""

    ProgrammingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error related to database programming (SQL error, table not found etc)."""

    protocol_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Protocol version used for this connection. Currently always 3."""

    server_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Server version."""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current transaction status."""

    string_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A set of typecasters to convert textual values."""

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A database warning."""



class cursor(object):
    """ A database cursor. """
    def callproc(self, procname, parameters=None): # real signature unknown; restored from __doc__
        """ callproc(procname, parameters=None) -- Execute stored procedure. """
        pass

    def cast(self, oid, s): # real signature unknown; restored from __doc__
        """
        cast(oid, s) -> value
        
        Convert the string s to a Python object according to its oid.
        
        Look for a typecaster first in the cursor, then in its connection,then in the global register. If no suitable typecaster is found,leave the value as a string.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close() -- Close the cursor. """
        pass

    def copy_expert(self, sql, file, size=8192): # real signature unknown; restored from __doc__
        """
        copy_expert(sql, file, size=8192) -- Submit a user-composed COPY statement.
        `file` must be an open, readable file for COPY FROM or an open, writable
        file for COPY TO. The optional `size` argument, when specified for a COPY
        FROM statement, will be passed to file's read method to control the read
        buffer size.
        """
        pass

    def copy_from(self, file, table, sep=None, null=None, size=8192, columns=None): # real signature unknown; restored from __doc__
        """ copy_from(file, table, sep='\t', null='\\N', size=8192, columns=None) -- Copy table from file. """
        pass

    def copy_to(self, file, table, sep=None, null=None, columns=None): # real signature unknown; restored from __doc__
        """ copy_to(file, table, sep='\t', null='\\N', columns=None) -- Copy table to file. """
        pass

    def execute(self, query, vars=None): # real signature unknown; restored from __doc__
        """ execute(query, vars=None) -- Execute query with bound vars. """
        pass

    def executemany(self, query, vars_list): # real signature unknown; restored from __doc__
        """ executemany(query, vars_list) -- Execute many queries with bound vars. """
        pass

    def fetchall(self): # real signature unknown; restored from __doc__
        """
        fetchall() -> list of tuple
        
        Return all the remaining rows of a query result set.
        
        Rows are returned in the form of a list of tuples (by default) or using
        the sequence factory previously set in the `row_factory` attribute.
        Return `!None` when no more data is available.
        """
        return []

    def fetchmany(self, size=None): # real signature unknown; restored from __doc__
        """
        fetchmany(size=self.arraysize) -> list of tuple
        
        Return the next `size` rows of a query result set in the form of a list
        of tuples (by default) or using the sequence factory previously set in
        the `row_factory` attribute.
        
        Return an empty list when no more data is available.
        """
        return []

    def fetchone(self): # real signature unknown; restored from __doc__
        """
        fetchone() -> tuple or None
        
        Return the next row of a query result set in the form of a tuple (by
        default) or using the sequence factory previously set in the
        `row_factory` attribute. Return `!None` when no more data is available.
        """
        return ()

    def mogrify(self, query, vars=None): # real signature unknown; restored from __doc__
        """ mogrify(query, vars=None) -> str -- Return query after vars binding. """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def nextset(self): # real signature unknown; restored from __doc__
        """
        nextset() -- Skip to next set of data.
        
        This method is not supported (PostgreSQL does not have multiple data 
        sets) and will raise a NotSupportedError exception.
        """
        pass

    def scroll(self, value, mode='relative'): # real signature unknown; restored from __doc__
        """ scroll(value, mode='relative') -- Scroll to new position according to mode. """
        pass

    def setinputsizes(self, sizes): # real signature unknown; restored from __doc__
        """
        setinputsizes(sizes) -- Set memory areas before execute.
        
        This method currently does nothing but it is safe to call it.
        """
        pass

    def setoutputsize(self, size, column=None): # real signature unknown; restored from __doc__
        """
        setoutputsize(size, column=None) -- Set column buffer size.
        
        This method currently does nothing but it is safe to call it.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ __enter__ -> self """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ __exit__ -- close the cursor """
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of records `fetchmany()` must fetch if not explicitly specified."""

    binary_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if cursor is closed, False if cursor is open"""

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connection where the cursor comes from."""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cursor description as defined in DBAPI-2.0."""

    itersize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of records ``iter(cur)`` must fetch per network roundtrip."""

    lastrowid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ``oid`` of the last row inserted by the cursor."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The last query text sent to the backend."""

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of rows read from the backend in the last command."""

    rownumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current row position."""

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scrollable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set or return cursor use of SCROLL"""

    statusmessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The return message of the last command."""

    string_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typecaster = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    withhold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set or return cursor use of WITH HOLD"""



class Error(StandardError):
    """ Base class for error exceptions. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cursor that raised the exception, if available, else None"""

    diag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A Diagnostics object to get further information about the error"""

    pgcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The error code returned by the backend, if available, else None"""

    pgerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The error message returned by the backend, if available, else None"""



class DatabaseError(__psycopg2.Error):
    """ Error related to the database engine. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DataError(__psycopg2.DatabaseError):
    """ Error related to problems with the processed data. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Decimal(object):
    """ Decimal(str) -> new Decimal adapter object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Diagnostics(object):
    """
    Details from a database error report.
    
    The object is returned by the `~psycopg2.Error.diag` attribute of the
    `!Error` object.
    All the information available from the |PQresultErrorField|_ function
    are exposed as attributes by the object, e.g. the `!severity` attribute
    returns the `!PG_DIAG_SEVERITY` code. Please refer to the `PostgreSQL documentation`__ for the meaning of all the attributes.
    
    .. |PQresultErrorField| replace:: `!PQresultErrorField()`
    .. _PQresultErrorField: http://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQRESULTERRORFIELD
    .. __: PQresultErrorField_
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    column_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constraint_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    datatype_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    internal_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    internal_query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_detail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_primary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schema_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sqlstate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    statement_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Float(object):
    """ Float(str) -> new Float adapter object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Int(object):
    """ Int(str) -> new Int adapter object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IntegrityError(__psycopg2.DatabaseError):
    """ Error related to database integrity. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(__psycopg2.Error):
    """ Error related to the database interface. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class InternalError(__psycopg2.DatabaseError):
    """ The database encountered an internal error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ISQLQuote(object):
    """
    Abstract ISQLQuote protocol
    
    An object conform to this protocol should expose a ``getquoted()`` method
    returning the SQL representation of the object.
    """
    def getbinary(self): # real signature unknown; restored from __doc__
        """ getbinary() -- return SQL-quoted binary representation of this object """
        pass

    def getbuffer(self): # real signature unknown; restored from __doc__
        """ getbuffer() -- return this object """
        pass

    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -- return SQL-quoted representation of this object """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    _wrapped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class List(object):
    """ List(list) -> new list wrapper object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL date/time """
        pass

    def prepare(self, conn): # real signature unknown; restored from __doc__
        """ prepare(conn) -> set encoding to conn->encoding """
        return set(*(), **{})

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_list): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class lobject(object):
    """ A database large object. """
    def close(self): # real signature unknown; restored from __doc__
        """ close() -- Close the lobject. """
        pass

    def export(self, filename): # real signature unknown; restored from __doc__
        """ export(filename) -- Export large object to given file. """
        pass

    def read(self, size=-1): # real signature unknown; restored from __doc__
        """ read(size=-1) -- Read at most size bytes or to the end of the large object. """
        pass

    def seek(self, offset, whence=0): # real signature unknown; restored from __doc__
        """ seek(offset, whence=0) -- Set the lobject's current position. """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """ tell() -- Return the lobject's current position. """
        pass

    def truncate(self, len=0): # real signature unknown; restored from __doc__
        """ truncate(len=0) -- Truncate large object to given size. """
        pass

    def unlink(self): # real signature unknown; restored from __doc__
        """ unlink() -- Close and then remove the lobject. """
        pass

    def write(self, p_str): # real signature unknown; restored from __doc__
        """ write(str) -- Write a string to the large object. """
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

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The if the large object is closed (no file-like methods)."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Open mode."""

    oid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The backend OID associated to this lobject."""



class Notify(object):
    """
    A notification received from the backend.
    
    `!Notify` instances are made available upon reception on the
    `~connection.notifies` member of the listening connection. The object
    can be also accessed as a 2 items tuple returning the members
    :samp:`({pid},{channel})` for backward compatibility.
    
    See :ref:`async-notify` for details.
    """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the channel to which the notification was sent."""

    payload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The payload message of the notification.

Attaching a payload to a notification is only available since
PostgreSQL 9.0: for notifications received from previous versions
of the server this member is always the empty string."""

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the backend process that sent the notification.

Note: if the sending session was handled by Psycopg, you can use
`~connection.get_backend_pid()` to know its PID."""



class NotSupportedError(__psycopg2.DatabaseError):
    """ A method or database API was used which is not supported by the database. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(__psycopg2.DatabaseError):
    """ Error related to database operation (disconnect, memory allocation etc). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ProgrammingError(__psycopg2.DatabaseError):
    """ Error related to database programming (SQL error, table not found etc). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QueryCanceledError(__psycopg2.OperationalError):
    """ Error related to SQL query cancellation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QuotedString(object):
    """ QuotedString(str) -> new quoted object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted string """
        pass

    def prepare(self, conn): # real signature unknown; restored from __doc__
        """ prepare(conn) -> set encoding to conn->encoding and store conn """
        return set(*(), **{})

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current encoding of the adapter"""



class TransactionRollbackError(__psycopg2.OperationalError):
    """ Error causing transaction rollback (deadlocks, serialization failures, etc). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Warning(StandardError):
    """ A database warning. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Xid(object):
    """
    A transaction identifier used for two-phase commit.
    
    Usually returned by the connection methods `~connection.xid()` and
    `~connection.tpc_recover()`.
    `!Xid` instances can be unpacked as a 3-item tuples containing the items
    :samp:`({format_id},{gtrid},{bqual})`.
    The `!str()` of the object returns the *transaction ID* used
    in the commands sent to the server.
    
    See :ref:`tpc` for an introduction.
    """
    def from_string(self, *args, **kwargs): # real signature unknown
        """
        Create a `!Xid` object from a string representation. Static method.
        
        If *s* is a PostgreSQL transaction ID produced by a XA transaction,
        the returned object will have `format_id`, `gtrid`, `bqual` set to
        the values of the preparing XA id.
        Otherwise only the `!gtrid` is populated with the unparsed string.
        The operation is the inverse of the one performed by `!str(xid)`.
        """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    bqual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Branch qualifier of the transaction.

In a XA transaction every resource participating to a transaction
receives a distinct branch qualifier.
`!None` if the transaction doesn't follow the XA standard."""

    database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Database the recovered transaction belongs to."""

    format_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Format ID in a XA transaction.

A non-negative 32 bit integer.
`!None` if the transaction doesn't follow the XA standard."""

    gtrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Global transaction ID in a XA transaction.

If the transaction doesn't follow the XA standard, it is the plain
*transaction ID* used in the server commands."""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the user who prepared a recovered transaction."""

    prepared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Timestamp (with timezone) in which a recovered transaction was prepared."""



# variables with complex values

adapters = {
    (
        None, # (!) real value is ''
        ISQLQuote,
    ): 
        None # (!) real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        Decimal
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: TimeFromPy, real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: IntervalFromPy, real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: TimestampFromPy, real value is ''
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: DateFromPy, real value is ''
    ,
    (
        bool,
        '<value is a self-reference, replaced by this string>',
    ): 
        Boolean
    ,
    (
        buffer,
        '<value is a self-reference, replaced by this string>',
    ): 
        Binary
    ,
    (
        bytearray,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
    (
        float,
        '<value is a self-reference, replaced by this string>',
    ): 
        Float
    ,
    (
        int,
        '<value is a self-reference, replaced by this string>',
    ): 
        Int
    ,
    (
        list,
        '<value is a self-reference, replaced by this string>',
    ): 
        List
    ,
    (
        long,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
    (
        memoryview,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
    (
        None, # (!) real value is ''
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is ''
    ,
    (
        bytes,
        '<value is a self-reference, replaced by this string>',
    ): 
        QuotedString
    ,
    (
        tuple,
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is ''
    ,
    (
        unicode,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
}

binary_types = {}

encodings = {
    'ABC': 'cp1258',
    'ALT': 'cp866',
    'BIG5': 'big5',
    'EUCCN': 'euccn',
    'EUCJIS2004': 'euc_jis_2004',
    'EUCJP': 'euc_jp',
    'EUCKR': 'euc_kr',
    'EUC_CN': 'euccn',
    'EUC_JIS_2004': 'euc_jis_2004',
    'EUC_JP': 'euc_jp',
    'EUC_KR': 'euc_kr',
    'GB18030': 'gb18030',
    'GBK': 'gbk',
    'ISO88591': 'iso8859_1',
    'ISO885910': 'iso8859_10',
    'ISO885913': 'iso8859_13',
    'ISO885914': 'iso8859_14',
    'ISO885915': 'iso8859_15',
    'ISO885916': 'iso8859_16',
    'ISO88592': 'iso8859_2',
    'ISO88593': 'iso8859_3',
    'ISO88595': 'iso8859_5',
    'ISO88596': 'iso8859_6',
    'ISO88597': 'iso8859_7',
    'ISO88598': 'iso8859_8',
    'ISO88599': 'iso8859_9',
    'ISO_8859_1': 'iso8859_1',
    'ISO_8859_10': 'iso8859_10',
    'ISO_8859_13': 'iso8859_13',
    'ISO_8859_14': 'iso8859_14',
    'ISO_8859_15': 'iso8859_15',
    'ISO_8859_16': 'iso8859_16',
    'ISO_8859_2': 'iso8859_2',
    'ISO_8859_3': 'iso8859_3',
    'ISO_8859_5': 'iso8859_5',
    'ISO_8859_6': 'iso8859_6',
    'ISO_8859_7': 'iso8859_7',
    'ISO_8859_8': 'iso8859_8',
    'ISO_8859_9': 'iso8859_9',
    'JOHAB': 'johab',
    'KOI8': 'koi8_r',
    'KOI8R': 'koi8_r',
    'KOI8U': 'koi8_u',
    'LATIN1': 'iso8859_1',
    'LATIN10': 'iso8859_16',
    'LATIN2': 'iso8859_2',
    'LATIN3': 'iso8859_3',
    'LATIN4': 'iso8859_4',
    'LATIN5': 'iso8859_9',
    'LATIN6': 'iso8859_10',
    'LATIN7': 'iso8859_13',
    'LATIN8': 'iso8859_14',
    'LATIN9': 'iso8859_15',
    'MSKANJI': 'cp932',
    'Mskanji': 'cp932',
    'SHIFTJIS': 'cp932',
    'SHIFTJIS2004': 'shift_jis_2004',
    'SHIFT_JIS_2004': 'shift_jis_2004',
    'SJIS': 'cp932',
    'SQLASCII': 'ascii',
    'SQL_ASCII': 'ascii',
    'ShiftJIS': 'cp932',
    'TCVN': 'cp1258',
    'TCVN5712': 'cp1258',
    'UHC': 'cp949',
    'UNICODE': 'utf_8',
    'UTF8': 'utf_8',
    'VSCII': 'cp1258',
    'WIN': 'cp1251',
    'WIN1250': 'cp1250',
    'WIN1251': 'cp1251',
    'WIN1252': 'cp1252',
    'WIN1253': 'cp1253',
    'WIN1254': 'cp1254',
    'WIN1255': 'cp1255',
    'WIN1256': 'cp1256',
    'WIN1257': 'cp1257',
    'WIN1258': 'cp1258',
    'WIN866': 'cp866',
    'WIN874': 'cp874',
    'WIN932': 'cp932',
    'WIN936': 'gbk',
    'WIN949': 'cp949',
    'WIN950': 'cp950',
    'WINDOWS932': 'cp932',
    'WINDOWS936': 'gbk',
    'WINDOWS949': 'cp949',
    'WINDOWS950': 'cp950',
    'Windows932': 'cp932',
    'Windows936': 'gbk',
    'Windows949': 'cp949',
    'Windows950': 'cp950',
}

string_types = {} # real value of type <type 'dict'> replaced

_C_API = None # (!) real value is ''

