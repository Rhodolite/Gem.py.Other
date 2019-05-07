#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Many_V4 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 4.
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


#
#   Difference between Version Version 2, Version 3, and Version 4.
#
#       Version 2:
#
#           Pass in a context to `create_Tree_List_Expression`
#
#           Pass in a context to `create_Tree_Tuple_Expression`
#
#       Version 3:
#
#           Does *NOT* exist.
#
#       Version 4:
#
#           Do not pass in a context to create `Tree_List_Expression`, but instead create one of the following two
#           classes:
#
#               Tree_Evaluate_List
#               Tree_Store_List
#
#           Do not pass in a context to create `Tree_Tuple_Expression`, but instead create one of the following two
#           classes:
#
#               Tree_Evaluate_Tuple
#               Tree_Store_Tuple
#


from    Z.Tree.Convert_Zone                 import  convert_zone
from    Z.Tree.Many_V4                      import  create_Tree_Evaluate_List
from    Z.Tree.Many_V4                      import  create_Tree_Evaluate_Tuple
from    Z.Tree.Many_V4                      import  create_Tree_Store_List
from    Z.Tree.Many_V4                      import  create_Tree_Store_Tuple
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT


#
#   convert__load_OR_store_context__TO__create_{list,tuple}_function(v)
#
#       Convert a "load" or "store" context to a create list or create tuple function.
#
map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_list_function = {
        Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_List,
        Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_List,
    }


map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_tuple_function = {
        Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Tuple,
        Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Tuple,
    }


if __debug__:
    def assert_no_context_fields(mapping):
        for k in mapping:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields(map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_list_function)
    assert_no_context_fields(map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_tuple_function)


def convert__load_OR_store_context__TO__create_list_function(v):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_list_function[type(v)]


def convert__load_OR_store_context__TO__create_tuple_function(v):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_tuple_function[type(v)]



#
#   convert_many_expression(v) - Common code for `convert_list_expression` and `convert_tuple_expression`
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_List_Expression`.
#
def convert_many_expression(v, create):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_list                                         (v.elts)
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v.ctx)

    z = convert_zone

    return create(
               v.lineno,
               v.col_offset,

               z.convert_some_list_of_expressions(z, v.elts),
           )


#
#   convert_list_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_Evaluate_List` or a
#       `Tree_Store_List`.
#
assert Native_AbstractSyntaxTree_List_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Expression._fields     == (('elts', 'ctx'))


def convert_list_expression(v):
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v.ctx)

    create_list = convert__load_OR_store_context__TO__create_list_function(v.ctx)

    return convert_many_expression(v, create_list)


#
#   convert_tuple_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Tuple_Expression` (i.e.: `_ast.Tuple`) to a `Tree_Evaluate_Tuple` or a
#       `Tree_Store_Tuple`.
#
assert Native_AbstractSyntaxTree_Tuple_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Tuple_Expression._fields     == (('elts', 'ctx'))


def convert_tuple_expression(v):
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v.ctx)

    create_tuple = convert__load_OR_store_context__TO__create_tuple_function(v.ctx)

    return convert_many_expression(v, create_tuple)
