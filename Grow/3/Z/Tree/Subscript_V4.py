#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Subscript_V4 - Implementation of `Tree_Subscript`, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1, Version 2, Version 3, and Version 4.
#
#       Version 1:
#
#           `Tree_Subscript_Expression` had a `.context` member which three possible values:
#
#               tree_delete_context
#               tree_load_context
#               tree_store_context
#
#       Version 2 & 3:
#
#           Does *NOT* exist.
#
#       Version 4:
#
#           Instead of a single class with a `.context` member, three classes exist instead:
#
#               Tree_Delete_Subscript
#               Tree_Evaluate_Subscript
#               Tree_Store_Subscript
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target


if __debug__:
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Index                import  fact_is_tree_index_clause


#
#   Tree: Subscript Expression - Base of `Tree_{Delete,Evaluate,Store}_Subscript`.
#
class Tree_Subscript_Expression(object):
    __slots__ = ((
        'line_number',                  #   Native_Positive_Integer
        'column',                       #   Native_Substantial_Integer

        'value',                        #   Tree_Value_Expression
        'index',                        #   Tree_Index_Clause
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, index):
        self.line_number = line_number
        self.column      = column

        self.value = value
        self.index = index


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.value, self.index)


#
#   Tree: Delete Subscript
#
class Tree_Delete_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


    #
    #   Interface Tree_Delete_Target
    #
    def dump_delete_target_tokens(self, f):
        f.arrange('<delete-subscript @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Delete_Subscript(line_number, column, value, index):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_tree_index_clause    (index)

    return Tree_Delete_Subscript(line_number, column, value, index)


#
#   Tree: Evaluate Subscript
#
class Tree_Evaluate_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Value_Expression,
):
    __slots__ = (())


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        #
        #   NOTE:
        #       Omit the keyword "evaluate-subscript" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Evaluate_Subscript(line_number, column, value, index):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_tree_index_clause    (index)

    return Tree_Evaluate_Subscript(line_number, column, value, index)


#
#   Tree: Store Subscript
#
class Tree_Store_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Store_Target,
):
    __slots__ = (())


    #
    #   Interface Tree_Store_Target
    #
    def dump_store_target_tokens(self, f):
        f.arrange('<store-subscript @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Store_Subscript(line_number, column, value, index):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_tree_index_clause    (index)

    return Tree_Store_Subscript(line_number, column, value, index)
