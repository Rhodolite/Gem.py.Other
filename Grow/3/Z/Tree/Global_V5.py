#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Global_V5 - Implementation of tree `global` statement, Version 5.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Versions 1..5.
#
#       Version 1:
#
#           The `Tree_Global_Statement.names` member is a `Full_Native_List of Full_Native_String`.
#
#       Version 2..5:
#
#           Does not exist.
#
#       Version 5:
#
#           The `Tree_Global_Statement.names` member is renamed to `.symbols` and it's type changes to a
#           `Full_Native_List of Parser_Symbol`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer


#
#   Tree: Global Statement
#
class Tree_Global_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Keen_Native_Integer

        'symbols',                      #   Full_Native_List of Parser_Symbol
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
        first = True

        f.arrange('<global @{}:{}', self.line_number, self.column)

        for v in self.symbols:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            v.dump_symbol_token(f)

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

    assert fact_is_full_native_list(symbols)

    return Tree_Global_Statement(line_number, column, symbols)
