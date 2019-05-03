#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Conjure_Symbol_V1 - Conjure a unique `Symbol`, Version 1
#


from    Z.Capital.Symbol                    import  Symbol
from    Capital.StringKey_V3                import  create_string_key_v3


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   conjure_symbol(s) - Conjure a symbol, based on `s`.  Guarentees Uniqueness.
#
#       `s` must be of type `FullNativeString`
#
#   NOTE:
#
#       This function is pretty much a copy of `conjure_String_v3` found in `Z.Capital.Conjure_V3`.
#
#       Differences between `conjure_string_V3` and `conjure_symbol_V1`:
#
#           `conjure_string_V3`:
#
#               1)  Allows an empty string (since it's cache is initialized with `empty_string_v3`).
#
#               2)  Uses `fact_is_some_native_string` to allow an empty or full string.
#
#               3)  Creates full strings of type `FullString_V3`
#
#           `conjure_symbol_V1`
#
#               1)  Does not allow an empty string.
#
#               2)  Uses `fact_is_full_native_string` to only allow a full string.
#
#               3)  Creates full strings of type `Symbol`.
#
#       Please read the comments in `Z.Capital.Conjure_V3` for extensive documentation on `conjure_string_V3`
#       (these commens all apply to `conjure_symbol_V1).
#
cache   = {}                 #   Map { StringKey_V3 | Symbol } of { StringKey_V3 | symbol }
lookup  = cache.get
provide = cache.setdefault


def conjure_symbol_V1(s):
    assert fact_is_full_native_string(s)

    r = lookup(s)

    if r is not None:
        if r.temporary_key_has_definitively_been_transformed:
            return r

        r.__class__ = Symbol

        assert r.temporary_key_has_definitively_been_transformed

        return r

    k = create_string_key_v3(s)

    r = provide(k, k)

    if r.temporary_key_has_definitively_been_transformed:
        return r

    r.__class__ = Symbol

    assert r.temporary_key_has_definitively_been_transformed

    return r
