#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Expression - Convert Python Abstract Syntax Tree Expressions to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Capital.Types                       import  NoneType
from    Z.Tree.Convert_Argument             import  convert_some_list_of_keyword_arguments
from    Z.Tree.Convert_Comprehension        import  convert_full_list_of_comprehensions
from    Z.Tree.Convert_Name                 import  convert_name_expression
from    Z.Tree.Convert_Operator             import  convert_binary_operator
from    Z.Tree.Convert_Operator             import  convert_full_list_of_compare_operators
from    Z.Tree.Convert_Operator             import  convert_logical_operator
from    Z.Tree.Convert_Operator             import  convert_unary_operator
from    Z.Tree.Convert_Parameter            import  convert_parameters_all
from    Z.Tree.Convert_Target               import  convert_attribute_expression
from    Z.Tree.Convert_Target               import  convert_list_expression
from    Z.Tree.Convert_Target               import  convert_subscript_expression
from    Z.Tree.Convert_Target               import  convert_tuple_expression
from    Z.Tree.Expression                   import  create_Tree_Backquote_Expression
from    Z.Tree.Expression                   import  create_Tree_Binary_Expression
from    Z.Tree.Expression                   import  create_Tree_Call
from    Z.Tree.Expression                   import  create_Tree_Compare_Expression
from    Z.Tree.Expression                   import  create_Tree_Generator_Comprehension
from    Z.Tree.Expression                   import  create_Tree_If_Expression
from    Z.Tree.Expression                   import  create_Tree_Lambda_Expression
from    Z.Tree.Expression                   import  create_Tree_List_Comprehension
from    Z.Tree.Expression                   import  create_Tree_Logical_Expression
from    Z.Tree.Expression                   import  create_Tree_Map_Comprehension
from    Z.Tree.Expression                   import  create_Tree_Map_Expression
from    Z.Tree.Expression                   import  create_Tree_Number
from    Z.Tree.Expression                   import  create_Tree_Set_Comprehension
from    Z.Tree.Expression                   import  create_Tree_Set_Expression
from    Z.Tree.Expression                   import  create_Tree_String
from    Z.Tree.Expression                   import  create_Tree_Unary_Expression
from    Z.Tree.Expression                   import  create_Tree_Yield_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
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
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression
from    Z.Tree.Produce_Convert_List         import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List         import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


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
#   convert_value_comprehension(self)
#
#       Base code for `convert_generator_comprehension` & `convert_list_comprehension`.
#
def convert_value_comprehension(self, create):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.elt)
    assert fact_is_full_native_list                              (self.generators)

    return create(
               self.lineno,
               self.col_offset,

               convert_expression                 (self.elt),
               convert_full_list_of_comprehensions(self.generators),
           )


#
#   convert_backquote_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Backquote_Expression` (i.e.: `_ast.Repr`) to a `Tree_Backquote_Expression`.
#
assert Native_AbstractSyntaxTree_Backquote_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Backquote_Expression._fields     == (('value',))


def convert_backquote_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Backquote_Expression(
               self.lineno,
               self.col_offset,

               convert_expression(self.value),
          )


#
#   convert_binary_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Binary_Expression` (i.e.: `_ast.BinOp`) to a `Tree_Binary_Expression`.
#
assert Native_AbstractSyntaxTree_Binary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Binary_Expression._fields     == (('left', 'op', 'right'))


def convert_binary_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (self.left)
    assert fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR(self.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (self.right)

    return create_Tree_Binary_Expression(
               self.lineno,
               self.col_offset,

               convert_expression     (self.left),
               convert_binary_operator(self.op),
               convert_expression     (self.right),
          )


#
#   convert_call_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Call_Expression` (i.e.: `_ast.Call`) to a `Tree_Call`.
#
assert Native_AbstractSyntaxTree_Call_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Call_Expression._fields     == (('func', 'args', 'keywords', 'starargs', 'kwargs'))


def convert_call_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (self.func)
    assert fact_is_some_native_list                                                  (self.args)
    assert fact_is_some_native_list                                                  (self.keywords)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.starargs)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.kwargs)

    return create_Tree_Call(
               self.lineno,
               self.col_offset,

               convert_expression                    (self.func),
               convert_some_list_of_expressions      (self.args),
               convert_some_list_of_keyword_arguments(self.keywords),
               convert_none_OR_expression            (self.starargs),
               convert_none_OR_expression            (self.kwargs),
           )


