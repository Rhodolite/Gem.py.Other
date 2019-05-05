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
            FATAL("Parser_Symbol_V1.operator new (`__new__`): A Parser_Symbol_V1 may not be created");


    if __debug__:
        def __init__(self, s):
            FATAL("Parser_Symbol_V1.constructor (`__init__`): A Parser_Symbol_V1 may not be contructed");


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_V1 {}>', self)


conjure_parser_symbol = produce_conjure_full_name(Parser_Symbol_V1)


export(conjure_parser_symbol)
