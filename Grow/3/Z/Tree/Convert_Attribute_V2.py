#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Attribute_V2 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           The `attribute` parameter (fourth parameter) to `create_Tree_Attribute` is a `NativeString`.
#
#       Version 2:
#
#           The `attribute` parameter (fourth parameter) to `create_Tree_Attribute` is a `Parser_Symbol`.
#


from    Z.Parser.Symbol                     import  conjure_parser_symbol
from    Z.Tree.Attribute_V2                 import  create_Tree_Attribute
from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT


#
#   convert_attribute_expression(self)
#
#       Convert a `Native_AbstractSyntaxTree_Attribute_Expression` (i.e.: `_ast.Expr`) to a `Tree_Attribute`.
#
assert Native_AbstractSyntaxTree_Attribute_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Attribute_Expression._fields     == (('value', 'attr', 'ctx'))


def convert_attribute_expression(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (self.value)
    assert fact_is_full_native_string                                              (self.attr)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(self.ctx)

    return create_Tree_Attribute(
               self.lineno,
               self.col_offset,

               convert_expression                  (self.value),
               conjure_parser_symbol               (self.attr),
               convert_delete_load_OR_store_context(self.ctx),
          )
