#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Subscript_V4
#
#       Convert Python Abstract Syntax Tree Subscript Expression to a `Tree_Subscript_Expression`, Version 4.
#


#
#   Difference between Version 2, Version 3 & Version 4.
#
#       Version 2:
#
#           Pass in a context to `create_Tree_Subscript_Expression`
#
#       Version 3:
#
#           Does *NOT* exist.
#
#       Version 4:
#
#           Do not pass in a context to create `Tree_Subscript_Expression`, but instead create one of the following
#           three classes:
#
#               Tree_Delete_Subscript
#               Tree_Evaluate_Subscript
#               Tree_Store_Subscript
#


from    Z.Tree.Convert_Zone                 import  convert_zone
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Subscript_V4                 import  create_Tree_Delete_Subscript
from    Z.Tree.Subscript_V4                 import  create_Tree_Evaluate_Subscript
from    Z.Tree.Subscript_V4                 import  create_Tree_Store_Subscript


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__INDEX



#
#   convert__delete_load_OR_store_context__TO__create_subscript_function
#
#       Convert a "delete", "load", or "store" context to a create subscript function.
#
map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript_function = {
        Native_AbstractSyntaxTree_Delete_Context : create_Tree_Delete_Subscript,
        Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Subscript,
        Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Subscript,
    }


if __debug__:
    def assert_no_context_fields(mapping):
        for k in mapping:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields(
            map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript_function,
        )


def convert__delete_load_OR_store_context__TO__create_subscript_function(v):
    return map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript_function[type(v)]


#
#   convert_subscript_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Subscript_Expression` (i.e.: `_ast.Subscript`) to a
#       `Tree_Subscript_Expression`.
#
assert Native_AbstractSyntaxTree_Subscript_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Subscript_Expression._fields     == (('value', 'slice', 'ctx'))


def convert_subscript_expression(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (v.value)
    assert fact_is__ANY__native__abstract_syntax_tree__INDEX                       (v.slice)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    create_subscript = convert__delete_load_OR_store_context__TO__create_subscript_function(v.ctx)

    z = convert_zone

    return create_subscript(
               v.lineno,
               v.col_offset,

               z.convert_expression  (z, v.value),
               z.convert_index_clause(z, v.slice),
           )
