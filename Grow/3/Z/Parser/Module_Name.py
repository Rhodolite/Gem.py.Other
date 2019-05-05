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
#           method
#               dump_module_name_token (f : Build_DumpToken)
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
    def fact_is_module_name(v):
        assert v.is_module_name

        return True


#
#   Imports (must be after the "fact" above).
#
from    Z.Parser.Module_Name_With_Dot   import  conjure_parser_module_name
from    Z.Parser.Symbol                 import  conjure_parser_symbol
from    Capital.NativeString            import  native_string__lookup_index__OR__MINUS_1


#
#   conjure_parser_module_name(s) - Conjure a parser module name with module name `s`.
#
#       If `s` has a `"."` in it:
#
#           1)  It conjures a `Parser_Module_Name_With_Dot`; else
#
#           2)  It conjures a `Parser_Symbol`.
#
#       NOTE:
#
#           Both `Parser_Module_Name_With_Dot` and `Parser_Symbol` implement `Parser_Module_Name`, hence this routine
#           is conjuring a parser module name.
#
def conjure_parser_module_name(s):
    dot_index = native_string__lookup_index__OR__MINUS_1(s, '.')

    if dot_index == -1:
        return conjure_parser_symbol(s)

    return conjure_parser_module_name_with_dot(s)
