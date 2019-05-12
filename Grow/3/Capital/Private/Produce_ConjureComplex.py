#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Produce_ConjureComplex - Produce `conjure_complex` functions
#
#   NOTE:
#       The code here is a bit absurd with *TWO* producer functions, where, really, neither is needed.
#
#       However, it is basically a "reduced" version of `Capital.Private.Produce_ConjureNumber` removing
#       all the special handling for "avid", "contrary", "negative", and "positive".
#
#       It seemed best to just leave it as the "reduced" version, instead of simplifying it even futhur.
#


#
#   +===========================================================================================================+
#   |                                                                                                           |
#   |   MULTI THREADING WARNING                                                                                 |
#   |                                                                                                           |
#   |       This code (like all good multi-threading code that properly handles errors) is quite convoluted.    |
#   |                                                                                                           |
#   |       You can *IGNORE* reading and understanding the rest of this file, since it is the *PRIVATE*         |
#   |       implementation of the public `Integer` Interface.                                                   |
#   |                                                                                                           |
#   |       Initially, you really only need to read and understand the public `Integer` interface.              |
#   |                                                                                                           |
#   +===========================================================================================================+
#


from    Capital.Core                            import  arrange
from    Capital.Core                            import  creator
from    Capital.Core                            import  export
from    Capital.Exception                       import  PREPARE_ValueError
from    Capital.Temporary_None                  import  temporary_none
from    Capital.Private.Temporary_Complex_V1    import  create_temporary_complex


if __debug__:
    from    Capital.Fact                import  fact_is_native_built_in_method
    from    Capital.Fact                import  fact_is_native_type
    from    Capital.Native_Complex      import  fact_is_native_complex
    from    Capital.Native_String       import  fact_is_full_native_string


#
#   produce_conjure_X_functions(function_name, lookup_complex, provide_complex, Complex_Type)
#
#       Produce a `conjure_complex` functions.
#
#       PARAMETERS:
#
#           1)  function_name           - Function name produced:
#
#                   1a) Currently unused.
#
#                   1b) In the future, will also rename the internal conjure_X_routine to this name
#                       (for debugging purposes).
#
#           2)  lookup_complex           - Lookup a complex in complex_cache.
#
#           3)  provide_complex          - Provide a complex in complex_cache.
#
#           4)  Complex_Type             - The type to transform a temporary "complex" to when creating a new complex.
#
#
#       PRODUCED FUNCTION:
#
#           conjure_X_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
#
#               `v` must be a *DIRECT* `Native_Complex` instance
#
#               `v` may *NOT* be an instance of a subclass of `Native_Complex`.
#
@export
def produce_conjure_X_complex(function_name, lookup_complex, provide_complex, Complex_Type):
    assert fact_is_full_native_string(function_name)

    assert fact_is_native_built_in_method(lookup_complex)
    assert fact_is_native_built_in_method(provide_complex)

    assert fact_is_native_type(Complex_Type)

    #
    #    conjure_X_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
    #
    #        `v` must be a *DIRECT* `Native_Complex` instance
    #
    #        `v` may *NOT* be an instance of a subclass of `Native_Complex`.
    #
    #   NOTE:
    #       To understand this code please see:
    #
    #           `Capital.Private.ConjureString_V7.conjure_X_string` (which is extensivly commented).
    #
    @creator
    def conjure_X_complex(v):
        assert fact_is_native_complex(v)

        r = lookup_complex(v, temporary_none)

        if r.definitively_not_temporary:
            return r

        if r is temporary_none:
            temporary_complex__maybe_duplicate = create_temporary_complex(v)

            r = provide_complex(temporary_complex__maybe_duplicate, temporary_complex__maybe_duplicate)

            if r.definitively_not_temporary:
                return r

        r.__class__ = Complex_Type

        assert r.definitively_not_temporary

        return r


    return conjure_X_complex


#
#   produce_conjure_complex(Complex_Type)
#
#       Produce a `conjure_complex` funtion.
#
@export
def produce_conjure_complex(Complex_Type):
    assert fact_is_native_type(Complex_Type)


    #
    #   complex_cache - A cache of `Complex_Type` (and possibly `Temporary_Complex`).
    #
    #       All complexs are stored in this as key/value pairs:
    #
    #           1)  The key is `Complex_Type` or a `Temporary_Complex`.
    #
    #           2)  The value is the same as the key.
    #
    complex_cache = {}

    lookup_complex  = complex_cache.get
    provide_complex = complex_cache.setdefault


    #
    #   Return `conjure_complex`
    #
    return produce_conjure_X_complex(
            'conjure_complex',

            lookup_complex,
            provide_complex,

            Complex_Type,
        )
