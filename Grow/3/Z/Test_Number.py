#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Test_Number - Test the `Integer` & `Long` interface.
#


from    Capital.Core                    import  trace
from    Capital.Integer                 import  conjure_avid_integer
from    Capital.Integer                 import  conjure_contrary_integer
from    Capital.Integer                 import  conjure_integer
from    Capital.Integer                 import  conjure_negative_integer
from    Capital.Integer                 import  conjure_positive_integer
from    Capital.Integer                 import  zero_integer
from    Capital.Long                    import  conjure_avid_long
from    Capital.Long                    import  conjure_contrary_long
from    Capital.Long                    import  conjure_long
from    Capital.Long                    import  conjure_negative_long
from    Capital.Long                    import  conjure_positive_long
from    Capital.Long                    import  zero_long
from    Capital.System                  import  is_python_2


def verify_throws_value_error(f, expected):
    caught = None

    try:
        f()
    except ValueError as e:
        caught = e

    assert caught.args[0] == expected


def command_test_integer():
    minus_five = conjure_integer(-5)
    seven      = conjure_integer(7)
    zero       = conjure_integer(0)

    assert zero is zero_integer

    trace('minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)

    #
    #   -5
    #
    assert not minus_five.is_avid_integer
    assert     minus_five.is_contrary_integer
    assert     minus_five.is_negative_integer
    assert not minus_five.is_positive_integer
    assert not minus_five.is_zero_integer

    verify_throws_value_error(
        lambda: conjure_avid_integer(-5),
        "parameter `v` is negative; `conjure_avid_integer` requires zero or a positive value",
    )

    assert minus_five is conjure_contrary_integer(-5)
    assert minus_five is conjure_negative_integer(-5)

    verify_throws_value_error(
        lambda: conjure_positive_integer(-5),
        "parameter `v` is negative; `conjure_positive_integer` requires a positive value",
    )


    #
    #   0
    #
    assert     zero.is_avid_integer
    assert     zero.is_contrary_integer
    assert not zero.is_negative_integer
    assert not zero.is_positive_integer
    assert     zero.is_zero_integer

    assert zero is conjure_avid_integer(0)
    assert zero is conjure_contrary_integer(0)

    verify_throws_value_error(
        lambda: conjure_negative_integer(0),
        "parameter `v` is zero; `conjure_negative_integer` requires a negative value",
    )

    verify_throws_value_error(
        lambda: conjure_positive_integer(0),
        "parameter `v` is zero; `conjure_positive_integer` requires a positive value",
    )


    #
    #   7
    #
    assert     seven.is_avid_integer
    assert not seven.is_contrary_integer
    assert not seven.is_negative_integer
    assert     seven.is_positive_integer
    assert not seven.is_zero_integer

    assert seven is conjure_avid_integer(7)

    verify_throws_value_error(
        lambda: conjure_contrary_integer(7),
        "parameter `v` is positive; `conjure_contrary_integer` requires zero or a negative value",
    )

    verify_throws_value_error(
        lambda: conjure_negative_integer(7),
        "parameter `v` is positive; `conjure_negative_integer` requires a negative value",
    )

    assert seven is conjure_positive_integer(7)


    #
    #   Passed
    #
    trace('Passed: Integer Test')


if is_python_2:
    def command_test_long():
        minus_five = conjure_long(-5)
        seven      = conjure_long(7)
        zero       = conjure_long(0)

        assert zero is zero_long

        trace('test long: minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)

        #
        #   -5
        #
        assert not minus_five.is_avid_long
        assert     minus_five.is_contrary_long
        assert     minus_five.is_negative_long
        assert not minus_five.is_positive_long
        assert not minus_five.is_zero_long

        verify_throws_value_error(
            lambda: conjure_avid_long(-5),
            "parameter `v` is negative; `conjure_avid_long` requires zero or a positive value",
        )

        assert minus_five is conjure_contrary_long(-5)
        assert minus_five is conjure_negative_long(-5)

        verify_throws_value_error(
            lambda: conjure_positive_long(-5),
            "parameter `v` is negative; `conjure_positive_long` requires a positive value",
        )


        #
        #   0
        #
        assert     zero.is_avid_long
        assert     zero.is_contrary_long
        assert not zero.is_negative_long
        assert not zero.is_positive_long
        assert     zero.is_zero_long

        assert zero is conjure_avid_long(0)
        assert zero is conjure_contrary_long(0)

        verify_throws_value_error(
            lambda: conjure_negative_long(0),
            "parameter `v` is zero; `conjure_negative_long` requires a negative value",
        )

        verify_throws_value_error(
            lambda: conjure_positive_long(0),
            "parameter `v` is zero; `conjure_positive_long` requires a positive value",
        )


        #
        #   7
        #
        assert     seven.is_avid_long
        assert not seven.is_contrary_long
        assert not seven.is_negative_long
        assert     seven.is_positive_long
        assert not seven.is_zero_long

        assert seven is conjure_avid_long(7)

        verify_throws_value_error(
            lambda: conjure_contrary_long(7),
            "parameter `v` is positive; `conjure_contrary_long` requires zero or a negative value",
        )

        verify_throws_value_error(
            lambda: conjure_negative_long(7),
            "parameter `v` is positive; `conjure_negative_long` requires a negative value",
        )

        assert seven is conjure_positive_long(7)


        #
        #   Passed
        #
        trace('Passed: Long Test')


def command_test_number():
    command_test_integer()

    if is_python_2:
        command_test_long()
