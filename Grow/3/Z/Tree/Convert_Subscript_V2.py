#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Subscript_V2
#
#       Convert Python Abstract Syntax Tree Subscript Expression to a `Tree_Subscript_Expression`, Version 2.
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


if __debug__:
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__INDEX
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression


#
#   convert_subscript_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Subscript_Expression` (i.e.: `_ast.Subscript`) to a
#       `Tree_Subscript_Expression`.
#
assert Native_AbstractSyntaxTree_Subscript_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Subscript_Expression._fields     == (('value', 'slice', 'ctx'))


def convert_subscript_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION            (v.value)
    assert fact_is__ANY__native__abstract_syntax_tree__INDEX                       (v.slice)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    return z.create_Tree_Subscript_Expression(
               v.lineno,
               v.col_offset,

               z.convert_expression                  (z, v.value),
               z.convert_index_clause                (z, v.slice),
               z.convert_delete_load_OR_store_context(z, v.ctx),
           )
