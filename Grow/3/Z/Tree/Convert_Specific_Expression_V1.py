#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Specific_Expression_V1 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Argument_V1          import  convert_list_of_keyword_arguments
from    Z.Tree.Convert_Comprehension_V1     import  convert_full_list_of_comprehensions
from    Z.Tree.Convert_Expression_V1        import  convert_value_expression
from    Z.Tree.Convert_Expression_V1        import  convert_full_list_of_value_expressions
from    Z.Tree.Convert_Expression_V1        import  convert_none_OR_value_expression
from    Z.Tree.Convert_Expression_V1        import  convert_list_of_value_expressions
from    Z.Tree.Convert_Operator_V1          import  convert_binary_operator
from    Z.Tree.Convert_Operator_V1          import  convert_full_list_of_compare_operators
from    Z.Tree.Convert_Operator_V1          import  convert_logical_operator
from    Z.Tree.Convert_Operator_V1          import  convert_unary_operator
from    Z.Tree.Convert_Parameter_V1         import  convert_parameter_tuple_0
from    Z.Tree.Expression_V1                import  create_Tree_Backquote_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Binary_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Call_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Compare_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Generator_Comprehension
from    Z.Tree.Expression_V1                import  create_Tree_If_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Lambda_Expression
from    Z.Tree.Expression_V1                import  create_Tree_List_Comprehension
from    Z.Tree.Expression_V1                import  create_Tree_Logical_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Map_Comprehension
from    Z.Tree.Expression_V1                import  create_Tree_Map_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Number
from    Z.Tree.Expression_V1                import  create_Tree_Set_Comprehension
from    Z.Tree.Expression_V1                import  create_Tree_Set_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Unary_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Yield_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_ANY_native_number
    from    Capital.Fact                        import  fact_is_native_list
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__all_parameters
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Backquote_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Call_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Generator_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Lambda_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression


#
#   convert_value_comprehension(v)
#
#       Base code for `convert_generator_comprehension` & `convert_list_comprehension`.
#
def convert_value_comprehension(v, create):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.elt)
    assert fact_is_full_native_list                                    (v.generators)

    return create(
               v.lineno,
               v.col_offset,

               convert_value_expression           (v.elt),
               convert_full_list_of_comprehensions(v.generators),
           )


#
#   convert_backquote_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Backquote_Expression` (i.e.: `_ast.Repr`) to a `Tree_Backquote_Expression`.
#
assert Native_AbstractSyntaxTree_Backquote_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Backquote_Expression._fields     == (('value',))


def convert_backquote_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Backquote_Expression(
               v.lineno,
               v.col_offset,

               convert_value_expression(v.value),
          )


#
#   convert_binary_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Binary_Expression` (i.e.: `_ast.BinOp`) to a `Tree_Binary_Expression`.
#
assert Native_AbstractSyntaxTree_Binary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Binary_Expression._fields     == (('left', 'op', 'right'))


def convert_binary_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.left)
    assert fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR (v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.right)

    return create_Tree_Binary_Expression(
               v.lineno,
               v.col_offset,

               convert_value_expression(v.left),
               convert_binary_operator (v.op),
               convert_value_expression(v.right),
          )


#
#   convert_call_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Call_Expression` (i.e.: `_ast.Call`) to a `Tree_Call`.
#
assert Native_AbstractSyntaxTree_Call_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Call_Expression._fields     == (('func', 'args', 'keywords', 'starargs', 'kwargs'))


def convert_call_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION                    (v.func)
    assert fact_is_native_list                                                             (v.args)
    assert fact_is_native_list                                                             (v.keywords)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.starargs)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.kwargs)

    return create_Tree_Call_Expression(
               v.lineno,
               v.col_offset,

               convert_value_expression         (v.func),
               convert_list_of_value_expressions(v.args),
               convert_list_of_keyword_arguments(v.keywords),
               convert_none_OR_value_expression (v.starargs),
               convert_none_OR_value_expression (v.kwargs),
           )


