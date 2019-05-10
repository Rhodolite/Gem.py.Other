#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Many_V1 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 1
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#

from    Z.Tree.Convert_Context_V1           import  convert_load_OR_store_context
from    Z.Tree.Convert_Expression_V1        import  convert_some_list_of_expressions
from    Z.Tree.Many_V1                      import  create_Tree_List_Expression
from    Z.Tree.Many_V1                      import  create_Tree_Tuple_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_native_list
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression



#
#   convert_many_expression(v, create) - Common code for `convert_{list,tuple}_expression`.
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
def convert_many_expression(v, create):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_native_list                                              (v.elts)
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v.ctx)

    return create(
               v.lineno,
               v.col_offset,

               convert_some_list_of_expressions(v.elts),
               convert_load_OR_store_context   (v.ctx),
           )


#
#   convert_list_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
assert Native_AbstractSyntaxTree_List_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Expression._fields     == (('elts', 'ctx'))


def convert_list_expression(v):
    return convert_many_expression(v, create_Tree_List_Expression)


#
#   convert_tuple_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Tuple_Expression` (i.e.: `_ast.Tuple`) to a `Tree_Tuple_Expression`.
#
assert Native_AbstractSyntaxTree_Tuple_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Tuple_Expression._fields     == (('elts', 'ctx'))


def convert_tuple_expression(v):
    return convert_many_expression(v, create_Tree_Tuple_Expression)
