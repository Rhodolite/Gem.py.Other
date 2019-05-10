#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Attribute_V3 - Implementation of Tree Attribute, Version 3
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1, Version 2 & Version 3.
#
#       Version 1:
#
#           `Tree_Attribute` has a `.attribute` member that is a `Full_Native_String`.
#
#       Version 2:
#
#           Does not exist.
#
#       Version 3:
#
#           `Tree_Attribute` has a `.attribute` member that is a `Parser_Symbol`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  replace
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target


if __debug__:
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_store_context
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree_Attribute - An attribute access in an expresssion.
#
#   Example:
#
#       In the following statement:
#
#           a.b = c.d
#
#       The left hand side  `a.b` will be an attribute access, and the context will be `store`.
#
#       The right hand side `c.d` will be an attribute access, and the context will be `load`.
#
class Tree_Attribute(
        TRAIT_Tree_Delete_Target,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Value_Expression,
):
    __slots__ = ((
        'line_number',                  #   Native_Positive_Integer
        'column',                       #   Native_Substantial_Integer

        'value',                        #   Tree_Value_Expression
        'attribute',                    #   Parser_Symbol
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, attribute, context):
        self.line_number = line_number
        self.column      = column

        self.value     = value
        self.attribute = attribute
        self.context   = context


    def _dump_tree_attribute_token(self, f):
        f.arrange('<attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.space()
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        @replace
        @property
        def is_tree_delete_target(self):
            return self.context.is_tree_delete_context


    if __debug__:
        def dump_delete_target_tokens(self, f):
            assert fact_is_tree_delete_context(self.context)

            self._dump_tree_attribute_token(f)
    else:
        dump_delete_target_tokens = _dump_tree_attribute_token


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context


    if __debug__:
        def dump_store_target_tokens(self, f):
            assert fact_is_tree_store_context(self.context)

            self._dump_tree_attribute_token(f)
    else:
        dump_store_target_tokens = _dump_tree_attribute_token


    #
    #   Interface Tree_Value_Expression
    #
    if __debug__:
        @replace
        @property
        def is_tree_value_expression(self):
            return self.context.is_tree_load_context


    if __debug__:
        def dump_value_expression_tokens(self, f):
            assert fact_is_tree_load_context(self.context)

            self._dump_tree_attribute_token(f)
    else:
        dump_value_expression_tokens = _dump_tree_attribute_token


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Attribute @{}:{} {!r}.{} {}>',
                       self.line_number, self.column, self.value, self.attribute, self.context)


@creator
def create_Tree_Attribute(line_number, column, value, attribute, context):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_parser_symbol        (attribute)
    assert fact_is_tree_context         (context)

    return Tree_Attribute(line_number, column, value, attribute, context)
