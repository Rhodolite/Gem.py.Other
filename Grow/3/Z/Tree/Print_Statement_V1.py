#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Print_Statement_V1 - Implementation of `Tree_Print_Statement`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_list
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression


#
#   Tree: Print Statement
#
class Tree_Print_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'destination',                  #   None | Tree_Value_Expression
        'values',                       #   Native_List of Tree_Value_Expression
        'newline',                      #   Native_Boolean
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, destination, values, newline):
        self.line_number = line_number
        self.column      = column

        self.destination = destination
        self.values      = values
        self.newline     = newline


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        first = True

        f.arrange('<print @{}:{}', self.line_number, self.column)

        if self.destination is not None:
            first = False

            f.write(' {>>} ')
            self.destination.dump_value_expression_tokens(f)

        for v in self.values:
            if first:
                first = True
            else:
                f.write(',')

            f.space()
            v.dump_value_expression_tokens(f)

        if not self.newline:
            f.write(',')

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Print_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.destination, self.values, self.newline)


@creator
def create_Tree_Print_Statement(line_number, column, destination, values, newline):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is__native_none__OR__tree_value_expression(destination)
    assert fact_is_native_list                            (values)
    assert fact_is_native_boolean                         (newline)

    return Tree_Print_Statement(line_number, column, destination, values, newline)
