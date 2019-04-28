#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V3 - Implementation of Tree Name, Version 3
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2 & Version 3
#
#       Version 2:
#
#           Tree_Name had a `.context` member which four possible values:
#
#               tree_delete_context
#               tree_load_context
#               tree_parameter_context
#               tree_store_context
#
#       Version 3:
#
#           Instead of a single class with a `.context` member, four classes exist instead:
#
#               Tree_Delete_Name            -   Replacement for the `tree_delete_context` value.
#               Tree_Evaluate_Name          -   Replacement for the `tree_load_context` value.
#               Tree_Normal_Parameter       -   Replacement for the `tree_parameter_context` value.
#               Tree_Store_Name             -   Replacement for the `tree_store_context` value.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Parser.Symbol                 import  conjure_symbol


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Parser.Symbol             import  fact_is_symbol



#
#   Tree: Name - Base of class that with a name.
#
class Tree_Name(object):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'symbol',                       #   Symbol
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column, symbol):
        self.line_number = line_number
        self.column      = column

        self.symbol  = symbol


    #
    #   Public
    #
    is_tree_token_name = True


    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {}>',
                       self.__class__.__name__, self.line_number, self.column, self.symbol, self.context)


#
#   Tree: Delete Name
#
class Tree_Delete_Name(Tree_Name):
    #
    #   Implements Tree_Delete_Target
    #
    __slots__ = (())


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        is_tree_delete_target = True


    def dump_delete_target_tokens(self, f):
        f.arrange('<delete-name @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Delete_Name(line_number, column, symbol):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_symbol(symbol)

    return Tree_Delete_Name(line_number, column, symbol)


#
#   Tree: Evaluate Name
#
class Tree_Evaluate_Name(Tree_Name):
    #
    #   Implements Tree_Expression
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
        #       Omit the keyword "evaluate-name" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Evaluate_Name(line_number, column, symbol):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_symbol(symbol)

    return Tree_Evaluate_Name(line_number, column, symbol)


#
#   Tree: Normal Parameter
#
class Tree_Normal_Parameter(Tree_Name):
    #
    #   Implements Tree_Parameter
    #
    __slots__ = (())


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
        is_tree_keyword_parameter = False
        is_tree_parameters_all    = False
        is_tree_parameter         = True
        is_tree_normal_parameter  = True


    def dump_parameter_tokens(self, f):
        f.arrange('<normal-parameter @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Normal_Parameter(line_number, column, symbol):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_symbol(symbol)

    return Tree_Normal_Parameter(line_number, column, symbol)


#
#   Tree: Store Name
#
class Tree_Store_Name(Tree_Name):
    #
    #   Implements Tree_Store_Target
    #
    __slots__ = (())


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        is_tree_store_target = True


    def dump_store_target_tokens(self, f):
        f.arrange('<store-name @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Store_Name(line_number, column, symbol):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_symbol(symbol)

    return Tree_Store_Name(line_number, column, symbol)
