#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V2 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Native_String               import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause


#
#   convert_module_alias(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Alias_Clause`.
#
#       NOTE:
#
#           In version 2, `z.create_Tree_Module_Alias` maps to `Z.Tree.Alias_1.create_Tree_Alias_Clause`.
#
#           Hence, in version 2, this routine is identical to `convert_symbol_alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_module_alias(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_string                  (v.name)
    assert fact_is__native_none__OR__full_native_string(v.asname)

    return z.create_Tree_Module_Alias(v.name, v.asname)


#
#   convert_symbol_alias(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Alias_Clause`.
#
#       NOTE:
#
#           In version 2, `z.create_Tree_Symbol_Alias` maps to `Z.Tree.Alias_1.create_Tree_Alias_Clause`.
#
#           Hence, in version 2, this routine is identical to `convert_module_alias`.
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
#       `FullNativeList of Tree_Alias_Clause`.
#
convert_full_list_of_module_aliases = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_module_alias)
    )


#
#   convert_full_list_of_symbol_aliases(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Alias_Clause`.
#
#       In Version 1, identical to `convert_full_list_of_alias_clauses` (since `convert_module_alias` is
#       identical to `convert_symbol_alias`).
#
convert_full_list_of_symbol_aliases = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_symbol_alias)
    )
