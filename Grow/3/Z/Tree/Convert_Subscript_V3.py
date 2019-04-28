#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Subscript_V3
#
#       Convert Python Abstract Syntax Tree Subscript Expression to a `Tree_Subscript_Expression`, Version 3.
#



#
#   Difference between Version 1 & Version 3
#
#       Version 1:
#
#           Pass in a context to `create_Tree_Subscript_Expression`
#
#       Version 2:
#
#           Does *NOT* exist.
#
#       Version 3:
#
#           Do not pass in a context to create `Tree_Subscript_Expression`, but instead create one of the following
#           three classes:
#
#               Tree_Delete_Subscript
#               Tree_Evaluate_Subscript
#               Tree_Store_Subscript
#


from    Z.Tree.Convert_Index                import  convert_index_clause
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Subscript_V3                 import  create_Tree_Delete_Subscript
from    Z.Tree.Subscript_V3                 import  create_Tree_Evaluate_Subscript
from    Z.Tree.Subscript_V3                 import  create_Tree_Store_Subscript


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


def convert__delete_load_OR_store_context__TO__create_subscript_function(self):
    return map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript_function[type(self)]


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

    create_subscript = convert__delete_load_OR_store_context__TO__create_subscript_function(self.ctx)

    return create_subscript(
               self.lineno,
               self.col_offset,

               convert_expression  (self.value),
               convert_index_clause(self.slice),
           )
