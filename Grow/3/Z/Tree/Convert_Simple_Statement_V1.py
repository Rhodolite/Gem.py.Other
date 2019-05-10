#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Simple_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Expression_V1        import  convert_expression
from    Z.Tree.Convert_Expression_V1        import  convert_none_OR_expression
from    Z.Tree.Convert_Expression_V1        import  convert_some_list_of_expressions
from    Z.Tree.Convert_Operator_V1          import  convert_modify_operator
from    Z.Tree.Convert_Target_V1            import  convert_full_list_of_targets
from    Z.Tree.Convert_Target_V1            import  convert_target
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Assert_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Assign_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Break_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Continue_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Delete_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Execute_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Expression_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Modify_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Pass_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Print_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Raise_Statement
from    Z.Tree.Simple_Statement_V1          import  create_Tree_Return_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_boolean
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement


#
#   create_keyword_statement(v) - Common code for `convert_{break,continue,pass}_statement`.
#
def convert_keyword_statement(v, create):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    return create(v.lineno, v.col_offset)



#
#   convert_assert_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Assert_Statement` (i.e.: `_ast.Assert`) to a `Tree_Assert_Statement`.
#
assert Native_AbstractSyntaxTree_Assert_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assert_Statement._fields     == (('test', 'msg'))


def convert_assert_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION                    (v.test)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.msg)

    return create_Tree_Assert_Statement(
               v.lineno,
               v.col_offset,

               convert_expression        (v.test),
               convert_none_OR_expression(v.msg),
           )


#
#   convert_assign_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Assign_Statement` (i.e.: `_ast.Assign`) to a `Tree_Assign`.
#
assert Native_AbstractSyntaxTree_Assign_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assign_Statement._fields     == (('targets', 'value'))


def convert_assign_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list                                    (v.targets)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Assign_Statement(
               v.lineno,
               v.col_offset,

               convert_full_list_of_targets(v.targets),
               convert_expression          (v.value),
           )


#
#   convert_break_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Break_Statement` (i.e.: `_ast.Break`) to a `Tree_Break_Statement`.
#
assert Native_AbstractSyntaxTree_Break_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Break_Statement._fields     == (())


def convert_break_statement(v):
    return convert_keyword_statement(v, create_Tree_Break_Statement)


#
#   convert_continue_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Continue_Statement` (i.e.: `_ast.Continue`) to a
#       `Tree_Continue_Statement`.
#
assert Native_AbstractSyntaxTree_Continue_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Continue_Statement._fields     == (())


def convert_continue_statement(v):
    return convert_keyword_statement(v, create_Tree_Continue_Statement)


#
#   convert_delete_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Statement` (i.e.: `_ast.Delete`) to a `Tree_Extended_Delete_Statement`.
#
assert Native_AbstractSyntaxTree_Delete_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Delete_Statement._fields     == (('targets',))


def convert_delete_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.targets)

    return create_Tree_Delete_Statement(
               v.lineno,
               v.col_offset,

               convert_full_list_of_targets(v.targets),
           )


#
#   convert_execute_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Execute_Statement` (i.e.: `_ast.Exec`) to a
#       `Tree_Execute_Statement`.
#
assert Native_AbstractSyntaxTree_Execute_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Execute_Statement._fields     == (('body', 'globals', 'locals'))


def convert_execute_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION                    (v.body)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.globals)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.locals)

    return create_Tree_Execute_Statement(
               v.lineno,
               v.col_offset,

               convert_expression        (v.body),
               convert_none_OR_expression(v.globals),
               convert_none_OR_expression(v.locals),
           )


#
#   convert_expression_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Expression_Statement` (i.e.: `_ast.Expr`) to a
#       `Tree_Expression_Statement`.
#
assert Native_AbstractSyntaxTree_Expression_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Expression_Statement._fields     == (('value',))


def convert_expression_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Expression_Statement(
               v.lineno,
               v.col_offset,

               convert_expression(v.value),
           )


#
#   convert_modify_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Modify_Statement` (i.e.: `_ast.AugAssign`) to a `Tree_Modify_Statement`.
#
assert Native_AbstractSyntaxTree_Modify_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Modify_Statement._fields     == (('target', 'op', 'value'))


def convert_modify_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET          (v.target)
    assert fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR (v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Modify_Statement(
               v.lineno,
               v.col_offset,

               convert_target         (v.target),
               convert_modify_operator(v.op),
               convert_expression     (v.value),
           )


#
#   convert_pass_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Pass_Statement` (i.e.: `_ast.Pass`) to a `Tree_Pass_Statement`.
#
assert Native_AbstractSyntaxTree_Pass_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Pass_Statement._fields     == (())


def convert_pass_statement(v):
    return convert_keyword_statement(v, create_Tree_Pass_Statement)


#
#   convert_print_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Print_Statement` (i.e.: `_ast.Print`) to a `Tree_Print_Statement`.
#
assert Native_AbstractSyntaxTree_Print_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Print_Statement._fields     == (('dest', 'values', 'nl'))


def convert_print_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.dest)
    assert fact_is_some_native_list                                                        (v.values)
    assert fact_is_native_boolean                                                          (v.nl)

    return create_Tree_Print_Statement(
               v.lineno,
               v.col_offset,

               convert_none_OR_expression      (v.dest),
               convert_some_list_of_expressions(v.values),
               v.nl,
           )


#
#   convert_raise_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Raise_Statement` (i.e.: `_ast.Raise`) to a `Tree_Raise_Statement`.
#
assert Native_AbstractSyntaxTree_Raise_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Raise_Statement._fields     == (('type', 'inst', 'tback'))


def convert_raise_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.inst)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.tback)

    return create_Tree_Raise_Statement(
               v.lineno,
               v.col_offset,

               convert_none_OR_expression(v.type),
               convert_none_OR_expression(v.inst),
               convert_none_OR_expression(v.tback),
           )


#
#   convert_return_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_Return_Statement` (i.e.: `_ast.Return`) to a `Tree_Return_Statement`.
#
assert Native_AbstractSyntaxTree_Return_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Return_Statement._fields     == (('value',))


def convert_return_statement(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Return_Statement(
               v.lineno,
               v.col_offset,

               convert_none_OR_expression(v.value),
           )