#
#   convert_compare_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Compare_Expression` (i.e.: `_ast.Compare`) to a `Tree_Compare_Expression`.
#
assert Native_AbstractSyntaxTree_Compare_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Compare_Expression._fields     == (('left', 'ops', 'comparators'))


def convert_compare_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.left)
    assert fact_is_full_native_list                              (self.ops)
    assert fact_is_full_native_list                              (self.comparators)

    return create_Tree_Compare_Expression(
               self.lineno,
               self.col_offset,

               convert_expression                    (self.left),
               convert_full_list_of_compare_operators(self.ops),
               convert_full_list_of_expressions      (self.comparators),
          )


#
#   convert_generator_comprehension(self)
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


def convert_generator_comprehension(self):
    return convert_value_comprehension(self, create_Tree_Generator_Comprehension)


#
#   convert_if_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_If_Expression` (i.e.: `_ast.IfExp`) to a `Tree_If_Expression`.
#
assert Native_AbstractSyntaxTree_If_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Expression._fields     == (('test', 'body', 'orelse'))


def convert_if_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.test)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.body)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.orelse)

    return create_Tree_If_Expression(
               self.lineno,
               self.col_offset,

               convert_expression(self.test),
               convert_expression(self.body),
               convert_expression(self.orelse),
          )


#
#   convert_lambda_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_lambda_Expression` (i.e.: `_ast.Lambda`) to a `Tree_Lambda_Expression`.
#
assert Native_AbstractSyntaxTree_Lambda_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Lambda_Expression._fields     == (('args', 'body'))


def convert_lambda_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__native__abstract_syntax_tree__parameters_all (self.args)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.body)

    return create_Tree_Lambda_Expression(
               self.lineno,
               self.col_offset,

               convert_parameters_all(self.args),
               convert_expression    (self.body),
          )


#
#   convert_list_comprehension(self)
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


def convert_list_comprehension(self):
    return convert_value_comprehension(self, create_Tree_List_Comprehension)


#
#   convert_logical_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Logical_Expression` (i.e.: `_ast.BoolOp`) to a `Tree_Logical_Expression`.
#
assert Native_AbstractSyntaxTree_Logical_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Logical_Expression._fields     == (('op', 'values'))


def convert_logical_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR(self.op)
    assert fact_is_full_native_list                                    (self.values)

    return create_Tree_Logical_Expression(
               self.lineno,
               self.col_offset,

               convert_logical_operator        (self.op),
               convert_full_list_of_expressions(self.values),
          )


#
#   convert_map_comprehension(self)
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


def convert_map_comprehension(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.key)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.value)
    assert fact_is_full_native_list                              (self.generators)

    return create_Tree_Map_Comprehension(
               self.lineno,
               self.col_offset,

               convert_expression                 (self.key),
               convert_expression                 (self.value),
               convert_full_list_of_comprehensions(self.generators),
           )


#
#   convert_map_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Map_Expression` (i.e.: `_ast.Dict`) to a `Tree_Map_Expression`.
#
assert Native_AbstractSyntaxTree_Map_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Map_Expression._fields     == (('keys', 'values'))


def convert_map_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_some_native_list(self.keys)
    assert fact_is_some_native_list(self.values)

    assert len(self.keys) == len(self.values)

    return create_Tree_Map_Expression(
               self.lineno,
               self.col_offset,

               convert_some_list_of_expressions(self.keys),
               convert_some_list_of_expressions(self.values),
           )


