#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V5 - Implementation of Tree Name, Version 5
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 4 & Version 5.
#
#       Version 4:
#
#           1)  `Tree_Evaluate_Name` does not implement `Tree_Value_Expression_0`.
#
#           2)  `Tree_Store_Name`    does not implement `Tree_Store_Target_0`.
#
#       Version 5:
#
#           1)  `Tree_Evaluate_Name`         implements `Tree_Value_Expression_0`.
#
#           2)  `Tree_Store_Name`            implements `Tree_Store_Target_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression_0
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol



#
#   Tree: Name Branch - Base of class of `Tree_{Delete,Evaluate,Store}_Name` (and also of `Tree_Parameter_Name`).
#
class Tree_Name_Branch(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbol',                       #   Parser_Symbol
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column, symbol):
        self.line_number = line_number
        self.column      = column

        self.symbol = symbol


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {}>', self.__class__.__name__, self.line_number, self.column, self.symbol)


#
#   Tree: Delete Name
#
class Tree_Delete_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


    #
    #   Interface Tree_Delete_Target
    #
    def dump_delete_target_tokens(self, f):
        f.arrange('<delete-name @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Delete_Name(line_number, column, symbol):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Delete_Name(line_number, column, symbol)


#
#   Tree: Evaluate Name
#
class Tree_Evaluate_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        #
        #   NOTE:
        #       Omit the keyword "evaluate-name" on purpose to make the output shorter.
        #
        f.arrange('<@{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Evaluate_Name(line_number, column, symbol):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Evaluate_Name(line_number, column, symbol)


#
#   Tree: Store Name
#
class Tree_Store_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Store_Target
    #
    def dump_store_target_tokens(self, f):
        f.arrange('<store-name @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Store_Name(line_number, column, symbol):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Store_Name(line_number, column, symbol)
