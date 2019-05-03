#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Global - Globals to affect the behavior of the "Capital" modules.
#


version = 1


string_version = 1


#
#   Version 1: Introduce SomeString
#


#
#   Version 2: Introduce EmptyString
#
if version >= 2:
    string_version = 2


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
        'string_version',               #   PositiveInteger
    ))


    def __init__(self, string_version):
        self.string_version = string_version


    def __repr__(self):
        return arrange('<Capital_Globals {}>', self.string_version)


@creator
def create_capital_globals(string_version):
    assert fact_is_positive_integer(string_version)

    r = Capital_Globals(string_version)

    trace('Capital Globals: {}', r)

    return r


capital_globals = create_capital_globals(
                      string_version = string_version,
                  )