#
#   convert_compare_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Compare_Expression` (i.e.: `_ast.Compare`) to a `Tree_Compare_Expression`.
#
assert Native_AbstractSyntaxTree_Compare_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Compare_Expression._fields     == (('left', 'ops', 'comparators'))


def convert_compare_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.left)
    assert fact_is_full_native_list                                    (v.ops)
    assert fact_is_full_native_list                                    (v.comparators)

    return create_Tree_Compare_Expression(
               v.lineno,
               v.col_offset,

               convert_value_expression              (v.left),
               convert_full_list_of_compare_operators(v.ops),
               convert_full_list_of_value_expressions(v.comparators),
          )


#
#   convert_generator_comprehension(v)
#
#       Convert a `Native_AbstractSyntaxTree_Generator_Comprehension` (i.e.: `_ast.GeneratorExp`) to a
#       `Tree_Generator_Comprehension`.
#
#   Example:
#
#       In the following statement:
#
#           squares = (x * x   for x in range(10))
#
#       The expression `(x * x   for x in range(10))` is a "generator comprehension".
#
#   NOTE:
#
#       Python calls this a `_ast.GeneratorExp`, however, it is much more similiar to other comprehensions
#       (i.e.: what python calls `_ast.ListComp`) -- so we name it `Native_AbstractSyntaxTree_Generator_Comprehension`
#       (i.e.: a "comprehension" instead of an "expression").
#
assert Native_AbstractSyntaxTree_Generator_Comprehension._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Generator_Comprehension._fields     == (('elt', 'generators'))


def convert_generator_comprehension(v):
    return convert_value_comprehension(v, create_Tree_Generator_Comprehension)


#
#   convert_if_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_If_Expression` (i.e.: `_ast.IfExp`) to a `Tree_If_Expression`.
#
assert Native_AbstractSyntaxTree_If_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Expression._fields     == (('test', 'body', 'orelse'))


def convert_if_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.test)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.body)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.orelse)

    return create_Tree_If_Expression(
               v.lineno,
               v.col_offset,

               convert_value_expression(v.test),
               convert_value_expression(v.body),
               convert_value_expression(v.orelse),
          )


#
#   convert_lambda_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_lambda_Expression` (i.e.: `_ast.Lambda`) to a `Tree_Lambda_Expression`.
#
assert Native_AbstractSyntaxTree_Lambda_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Lambda_Expression._fields     == (('args', 'body'))


def convert_lambda_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__native__abstract_syntax_tree__all_parameters       (v.args)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.body)

    return create_Tree_Lambda_Expression(
               v.lineno,
               v.col_offset,

               convert_parameter_tuple_0(v.args),
               convert_value_expression (v.body),
          )


#
#   convert_list_comprehension(v)
#
#       Convert a `Native_AbstractSyntaxTree_List_Comprehension` (i.e.: `_ast.ListComp`) to a `Tree_List_Comprehension`.
#
#   Example:
#
#       In the following statement:
#
#           squares = [x * x   for x in range(10)]
#
#       The expression `[x * x   for x in range(10)]` is a "list comprehension" (i.e.: a `list` created from a
#       `for` loop).
#
assert Native_AbstractSyntaxTree_List_Comprehension._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Comprehension._fields     == (('elt', 'generators'))


def convert_list_comprehension(v):
    return convert_value_comprehension(v, create_Tree_List_Comprehension)


#
#   convert_logical_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Logical_Expression` (i.e.: `_ast.BoolOp`) to a `Tree_Logical_Expression`.
#
assert Native_AbstractSyntaxTree_Logical_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Logical_Expression._fields     == (('op', 'values'))


def convert_logical_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR(v.op)
    assert fact_is_full_native_list                                    (v.values)

    return create_Tree_Logical_Expression(
               v.lineno,
               v.col_offset,

               convert_logical_operator              (v.op),
               convert_full_list_of_value_expressions(v.values),
          )


