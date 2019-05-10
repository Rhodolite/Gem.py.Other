#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Produce_ConjureFullName - Produce a `conjure_full_name__with_unused_Z_parameter` function.
#


from    Capital.Core                        import  creator
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_string


if __debug__:
    from    Capital.Native_String           import  fact_is_native_string
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   produce_conjure_full_name__with_unused_Z_parameter(Full_Name_Type)
#
#       Produce a `conjure_full_name__with_unused_Z_parameter(s)` method.
#
#       PARAMETER:
#
#           1)  Full_Name_Type  - The type to transform a Temporary_String to when creating a new name.
#
#       PRODUCED FUNCTION:
#
#           conjure_full_name(z, name) - Conjure a `Full_Name_Type`, based on `name`.  Guarantees Uniqueness.
#
#                `z` must be a `Convert_Zone`, but is otherwise ignored.
#
#                `name` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#                `name` may *NOT* be an instance of a subclass of `str`.
#
#           EXCEPTION
#
#               If `name` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
def produce_conjure_full_name__with_unused_Z_parameter(Full_Name_Type):
    conjure_full_name = produce_conjure_full_string('conjure_full_name', Full_Name_Type)


    #
    #   conjure_full_name(z, name) - Conjure a `Full_Name_Type`, based on `name`.  Guarantees Uniqueness.
    #
    #        `z` must be a `Convert_Zone`, but is otherwise ignored.
    #
    #        `name` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
    #
    #        `name` may *NOT* be an instance of a subclass of `str`.
    #
    #   EXCEPTION
    #
    #       If `name` is empty (i.e.: has 0 characters), throws a `ValueError`.
    #
    @creator
    def conjure_full_name__with_unused_Z_parameter(z, name):
        assert fact_is_convert_zone(z)

        #
        #   The following test is `fact_is_native_string` on purpose.
        #
        #   This is to allow the case of `s` is `""` to throw a `ValueError` (the `ValueError` is thrown by
        #   `convert_full_name`).
        #
        assert fact_is_native_string(name)

        return conjure_full_name(name)


    return conjure_full_name__with_unused_Z_parameter
