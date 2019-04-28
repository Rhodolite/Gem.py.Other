#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Subscript_V1 - Implementation of `Tree_Subscript`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_store_context
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Index                import  fact_is_tree_index_clause


#
#   Tree: Subscript Expression
#
class Tree_Subscript_Expression(object):
    #
    #   implements Tree_Delete_Target,
    #              Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
        'index',                        #   Tree_Index_Clause
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, index, context):
        self.line_number = line_number
        self.column      = column

        self.value   = value
        self.index   = index
        self.context = context


    def _dump_tree_subscript_expression_tokens(self, f):
        first = True

        f.arrange('<subscript @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.write(' [')
        self.index.dump_index_clause_tokens(f)
        f.write(']; ')
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        @property
        def is_tree_delete_target(self):
            return self.context.is_tree_delete_context


    if __debug__:
        def dump_delete_target_tokens(self, f):
            assert fact_is_tree_delete_context(self.context)

            self._dump_tree_subscript_expression_tokens(f)
    else:
        dump_delete_target_tokens = _dump_tree_subscript_expression_tokens


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    if __debug__:
        def dump_evaluate_tokens(self, f):
            assert fact_is_tree_load_context(self.context)

            self._dump_tree_subscript_expression_tokens(f)
    else:
        dump_evaluate_tokens = _dump_tree_subscript_expression_tokens


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context

    if __debug__:
        def dump_store_target_tokens(self, f):
            assert fact_is_tree_store_context(self.context)

            self._dump_tree_subscript_expression_tokens(f)
    else:
        dump_store_target_tokens = _dump_tree_subscript_expression_tokens


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Subscript_Expression @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.value, self.index, self.context)


@creator
def create_Tree_Subscript_Expression(line_number, column, value, index, context):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression  (value)
    assert fact_is_tree_index_clause(index)
    assert fact_is_tree_context     (context)

    return Tree_Subscript_Expression(line_number, column, value, index, context)
