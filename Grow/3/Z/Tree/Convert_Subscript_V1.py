#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Subscript_V1
#
#       Convert Python Abstract Syntax Tree Subscript Expression to a `Tree_Subscript_Expression`, Version 1.
#


from    Capital.Core                        import  FATAL
from    Capital.Core                        import  trace
from    Z.Tree.Convert_Context_V1           import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Expression_V1        import  convert_expression
from    Z.Tree.Convert_Index_V1             import  convert_index_clause
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Subscript_V1                 import  create_Tree_Subscript_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__INDEX



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

    return create_Tree_Subscript_Expression(
               v.lineno,
               v.col_offset,

               convert_expression                  (v.value),
               convert_index_clause                (v.slice),
               convert_delete_load_OR_store_context(v.ctx),
           )
