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
