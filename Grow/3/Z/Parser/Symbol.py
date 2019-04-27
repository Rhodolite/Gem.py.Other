#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol - An identifier used in the Z parser.
#


from    Capital.Core                        import  FATAL
from    Captial.String_Key_V3               import  create_string_key_v3


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_string


class Symbol(str):
    #
    #   implements Temporary_Key
    #
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL("Symbol.operator new (`__new__`): A Symbol may not be created");


    if __debug__:
        def __init__(self, s):
            FATAL("Symbol.constructor (`__init__`): A Symbol may not be contructed");

    
    #
    #   Interface Temporary_Key
    #
    temporary_key_has_definitively_been_transformed = True


    #__init__    - inherited from `str.__init__`        #   Not Used.
    #__new__     - inherited from `str.__new__`         #   Not Used.
    #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


    def __repr__(self):
        return '$' + self



#
#   The rest of this code is pretty much a copy of `conjure_string_v3` in "Capital.Private.ConjureString_V3".
#
#   See that module for comments.
#
#   The only real difference is that there `s` may be an empty string, while in this module `s` must be a full string.
#
symbol_cache       = {}                 #   Map { StringKey_V3 | Symbol } of { StringKey_V3 | Symbol }
lookup_symbol      = symbol_cache.get
provide_string_key = string_cache.setdefault


#
#   conjure_symbol(s) - Conjure a symbol, based on `s`.  Guarentees Uniqueness.
#
#       `s` must be of type `FullNativeString`
#
def conjure_symbol(s):
    assert fact_is_full_native_string(s)

    r = lookup_string(s)

    if r is not None:
        if r.temporary_key_has_definitively_been_transformed:
            return r

        r.__class__ = Symbol

        assert r.temporary_key_has_definitively_been_transformed

        return r

    k = create_string_key_v3(s)

    r = provide_string_key(k, k)

    if r.temporary_key_has_definitively_been_transformed:
        return r

    r.__class__ = Symbol

    assert r.temporary_key_has_definitively_been_transformed

    return r
