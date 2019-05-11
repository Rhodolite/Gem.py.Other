
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Produce_ConjureNunber - Produce conjure number functions
#
#   NOTE:
#       To understand this code please see:
#
#           "Capital.Private.Conjure_String_V8.py"
#
#       (which is extensivly commented).
#


#
#   +===========================================================================================================+
#   |                                                                                                           |
#   |   MULTI THREADING WARNING                                                                                 |
#   |                                                                                                           |
#   |       This code (like all good multi-threading code that properly handles errors) is quite convoluted.    |
#   |                                                                                                           |
#   |       You can *IGNORE* reading and understanding the rest of this file, since it is the *PRIVATE*         |
#   |       implementation of the public `String` Interface.                                                    |
#   |                                                                                                           |
#   |       Initially, you really only need to read and understand the public `String` interface.               |
#   |                                                                                                           |
#   +===========================================================================================================+
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Exception               import  PREPARE_ValueError
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V7       import  empty_string
from    Capital.Private.String_V7       import  Full_String_Leaf
from    Capital.Temporary_None          import  temporary_none
from    Capital.Temporary_String_V7     import  create_temporary_string


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_built_in_method
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_native_type
    from    Capital.Fact                import  fact_is_not_native_none
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Capital.Native_String       import  fact_is_native_string


#
#   produce_conjure_X_functions(
#           function_name,
#
#           fact_is_native_number,
#
#           lookup_number,
#           provide_number,
#
#           create_temporary_number,
#           Negative_Number_Type,
#           Positive_Number_Type,
#
#           allow_negative = False,
#           allow_zero     = False,
#           allow_positive = False,
#
#           zero_number = None,
#   )
#
#       Produce a `conjure_*_integer` functions.
#
#       PARAMETERS:
#
#           1)  function_name           - Function name produced:
#
#                   1a) For Value_Error message;
#
#                   1b) In the future, will also rename the internal conjure_X_routine to this name
#                       (for debugging purposes).
#
#           2)  fact_is_native_number   - fact routine to test for `Native_{Integer,Long,Float}`.
#
#           3)  lookup_number           - Lookup a number in string_cache.
#
#           4)  provide_number          - Provide a number in string_cache.
#
#           5)  create_temporary_number - Create routine to create a temporary "number" (temporary integer,
#                                         temporary long, or temporary float).
#
#           6)  Negative_Number_Type    - The type to transform a temporary "number" to when creating a new negative
#                                         number.
#
#           7)  Positive_Number_Type    - The type to transform a temporary "number" to when creating a new positive
#                                         number.
#
#           8)  allow_negative_number   - True if `v` may be negative (i.e.: can conjure negative numbers)
#
#           9)  allow_zero              - True if `v` may be zero     (i.e.: can conjure the zero number).
#
#           10) allow_positive_number   - True if `v` may be positive (i.e.: can conjure positive numbers).
#
#           11) negative_value_message  - Message to use to prepare a `Value_Error` when v is negative.
#
#                                         Must be `None` if `allow_negative` is `True`.
#
#           12) zero_value_message      - Message to use to prepare a `Value_Error` when v is 0.
#
#                                         Must be `None` if `allow_zero` is `True`.
#
#           13) positive_value_message  - Message to use to prepare a `Value_Error` when v is positive.
#
#                                         Must be `None` if `allow_negative` is `True`.
#
#           14) zero_number             - The singleton to return when the conjuring a zero number.
#
#                                         Must be `None` if `allow_zero` is `False`.
#
#       PRODUCED FUNCTION:
#
#           conjure_X_number(v) - Conjure a `Number`, based on `v`.  Guarantees Uniqueness.
#
#               `v` must be a *DIRECT* `Native_Number` instance
#
#               `v` may *NOT* be an instance of a subclass of `Native_Number`.
#
#           EXCEPTIONS
#
#               If `allow_negative` is `False`, then the produced function has this behavior:
#
#                   If `v` is negative, throws a `ValueError`.
#
#               If `allow_zero` is `False`, then the produced function has this behavior:
#
#                   If `v` is zero, throws a `ValueError`.
#
#               If `allow_positive` is `False`, then the produced function has this behavior:
#
#                   If `v` is positive, throws a `ValueError`.
#
@export
def produce_conjure_X_number(
        function_name,

        fact_is_native_number,

        lookup_number,
        provide_number,

        create_temporary_number,
        Negative_Number_Type,
        Positive_Number_Type,

        allow_negative = False,
        allow_zero     = False,
        allow_positive = False,

        negative_value_message = None,
        zero_value_message     = None,
        positive_value_message = None,

        zero_number = None,
):
    assert fact_is_full_native_string(function_name)

    assert fact_is_native_function(fact_is_native_number)

    assert fact_is_native_built_in_method(lookup_number)
    assert fact_is_native_built_in_method(provide_number)

    assert fact_is_native_function(create_temporary_number)
    assert fact_is_native_type    (Negative_Number_Type)
    assert fact_is_native_type    (Positive_Number_Type)

    assert fact_is_native_boolean(allow_negative)
    assert fact_is_native_boolean(allow_zero)
    assert fact_is_native_boolean(allow_positive)

    if allow_negative:
        assert fact_is_none              (negative_value_message)
    else:
        assert fact_is_full_native_string(negative_value_message)

    if allow_zero:
        assert fact_is_none              (zero_value_message)
    else:
        assert fact_is_full_native_string(zero_value_message)

    if allow_positive:
        assert fact_is_none              (positive_value_message)
    else:
        assert fact_is_full_native_string(positive_value_message)

    if allow_zero:
        assert fact_is_not_native_none(zero_nunber)
    else:
        assert fact_is_native_none    (zero_nunber)


    #
    #    conjure_X_number(v) - Conjure a `Number`, based on `v`.  Guarantees Uniqueness.
    #
    #        `v` must be a *DIRECT* `Native_Number` instance
    #
    #        `v` may *NOT* be an instance of a subclass of `Native_Number`.
    #
    #    EXCEPTIONS
    #
    #        If `allow_negative` is `False`, then has this behavior:
    #
    #            If `v` is negative, throws a `ValueError`.
    #
    #        If `allow_zero` is `False`, then has this behavior:
    #
    #            If `v` is zero, throws a `ValueError`.
    #
    #        If `allow_positive` is `False`, then has this behavior:
    #
    #            If `v` is positive, throws a `ValueError`.
    #
    @creator
    def conjure_X_number(v):
        #
        #   The following test is `fact_is_native_number` on purpose.
        #
        #   This is to allow throwing a `ValueError` below.
        #
        assert fact_is_native_number(v)

        r = lookup_number(v, temporary_none)

        if r.definitively_not_temporary:
            return r

        if r is temporary_none:
            if v > 0:
                if allow_positive:
                    #
                    #   Ok, handle positive numbers below.
                    #
                    pass
                else:
                    value_error = PREPARE_ValueError(positive_value_message, function_name)

                    raise value_error
            elif v == 0:
                if allow_zero:
                    return zero_value
                else:
                    value_error = PREPARE_ValueError(positive_value_message, function_name)

                    raise value_error
            else:
                assert v < 0

                if allow_negative:
                    #
                    #   Ok, handle negative numbers below.
                    #
                    pass
                else:
                    value_error = PREPARE_ValueError(negative_value_message, function_name)

                    raise value_error

            temporary_number__maybe_duplicate = create_temporary_number(v)

            r = provide_number(temporary_number__maybe_duplicate, temporary_number__maybe_duplicate)

            if r.definitively_not_temporary:
                return r

        r.__class__ = (Positive_Number_Type   if v > 0 else   Negative_Number_Type)

        assert r.definitively_not_temporary

        return r


    return conjure_X_number


