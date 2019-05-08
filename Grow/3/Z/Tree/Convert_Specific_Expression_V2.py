#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Specific_Expression_V2 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 2.
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


from    Z.Tree.Convert_Operator_V1          import  convert_binary_operator


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Native_String               import  fact_is_some_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Backquote_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Call_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Generator_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Lambda_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Comprehension
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression


#
#   convert_value_comprehension(z, v)
#
#       Base code for `convert_{generator,list,set}_comprehension`.
#
def convert_value_comprehension(z, v, create):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.elt)
    assert fact_is_full_native_list                              (v.generators)

    return create(
               v.lineno,
               v.col_offset,

               z.convert_expression                 (z, v.elt),
               z.convert_full_list_of_comprehensions(z, v.generators),
           )


#
#   convert_backquote_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Backquote_Expression` (i.e.: `_ast.Repr`) to a `Tree_Backquote_Expression`.
#
assert Native_AbstractSyntaxTree_Backquote_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Backquote_Expression._fields     == (('value',))


def convert_backquote_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.value)

    return z.create_Tree_Backquote_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression(z, v.value),
          )


#
#   convert_binary_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Binary_Expression` (i.e.: `_ast.BinOp`) to a `Tree_Binary_Expression`.
#
assert Native_AbstractSyntaxTree_Binary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Binary_Expression._fields     == (('left', 'op', 'right'))


def convert_binary_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (v.left)
    assert fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR(v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (v.right)

    return z.create_Tree_Binary_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression   (z, v.left),
               convert_binary_operator(v.op),
               z.convert_expression   (z, v.right),
          )


#
#   convert_call_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Call_Expression` (i.e.: `_ast.Call`) to a `Tree_Call`.
#
assert Native_AbstractSyntaxTree_Call_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Call_Expression._fields     == (('func', 'args', 'keywords', 'starargs', 'kwargs'))


def convert_call_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (v.func)
    assert fact_is_some_native_list                                                  (v.args)
    assert fact_is_some_native_list                                                  (v.keywords)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.starargs)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.kwargs)

    return z.create_Tree_Call_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression                    (z, v.func),
               z.convert_some_list_of_expressions      (z, v.args),
               z.convert_some_list_of_keyword_arguments(z, v.keywords),
               z.convert_none_OR_expression            (z, v.starargs),
               z.convert_none_OR_expression            (z, v.kwargs),
           )


#
#   convert_compare_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Compare_Expression` (i.e.: `_ast.Compare`) to a `Tree_Compare_Expression`.
#
assert Native_AbstractSyntaxTree_Compare_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Compare_Expression._fields     == (('left', 'ops', 'comparators'))


def convert_compare_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.left)
    assert fact_is_full_native_list                              (v.ops)
    assert fact_is_full_native_list                              (v.comparators)

    return z.create_Tree_Compare_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression                    (z, v.left),
               z.convert_full_list_of_compare_operators(z, v.ops),
               z.convert_full_list_of_expressions      (z, v.comparators),
          )


#
#   convert_generator_comprehension(z, v)
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


def convert_generator_comprehension(z, v):
    assert fact_is_convert_zone(z)

    return convert_value_comprehension(z, v, z.create_Tree_Generator_Comprehension)


#
#   convert_if_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_If_Expression` (i.e.: `_ast.IfExp`) to a `Tree_If_Expression`.
#
assert Native_AbstractSyntaxTree_If_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Expression._fields     == (('test', 'body', 'orelse'))


def convert_if_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.test)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.body)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.orelse)

    return z.create_Tree_If_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression(z, v.test),
               z.convert_expression(z, v.body),
               z.convert_expression(z, v.orelse),
          )


#
#   convert_lambda_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_lambda_Expression` (i.e.: `_ast.Lambda`) to a `Tree_Lambda_Expression`.
#
assert Native_AbstractSyntaxTree_Lambda_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Lambda_Expression._fields     == (('args', 'body'))


