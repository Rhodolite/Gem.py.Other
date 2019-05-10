#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Produce_ConjureFullString - Produce a `conjure_full_string` function.
#


from    Capital.Private.ConjureString_V7    import  produce_conjure_X_string


if __debug__:
    from    Capital.Native_String           import  fact_is_full_native_string
    from    Capital.Fact                    import  fact_is_native_type


#
#   produce_conjure_full_string(function_name, Full_String_Type) - Produce a `conjure_full_string` method.
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
#           2)  Full_String_Type        - The type to transform a Temporary_String to when creating a new string.
#
#       PRODUCED FUNCTION:
#
#           `conjure_full_string(s)` - Conjure a `Full_String_Type`, based on `s`.  Guarantees Uniqueness.
#
#                `s` must be a `Full_Native_String` (i.e.: `str` instance, with a length greater than 0).
#
#                `s` may *NOT* be an instance of a subclass of `Native_String` (i.e.: `str`).
#
#           EXCEPTION
#
#               If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
#   NOTE:
#
#       This code is based on `Capital.Private.ConjureString_V7.produce_conjure_string_functions`.
#
#       Differences from `Capital.Private.ConjureString_V7.produce_conjure_X_functions`:
#
#           `Capital.Private.ConjureString_V7.produce_conjure_X_functions`:
#
#               1)  Does not take a `function_name`.
#
#               2)  Produces two functions, a `conjure_full_string` function and a `conjure_string` function.
#
#           `produce_conjure_full_string` below:
#
#               1)  Takes a `function_name` parameter.
#
#               2)  Only produces one function, the `conjure_full_string` funtion.
#
def produce_conjure_full_string(function_name, Full_String_Type):
    assert fact_is_full_native_string(function_name)
    assert fact_is_native_type       (Full_String_Type)

    #
    #   string_cache - A cache of `Full_String_Type` (and possibly some temporary strings).
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is `Full_String_Type` or a `Temporary_String`.
    #
    #           2)  The value is the same as the key.
    #
    string_cache = {}                   #   Map { Full_String_Full | Temporary_String
                                        #       : Full_String_Type | Temporary_String }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault

    return produce_conjure_X_string(function_name, lookup_string, provide_string, Full_String_Type)
