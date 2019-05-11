#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V4 - Implementation of Tree Name, Version 4
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 3 & Version 4.
#
#       Version 3:
#
#           `Tree_Name` had a `.context` member which four possible values:
#
#               tree_delete_context
#
#               tree_load_context
#
#               tree_parameter_context
#
#               tree_store_context
#
#       Version 4:
#
#           Instead of a single class with a `.context` member, four classes exist instead:
#
#               A)  Tree_Delete_Name            -   Replacement for the `tree_delete_context` value.
#
#               B)  Tree_Evaluate_Name          -   Replacement for the `tree_load_context` value.
#
#               C)  Tree_Normal_Parameter       -   Replacement for the `tree_parameter_context` value.
#
#                       *NOT* Implemented in this file, but implemented in `Capital.Tree.Parameter_V4`.
#
#               D)  Tree_Store_Name             -   Replacement for the `tree_store_context` value.
#
#           Of these four classes, `Tree_{Delete,Evaluate,Store}_Name` are implemented in this file.
#
#
#   SEE ALSO
#
#       See "Z.Tree.Parameter_V4.py" for `Tree_Normal_Parameter`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target


if __debug__:
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
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
