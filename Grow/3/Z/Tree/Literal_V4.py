#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Literal_V4 - Implementation of `Tree_String_Literal`, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           `Tree_{Number,String}_Literal` do not implement `Tree_Value_Expression_0`.
#
#       Version 4:
#
#           `Tree_{Number,String}_Literal`        implement `Tree_Value_Expression_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Number              import  fact_is_number
    from    Capital.String              import  fact_is_string


#
#   Tree: Number Literal
#
class Tree_Number_Literal(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'n',                            #   Number
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, n):
        self.line_number = line_number
        self.column      = column

        self.n = n


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        f.arrange('<number @{}:{} {!r}>', self.line_number, self.column, self.n)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Number_Literal @{}:{} {!r}>', self.line_number, self.column, self.n)


@creator
def create_Tree_Number_Literal(line_number, column, n):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_number(n)

    return Tree_Number_Literal(line_number, column, n)


#
#   Tree: String Literal
#
class Tree_String_Literal(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        's',                            #   String
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
        return arrange('<Tree_String_Literal @{}:{} {!r}>', self.line_number, self.column, self.s)


@creator
def create_Tree_String_Literal(line_number, column, s):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_string(s)

    return Tree_String_Literal(line_number, column, s)
