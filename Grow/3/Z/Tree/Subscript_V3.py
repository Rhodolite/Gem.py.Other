#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Subscript_V3 - Implementation of `Tree_Subscript`, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 3
#
#       Version 1:
#
#           `Tree_Subscript_Expression` had a `.context` member which three possible values:
#
#               tree_delete_context
#               tree_load_context
#               tree_store_context
#
#       Version 2:
#
#           Does *NOT* exist.
#
#       Version 3:
#
#           Instead of a single class with a `.context` member, three classes exist instead:
#
#               Tree_Delete_Subscript
#               Tree_Evaluate_Subscript
#               Tree_Store_Subscript
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_store_context
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Index                import  fact_is_tree_index_clause


#
#   Tree: Subscript Expression
#
#       Base of `Tree_Delete_Subscript`, `Tree_Evaluate_Subscript`, and `Tree_Store_Subscript`.
#
class Tree_Subscript_Expression(object):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
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
class Tree_Delete_Subscript(Tree_Subscript_Expression):
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
        f.arrange('<delete-subscript @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Delete_Subscript(line_number, column, value, index):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression  (value)
    assert fact_is_tree_index_clause(index)

    return Tree_Delete_Subscript(line_number, column, value, index)


#
#   Tree: Evaluate Subscript
#
class Tree_Evaluate_Subscript(Tree_Subscript_Expression):
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
        #       Omit the keyword "evaluate-subscript" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Evaluate_Subscript(line_number, column, value, index):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression  (value)
    assert fact_is_tree_index_clause(index)

    return Tree_Evaluate_Subscript(line_number, column, value, index)


#
#   Tree: Store Subscript
#
class Tree_Store_Subscript(Tree_Subscript_Expression):
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
        f.arrange('<store-subscript @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']>')


@creator
def create_Tree_Store_Subscript(line_number, column, value, index):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression  (value)
    assert fact_is_tree_index_clause(index)

    return Tree_Store_Subscript(line_number, column, value, index)
