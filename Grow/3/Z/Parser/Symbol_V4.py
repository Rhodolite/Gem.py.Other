#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V4 - Implementation of an identifier used in the Z parser, Version 4
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           1)  `Parser_Symbol_Leaf` does not implement `Parser_Symbol_0`
#
#           2)  Does not define `conjure_parser_symbol_0`.
#
#       Version 4:
#
#           1)  `Parser_Symbol_Leaf` implements `Parser_Symbol_0`.
#
#           2)  Defines `conjure_parser_symbol_0`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol_0


if __debug__:
    from    Capital.Core                    import  FATAL
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   Parser: Symbol [Leaf]
#
class Parser_Symbol_Leaf(
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
            FATAL('{}: A Parser_Symbol_Leaf may not be created',
                  "Parser_Symbol_Leaf.operator new (`__new__`)");


    if __debug__:
        def __init__(self, s):
            FATAL('{}: A Parser_Symbol_Leaf may not be constructed',
                  "Parser_Symbol_Leaf.constructor (`__init__`)");


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
        return arrange('<Parser_Symbol_Leaf {}>', self)


conjure_parser_symbol = produce_conjure_full_name__with_unused_Z_parameter(Parser_Symbol_Leaf)


export(conjure_parser_symbol)


@export
def conjure_parser_symbol_0(z, s):
    assert fact_is_convert_zone                        (z)
    assert fact_is__native_none__OR__full_native_string(s)

    if s is None:
        return parser_none

    return z.conjure_parser_symbol(z, s)
