#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Raise_Statement_V1 - Implementation of `Tree_Raise_Statement`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression


#
#   Tree: Raise Statement
#
class Tree_Raise_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'type',                         #   None | Tree_Value_Expression
        'instance',                     #   None | Tree_Value_Expression
        'traceback',                    #   None | Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, type, instance, traceback):
        self.line_number = line_number
        self.column      = column

        self.type      = type
        self.instance  = instance
        self.traceback = traceback


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<raise @{}:{}', self.line_number, self.column)

        if self.type is None:
            assert self.instance is self.traceback is None
        else:
            f.space()
            self.type.dump_value_expression_tokens(f)

            if self.instance is None:
                assert self.traceback is None
            else:
                f.write(', ')
                self.instance.dump_value_expression_tokens(f)

                if self.traceback is not None:
                    f.write(', ')
                    self.traceback.dump_value_expression_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Raise_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.type, self.instance, self.traceback)


@creator
def create_Tree_Raise_Statement(line_number, column, type, instance, traceback):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is__native_none__OR__tree_value_expression(type)
    assert fact_is__native_none__OR__tree_value_expression(instance)
    assert fact_is__native_none__OR__tree_value_expression(traceback)

    if type is None:
        assert fact_is_native_none(instance)

    if instance is None:
        assert fact_is_native_none(traceback)

    return Tree_Raise_Statement(line_number, column, type, instance, traceback)
