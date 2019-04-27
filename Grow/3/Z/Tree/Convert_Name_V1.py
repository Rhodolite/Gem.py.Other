#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Name_V1 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Context              import  convert_parameter_context
from    Z.Tree.Name_V1                      import  create_Tree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context


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
#       The context (`.ctx` member) MAY NOT be an instance of `Native_AbstractSyntaxTree_Parameter_Context`.
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
#   convert_name_parameter(self)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to `Tree_Name`
#
#       The context (`.ctx` member) MUST BE a `Native_AbstractSyntaxTree_Param`.
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

    return create_Tree_Name(
               self.lineno,
               self.col_offset,

               self.id,
               convert_parameter_context(self.ctx),
           )
