#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Global_V6 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 6.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 5 and Version 6.
#
#       Version 5:
#
#           The third argument to `z.create_Tree_Global_Statement` is a `Full_Native_List of Parser_Symbol`.
#
#       Version 6:
#
#           The third argument to `z.create_Tree_Global_Statement` is a `Parser_Symbol_Tuple`.
#


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_native_integer
    from    Capital.Fact                        import  fact_is_substantial_native_integer
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

    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_full_native_list(v.names)

    return z.create_Tree_Global_Statement(
               v.lineno,
               v.col_offset,

               convert_parser_symbol_tuple(z, v.names),
           )


#
#   convert_parser_symbol_tuple(z, sequence)
#
#       Convert a `Full_Native_List of Full_Native_String` to a `Parser_Symbol_Tuple`.
#
def convert_parser_symbol_tuple(z, sequence):
    assert fact_is_convert_zone    (z)
    assert fact_is_full_native_list(sequence)

    if len(sequence) == 1:
        return z.conjure_parser_symbol(z, sequence[0])

    return z.create_Parser_Symbol_Tuple([z.conjure_parser_symbol(z, v)   for v in sequence])
