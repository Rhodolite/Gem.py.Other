#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol - An identifier used in the Z parser.
#


from    Capital.Core                        import  arrange
from    Capital.NativeString                import  NativeString
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name


if __debug__:
    from    Capital.Core                    import  FATAL


class Symbol(
        NativeString,
        TRAIT_TemporaryElement,
):
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
    #   Public
    #
    is_symbol = True


    def __repr__(self):
        return arrange('<Symbol {}>', self)


conjure_symbol = produce_conjure_full_name(Symbol)


if __debug__:
    #
    #   fact_is_symbol(v) - Assert the fact that `v` is a `Symbol`.
    #
    def fact_is_symbol(v):
        assert v.is_symbol

        return True