#
#   produce_conjure_number_functions(zero_number, Negative_Number_Type, Positive_Number_Type)
#
#       Produce 5 functions:
#
#           conjure_avid_number(v)
#
#           conjure_contrary_number(v)
#
#           conjure_negative_number(v)
#
#           conjure_number(v)
#
#           conjure_positive_number(v)
#
#   NOTE:
#
#       `number_cache` is shared between the 5 functions.
#
@export
def produce_conjure_number_functions(
        number_name,
        fact_is_native_number,
        create_temporary_number,
        Negative_Number_Type,
        Positive_Number_Type,
        zero_number,
)
    assert fact_is_full_string    (number_name)
    assert fact_is_native_function(fact_is_native_number)
    assert fact_is_native_type    (Negative_Number_Type)
    assert fact_is_native_type    (Positive_Number_Type)
    assert fact_is_not_native_none(zero_number)


    #
    #   number_cache - A cache of `{Negative,Positive}_Number_Type` (and possibly some temporary strings).
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is `{Negative,Positive}_Number_Type` or a `Temporary_{Integer,Long,Float}`
    #
    #           2)  The value is the same as the key.
    #
    number_cache = {}

    lookup_number  = number_cache.get
    provide_number = number_cache.setdefault


    #
    #   Produce 5 functions, sharing `number_cache` (via `{lookup,provide}_number`).
    #
    conjure_avid_number = produce_conjure_X_number(
            arrange('conjure_avid_{}', number_name),

            fact_is_native_number,

            lookup_number,
            provide_number,

            create_temporary_number,
            Negative_Number_Type,
            Positive_Number_Type,

            allow_zero     = True,
            allow_positive = True,

            negative_value_message = "parameter `v` is negative; `{}` requires zero or a positive value",

            zero_number = zero_number,
        )
    
    conjure_contrary_number = produce_conjure_X_number(
            arrange('conjure_contrary_{}', number_name),

            fact_is_native_number,

            lookup_number,
            provide_number,

            create_temporary_number,
            Negative_Number_Type,
            Positive_Number_Type,

            allow_negative = True,
            allow_zero     = True,

            postive_value_message = "parameter `v` is positive; `{}` requires zero or a negative value",

            zero_number = zero_number,
        )

    conjure_negative_number = produce_conjure_X_number(
            arrange('conjure_negative_{}', number_name),

            fact_is_native_number,

            lookup_number,
            provide_number,

            create_temporary_number,
            Negative_Number_Type,
            Positive_Number_Type,

            allow_negative = True,

            zero_value_message    = "parameter `v` is zero; `{}` requires a negative value",
            postive_value_message = "parameter `v` is positive; `{}` requires a negative value",
        )


    conjure_number = produce_conjure_X_number(
            arrange('conjure_{}', number_name),

            fact_is_native_number,

            lookup_number,
            provide_number,

            create_temporary_number,
            Negative_Number_Type,
            Positive_Number_Type,

            allow_negative = True,
            allow_zero     = True,
            allow_positive = True,

            zero_number = zero_number,
        )

    conjure_positive_number = produce_conjure_X_number(
            arrange('conjure_positive_{}', number_name),

            fact_is_native_number,

            lookup_number,
            provide_number,

            create_temporary_number,
            Negative_Number_Type,
            Positive_Number_Type,

            allow_positive = Positive,

            negative_value_message = "parameter `v` is positive; `{}` requires a positive value",
            zero_value_message     = "parameter `v` is zero; `{}` requires a positive value",
        )


    #
    #   Return 5 produced functions.
    #
    return ((
                 conjure_avid_number,
                 conjure_contrary_number,
                 conjure_negative_number,
                 conjure_number,
                 conjure_positive_number,
           ))
