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
#           1)  `Parser_Symbol_Implementation` does not implement `Tree_{Module,Symbol}_Alias`.
#
#           2)  `Parser_Symbol_Implementation` implements `Parser_Symbol_0`.
#
#           3)  Defines `conjure_parser_symbol_0`.
#
#       Version 4:
#
#           1)  `Parser_Symbol_Implementation` implements `Tree_{Module,Symbol}_Alias`.
#
#           2)  `Parser_Symbol_Implementation` does not implement `Parser_Symbol_0`.
#
#           3)  Does not define `conjure_parser_symbol_0`.
#
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Tree.Alias                        import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                        import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Capital.Core                    import  FATAL
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


class Parser_Symbol_Implementation(
        NativeString,
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
            FATAL('{}: A Parser_Symbol_Implementation may not be created',
                  "Parser_Symbol_Implementation.operator new (`__new__`)");


    if __debug__:
        def __init__(self, s):
            FATAL('{}: A Parser_Symbol_Implementation may not be constructed',
                  "Parser_Symbol_Implementation.constructor (`__init__`)");


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
        f.arrange('<$ module-alias {}>', self)


    #
    #   Interface Tree_Symbol_Alias
    #
    def dump_symbol_alias_tokens(self, f):
        f.arrange('<$ symbol-alias {}>', self)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_Implementation {}>', self)


conjure_parser_symbol = produce_conjure_full_name(Parser_Symbol_Implementation)


export(conjure_parser_symbol)