#
#   convert_map_comprehension(v)
#
#       Convert a `Native_AbstractSyntaxTree_Map_Comprehension` (i.e.: `_ast.DictComp`) to a `Tree_Map_Comprehension`.
#
#   Example:
#
#       In the following statement:
#
#           cost = { k : v   for [k, v] in [ [ 'apple', 10 ], [ 'cherry', 20 ] ] }
#
#       The expression `{ k : v   for [k, v] in [ [ 'apple', 10 ], [ 'cherry', 20 ] ] }` is a "Map comprehension"
#       (i.e.: a `dict` created from a `for` loop).
#
assert Native_AbstractSyntaxTree_Map_Comprehension._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Map_Comprehension._fields     == (('key', 'value', 'generators'))


def convert_map_comprehension(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.key)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)
    assert fact_is_full_native_list                                    (v.generators)

    return create_Tree_Map_Comprehension(
               v.lineno,
               v.col_offset,

               convert_value_expression           (v.key),
               convert_value_expression           (v.value),
               convert_full_list_of_comprehensions(v.generators),
           )


#
#   convert_map_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Map_Expression` (i.e.: `_ast.Dict`) to a `Tree_Map_Expression`.
#
assert Native_AbstractSyntaxTree_Map_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Map_Expression._fields     == (('keys', 'values'))


def convert_map_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_native_list(v.keys)
    assert fact_is_native_list(v.values)

    assert len(v.keys) == len(v.values)

    return create_Tree_Map_Expression(
               v.lineno,
               v.col_offset,

               convert_list_of_value_expressions(v.keys),
               convert_list_of_value_expressions(v.values),
           )


#
#   convert_number(v)
#
#       Convert a `Native_AbstractSyntaxTree_Number` (i.e.: `_ast.Num`) to a `Tree_Number`.
#
assert Native_AbstractSyntaxTree_Number._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Number._fields     == (('n',))


def convert_number(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_ANY_native_number(v.n)

    return create_Tree_Number(v.lineno, v.col_offset, v.n)


#
#   convert_set_comprehension(v)
#
#       Convert a `Native_AbstractSyntaxTree_Set_Comprehension` (i.e.: `_ast.SetComp`) to a `Tree_Set_Comprehension`.
#
#   Example:
#
#       In the following statement:
#
#           squares = {x * x   for x in range(10)}
#
#       The expression `{x * x   for x in range(10)}` is a "set comprehension" (i.e.: a `set` created from a
#       `for` loop).
#
assert Native_AbstractSyntaxTree_Set_Comprehension._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Set_Comprehension._fields     == (('elt', 'generators'))


def convert_set_comprehension(v):
    return convert_value_comprehension(v, create_Tree_Set_Comprehension)


#
#   convert_set_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Set_Expression` (i.e.: `_ast.Set`) to a `Tree_Set_Expression`.
#
assert Native_AbstractSyntaxTree_Set_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Set_Expression._fields     == (('elts',))


def convert_set_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_native_list(v.elts)

    return create_Tree_Set_Expression(
               v.lineno,
               v.col_offset,

               convert_list_of_value_expressions(v.elts),
           )


#
#   convert_unary_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Unary_Expression` (i.e.: `_ast.UnaryOp`) to a `Tree_Unary_Expression`.
#
assert Native_AbstractSyntaxTree_Unary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Unary_Expression._fields     == (('op', 'operand'))


def convert_unary_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR  (v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.operand)

    return create_Tree_Unary_Expression(
               v.lineno,
               v.col_offset,

               convert_unary_operator  (v.op),
               convert_value_expression(v.operand),
          )


#
#   convert_yield_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Yield_Expression` (i.e.: `_ast.Yield`) to a `Tree_Yield_Expression`.
#
assert Native_AbstractSyntaxTree_Yield_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Yield_Expression._fields     == (('value',))


def convert_yield_expression(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Yield_Expression(
               v.lineno,
               v.col_offset,

               convert_none_OR_value_expression(v.value),
          )
