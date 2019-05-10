#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Literal_V3 - Implementation of `Tree_String`, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#


#
#   Difference between Version 1 & Version 4.
#
#       Version 3:
#
#           `Tree_String.s` is a `Some_Native_String`.
#
#       Version 2:
#
#           `Tree_String.s` is a `Some_String`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression


if __debug__:
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer
    from    Capital.String              import  fact_is_some_string


#
#   Tree: String
#
class Tree_String(
        TRAIT_Tree_Value_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Substantial_Native_Integer

        's',                            #   Some_String
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, s):
        self.line_number = line_number
        self.column      = column

        self.s = s


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        f.arrange('<string @{}:{} {!r}>', self.line_number, self.column, self.s)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_String @{}:{} {!r}>', self.line_number, self.column, self.s)


@creator
def create_Tree_String(line_number, column, s):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_some_string(s)

    return Tree_String(line_number, column, s)
