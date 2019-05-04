#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Produce_ConjureFullName - An identifier used in the Z parser.
#


from    Capital.StringKey_V7            import  create_string_key


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#   produce_conjure_full_name(Meta)
#
#       Produce a `conjure_full_name(s)` method.
#
#       This produce method is pretty much a copy of `conjure_string` in "Capital.Private.ConjureString_V7".
#
#       See that module for comments.
#
#       The only real difference are:
#
#           1)  The method is "produced" with `Meta`; while in `conjure_string` it always makes a `FullString`.
#
#           2)  The method can only handle full strings; while `conjure_string` can handle an empty string
#       
#           2A) `conjure_string` only handles an empty due to how:
#
#                   2A.i)   `string_cache` is initialized with an empty string:
#
#                               string_cache = { empty_string : empty_string }
#
#                   2A.ii)  It uses `assert fact_is_some_native_string` [to allow an empty string].
#
#               Other than these two minor differences, `conjure_string` is basically the "template" for
#               the `conjure_full_name` function that is "produced" here.
#
def produce_conjure_full_name(Meta):
    cacche  = {}                        #   Map { StringKey | Meta } of { StringKey | Meta }
    lookup  = cacche.get
    provide = cacche.setdefault


    #
    #   conjure_full_name(s) - Conjure a `Meta`, based on `s`.  Guarentees Uniqueness.
    #
    #       `s` must be of type `NativeString` (or a type that is a subclass of `NativeString`).
    #
    #       `s` must be a "full" string (i.e.: length greater than 0).
    #
    def conjure_full_name(s):
        assert fact_is_full_native_string(s)

        r = lookup_symbol(s)

        if r is not None:
            if r.temporary_element_has_definitively_been_transformed:
                return r

            r.__class__ = Meta

            assert r.temporary_element_has_definitively_been_transformed

            return r

        k = create_string_key(s)

        r = provide_string_key(k, k)

        if r.temporary_element_has_definitively_been_transformed:
            return r

        r.__class__ = Meta

        assert r.temporary_element_has_definitively_been_transformed

        return r


    return conjure_full_name
