#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Attribute_V5 - Implementation of Tree Name, Version 5
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 4 & Version 5.
#
#       Version 3:
#
#           `Tree_Store_Attribute` does not implement `Tree_Store_Target_0`.
#
#       Version 4:
#
#           Tree_Store_Attribute` implements `Tree_Store_Target_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Attribute - Base of classes with delete, evaluate, or store an attribute.
#
#   Example:
#
#       In the following statement:
#
#           a.b = c.d
#           del e.g
#
#       The left  hand side of the first statement: `a.b` will be a `Tree_Store_Attribute`.
#
#       The right hand side of the first statement: `c.d` will be a `Tree_Evauluate_Attribute`.
#
#       The second statement after the `del` keyword: `e.g` will be a `Tree_Delete_Attribute`.
#
class Tree_Attribute(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
        'attribute',                    #   Parser_Symbol
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, attribute):
        self.line_number = line_number
        self.column      = column

        self.value     = value
        self.attribute = attribute

    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r}.{}>',
                       self.__class__.__name__, self.line_number, self.column, self.value, self.attribute)


#
#   Tree: Delete Attribute
#
class Tree_Delete_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


    #
    #   Interface Tree_Delete_Target
    #
    def dump_delete_target_tokens(self, f):
        f.arrange('<delete-attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Delete_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_parser_symbol        (attribute)

    return Tree_Delete_Attribute(line_number, column, value, attribute)


#
#   Tree: Evaluate Attribute
#
class Tree_Evaluate_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Value_Expression,
):
    __slots__ = (())


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        #
        #   NOTE:
        #       Omit the keyword "evaluate-attribute" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Evaluate_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_parser_symbol        (attribute)

    return Tree_Evaluate_Attribute(line_number, column, value, attribute)


#
#   Tree: Store Attribute
#
class Tree_Store_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Store_Target
    #
    def dump_store_target_tokens(self, f):
        f.arrange('<store-attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Store_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_parser_symbol        (attribute)

    return Tree_Store_Attribute(line_number, column, value, attribute)