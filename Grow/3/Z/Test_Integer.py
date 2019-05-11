#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Test_Integer - Test the `Integer` interface.
#


from    Capital.Core                    import  trace
from    Capital.Integer                 import  conjure_integer
from    Capital.Integer                 import  zero_integer


def command_test_integer():
    minus_five = conjure_integer(-5)
    seven      = conjure_integer(7)
    zero       = conjure_integer(0)

    assert zero is zero_integer

    trace('minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)

    assert not minus_five.is_avid_integer
    assert     minus_five.is_contrary_integer
    assert     minus_five.is_negative_integer
    assert not minus_five.is_positive_integer
    assert not minus_five.is_zero_integer

    assert     seven.is_avid_integer
    assert not seven.is_contrary_integer
    assert not seven.is_negative_integer
    assert     seven.is_positive_integer
    assert not seven.is_zero_integer

    trace('Passed: Integer Test')
