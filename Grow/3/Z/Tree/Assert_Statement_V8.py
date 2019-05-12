#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Assert_Statement_V8 - Implementation of `Tree_Assert_Statement`, Version 8.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 7 and Version 8.
#
#       Version 7:
#
#           `.message` is of type `None | Tree_Value_Expression`.
#
#       Version 8:
#
#           `.message` is of type `Tree_Value_Expression_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Expression           import  fact_is_tree_value_expression_0


#
#   Tree: Assert Statement
#
class Tree_Assert_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'test',                         #   Tree_Value_Expression
        'message',                      #   Tree_Value_Expression_0
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, test, message):
        self.line_number = line_number
        self.column      = column

        self.test    = test
        self.message = message


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<assert @{}:{} ', self.line_number, self.column)
        self.test.dump_value_expression_tokens(f)

        if self.message.has_tree_value_expression:
            f.write(', ')
            self.message.dump_value_expression_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Assert_Statement @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.test, self.message)



@creator
def create_Tree_Assert_Statement(line_number, column, test, message):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression  (test)
    assert fact_is_tree_value_expression_0(message)

    return Tree_Assert_Statement(line_number, column, test, message)
