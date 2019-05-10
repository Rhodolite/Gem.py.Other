#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Statement - Implementation of `Tree_Statement`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Operator             import  fact_is_tree_operator
    from    Z.Tree.Target               import  fact_is__native_none__OR__tree_store_target
    from    Z.Tree.Target               import  fact_is_tree_store_target


#
#   Tree: "Test" Statement
#
#       A "Test" Statement is either a `if` or `while` statement.
#
class Tree_Test_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'test',                         #   Tree_Value_Expression
        'body',                         #   Full_Native_List of Tree_Statement
        'else_clause_0',                #   Some_Native_List of Tree_Statement
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
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<{} @{}:{} ', self.keyword, self.line_number, self.column)
        self.test.dump_value_expression_tokens(f)
        f.line(' {')

        with f.indent_2():
            for v in self.body:
                v.dump_statement_tokens(f)

        if len(self.else_clause_0) > 0:
            with f.indent('} else {'):
                for v in self.else_clause_0:
                    v.dump_statement_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.test, self.body,
                       self.else_clause_0)


@creator
def create_Tree_Test_Statement(Meta, line_number, column, test, body, else_clause_0):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_value_expression(test)
    assert fact_is_full_native_list     (body)
    assert fact_is_some_native_list     (else_clause_0)

    return Meta(line_number, column, test, body, else_clause_0)


#
#   Tree: For Statement
#
class Tree_For_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'target',                       #   Tree_Target
        'sequence',                     #   Tree_Value_Expression
        'body',                         #   Full_Native_List of Tree_Statement
        'else_clause_0',                #   Some_Native_List of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, target, sequence, body, else_clause_0):
        self.line_number = line_number
        self.column      = column

        self.target        = target
        self.sequence      = sequence
        self.body          = body
        self.else_clause_0 = else_clause_0


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<for @{}:{} ', self.line_number, self.column)
        self.target.dump_store_target_tokens(f)
        f.write(' in ')
        self.sequence.dump_value_expression_tokens(f)
        f.line(' {')

        with f.indent_2():
            for v in self.body:
                v.dump_statement_tokens(f)

        if len(self.else_clause_0) > 0:
            with f.indent('} else {'):
                for v in self.else_clause_0:
                    v.dump_statement_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_For_Statement @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.target, self.sequence, self.body, self.else_clause_0)


@creator
def create_Tree_For_Statement(line_number, column, target, sequence, body, else_clause_0):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_store_target    (target)
    assert fact_is_tree_value_expression(sequence)
    assert fact_is_full_native_list     (body)
    assert fact_is_some_native_list     (else_clause_0)

    return Tree_For_Statement(line_number, column, target, sequence, body, else_clause_0)


#
#   Tree: `if` statement
#
class Tree_If_Statement(Tree_Test_Statement):
    __slots__ = (())

    keyword = 'if'


@creator
def create_Tree_If_Statement(line_number, column, test, body, orelse):
    return create_Tree_Test_Statement(Tree_If_Statement, line_number, column, test, body, orelse)


#
#   Tree: Try Except Statement
#
class Tree_Try_Except_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'body',                         #   Full_Native_List of Tree_Statement
        'except_handlers',              #   Full_Native_List of Tree_Except_Handler
        'else_clause_0',                #   Some_Native_List of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, body, except_handlers, else_clause_0):
        self.line_number = line_number
        self.column      = column

        self.body            = body
        self.except_handlers = except_handlers
        self.else_clause_0   = else_clause_0


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.line('<try @{}:{} {{', self.line_number, self.column)

        with f.indent_2():
            with f.indent_2():
                for v in self.body:
                    v.dump_statement_tokens(f)

            f.line('}')

            for v in self.except_handlers:
                v.dump_except_clause_tokens(f)

            if len(self.else_clause_0) > 0:
                with f.indent('else {', '}'):
                    for v in self.else_clause_0:
                        v.dump_statement_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Try_Except_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.except_handlers, self.else_clause_0)


@creator
def create_Tree_Try_Except_Statement(line_number, column, body, except_handlers, else_clause_0):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(body)
    assert fact_is_full_native_list(except_handlers)
    assert fact_is_some_native_list(else_clause_0)

    return Tree_Try_Except_Statement(line_number, column, body, except_handlers, else_clause_0)


#
#   Tree: Try Finally Statement
#
class Tree_Try_Finally_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'body',                         #   Full_Native_List of Tree_Statement
        'finally_body',                 #   Full_Native_List of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, body, finally_body):
        self.line_number = line_number
        self.column      = column

        self.body         = body
        self.finally_body = finally_body


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        header = arrange('<try @{}:{} {{', self.line_number, self.column)

        with f.indent_2(header):
            for v in self.body:
                v.dump_statement_tokens(f)

        with f.indent_2('} finally {'):
            for v in self.finally_body:
                v.dump_statement_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Try_Finally_Statement @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.finally_body)


@creator
def create_Tree_Try_Finally_Statement(line_number, column, body, finally_body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(body)
    assert fact_is_full_native_list(finally_body)

    return Tree_Try_Finally_Statement(line_number, column, body, finally_body)


#
#   Tree: `while` statement
#
class Tree_While_Statement(Tree_Test_Statement):
    __slots__ = (())

    keyword = 'while'


@creator
def create_Tree_While_Statement(line_number, column, test, body, orelse):
    return create_Tree_Test_Statement(Tree_While_Statement, line_number, column, test, body, orelse)


#
#   Tree: With Statement
#
class Tree_With_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Value_Expression
        'target',                       #   None | Tree_Target
        'body',                         #   Full_Native_List of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, target, body):
        self.line_number = line_number
        self.column      = column

        self.value  = value
        self.target = target
        self.body   = body


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<with @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)

        if self.target is not None:
            f.write(' as ')
            self.target.dump_store_target_tokens(f)

        f.line(' {')

        with f.indent_2():
            for v in self.body:
                v.dump_statement_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_With_Statement @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.value, self.target)


@creator
def create_Tree_With_Statement(line_number, column, value, target, body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_value_expression              (value)
    assert fact_is__native_none__OR__tree_store_target(target)
    assert fact_is_full_native_list                   (body)

    return Tree_With_Statement(line_number, column, value, target, body)
