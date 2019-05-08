#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V4 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           The first argument to `z.create_Tree_Module_Alias` is a `Full_Native_String`.
#
#       Version 4:
#
#           The first argument to `z.create_Tree_Module_Alias` is a `Parser_Module_Name`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause


#
#   convert_module_alias(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Module_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_module_alias(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_string                  (v.name)
    assert fact_is__native_none__OR__full_native_string(v.asname)

    return z.create_Tree_Module_Alias(
               z.conjure_parser_module_name(z, v.name),
               v.asname,
           )


#
#   convert_symbol_alias(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Symbol_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_symbol_alias(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_string                  (v.name)
    assert fact_is__native_none__OR__full_native_string(v.asname)

    return z.create_Tree_Symbol_Alias(v.name, v.asname)


#
#   convert_full_list_of_module_aliases(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Module_Alias`.
#
convert_full_list_of_module_aliases = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_module_alias)


#
#   convert_full_list_of_symbol_aliases(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Symbol_Alias`.
#
convert_full_list_of_symbol_aliases = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_symbol_alias)
