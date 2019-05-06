#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Module_Name - Interface to a module name used in the Z parser.
#


#
#   interface Parser_Module_Name - Interface to a module name used in the Z parser.
#
#       interface Parser_Module_Name
#           debug
#               is_parser_module_name := true
#
#           attribute
#               native_string : NativeString
#
#           method
#               dump_module_name_token(f : Build_DumpToken)
#
class TRAIT_Parser_Module_Name(object):
    __slots__ = (())


    if __debug__:
        is_parser_module_name = True


#
#   USAGE (debug mode):
#
#       v.is_parser_module_name                 #   Test if `v` is a parser module name.
#
#       assert fact_is_parser_module_name(v)    #   Assert that `v` is a parser module name.
#


if __debug__:
    #
    #   fact_is_parser_module_name(v) - Assert the fact that `v` is a parser module name.
    #
    def fact_is_parser_module_name(v):
        assert v.is_parser_module_name

        return True


#
#   Import the version of tree expressions we want to use (must be after the "facts" above)
#
from    Z.Parser.Global                 import  parser_globals


module_name_version = parser_globals.module_name_version


if module_name_version == 1:
    from    Z.Parser.Module_Name_V1     import  conjure_parser_module_name_with_dot
elif module_name_version == 2:
    from    Z.Parser.Module_Name_V2     import  conjure_parser_module_name_with_dot
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Parser/Module_name.py: unknown module name version: {!r}', module_name_version)
