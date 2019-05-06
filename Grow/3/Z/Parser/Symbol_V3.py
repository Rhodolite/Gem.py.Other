#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V3 - Implementation of an identifier used in the Z parser, Version 3
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           1)  `Parser_Symbol_V2` does not implement `Parser_Symbol_0`
#
#           2)  Does not define `conjure_parser_symbol_0`.
#
#       Version 2:
#
#           1)  `Parser_Symbol_V3` implements `Parser_Symbol_0`.
#
#           2)  Defines `conjure_parser_symbol_0`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol_0


if __debug__:
    from    Capital.Core                    import  FATAL
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


class Parser_Symbol_V3(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_Parser_Module_Name,
        TRAIT_Parser_Symbol,
        TRAIT_Parser_Symbol_0,
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
    #   Interface Parser_Module_Name
    #
    @property
    def native_string(self):
        return self


    def dump_module_name_token(self, f):
        f.arrange('<module-name $ {}>', self)


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


conjure_parser_symbol = produce_conjure_full_name(Parser_Symbol_V3)


export(conjure_parser_symbol)


@export
def conjure_parser_symbol_0(s):
    assert fact_is__native_none__OR__full_native_string(s)

    if s is None:
        return parser_none

    return conjure_parser_symbol(s)
