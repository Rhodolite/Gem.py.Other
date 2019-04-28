#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Attribute_V3 - Implementation of Tree Name, Version 3
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Version 2:
#
#       Tree_Attribute had a `.context` member which three possible values:
#
#               tree_delete_context
#               tree_load_context
#               tree_store_context
#
#   Version 3:
#
#       Instead of a single class with a `.context` member, three classes exist instead:
#
#               Tree_Delete_Attribute       -   Replacement for the `tree_delete_context` value.
#               Tree_Evaluate_Attribute     -   Replacement for the `tree_load_context` value.
#               Tree_Store_Attribute        -   Replacement for the `tree_store_context` value.
#
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Parser.Symbol                 import  conjure_symbol


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Parser.Symbol             import  fact_is_symbol
    from    Z.Tree.Expression           import  fact_is_tree_expression


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
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
        'attribute',                    #   Symbol
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
class Tree_Delete_Attribute(Tree_Attribute):
    #
    #   implements Tree_Delete_Target
    #
    __slots__ = (())


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        is_tree_delete_target = True


    def dump_delete_target_tokens(self, f):
        f.arrange('<delete-attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Delete_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(value)
    assert fact_is_symbol         (attribute)

    return Tree_Delete_Attribute(line_number, column, value, attribute)


#
#   Tree: Evaluate Attribute
#
class Tree_Evaluate_Attribute(Tree_Attribute):
    #
    #   implements Tree_Expression
    #
    __slots__ = (())


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        #
        #   NOTE:
        #       Omit the keyword "evaluate-attribute" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Evaluate_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(value)
    assert fact_is_symbol         (attribute)

    return Tree_Evaluate_Attribute(line_number, column, value, attribute)


#
#   Tree: Store Attribute
#
class Tree_Store_Attribute(Tree_Attribute):
    #
    #   implements Tree_Store_Target
    #
    __slots__ = (())


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        is_tree_store_target = True


    def dump_store_target_tokens(self, f):
        f.arrange('<store-attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write('.')
        f.write(self.attribute)
        f.greater_than_sign()


@creator
def create_Tree_Store_Attribute(line_number, column, value, attribute):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(value)
    assert fact_is_symbol         (attribute)

    return Tree_Store_Attribute(line_number, column, value, attribute)