#
#   convert_number(self)
#
#       Convert a `Native_AbstractSyntaxTree_Number` (i.e.: `_ast.Num`) to a `Tree_Number`.
#
assert Native_AbstractSyntaxTree_Number._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Number._fields     == (('n',))


def convert_number(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_some_native_integer(self.n)

    return create_Tree_Number(self.lineno, self.col_offset, self.n)


#
#   convert_set_comprehension(self)
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


def convert_set_comprehension(self):
    return convert_value_comprehension(self, create_Tree_Set_Comprehension)


#
#   convert_set_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Set_Expression` (i.e.: `_ast.Set`) to a `Tree_Set_Expression`.
#
assert Native_AbstractSyntaxTree_Set_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Set_Expression._fields     == (('elts',))


def convert_set_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_some_native_list(self.elts)

    return create_Tree_Set_Expression(
               self.lineno,
               self.col_offset,

               convert_some_list_of_expressions(self.elts),
           )


#
#   convert_string(self)
#
#       Convert a `Native_AbstractSyntaxTree_String` (i.e.: `_ast.Str`) to a `Tree_String`.
#
assert Native_AbstractSyntaxTree_String._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String._fields     == (('s',))


def convert_string(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_some_native_string(self.s)

    return create_Tree_String(self.lineno, self.col_offset, self.s)


#
#   convert_unary_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Unary_Expression` (i.e.: `_ast.UnaryOp`) to a `Tree_Unary_Expression`.
#
assert Native_AbstractSyntaxTree_Unary_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Unary_Expression._fields     == (('op', 'operand'))


def convert_unary_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR(self.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION    (self.operand)

    return create_Tree_Unary_Expression(
               self.lineno,
               self.col_offset,

               convert_unary_operator(self.op),
               convert_expression    (self.operand),
          )


#
#   convert_yield_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Yield_Expression` (i.e.: `_ast.Yield`) to a `Tree_Yield_Expression`.
#
assert Native_AbstractSyntaxTree_Yield_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Yield_Expression._fields     == (('value',))


def convert_yield_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Yield_Expression(
               self.lineno,
               self.col_offset,

               convert_none_OR_expression(self.value),
          )


#
#<convert_expression>
#
#   NOTE:
#       Although `convert_expression` and `convert_statement *COULD* be combined into one routine (and also only one
#       `map__Native_AbstractSyntaxTree_ANY__to__convert_*__pseudo_method` table, it is much clearer to have two
#       seperate routines, to distinguish betweeen "expression" and "statements"
#
#   map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__pseudo_method
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_expression" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__pseudo_method = {
        Native_AbstractSyntaxTree_Attribute_Expression    : convert_attribute_expression,
        Native_AbstractSyntaxTree_Backquote_Expression    : convert_backquote_expression,
        Native_AbstractSyntaxTree_Binary_Expression       : convert_binary_expression,
        Native_AbstractSyntaxTree_Call_Expression         : convert_call_expression,
        Native_AbstractSyntaxTree_Compare_Expression      : convert_compare_expression,
        Native_AbstractSyntaxTree_Generator_Comprehension : convert_generator_comprehension,
        Native_AbstractSyntaxTree_If_Expression           : convert_if_expression,
        Native_AbstractSyntaxTree_Lambda_Expression       : convert_lambda_expression,
        Native_AbstractSyntaxTree_List_Comprehension      : convert_list_comprehension,
        Native_AbstractSyntaxTree_List_Expression         : convert_list_expression,
        Native_AbstractSyntaxTree_Logical_Expression      : convert_logical_expression,
        Native_AbstractSyntaxTree_Map_Comprehension       : convert_map_comprehension,
        Native_AbstractSyntaxTree_Map_Expression          : convert_map_expression,
        Native_AbstractSyntaxTree_Name                    : convert_name_expression,
        Native_AbstractSyntaxTree_Number                  : convert_number,
        Native_AbstractSyntaxTree_Set_Comprehension       : convert_set_comprehension,
        Native_AbstractSyntaxTree_Set_Expression          : convert_set_expression,
        Native_AbstractSyntaxTree_String                  : convert_string,
        Native_AbstractSyntaxTree_Subscript_Expression    : convert_subscript_expression,
        Native_AbstractSyntaxTree_Tuple_Expression        : convert_tuple_expression,
        Native_AbstractSyntaxTree_Unary_Expression        : convert_unary_expression,
        Native_AbstractSyntaxTree_Yield_Expression        : convert_yield_expression,
    }


#
#   convert_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_expression(v):
    convert_expression__pseudo_method = (
            map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__pseudo_method[type(v)]
        )

    return convert_expression__pseudo_method(v)
#</convert_expression>


#
#   convert_none_OR_expression(v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
def convert_none_OR_expression(v):
    if v is None:
        return None

    return convert_expression(v)


#
#   convert_full_list_of_expressions(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Expression`.
#
convert_full_list_of_expressions = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#
#   convert_some_list_of_expressions(sequence)
#
#       Convert a `SomeNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `SomeNativeList of Tree_Expression`.
#
convert_some_list_of_expressions = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#
#   Handle import loops
#
from    Z.Parser.Global                 import  parser_globals


import  Z.Tree.Convert_Argument
import  Z.Tree.Convert_Comprehension
import  Z.Tree.Convert_Except
import  Z.Tree.Convert_Index
import  Z.Tree.Convert_Parameter
import  Z.Tree.Convert_Target


Z.Tree.Convert_Argument     .convert_expression               = convert_expression
Z.Tree.Convert_Comprehension.convert_expression               = convert_expression
Z.Tree.Convert_Comprehension.convert_some_list_of_expressions = convert_some_list_of_expressions
Z.Tree.Convert_Except       .convert_none_OR_expression       = convert_none_OR_expression
Z.Tree.Convert_Index        .convert_expression               = convert_expression
Z.Tree.Convert_Index        .convert_none_OR_expression       = convert_none_OR_expression
Z.Tree.Convert_Parameter    .convert_some_list_of_expressions = convert_some_list_of_expressions
Z.Tree.Convert_Target       .convert_expression               = convert_expression
Z.Tree.Convert_Target       .convert_some_list_of_expressions = convert_some_list_of_expressions



target_version = parser_globals.target_version


if target_version == 1:
    import  Z.Tree.Convert_Attribute_V1
    import  Z.Tree.Convert_Many_V1
    import  Z.Tree.Convert_Subscript_V1

    Z.Tree.Convert_Attribute_V1.convert_expression               = convert_expression
    Z.Tree.Convert_Many_V1     .convert_some_list_of_expressions = convert_some_list_of_expressions
    Z.Tree.Convert_Subscript_V1.convert_expression               = convert_expression
elif target_version == 2:
    import  Z.Tree.Convert_Attribute_V2
    import  Z.Tree.Convert_Many_V1                  #   "_V1" on purpose
    import  Z.Tree.Convert_Subscript_V1             #   "_V1" on purpose

    Z.Tree.Convert_Attribute_V2.convert_expression               = convert_expression
    Z.Tree.Convert_Many_V1     .convert_some_list_of_expressions = convert_some_list_of_expressions
    Z.Tree.Convert_Subscript_V1.convert_expression               = convert_expression
elif target_version == 3:
    import  Z.Tree.Convert_Attribute_V3
    import  Z.Tree.Convert_Many_V3
    import  Z.Tree.Convert_Subscript_V3

    Z.Tree.Convert_Attribute_V3.convert_expression               = convert_expression
    Z.Tree.Convert_Many_V3     .convert_some_list_of_expressions = convert_some_list_of_expressions
    Z.Tree.Convert_Subscript_V3.convert_expression               = convert_expression
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Expression.py: unknown tree target version: {!r}', target_version)
