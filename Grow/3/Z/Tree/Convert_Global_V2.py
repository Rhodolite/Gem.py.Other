#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Global_V2 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All convert functions take a `z` parameter of type `Convert_Zone.
#


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement


#
#   convert_global_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Global_Statement` (i.e.: `_ast.Global`) to a
#       `Tree_Global_Statement`.
#
assert Native_AbstractSyntaxTree_Global_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Global_Statement._fields     == (('names',))


def convert_global_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_list(v.names)

    return z.create_Tree_Global_Statement(
               v.lineno,
               v.col_offset,

               v.names,
           )
