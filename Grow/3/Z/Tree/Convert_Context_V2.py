#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Context_V2 - Convert Python Abstract Syntax Tree Contexts to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       See "Z/Tree/Context.py" for an explanation of "contexts".
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


from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Parameter_Context


if __debug__:
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__delete_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context


#
#   convert_delete_context(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Context` to the singleton `tree_delete_context`.
#
assert Native_AbstractSyntaxTree_Delete_Context._attributes == (())
assert Native_AbstractSyntaxTree_Delete_Context._fields     == (())

def convert_delete_context(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native__abstract_syntax_tree__delete_context(v)

    return z.tree_delete_context


#
#   convert_delete_load_OR_store_context(z, v)
#
#       Convert a "delete", "load", or "store" context to a `Tree_Context` enumerator.
#
def convert_delete_load_OR_store_context(z, v):
    assert fact_is_convert_zone(z)

    return z.map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(v)]


#
#   convert_load_OR_store_context(z, v)
#
#       Convert a "load" or "store" context to a `Tree_Context` enumerator.
#
def convert_load_OR_store_context(z, v):
    assert fact_is_convert_zone(z)

    return z.map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(v)]


#
#   convert_parameter_context(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Parameter_Context` to the singleton `tree_parameter_context`.
#
assert Native_AbstractSyntaxTree_Parameter_Context._attributes == (())
assert Native_AbstractSyntaxTree_Parameter_Context._fields     == (())

def convert_parameter_context(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native__abstract_syntax_tree__parameter_context(v)

    return z.tree_parameter_context
