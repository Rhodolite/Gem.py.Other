#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Compound_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Compound_Statement_V1        import  create_Tree_For_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_If_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Try_Except_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Try_Finally_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_While_Statement
from    Z.Tree.Convert_Except_V1            import  convert_full_list_of_except_clauses
from    Z.Tree.Convert_Expression_V1        import  convert_value_expression
from    Z.Tree.Convert_Statement_V1         import  convert_full_list_of_statements
from    Z.Tree.Convert_Statement_V1         import  convert_list_of_statements
from    Z.Tree.Convert_Target_V1            import  convert_store_target_0
from    Z.Tree.Convert_Target_V1            import  convert_store_target
from    Z.Tree.With_V1                      import  create_Tree_With_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_list
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement


#
#   convert_test_statement(v, create) - common code for `convert_{if,while}_statement`.
#
def convert_test_statement(v, create):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.test)
    assert fact_is_full_native_list                                    (v.body)
    assert fact_is_native_list                                         (v.orelse)

    return create(
               v.lineno,
               v.col_offset,

               convert_value_expression       (v.test),
               convert_full_list_of_statements(v.body),
               convert_list_of_statements     (v.orelse),
           )


#
#   convert_for_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_For_Statement` (i.e.: `_ast.For`) to a `Tree_Extended_For_Statement`.
#
assert Native_AbstractSyntaxTree_For_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_For_Statement._fields     == (('target', 'iter', 'body', 'orelse'))


def convert_for_statement(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET          (v.target)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.iter)
    assert fact_is_full_native_list                                    (v.body)
    assert fact_is_native_list                                         (v.orelse)

    return create_Tree_For_Statement(
               v.lineno,
               v.col_offset,

               convert_store_target           (v.target),
               convert_value_expression       (v.iter),
               convert_full_list_of_statements(v.body),
               convert_list_of_statements     (v.orelse),
           )


#
#   convert_if_statement
#
#       Convert a `Native_AbstractSyntaxTree_If_Statement` (i.e.: `_ast.If`) to a `Tree_If_Statement`.
#
assert Native_AbstractSyntaxTree_If_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Statement._fields     == (('test', 'body', 'orelse'))


def convert_if_statement(v):
    return convert_test_statement(v, create_Tree_If_Statement)


#
#   convert_try_except_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Try_Except_Statement` (i.e.: `_ast.TryExcept`) to a
#       `Tree_Try_Except_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Except_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Except_Statement._fields     == (('body', 'handlers', 'orelse'))


def convert_try_except_statement(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_list(v.body)
    assert fact_is_full_native_list(v.handlers)
    assert fact_is_native_list     (v.orelse)

    return create_Tree_Try_Except_Statement(
               v.lineno,
               v.col_offset,

               convert_full_list_of_statements    (v.body),
               convert_full_list_of_except_clauses(v.handlers),
               convert_list_of_statements         (v.orelse),
           )


#
#   convert_try_finally_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Try_Finally_Statement` (i.e.: `_ast.TryFinally`) to a
#       `Tree_Try_Finally_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Finally_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Finally_Statement._fields     == (('body', 'finalbody'))


def convert_try_finally_statement(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_list(v.body)
    assert fact_is_full_native_list(v.finalbody)

    return create_Tree_Try_Finally_Statement(
               v.lineno,
               v.col_offset,

               convert_full_list_of_statements(v.body),
               convert_full_list_of_statements(v.finalbody),
           )


#
#   convert_while_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_While_Statement` (i.e.: `_ast.While`) to a `Tree_While_Statement`.
#
assert Native_AbstractSyntaxTree_While_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_While_Statement._fields     == (('test', 'body', 'orelse'))


def convert_while_statement(v):
    return convert_test_statement(v, create_Tree_While_Statement)


#
#   convert_with_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_With_Statement` (i.e.: `_ast.With`) to a `Tree_With_Statement`.
#
assert Native_AbstractSyntaxTree_With_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_With_Statement._fields     == (('context_expr', 'optional_vars', 'body'))


def convert_with_statement(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION          (v.context_expr)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET(v.optional_vars)
    assert fact_is_full_native_list                                              (v.body)

    return create_Tree_With_Statement(
               v.lineno,
               v.col_offset,

               convert_value_expression       (v.context_expr),
               convert_store_target_0         (v.optional_vars),
               convert_full_list_of_statements(v.body),
           )
