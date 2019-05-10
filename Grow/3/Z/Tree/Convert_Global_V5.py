#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Global_V5 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 5.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2..5.
#
#       Version 2:
#
#           The third argument to `z.create_Tree_Global_Statement` is a `Full_Native_List of Full_Native_String`.
#
#       Versions 3..4:
#
#           Do not exist.
#
#       Version 5:
#
#           The third argument to `z.create_Tree_Global_Statement` is a `Full_Native_List of Parser_Symbol`.
#


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
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

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.names)

    return z.create_Tree_Global_Statement(
               v.lineno,
               v.col_offset,

               convert_list_of_parser_symbols(z, v.names),
           )


#
#   convert_list_of_parser_symbols(z, v)
#
#       Convert a `Full_Native_List of Full_Native_String` to a `Full_Native_List of Parser_Symbol`.
#
def convert_list_of_parser_symbols(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_list(v)

    return [z.conjure_parser_symbol(z, w)   for w in v]
