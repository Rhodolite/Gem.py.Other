#


#
#   Z.Tree.Statement - Implementation of `Tree_Statement`, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Operator             import  fact_is_tree_operator
    from    Z.Tree.Parameter            import  fact_is_tree_parameters_all
    from    Z.Tree.Statement            import  fact_is_tree_statement
    from    Z.Tree.Statement            import  fact_is_tree_statement_0
    from    Z.Tree.Target               import  fact_is__native_none__OR__tree_store_target
    from    Z.Tree.Target               import  fact_is_tree_store_target


#
#   Tree: "Test" Statement
#
#       A "Test" Statement is either a `if` or `while` statement.
#
class Tree_Test_Statement(object):
    #
    #   Implements Tree_Statement,
    #              Tree_Statement_0
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'test',                         #   Tree_Expression
        'body',                         #   Tree_Statement
        'else_clause_0',                #   Tree_Statement_0
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column, test, body, else_clause_0):
        self.line_number = line_number
        self.column      = column

        self.test          = test
        self.body          = body
        self.else_clause_0 = else_clause_0


    #
    #   Interface Tree_Statement,
    #             Tree_Statement_0
    #
    if __debug__:
        is_tree_statement   = True
        is_tree_statement_0 = True


    is_tree_statement_none = False
    suite_estimate         = 1


    def dump_suite_tokens(self, f):
        f.arrange('<{} @{}:{} ', self.keyword, self.line_number, self.column)
        self.test.dump_evaluate_tokens(f)
        f.line(' {')

        with f.indent_2():
            self.body.dump_suite_tokens(f)

        if self.else_clause_0.suite_estimate:
            with f.indent('} else {'):
                self.else_clause_0.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.test, self.body, self.else_clause_0)


def create_Tree_Test_Statement(Meta, line_number, column, test, body, else_clause_0):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression (test)
    assert fact_is_tree_statement  (body)
    assert fact_is_tree_statement_0(body)

    return Meta(line_number, column, test, body, else_clause_0)


#
#   Tree: `if` statement
#
class Tree_If_Statement(Tree_Test_Statement):
    __slots__ = (())

    keyword = 'if'


def create_Tree_If_Statement(line_number, column, test, body, orelse):
    return create_Tree_Test_Statement(Tree_If_Statement, line_number, column, test, body, orelse)
