#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V5 - Implementation of an identifier used in the Z parser, Version 5
#


#
#   Difference between Version 4 & Version 5.
#
#       Version 4:
#
#           1)  `Parser_Symbol_Leaf` does not implement `Tree_{Module,Symbol}_Alias`.
#
#           2)  `Parser_Symbol_Leaf` implements `Parser_Symbol_0`.
#
#           3)  Defines `conjure_parser_symbol_0`.
#
#       Version 5:
#
#           1)  `Parser_Symbol_Leaf` implements `Tree_{Module,Symbol}_Alias`.
#
#           2)  `Parser_Symbol_Leaf` does not implement `Parser_Symbol_0`.
#
#           3)  Does not define `conjure_parser_symbol_0`.
#
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.Native_String               import  Full_Native_String
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Tree.Alias                        import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                        import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Capital.Core                    import  FATAL
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


#
#   Parser: Symbol [Leaf]
#
class Parser_Symbol_Leaf(
        Full_Native_String,
        TRAIT_TemporaryElement,
        TRAIT_Parser_Module_Name,
        TRAIT_Parser_Symbol,
        TRAIT_Tree_Module_Alias,
        TRAIT_Tree_Symbol_Alias,
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
    #   Interface Tree_Module_Alias
    #
    def dump_module_alias_tokens(self, f):
        f.arrange('<module-alias $ {}>', self)


    #
    #   Interface Tree_Symbol_Alias
    #
    def dump_symbol_alias_tokens(self, f):
        f.arrange('<symbol-alias $ {}>', self)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_Leaf {}>', self)


conjure_parser_symbol = produce_conjure_full_name__with_unused_Z_parameter(Parser_Symbol_Leaf)


export(conjure_parser_symbol)
