#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Module_Name_V3: Implementation of a module name used in the Z parser, Version 3
#


#
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           `Parser_Module_Name_With_Dot` does not implement `Tree_Module_Alias`.
#
#       Version 3:
#
#           `Parser_Module_Name_With_Dot` implements `Tree_Module_Alias`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.Native_String               import  Full_Native_String
from    Capital.Maybe_Temporary             import  TRAIT_Maybe_Temporary_0
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Tree.Alias                        import  TRAIT_Tree_Module_Alias


if __debug__:
    from    Capital.Core                    import  FATAL


#
#   Parser: Module Name With Dot
#
class Parser_Module_Name_With_Dot(
        Full_Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Parser_Module_Name,
        TRAIT_Tree_Module_Alias,
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
    def dump_module_name_token(self, f):
        f.arrange('<module-name-with-dot {}>', self)


    #
    #   Interface Tree_Module_Alias
    #
    def dump_module_alias_tokens(self, f):
        f.arrange('<module-alias module-name-with-dot {}>', self)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Module_Name_With_Dot {}>', self)


conjure_parser_module_name_with_dot = produce_conjure_full_name__with_unused_Z_parameter(Parser_Module_Name_With_Dot)


#
#   conjure_parser_module_name_with_dot(z, name)
#
#       Conjure a `Parser_Module_Name_With_Dot`, based on `name`.  Guarantees Uniqueness.
#
#       PARAMETERS:
#
#            `z` must be a `Convert_Zone`, but is otherwise ignored.
#
#            `name` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#            `name` may *NOT* be an instance of a subclass of `str`.
#
#       EXCEPTION
#
#           If `name` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
export(conjure_parser_module_name_with_dot)
