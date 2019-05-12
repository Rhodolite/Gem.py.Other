#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Execute_Statement_V1 - Implementation of `Tree_Execute_Statement`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Example:
#
#       exec a in b, c
#
#   The above will be a `Tree_Execute_Statement`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Execute Statement
#
class Tree_Execute_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'body',                         #   Tree_Value_Expression
        'globals',                      #   None | Tree_Value_Expression
        'locals',                       #   None | Tree_Value_Expression
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

        if self.globals is not None:
            f.write(' in ')
            self.globals.dump_value_expression_tokens(f)

            if self.locals is not None:
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

    assert fact_is_tree_value_expression                  (body)
    assert fact_is__native_none__OR__tree_value_expression(globals)
    assert fact_is__native_none__OR__tree_value_expression(locals)

    if globals is None:
        assert fact_is_native_none(locals)

    return Tree_Execute_Statement(line_number, column, body, globals, locals)
