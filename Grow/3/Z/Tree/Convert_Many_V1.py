#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Many_V1 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 1
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


from    Z.Tree.Convert_Context              import  convert_load_OR_store_context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Target                       import  create_Tree_List_Expression
from    Z.Tree.Target                       import  create_Tree_Tuple_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT



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
#   convert_list_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
assert Native_AbstractSyntaxTree_List_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Expression._fields     == (('elts', 'ctx'))


def convert_list_expression(self):
    return convert_many_expression(self, create_Tree_List_Expression)


#
#   convert_tuple_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Tuple_Expression` (i.e.: `_ast.Tuple`) to a `Tree_Tuple_Expression`.
#
assert Native_AbstractSyntaxTree_Tuple_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Tuple_Expression._fields     == (('elts', 'ctx'))


def convert_tuple_expression(self):
    return convert_many_expression(self, create_Tree_Tuple_Expression)
