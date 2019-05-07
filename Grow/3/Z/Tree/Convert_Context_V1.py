#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Context_V1 - Convert Python Abstract Syntax Tree Contexts to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       See "Z/Tree/Context.py" for an explanation of "contexts".
#


from    Z.Tree.Context_V1                       import  tree_delete_context
from    Z.Tree.Context_V1                       import  tree_load_context
from    Z.Tree.Context_V1                       import  tree_parameter_context
from    Z.Tree.Context_V1                       import  tree_store_context


if __debug__:
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__delete_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Parameter_Context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context


#
#   convert_delete_context(v)
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Context` to the singleton `tree_delete_context`.
#
assert Native_AbstractSyntaxTree_Delete_Context._attributes == (())
assert Native_AbstractSyntaxTree_Delete_Context._fields     == (())

def convert_delete_context(v):
    assert fact_is__native__abstract_syntax_tree__delete_context(v)

    return tree_delete_context


#
#   convert_delete_load_OR_store_context(v)
#
#       Convert a "delete", "load", or "store" context to a `Tree_Context` enumerator.
#
map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
        Native_AbstractSyntaxTree_Delete_Context : tree_delete_context,
        Native_AbstractSyntaxTree_Load_Context   : tree_load_context,
        Native_AbstractSyntaxTree_Store_Context  : tree_store_context,
    }


if __debug__:
    def assert_no_context_fields(mapping):
        for k in mapping:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields(map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context)


def convert_delete_load_OR_store_context(v):
    return map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(v)]


#
#   convert_load_OR_store_context(v)
#
#       Convert a "load" or "store" context to a `Tree_Context` enumerator.
#
map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
        Native_AbstractSyntaxTree_Load_Context  : tree_load_context,
        Native_AbstractSyntaxTree_Store_Context : tree_store_context,
    }


if __debug__:
    assert_no_context_fields(map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context)


def convert_load_OR_store_context(v):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(v)]


#
#   convert_parameter_context(v)
#
#       Convert a `Native_AbstractSyntaxTree_Parameter_Context` to the singleton `tree_parameter_context`.
#
assert Native_AbstractSyntaxTree_Parameter_Context._attributes == (())
assert Native_AbstractSyntaxTree_Parameter_Context._fields     == (())

def convert_parameter_context(v):
    assert fact_is__native__abstract_syntax_tree__parameter_context(v)

    return tree_parameter_context
