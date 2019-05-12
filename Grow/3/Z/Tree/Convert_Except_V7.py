#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Except_V7 - Convert Python Abstract Syntax Tree Except Handler to `Tree_Except_Handler`, Version 7
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2..7:
#
#       Version 2:
#
#           Uses `Full_Native_List of Tree_Statement` for a suite of statements.
#
#       Versions 3..6:
#
#           Do not exist.
#
#       Version 7:
#
#           Uses `Tree_Suite` for a suite of statements.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_none
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Except_Handler


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

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET          (v.name)
    assert fact_is_full_native_list                                                        (v.body)

    if v.type is None:
        assert fact_is_native_none(v.name)

    return z.create_Tree_Except_Handler(
               v.lineno,
               v.col_offset,

               z.convert_value_expression_0(z, v.type),
               z.convert_store_target_0    (z, v.name),
               z.convert_suite             (z, v.body),
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
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_Except_Handler` (i.e.: `list of _ast.ExceptHandler`) to
#       a `Full_Native_List of Tree_Except_Clause`.
#
convert_full_list_of_except_clauses = (
        produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_except_clause)
    )
