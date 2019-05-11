#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_From_Import_V4 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2, Version 3, and Version 4.
#
#       Version 2:
#
#           1)  The third parameter to `z.create_Tree_From_Import_Statement` is a `Full_Native_String`.
#
#       Version 3:
#
#           Does not exist.
#
#       Version 4:
#
#           1)  The third parameter to `z.create_Tree_From_Import_Statement` is a `Tree_Module_Name`.
#
#           2)  `convert_import_statement` is identical to Version 2 (the only function that changed between Version 2
#               and Version 4 is `convert_from_import_statement`).
#


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement


#
#   convert_from_import_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_From_Import_Statement` (i.e.: `_ast.ImportFrom`) to a
#       `Tree_From_Import_Statement`.
#
assert Native_AbstractSyntaxTree_From_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_From_Import_Statement._fields     == (('module', 'names', 'level'))


def convert_from_import_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_string (v.module)
    assert fact_is_full_native_list   (v.names)
    assert fact_is_avid_native_integer(v.level)

    return z.create_Tree_From_Import_Statement(
               v.lineno,
               v.col_offset,

               z.conjure_parser_module_name         (z, v.module),
               z.convert_full_list_of_symbol_aliases(z, v.names),
               v.level,
           )
