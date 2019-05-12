#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Test_Number - Test the `Integer` & `Long` interface.
#


from    Capital.Complex                 import  conjure_complex
from    Capital.Conjure_Number          import  conjure_number
from    Capital.Core                    import  trace
from    Capital.Float                   import  conjure_avid_float
from    Capital.Float                   import  conjure_contrary_float
from    Capital.Float                   import  conjure_float
from    Capital.Float                   import  conjure_negative_float
from    Capital.Float                   import  conjure_positive_float
from    Capital.Float                   import  zero_float
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


if is_python_2:
    from    Capital.Native_Long         import  Native_Long


if __debug__:
    from    Capital.Complex             import  fact_is_complex
    from    Capital.Float               import  fact_is_float
    from    Capital.Number              import  fact_is_number
    from    Capital.Integer             import  fact_is_integer


if (is_python_2) and (__debug__):
    from    Capital.Long                import  fact_is_long


def verify_throws_value_error(f, expected):
    caught = None

    try:
        f()
    except ValueError as e:
        caught = e

    assert caught.args[0] == expected


def command_test_complex():
    minus_five = conjure_complex(-5-5j)
    seven      = conjure_complex(7+7j)
    zero       = conjure_complex(0j)

    trace('minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)


    #
    #   conjure_number
    #
    assert minus_five is conjure_number(-5-5j)
    assert seven      is conjure_number(7+7j)
    assert zero       is conjure_number(0j)


    #
    #   .is_complex & .is_number
    #
    if __debug__:
        assert minus_five.is_complex
        assert minus_five.is_number
        assert seven     .is_complex
        assert seven     .is_number
        assert zero      .is_complex
        assert zero      .is_number

        assert fact_is_complex (minus_five)
        assert fact_is_number(minus_five)
        assert fact_is_complex (zero)
        assert fact_is_number(zero)
        assert fact_is_complex (seven)
        assert fact_is_number(seven)


    #
    #   Passed
    #
    trace('Passed: Complex Test')


def command_test_float():
    minus_five = conjure_float(-5.5)
    seven      = conjure_float(7.7)
    zero       = conjure_float(0.0)

    assert zero is zero_float

    trace('minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)


    #
    #   conjure_number
    #
    assert minus_five is conjure_number(-5.5)
    assert seven      is conjure_number(7.7)
    assert zero       is conjure_number(0.0)


    #
    #   -5.5
    #
    assert not minus_five.is_avid_float
    assert     minus_five.is_contrary_float
    assert     minus_five.is_negative_float
    assert not minus_five.is_positive_float
    assert not minus_five.is_zero_float

    verify_throws_value_error(
        lambda: conjure_avid_float(-5.5),
        "parameter `v` is negative; `conjure_avid_float` requires zero or a positive value",
    )

    assert minus_five is conjure_contrary_float(-5.5)
    assert minus_five is conjure_negative_float(-5.5)

    verify_throws_value_error(
        lambda: conjure_positive_float(-5.5),
        "parameter `v` is negative; `conjure_positive_float` requires a positive value",
    )


    #
    #   0.0
    #
    assert     zero.is_avid_float
    assert     zero.is_contrary_float
    assert not zero.is_negative_float
    assert not zero.is_positive_float
    assert     zero.is_zero_float

    assert zero is conjure_avid_float(0.0)
    assert zero is conjure_contrary_float(0.0)

    verify_throws_value_error(
        lambda: conjure_negative_float(0.0),
        "parameter `v` is zero; `conjure_negative_float` requires a negative value",
    )

    verify_throws_value_error(
        lambda: conjure_positive_float(0.0),
        "parameter `v` is zero; `conjure_positive_float` requires a positive value",
    )


    #
    #   7.7
    #
    assert     seven.is_avid_float
    assert not seven.is_contrary_float
    assert not seven.is_negative_float
    assert     seven.is_positive_float
    assert not seven.is_zero_float

    assert seven is conjure_avid_float(7.7)

    verify_throws_value_error(
        lambda: conjure_contrary_float(7.7),
        "parameter `v` is positive; `conjure_contrary_float` requires zero or a negative value",
    )

    verify_throws_value_error(
        lambda: conjure_negative_float(7.7),
        "parameter `v` is positive; `conjure_negative_float` requires a negative value",
    )

    assert seven is conjure_positive_float(7.7)


    #
    #   .is_float & .is_number
    #
    if __debug__:
        assert minus_five.is_float
        assert minus_five.is_number
        assert seven     .is_float
        assert seven     .is_number
        assert zero      .is_float
        assert zero      .is_number

        assert fact_is_float (minus_five)
        assert fact_is_number(minus_five)
        assert fact_is_float (zero)
        assert fact_is_number(zero)
        assert fact_is_float (seven)
        assert fact_is_number(seven)


    #
    #   Passed
    #
    trace('Passed: Float Test')


def command_test_integer():
    minus_five = conjure_integer(-5)
    seven      = conjure_integer(7)
    zero       = conjure_integer(0)

    assert zero is zero_integer

    trace('minus_five, zero, seven: {!r}, {!r}, {!r}', minus_five, zero, seven)


    #
    #   conjure_number
    #
    assert minus_five is conjure_number(-5)
    assert seven      is conjure_number(7)
    assert zero       is conjure_number(0)


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
    #   .is_integer & .is_number
    #
    if __debug__:
        assert minus_five.is_integer
        assert minus_five.is_number
        assert seven     .is_integer
        assert seven     .is_number
        assert zero      .is_integer
        assert zero      .is_number

        assert fact_is_integer(minus_five)
        assert fact_is_number (minus_five)
        assert fact_is_integer(zero)
        assert fact_is_number (zero)
        assert fact_is_integer(seven)
        assert fact_is_number (seven)


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
        #   conjure_number
        #
        #   NOTE:
        #       Have to use a cast like `Native_Long(-5)` to avoid compile errors in python 3.*
        #
        #       Using `-5L` will cause a compile error in python 3.*
        #
        #       Using `-5` will cause the assert to fail, as it will return an `Integer` instead of a `Long`.
        #
        assert minus_five is conjure_number(Native_Long(-5))
        assert seven      is conjure_number(Native_Long(7))
        assert zero       is conjure_number(Native_Long(0))

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
        #   .is_long & .is_number
        #
        if __debug__:
            assert minus_five.is_long
            assert minus_five.is_number
            assert seven     .is_long
            assert seven     .is_number
            assert zero      .is_long
            assert zero      .is_number

            assert fact_is_long  (minus_five)
            assert fact_is_number(minus_five)
            assert fact_is_long  (zero)
            assert fact_is_number(zero)
            assert fact_is_long  (seven)
            assert fact_is_number(seven)


        #
        #   Passed
        #
        trace('Passed: Long Test')


def command_test_number():
    command_test_integer()

    if is_python_2:
        command_test_long()

    command_test_float()
    command_test_complex()