def convert_lambda_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__native__abstract_syntax_tree__parameters_all (v.args)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.body)

    return z.create_Tree_Lambda_Expression(
               v.lineno,
               v.col_offset,

               z.convert_parameters_all(z, v.args),
               z.convert_expression    (z, v.body),
          )


#
#   convert_list_comprehension(z, v)
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


def convert_list_comprehension(z, v):
    assert fact_is_convert_zone(z)

    return convert_value_comprehension(z, v, z.create_Tree_List_Comprehension)


#
#   convert_logical_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Logical_Expression` (i.e.: `_ast.BoolOp`) to a `Tree_Logical_Expression`.
#
assert Native_AbstractSyntaxTree_Logical_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Logical_Expression._fields     == (('op', 'values'))


def convert_logical_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR(v.op)
    assert fact_is_full_native_list                                    (v.values)

    return z.create_Tree_Logical_Expression(
               v.lineno,
               v.col_offset,

               z.convert_logical_operator        (z, v.op),
               z.convert_full_list_of_expressions(z, v.values),
          )


#
#   convert_map_comprehension(z, v)
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


def convert_map_comprehension(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.key)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.value)
    assert fact_is_full_native_list                              (v.generators)

    return z.create_Tree_Map_Comprehension(
               v.lineno,
               v.col_offset,

               z.convert_expression                 (z, v.key),
               z.convert_expression                 (z, v.value),
               z.convert_full_list_of_comprehensions(z, v.generators),
           )


#
#   convert_map_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Map_Expression` (i.e.: `_ast.Dict`) to a `Tree_Map_Expression`.
#
assert Native_AbstractSyntaxTree_Map_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Map_Expression._fields     == (('keys', 'values'))


def convert_map_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_list(v.keys)
    assert fact_is_some_native_list(v.values)

    assert len(v.keys) == len(v.values)

    return z.create_Tree_Map_Expression(
               v.lineno,
               v.col_offset,

               z.convert_some_list_of_expressions(z, v.keys),
               z.convert_some_list_of_expressions(z, v.values),
           )


#
#   convert_number(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Number` (i.e.: `_ast.Num`) to a `Tree_Number`.
#
assert Native_AbstractSyntaxTree_Number._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Number._fields     == (('n',))


def convert_number(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_integer(v.n)

    return z.create_Tree_Number(v.lineno, v.col_offset, v.n)


#
#   convert_set_comprehension(z, v)
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


def convert_set_comprehension(z, v):
    assert fact_is_convert_zone(z)

    return convert_value_comprehension(z, v, z.create_Tree_Set_Comprehension)


#
#   convert_set_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Set_Expression` (i.e.: `_ast.Set`) to a `Tree_Set_Expression`.
#
assert Native_AbstractSyntaxTree_Set_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Set_Expression._fields     == (('elts',))


def convert_set_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_list(v.elts)

    return z.create_Tree_Set_Expression(
               v.lineno,
               v.col_offset,

               z.convert_some_list_of_expressions(z, v.elts),
           )


#
#   convert_string(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_String` (i.e.: `_ast.Str`) to a `Tree_String`.
#
assert Native_AbstractSyntaxTree_String._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String._fields     == (('s',))


def convert_string(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_string(v.s)

    return z.create_Tree_String(v.lineno, v.col_offset, v.s)


#
#   convert_unary_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Unary_Expression` (i.e.: `_ast.UnaryOp`) to a `Tree_Unary_Expression`.
#
assert Native_AbstractSyntaxTree_Unary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Unary_Expression._fields     == (('op', 'operand'))


def convert_unary_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR(v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION    (v.operand)

    return z.create_Tree_Unary_Expression(
               v.lineno,
               v.col_offset,

               z.convert_unary_operator(z, v.op),
               z.convert_expression    (z, v.operand),
          )


#
#   convert_yield_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Yield_Expression` (i.e.: `_ast.Yield`) to a `Tree_Yield_Expression`.
#
assert Native_AbstractSyntaxTree_Yield_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Yield_Expression._fields     == (('value',))


def convert_yield_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.value)

    return z.create_Tree_Yield_Expression(
               v.lineno,
               v.col_offset,

               z.convert_none_OR_expression(z, v.value),
          )
