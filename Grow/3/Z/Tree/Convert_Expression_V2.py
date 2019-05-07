#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Expression_V2 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 2.
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


#
#<order>
#
#   To avoid import loops:
#
#           1)  `convert_expression`,
#
#           2)  `convert_full_list_of_expressions`, and
#
#           3)  `convert_some_list_of_expressions`
#
#   must be defined fisrt, since lots of other modules (that we import) need to import these function.s
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   convert_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_expression(z, v):
    convert_expression__function = (
            z.map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function[type(v)]
        )

    return convert_expression__function(z, v)


#
#   convert_none_OR_expression(z, v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
def convert_none_OR_expression(z, v):
    assert fact_is_convert_zone(z)

    if v is None:
        return None

    return convert_expression(z, v)


#
#   convert_full_list_of_expressions(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Expression`.
#
convert_full_list_of_expressions = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#
#   convert_some_list_of_expressions(z, sequence)
#
#       Convert a `SomeNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `SomeNativeList of Tree_Expression`.
#
convert_some_list_of_expressions = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#</order>


from    Capital.Core                        import  trace
from    Capital.Types                       import  NoneType
from    Z.Tree.Convert_Operator             import  convert_binary_operator
from    Z.Tree.Convert_Operator             import  convert_full_list_of_compare_operators
from    Z.Tree.Convert_Operator             import  convert_logical_operator
from    Z.Tree.Convert_Operator             import  convert_unary_operator
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
from    Z.Tree.Expression_V1                import  create_Tree_String
from    Z.Tree.Expression_V1                import  create_Tree_Unary_Expression
from    Z.Tree.Expression_V1                import  create_Tree_Yield_Expression
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
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_empty_native_list
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_native_none
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_some_native_string
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION


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

    return create_Tree_Backquote_Expression(
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

    return create_Tree_Binary_Expression(
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

    return create_Tree_Call_Expression(
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

    return create_Tree_Compare_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression                  (z, v.left),
               convert_full_list_of_compare_operators(v.ops),
               z.convert_full_list_of_expressions    (z, v.comparators),
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

    return convert_value_comprehension(z, v, create_Tree_Generator_Comprehension)


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

    return create_Tree_If_Expression(
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

    return create_Tree_Lambda_Expression(
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

    return convert_value_comprehension(z, v, create_Tree_List_Comprehension)


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

    return create_Tree_Logical_Expression(
               v.lineno,
               v.col_offset,

               convert_logical_operator          (v.op),
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

    return create_Tree_Map_Comprehension(
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

    return create_Tree_Map_Expression(
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

    return create_Tree_Number(v.lineno, v.col_offset, v.n)


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

    return convert_value_comprehension(z, v, create_Tree_Set_Comprehension)


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

    return create_Tree_Set_Expression(
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

    return create_Tree_String(v.lineno, v.col_offset, v.s)


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

    return create_Tree_Unary_Expression(
               v.lineno,
               v.col_offset,

               convert_unary_operator(v.op),
               z.convert_expression  (z, v.operand),
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

    return create_Tree_Yield_Expression(
               v.lineno,
               v.col_offset,

               z.convert_none_OR_expression(z, v.value),
          )
