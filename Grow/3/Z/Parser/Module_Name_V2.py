#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Module_Name_V2: Implementation of a module name used in the Z parser, Version 2
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not exist.
#
#       Version 2:
#
#           Exists
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.Native_String               import  Native_String
from    Capital.Maybe_Temporary             import  TRAIT_Maybe_Temporary_0
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.Produce_ConjureFullName    import  produce_conjure_full_name__with_unused_Z_parameter


if __debug__:
    from    Capital.Cannot                  import  raise__CANNOT__create__ERROR
    from    Capital.Cannot                  import  raise__CANNOT__construct__ERROR


#
#   Parser: Module Name With Dot
#
class Parser_Module_Name_With_Dot(
        Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Parser_Module_Name,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Parser_Module_Name
    #
    def dump_module_name_token(self, f):
        f.arrange('<module-name-with-dot {}>', self)


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
