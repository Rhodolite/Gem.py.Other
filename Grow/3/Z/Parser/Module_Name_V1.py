#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Module_Name_V1: Implementation of a module name used in the Z parser, Version 1
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.NativeString                import  NativeString
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name


if __debug__:
    from    Capital.Core                    import  FATAL


#
#   Parser: Module Name With Dot
#
class Parser_Module_Name_With_Dot(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_Parser_Module_Name,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL('{}, A Parser_Module_Name_With_Dot not be created'
                  "Parser_Module_Name_With_Dot.operator new (`__new__`)")


    if __debug__:
        def __init__(self, s):
            FATAL('{}, A Parser_Module_Name_With_Dot not be constructed'
                  "Parser_Module_Name_With_Dot.constructor (`__init__`)")


    #
    #   Interface Parser_Module_Name
    #
    @property
    def native_string(self):
        return self


    def dump_module_name_token(self, f):
        f.arrange('<module-name-with-dot {}>', self)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Module_Name_With_Dot {}>', self)


conjure_parser_module_name_with_dot = produce_conjure_full_name(Parser_Module_Name_With_Dot)


export(conjure_parser_module_name_with_dot)