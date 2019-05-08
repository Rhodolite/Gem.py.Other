#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Global_V6 - Implementation of tree `global` statement, Version 6.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Versions 1..6.
#
#       Version 1:
#
#           Tree Statements implement `Tree_Statement`.
#
#       Version 2..5:
#
#           Does not exist.
#
#       Version 6:
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
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Tree: Global Statement
#
class Tree_Global_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'names',                        #   FullNativeList of Full_Native_String
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, names):
        self.line_number = line_number
        self.column      = column

        self.names = names


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        first = True

        f.arrange('<global @{}:{}', self.line_number, self.column)

        for s in self.names:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            f.write(s)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Global_Statement @{}:{} {!r}>', self.line_number, self.column, self.names)


@creator
def create_Tree_Global_Statement(line_number, column, names):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(names)

    return Tree_Global_Statement(line_number, column, names)
