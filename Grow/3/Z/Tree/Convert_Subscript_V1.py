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
from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Index                import  convert_index_clause
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Subscript_V1                 import  create_Tree_Subscript_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__INDEX



#
#   convert_subscript_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Subscript_Expression` (i.e.: `_ast.Subscript`) to a
#       `Tree_Subscript_Expression`.
#
assert Native_AbstractSyntaxTree_Subscript_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Subscript_Expression._fields     == (('value', 'slice', 'ctx'))


def convert_subscript_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (self.value)
    assert fact_is__ANY__native__abstract_syntax_tree__INDEX                       (self.slice)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    return create_Tree_Subscript_Expression(
               self.lineno,
               self.col_offset,
               
               convert_expression                  (self.value),
               convert_index_clause                (self.slice),
               convert_delete_load_OR_store_context(self.ctx),
           )
