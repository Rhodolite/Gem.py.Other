#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Raise_Statement_V8 - Implementation of `Tree_Raise_Statement`, Version 8.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 7 and Version 8.
#
#       Version 7:
#
#           `.{type,instance,traceback}` is of type `None | Tree_Value_Expression`.
#
#       Version 8:
#
#           `.{type,instance,traceback}` is of type `Tree_Value_Expression_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression_0


#
#   Tree: Raise Statement
#
class Tree_Raise_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'type',                         #   Tree_Value_Expression_0
        'instance',                     #   Tree_Value_Expression_0
        'traceback',                    #   Tree_Value_Expression_0
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

        if self.type.has_tree_value_expression:
            f.space()
            self.type.dump_value_expression_tokens(f)

            if self.instance.has_tree_value_expression:
                f.write(', ')
                self.instance.dump_value_expression_tokens(f)

                if self.traceback.has_tree_value_expression:
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

    assert fact_is_tree_value_expression_0(type)
    assert fact_is_tree_value_expression_0(instance)
    assert fact_is_tree_value_expression_0(traceback)

    if not type.has_tree_value_expression:
        assert not instance.has_tree_value_expression

    if not instance.has_tree_value_expression:
        assert not traceback.has_tree_value_expression

    return Tree_Raise_Statement(line_number, column, type, instance, traceback)
