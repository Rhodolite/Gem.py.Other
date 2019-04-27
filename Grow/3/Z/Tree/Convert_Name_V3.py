#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Name_V3 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2 & Version 3
#
#       Version 1:
#
#           Pass in `self.id` as the `id` parameter (third parameter) to `create_Tree_Name`.
#
#       Version 2:
#
#           Pass in a context to `create_Tree_Name`
#
#       Version 3:
#
#           Do not pass in a context to create `Tree_Name`, but instead create one of the following four classes:
#
#               Tree_Delete_Name
#               Tree_Evaluate_Name
#               Tree_Normal_Parameter
#               Tree_Store_Name
#


from    Z.Parser.Symbol                     import  conjure_symbol
from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Context              import  convert_parameter_context
from    Z.Tree.Name_V3                      import  create_Tree_Delete_Name
from    Z.Tree.Name_V3                      import  create_Tree_Evaluate_Name
from    Z.Tree.Name_V3                      import  create_Tree_Normal_Parameter
from    Z.Tree.Name_V3                      import  create_Tree_Store_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context


#
#   convert__delete_load_OR_store_context__TO__create_name_function
#
#       Convert a "delete", "load", or "store" context to a create name function.
#
map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name_function = {
        Native_AbstractSyntaxTree_Delete_Context : create_Tree_Delete_Name,
        Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Name,
        Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Name,
    }


if __debug__:
    def assert_no_context_fields():
        for k in map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name_function:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields()


def convert__delete_load_OR_store_context__TO__create_name_function(self):
    return map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name_function[type(self)]


#
#   convert_name_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to one of the following three classes:
#
#               Tree_Delete_Name
#               Tree_Evaluate_Name
#               Tree_Store_Name
#
#       The context (`.ctx` member) must be an instance of one of the following types:
#
#           Native_AbstractSyntaxTree_Delete_Context
#           Native_AbstractSyntaxTree_Load_Context
#           Native_AbstractSyntaxTree_Store_Context
#
#       The context (`.ctx` member) MAY NOT be an instance of `Native_AbstractSyntaxTree_Parameter_Context`.
#
#       To handle a context which is an instance of `Native_AbstractSyntaxTree_Parameter_Context`, call
#       `convert_name_parameter` instead.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string                                              (self.id)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    create_name = convert__delete_load_OR_store_context__TO__create_name_function(self.ctx)

    return create_name(
               self.lineno,
               self.col_offset,

               conjure_symbol(self.id),
           )


#
#   convert_name_parameter(self)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to `Tree_Normal_Parameter`
#
#       The context (`.ctx` member) MUST BE a `Native_AbstractSyntaxTree_Parameter_Context`.
#
#       To handle other contexts, please see `convert_name_expression`.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_parameter(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string                              (self.id)
    assert fact_is__native__abstract_syntax_tree__parameter_context(self.ctx)

    return create_Tree_Normal_Parameter(
               self.lineno,
               self.col_offset,

               conjure_symbol(self.id),
           )
