#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Module_Name_With_Dot: Implementation of a module name (with dot) used in the Z parser.
#


from    Capital.Core                        import  arrange
from    Capital.NativeString                import  export
from    Capital.TemporaryElement            import  TRAIT_TemporaryElement
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name


if __debug__:
    from    Capital.Core                    import  FATAL


#
#   Parser: Module Name With Dot
#
class Parser_Module_Name_With_Dot
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
            FATAL("Parser_Module_Name_With_Dot.operator new (`__new__`): A Parser_Module_Name_With_Dot not be {}",
                  'created')


    if __debug__:
        def __init__(self, s):
            FATAL("Parser_Module_Name_With_Dot.constructor (`__init__`): A Parser_Module_Name_With_Dot not be {}",
                  'constructed');


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Module_Name_With_Dot {}>', self)


conjure_parser_module_name_with_dot = produce_conjure_full_name(Parser_Symbol_V1)


export(conjure_parser_module_name_with_dot)
