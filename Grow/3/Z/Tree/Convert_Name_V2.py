#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Name_V2 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 2.
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


from    Z.Tree.Name_V1                      import  create_Tree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context


#
#   convert_name_expression(z, v)
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
#       To handle a context which is an instance of `Native_AbstractSyntaxTree_Parameter_Context`, call
#       `convert_name_parameter` instead.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string                                              (v.id)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    return create_Tree_Name(
               v.lineno,
               v.col_offset,

               v.id,
               z.convert_delete_load_OR_store_context(z, v.ctx),
           )


#
#   convert_name_parameter(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to `Tree_Name`
#
#       The context (`.ctx` member) MUST BE a `Native_AbstractSyntaxTree_Parameter_Context`.
#
#       To handle other contexts, please see `convert_name_expression`.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string                              (v.id)
    assert fact_is__native__abstract_syntax_tree__parameter_context(v.ctx)

    return create_Tree_Name(
               v.lineno,
               v.col_offset,

               v.id,
               z.convert_parameter_context(z, v.ctx),
           )
