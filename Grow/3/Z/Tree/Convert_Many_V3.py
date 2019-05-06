#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Many_V3 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 3
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


#
#   Difference between Version 1 & Version 3
#
#       Version 1:
#
#           Pass in a context to `create_Tree_List_Expression`
#
#           Pass in a context to `create_Tree_Tuple_Expression`
#
#       Version 2:
#
#           Does *NOT* exist.
#
#       Version 3:
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


from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Many_V3                      import  create_Tree_Evaluate_List
from    Z.Tree.Many_V3                      import  create_Tree_Evaluate_Tuple
from    Z.Tree.Many_V3                      import  create_Tree_Store_List
from    Z.Tree.Many_V3                      import  create_Tree_Store_Tuple
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
#   convert__load_OR_store_context__TO__create_{list,tuple}_function(self)
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


def convert__load_OR_store_context__TO__create_list_function(self):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_list_function[type(self)]


def convert__load_OR_store_context__TO__create_tuple_function(self):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__TO__create_tuple_function[type(self)]



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
           )


#
#   convert_list_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_List_Expression` (i.e.: `_ast.List`) to a `Tree_Evaluate_List` or a
#       `Tree_Store_List`.
#
assert Native_AbstractSyntaxTree_List_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_List_Expression._fields     == (('elts', 'ctx'))


def convert_list_expression(self):
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(self.ctx)

    create_list = convert__load_OR_store_context__TO__create_list_function(self.ctx)

    return convert_many_expression(self, create_list)


#
#   convert_tuple_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Tuple_Expression` (i.e.: `_ast.Tuple`) to a `Tree_Evaluate_Tuple` or a
#       `Tree_Store_Tuple`.
#
assert Native_AbstractSyntaxTree_Tuple_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Tuple_Expression._fields     == (('elts', 'ctx'))


def convert_tuple_expression(self):
    assert fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(self.ctx)

    create_tuple = convert__load_OR_store_context__TO__create_tuple_function(self.ctx)

    return convert_many_expression(self, create_tuple)
