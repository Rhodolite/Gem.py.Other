#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Target - Convert Python Abstract Syntax Tree Targets to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Context              import  convert_load_OR_store_context
from    Z.Tree.Convert_Index                import  convert_index_clause
from    Z.Tree.Convert_Operator             import  convert_binary_operator
from    Z.Tree.Name                         import  create_Tree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Target                       import  create_Tree_Attribute
from    Z.Tree.Target                       import  create_Tree_List_Expression
from    Z.Tree.Target                       import  create_Tree_Subscript_Expression
from    Z.Tree.Target                       import  create_Tree_Tuple_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__INDEX


#
#   convert_many_expression(self) - Common code for `convert_list_expression` and `convert_tuple_expression`
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
def convert_many_expression(self, create):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_some_native_list                                         (self.elts)
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(self.ctx)

    return create(
               self.lineno,
               self.col_offset,

               convert_some_list_of_expressions(self.elts),
               convert_load_OR_store_context   (self.ctx),
           )


#
#   convert_attribute_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Attribute_Expression` (i.e.: `_ast.Expr`) to a `Tree_Attribute`.
#
assert Native_AbstractSyntaxTree_Attribute_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Attribute_Expression._fields     == (('value', 'attr', 'ctx'))


def convert_attribute_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (self.value)
    assert fact_is_full_native_string                                              (self.attr)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    return create_Tree_Attribute(
               self.lineno,
               self.col_offset,

               convert_expression(self.value),
               self.attr,
               convert_delete_load_OR_store_context(self.ctx),
          )


#
#   convert_list_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
assert Native_AbstractSyntaxTree_List_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Expression._fields     == (('elts', 'ctx'))


def convert_list_expression(self):
    return convert_many_expression(self, create_Tree_List_Expression)


#
#   convert_name_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to a `Tree_Name`.
#
#       The context (`.ctx` member) must be an instance of one of the following types:
#
#           Native_AbstractSyntaxTree_Delete_Context
#           Native_AbstractSyntaxTree_Load_Context
#           Native_AbstractSyntaxTree_Store_Context
#
#       The context (`.ctx` member) MAY NOT be an instance of `Native_AbstractSyntaxTree_Param`.
#
#       To handle a context which is an instance of `Native_AbstractSyntaxTree_Param`, call `convert_name_parameter`
#       instead.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string                                              (self.id)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    return create_Tree_Name(
               self.lineno,
               self.col_offset,

               self.id,
               convert_delete_load_OR_store_context(self.ctx),
           )


#
#   convert_subscript_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Subscript_Expression` (i.e.: `_ast.Subscript`) to a
#       `Tree_Subscript_Expression`.
#
assert Native_AbstractSyntaxTree_Subscript_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Subscript_Expression._fields     == (('value', 'slice', 'ctx'))


def convert_subscript_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (self.value)
    assert fact_is__ANY__native__abstract_syntax_tree__INDEX                       (self.slice)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    return create_Tree_Subscript_Expression(
               self.lineno,
               self.col_offset,
               
               convert_expression                  (self.value),
               convert_index_clause                (self.slice),
               convert_delete_load_OR_store_context(self.ctx),
           )


#
#   convert_tuple_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Tuple_Expression` (i.e.: `_ast.Tuple`) to a `Tree_Tuple_Expression`.
#
assert Native_AbstractSyntaxTree_Tuple_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Tuple_Expression._fields     == (('elts', 'ctx'))


def convert_tuple_expression(self):
    return convert_many_expression(self, create_Tree_Tuple_Expression)


#
#   convert_none_OR_target(v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Target`.
#
def convert_none_OR_target(v):
    if v is None:
        return None

    return convert_target(v)


#
#<convert_target>
#
#   map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_target" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method = {
        Native_AbstractSyntaxTree_Attribute_Expression : convert_attribute_expression,
        Native_AbstractSyntaxTree_List_Expression      : convert_list_expression,
        Native_AbstractSyntaxTree_Name                 : convert_name_expression,
        Native_AbstractSyntaxTree_Subscript_Expression : convert_subscript_expression,
        Native_AbstractSyntaxTree_Tuple_Expression     : convert_tuple_expression,
    }


#
#   convert_target(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
#       The expression must be a "target" expression.
#
def convert_target(v):
    convert_target__pseudo_method = (
            map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method[type(v)]
        )

    return convert_target__pseudo_method(v)
#</convert_target>


#
#   convert_full_list_of_targets(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Expression`.
#
#       Each of the expressions must be a target expresion.
#
def convert_full_list_of_targets(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_target(v)   for v in sequence]
