#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_From_Import_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Alias_V1             import  convert_full_list_of_symbol_aliases
from    Z.Tree.From_Import_V1               import  create_Tree_From_Import_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_native_integer
    from    Capital.Fact                        import  fact_is_substantial_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement


#
#   convert_from_import_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_From_Import_Statement` (i.e.: `_ast.ImportFrom`) to a
#       `Tree_From_Import_Statement`.
#
assert Native_AbstractSyntaxTree_From_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_From_Import_Statement._fields     == (('module', 'names', 'level'))


def convert_from_import_statement(v):
    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_full_native_string        (v.module)
    assert fact_is_full_native_list          (v.names)
    assert fact_is_substantial_native_integer(v.level)

    return create_Tree_From_Import_Statement(
               v.lineno,
               v.col_offset,

               v.module,
               convert_full_list_of_symbol_aliases(v.names),
               v.level,
           )
