#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Global - Globals to affect the behavior of the "Capital" modules.
#


version = 6


string_version = 1


#
#   Version 1: Introduce `String_V1`, a very simple string wrapper.
#


#
#   Version 2: Producer function `produce_conjure_string` to produce `conjure_string` functions.
#
if version >= 2:
    string_version = 2


#
#   Version 3: Add `Base_String`, `Empty_String` and `Full_String`.
#
if version >= 3:
    string_version = 3


#
#   Version 4: Remove `Base_String`.
#
if version >= 4:
    string_version = 4


#
#   Version 5: Guarantee Uniqueness of `Full_String` always (see "Capital/Private/ConjureString_V5.py for details).
#
if version >= 5:
    string_version = 5


#
#   Version 6: Derive String classes from `str` (instead of from `object`)
#
if version >= 6:
    string_version = 6

#
#   Version 7:  Old Code -- Until assigned a number.
#
if version >= 7:
    string_version = 7


#
#   Imports
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Capital_Globals - Globals to affect the behavior of the "Capital" modules.
#
class Capital_Globals(object):
    __slots__ = ((
        'string_version',               #   Positive_Integer
    ))


    def __init__(self, string_version):
        self.string_version = string_version


    def __repr__(self):
        return arrange('<Capital_Globals string={}>', self.string_version)


@creator
def create_capital_globals(string_version):
    assert fact_is_positive_integer(string_version)

    r = Capital_Globals(string_version)

    trace('Capital Globals: {}', r)

    return r


capital_globals = create_capital_globals(
                      string_version = string_version,
                  )
