#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V1 - Implementation of an identifier used in the Z parser, Version 1
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol


if __debug__:
    from    Capital.Core                    import  FATAL


class Parser_Symbol_V1(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_Parser_Symbol,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            class_name = Meta.__name__

            FATAL("{}.operator new (`__new__`): A {} may not be created", class_name, class_name)


    if __debug__:
        def __init__(self, s):
            class_name = self.__class__.__name__

            FATAL("{}.constructor (`__init__`): A {} may not be constructed", class_name, class_name)


    #
    #   Interface Parser_Symbol
    #
    def dump_symbol_token(self, f):
        f.arrange('<$ {}>', self)



    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} {}>', self.__class__.__name__, self)


conjure_parser_symbol = produce_conjure_full_name(Parser_Symbol_V1)


export(conjure_parser_symbol)
