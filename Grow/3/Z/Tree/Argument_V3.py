#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Argument_V3 - Implementation of class that implement `Tree_Argument`, Version 3.
#


#
#   Differences between Version 1, Version 2, and Version 3.
#
#       Version 1:
#
#           `Tree_Keyword_Argument.symbol` is a `Full_Native_String`.
#
#       Version 2:
#
#           Does not exist.
#
#       Version 3:
#
#           `Tree_Keyword_Argument.symbol` is a `Parser_Symbol`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Argument                 import  TRAIT_Tree_Argument


if __debug__:
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Keyword Argument - A keyword argment in a function call.
#
class Tree_Keyword_Argument(
        TRAIT_Tree_Argument,
):
    __slots__ = ((
        'symbol',                       #   Parser_Symbol
        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value  = value


    #
    #   Interface Tree_Argument
    #
    def dump_argument_tokens(self, f):
        f.arrange('<keyword-argument ')
        self.symbol.dump_symbol_token(f)
        f.write(' = ')
        self.value.dump_value_expression_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Keyword_Argument {!r} = {!r}>', self.symbol, self.value)


@creator
def create_Tree_Keyword_Argument(symbol, value):
    assert fact_is_parser_symbol        (symbol)
    assert fact_is_tree_value_expression(value)

    return Tree_Keyword_Argument(symbol, value)
