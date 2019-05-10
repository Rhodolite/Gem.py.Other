#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Global - Globals to affect the behavior of the "Capital" modules.
#


version = 9                 #   1..9


exception_version = 1       #   1..2
string_version    = 1       #   0..7


#
#   Version 2: Introduce `produce_PREPARE_Exception`
#
if version >= 2:
    exception_version = 2               #   "Capital/Private/Exception_V2.py" implements `produce_PREPARE_Exception`


#
#   Version 3: Add `conjure_X_string` to remove duplicate code.
#
if version >= 3:
    string_version = 2                  #   Add `conjure_X_string` to remove duplicate code.


#
#   Version 4: Producer function `produce_conjure_string` to produce `conjure_some_string` functions.
#
if version >= 4:
    string_version = 3


#
#   Version 5: Add `Base_String`, `Empty_String_Leaf` and `Full_String_Leaf`.
#
if version >= 5:
    string_version = 4


#
#   Version 6: Remove `Base_String`.
#
if version >= 6:
    string_version = 5


#
#   Version 7: Guarantee Uniqueness of `Full_String_Leaf` always
#              (see "Capital/Private/ConjureString_V6.py for details).
#
if version >= 7:
    string_version = 6


#
#   Version 8: Derive String classes from `str` (instead of from `object`)
#
if version >= 8:
    string_version = 7


#
#   Version 9: String classes implement interfaces `Empty_String` and `Full_String_Leaf`
#
if version >= 9:
    string_version = 8


#
#   Imports
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer


#
#   Capital_Globals - Globals to affect the behavior of the "Capital" modules.
#
class Capital_Globals(object):
    __slots__ = ((
        'version',                      #   Native_Positive_Integer
        'exception_version',            #   Native_Positive_Integer
        'string_version',               #   Native_Substantial_Integer
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
    assert fact_is_positive_native_integer   (version)
    assert fact_is_positive_native_integer   (exception_version)
    assert fact_is_substantial_native_integer(string_version)

    assert 1 <= version           <= 9
    assert 1 <= exception_version <= 8
    assert 0 <= string_version    <= 8

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
