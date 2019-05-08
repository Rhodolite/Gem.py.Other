#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Conjure_Module_Name - Conjure a module name
#


from    Capital.Native_String           import  native_string__lookup_index__OR__MINUS_1


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Z.Tree.Convert_Zone         import  fact_is_convert_zone


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
def conjure_parser_module_name(z, s):
    assert fact_is_convert_zone      (z)
    assert fact_is_full_native_string(s)

    dot_index = native_string__lookup_index__OR__MINUS_1(s, '.')

    if dot_index == -1:
        return z.conjure_parser_symbol(z, s)

    return z.conjure_parser_module_name_with_dot(z, s)
