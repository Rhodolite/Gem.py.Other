#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Global - Globals to affect the behavior of the "Capital" modules.
#


version = 9                             #   1..9


complex_version   = 1                   #   1..2
exception_version = 1                   #   1..2
string_version    = 1                   #   0..6


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
#   Version 4: Producer function `produce_conjure_string` to produce `conjure_string` functions.
#
if version >= 4:
    string_version = 3


#
#   Version 5: Add `String_Branch` and `{Empty,Full}_String_Leaf`.
#
if version >= 5:
    string_version = 4


#
#   Version 6: Remove `String_Branch`.
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
#   Version 9: Simplify `produce_conjure_complex`
#
if version >= 9:
    complex_version = 2


#
#   Imports
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer


#
#   Capital_Globals - Globals to affect the behavior of the "Capital" modules.
#
class Capital_Globals(object):
    __slots__ = ((
        'version',                      #   Positive_Native_Integer
        'complex_version',              #   Positive_Native_Integer
        'exception_version',            #   Positive_Native_Integer
        'string_version',               #   Avid_Native_Integer
    ))


    def __init__(self, version, complex_version, exception_version, string_version):
        self.version           = version
        self.complex_version   = complex_version
        self.exception_version = exception_version
        self.string_version    = string_version


    def __repr__(self):
        return arrange('<Capital_Globals version={} complex={} exception={} string={}>',
                       self.version, self.complex_version, self.exception_version, self.string_version)


@creator
def create_capital_globals(version, complex_version, exception_version, string_version):
    assert fact_is_positive_native_integer(version)
    assert fact_is_positive_native_integer(complex_version)
    assert fact_is_positive_native_integer(exception_version)
    assert fact_is_avid_native_integer    (string_version)

    assert 1 <= version           <= 9
    assert 1 <= complex_version   <= 2
    assert 1 <= exception_version <= 2
    assert 0 <= string_version    <= 7

    r = Capital_Globals(
            version           = version,
            complex_version   = complex_version,
            exception_version = exception_version,
            string_version    = string_version,
        )

    trace('Capital Globals: {}', r)

    return r


capital_globals = create_capital_globals(
                      version           = version,
                      complex_version   = complex_version,
                      exception_version = exception_version,
                      string_version    = string_version,
                  )
