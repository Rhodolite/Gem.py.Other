#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Name_V4 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 3 & Version 4.
#
#       Version 3:
#
#           Pass in a context to `z.create_Tree_Name`
#
#       Version 4:
#
#           Do not pass in a context to create a `Tree_Name`, but instead create one of the following four classes:
#
#               A)  Tree_Delete_Name            -   Implemented in this file.
#
#               B)  Tree_Evaluate_Name          -   Implemented in this file.
#
#               C)  Tree_Normal_Parameter       -   Implemented in "Z.Tree.Normal_Paramter_V4.py".
#
#               D)  Tree_Store_Name             -   Implemented in this file.
#
#


if __debug__:
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name


#
#   convert__delete_load_OR_store_context__TO__create_name__function(z, v)
#
#       Convert a "delete", "load", or "store" context to a create name function.
#
def convert__delete_load_OR_store_context__TO__create_name__function(z, v):
    return z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function[type(v)]


#
#   convert_name_expression(z, v)
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
#
#           Native_AbstractSyntaxTree_Load_Context
#
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

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_string                                              (v.id)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    create_name__function = convert__delete_load_OR_store_context__TO__create_name__function(z, v.ctx)

    return create_name__function(
               v.lineno,
               v.col_offset,

               z.conjure_parser_symbol(z, v.id),
           )
