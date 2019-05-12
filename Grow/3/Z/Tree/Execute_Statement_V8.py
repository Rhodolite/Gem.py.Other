#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Execute_Statement_V8 - Implementation of `Tree_Execute_Statement`, Version 8.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Example:
#
#       exec a, b, c
#
#   The above will be a `Tree_Execute_Statement`.
#


#
#   Differences between Version 7 and Version 8.
#
#       Version 7:
#
#           `.{globals,locals}` is of type `None | Tree_Value_Expression`.
#
#       Version 8:
#
#           `.{globals,locals}` is of type `Tree_Value_Expression_0`.
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
#   Tree: Execute Statement
#
#   Example:
#
#       exec a, b, c
#
#   The above will be a `Tree_Execute_Statement`.
#
class Tree_Execute_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'body',                         #   Tree_Value_Expression
        'globals',                      #   Tree_Value_Expression_0
        'locals',                       #   Tree_Value_Expression_0
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, body, globals, locals):
        self.line_number = line_number
        self.column      = column

        self.body    = body
        self.globals = globals
        self.locals  = locals


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<execute-statement @{}:{} ', self.line_number, self.column)
        self.body.dump_value_expression_tokens(f)

        if self.globals.has_tree_value_expression:
            f.write(' in ')
            self.globals.dump_value_expression_tokens(f)

            if self.locals.has_tree_value_expression:
                f.write(', ')
                self.locals.dump_value_expression_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Execute_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.globals, self.locals)


@creator
def create_Tree_Execute_Statement(line_number, column, body, globals, locals):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression  (body)
    assert fact_is_tree_value_expression_0(globals)
    assert fact_is_tree_value_expression_0(locals)

    if not globals.has_tree_value_expression:
        assert not locals.has_tree_value_expression

    return Tree_Execute_Statement(line_number, column, body, globals, locals)
