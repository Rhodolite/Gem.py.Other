#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Assert_Statement_V1 - Implementation of `Tree_Assert_Statement`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Assert Statement
#
class Tree_Assert_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'test',                         #   Tree_Value_Expression
        'message',                      #   None | Tree_Value_Expression
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

        if self.message is not None:
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

    assert fact_is_tree_value_expression                  (test)
    assert fact_is__native_none__OR__tree_value_expression(message)

    return Tree_Assert_Statement(line_number, column, test, message)
