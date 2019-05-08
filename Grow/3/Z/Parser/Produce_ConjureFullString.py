#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Produce_ConjureFullName - Produce a `conjure_full_name__with_unused_Z_parameter` function.
#
#       SEE: "Capital.Produce_ConjureFullName" for the code this is copied from.
#


from    Capital.Temporary_String_V6     import  create_temporary_string


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Z.Tree.Convert_Zone         import  fact_is_convert_zone


#
#   produce_conjure_full_name__with_unused_Z_parameter(Meta)
#
#       Produce a `conjure_full_name_with_unused_Z_parameter(s)` method.
#
#           Identical to `conjure_full_name` above, but with an extra unused `z` parameter.
#
#   This is a copy of "Capital.Produce_ConjureFullName.produce_conjure_full_name`:
#
#       The only difference is the extra unused `z` parameter.
#
def produce_conjure_full_name__with_unused_Z_parameter(Meta):
    string_cache  = {}                  #   Map { TemporaryKey | Meta } of { TemporaryKey | Meta }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   conjure_full_name__with_unused_Z_parameter(z, s) - Conjure a `Meta`, based on `s`.  Guarentees Uniqueness.
    #
    #       The `z` parameter is unused.
    #
    #       `s` must be of type `Full_Native_String` (or a type that is a subclass of `Full_Native_String`).
    #
    #       `s` must be a "full" string (i.e.: length greater than 0).
    #
    #   See comments in "Capital.Private.ConjureString_V6.py" to understand this code.
    #
    def conjure_full_name__with_unused_Z_parameter(z, s):
        assert fact_is_convert_zone      (z)
        assert fact_is_full_native_string(s)

        r = lookup_string(s)

        if r is not None:
            if r.temporary_element_has_definitively_been_transformed:
                return r

            r.__class__ = Meta

            assert r.temporary_element_has_definitively_been_transformed

            return r

        temporary_string__maybe_duplicate = create_temporary_string(s)

        r = provide_string(temporary_string__maybe_duplicate, temporary_string__maybe_duplicate)

        if r.temporary_element_has_definitively_been_transformed:
            return r

        r.__class__ = Meta

        assert r.temporary_element_has_definitively_been_transformed

        return r


    return conjure_full_name__with_unused_Z_parameter
