#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V3 - Implementation of an identifier used in the Z parser, Version 3
#


#
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           `Parser_Symbol_Implementation` does not implement `Parser_Module_Name`.
#
#       Version 3:
#
#           `Parser_Symbol_Implementation` implements `Parser_Module_Name`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol


if __debug__:
    from    Capital.Core                    import  FATAL


class Parser_Symbol_Implementation(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_Parser_Module_Name,
        TRAIT_Parser_Symbol,
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
        f.arrange('<module-name symbol {}>', self)


    #
    #   Interface Parser_Symbol
    #
    def dump_symbol_token(self, f):
        f.arrange('<$ {}>', self)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_Implementation {}>', self)


conjure_parser_symbol = produce_conjure_full_name__with_unused_Z_parameter(Parser_Symbol_Implementation)


export(conjure_parser_symbol)
