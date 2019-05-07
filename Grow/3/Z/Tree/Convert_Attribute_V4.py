#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Attribute_V4 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           Pass in a context to `z.create_Tree_Attribute`
#
#       Version 4:
#
#           Do not pass in a context to create `z.create_Tree_Attribute`, but instead create one of the following three
#           classes:
#
#               Tree_Delete_Attribute
#               Tree_Evaluate_Attribute
#               Tree_Store_Attribute
#


from    Z.Parser.Symbol                     import  conjure_parser_symbol


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression


#
#   convert__delete_load_OR_store_context__TO__create_attribute_function(z, v)
#
#       Convert a "delete", "load", or "store" context to a create attribute function.
#
def convert__delete_load_OR_store_context__TO__create_attribute_function(z, v):
    assert fact_is_convert_zone(z)

    return z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute_function[type(v)]


#
#   convert_attribute_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Attribute_Expression` (i.e.: `_ast.Attribute`) to one of the following
#       three classes:
#
#           Tree_Delete_Attribute
#           Tree_Evaluate_Attribute
#           Tree_Store_Attribute
#
#       The context (`.ctx` member) must be an instance of one of the following types:
#
#           Native_AbstractSyntaxTree_Delete_Context
#           Native_AbstractSyntaxTree_Load_Context
#           Native_AbstractSyntaxTree_Store_Context
#
assert Native_AbstractSyntaxTree_Attribute_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Attribute_Expression._fields     == (('value', 'attr', 'ctx'))


def convert_attribute_expression(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (v.value)
    assert fact_is_full_native_string                                              (v.attr)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    create_attribute__function = convert__delete_load_OR_store_context__TO__create_attribute_function(z, v.ctx)

    return create_attribute__function(
               v.lineno,
               v.col_offset,

               z.convert_expression (z, v.value),
               conjure_parser_symbol(v.attr),
          )
