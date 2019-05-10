#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Import_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Alias_V1             import  convert_full_list_of_module_aliases
from    Z.Tree.Import_V1                    import  create_Tree_Import_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_native_integer
    from    Capital.Fact                        import  fact_is_substantial_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement


#
#   convert_import_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Import_Statement` (i.e.: `_ast.Import`) to a `Tree_Import_Statement`.
#
assert Native_AbstractSyntaxTree_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Import_Statement._fields     == (('names',))


def convert_import_statement(v):
    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_full_native_list(v.names)

    return create_Tree_Import_Statement(
               v.lineno,
               v.col_offset,

               convert_full_list_of_module_aliases(v.names),
           )
