#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Yield_Expression_V4 - Implementation of `Tree_Yield_Expression`, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 1..4
#
#       Version 1:
#
#           `Tree_Yield_Expression` does not implement or use `Tree_Value_Expression_0`.
#
#       Versions 2..3:
#
#           Do not exist.
#
#       Version 4:
#
#           `Tree_Yield_Expression` both    implements & uses `Tree_Value_Expression_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression_0


#
#   Tree: Yield Expression
#
class Tree_Yield_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression_0
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value):
        self.line_number = line_number
        self.column      = column

        self.value = value


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        f.arrange('<yield @{}:{}', self.line_number, self.column)

        if self.value.has_tree_value_expression:
            f.space()
            self.value.dump_value_expression_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Yield_Expression @{}:{} {!r}>',
                       self.line_number, self.column, self.value)


@creator
def create_Tree_Yield_Expression(line_number, column, value):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression_0(value)

    return Tree_Yield_Expression(line_number, column, value)
