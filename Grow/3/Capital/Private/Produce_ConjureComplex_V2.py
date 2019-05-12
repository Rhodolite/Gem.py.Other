#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Produce_ConjureComplex_V1 - Produce `conjure_complex` function, Version 1.
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Has a `produce_conjure_X_functions` function.
#
#       Version 2:
#
#           Remove `produce_conjure_X_functions`, and merged it into the `produce_conjure_complex` function.
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


from    Capital.Core                            import  creator
from    Capital.Core                            import  export
from    Capital.Exception                       import  PREPARE_ValueError
from    Capital.Temporary_None                  import  temporary_none
from    Capital.Private.Temporary_Complex_V1    import  create_temporary_complex


if __debug__:
    from    Capital.Fact                import  fact_is_native_type
    from    Capital.Native_Complex      import  fact_is_native_complex


#
#   produce_conjure_complex(Complex_Type)
#
#       Produce a `conjure_complex` function.
#
#   PRODUCED FUNCTION:
#
#       conjure_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
#
#           `v` must be a *DIRECT* `Native_Complex` instance
#
#           `v` may *NOT* be an instance of a subclass of `Native_Complex`.
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
    complex_cache = {}                  #   Map { Complex_Type | Temporary_Complex : Complex_Type | Temporary_Complex }

    lookup_complex  = complex_cache.get
    provide_complex = complex_cache.setdefault


    #
    #    conjure_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
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
    def conjure_complex(v):
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


    return conjure_complex
