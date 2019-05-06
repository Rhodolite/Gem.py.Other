#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Except_V2 - Convert Python Abstract Syntax Tree Except Handler to `Tree_Except_Handler`, Version 2
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


from    Z.Tree.Convert_Expression           import  convert_none_OR_expression
from    Z.Tree.Except                       import  create_Tree_Except_Handler
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Except_Handler
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_none
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION


#
#   convert_except_handler(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Except_Handler` (i.e.: `_ast.ExceptHandler`) to a
#       `Tree_Except_Handler`.
#
assert Native_AbstractSyntaxTree_Except_Handler._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Except_Handler._fields     == (('type', 'name', 'body'))


def convert_except_handler(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.name)
    assert fact_is_full_native_list                                                  (v.body)

    if v.type is None:
        assert fact_is_native_none(v.name)

    return create_Tree_Except_Handler(
               v.lineno,
               v.col_offset,

               convert_none_OR_expression       (v.type),
               convert_none_OR_expression       (v.name),
               z.convert_full_list_of_statements(z, v.body),
           )


#
#   convert_except_clause(z, v)
#
#       Currently there is only one type of "except clause", the "except handler".
#
#       Hence this routine just calls `convert_except_handler`.
#
convert_except_clause = convert_except_handler


#
#   convert_full_list_of_except_clauses(z, v)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Except_Handler` (i.e.: `list of _ast.ExceptHandler`) to
#       a `NativeList of Tree_Except_Clause`.
#
convert_full_list_of_except_clauses = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_except_clause)
    )
