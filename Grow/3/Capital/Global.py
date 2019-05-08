#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Global - Globals to affect the behavior of the "Capital" modules.
#


version = 3


exception_version = 1
string_version    = 0


#
#   Version 2: Introduce `produce_PREPARE_Exception`
#
if version >= 2:
    exception_version = 2               #   "Capital/Private/Exception_V2.py" implements `produce_PREPARE_Exception`


#
#   Version 3: Introduce `String_Leaf`, a very simple string wrapper.
#
if version >= 3:
    string_version = 1                  #   "Capital/Private/String_1.py" implements `String_Leaf`


#
#   Version 4: Producer function `produce_conjure_string` to produce `conjure_some_string` functions.
#
if version >= 4:
    string_version = 2


#
#   Version 5: Add `Base_String`, `Empty_String` and `Full_String`.
#
if version >= 5:
    string_version = 3


#
#   Version 6: Remove `Base_String`.
#
if version >= 6:
    string_version = 4


#
#   Version 7: Guarantee Uniqueness of `Full_String` always (see "Capital/Private/ConjureString_V5.py for details).
#
if version >= 7:
    string_version = 5


#
#   Version 8: Derive String classes from `str` (instead of from `object`)
#
if version >= 8:
    string_version = 6



#
#   Imports
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Capital_Globals - Globals to affect the behavior of the "Capital" modules.
#
class Capital_Globals(object):
    __slots__ = ((
        'version',                      #   Positive_Integer
        'exception_version',            #   Positive_Integer
        'string_version',               #   Substantial_Integer
    ))


    def __init__(self, version, exception_version, string_version):
        self.version           = version
        self.exception_version = exception_version
        self.string_version    = string_version


    def __repr__(self):
        return arrange('<Capital_Globals version={} exception={} string={}>',
                       self.version, self.exception_version, self.string_version)


@creator
def create_capital_globals(version, exception_version, string_version):
    assert fact_is_positive_integer   (version)
    assert fact_is_positive_integer   (exception_version)
    assert fact_is_substantial_integer(string_version)

    r = Capital_Globals(
            version           = version,
            exception_version = exception_version,
            string_version    = string_version,
        )

    trace('Capital Globals: {}', r)

    return r


capital_globals = create_capital_globals(
                      version           = version,
                      exception_version = exception_version,
                      string_version    = string_version,
                  )
