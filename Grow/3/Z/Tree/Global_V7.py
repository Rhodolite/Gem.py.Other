#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Global_V7 - Implementation of tree `global` statement, Version 7.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 6 & 7.
#
#       Version 6:
#
#           Tree Statements implement `Tree_Statement`.
#
#       Version 7:
#
#           Tree Statements implement `Tree_Statement`; and ...
#
#           ... in addition also implement `Tree_Suite`, and `Tree_Suite_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Parser.Symbol_Tuple       import  fact_is_parser_symbol_tuple


#
#   Tree: Global Statement
#
class Tree_Global_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbols',                      #   Parser_Symbol_Tuple
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, symbols):
        self.line_number = line_number
        self.column      = column

        self.symbols = symbols


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<global @{}:{} ', self.line_number, self.column)
        self.symbols.dump_symbol_tuple_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Global_Statement @{}:{} {!r}>', self.line_number, self.column, self.symbols)


@creator
def create_Tree_Global_Statement(line_number, column, symbols):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol_tuple(symbols)

    return Tree_Global_Statement(line_number, column, symbols)
