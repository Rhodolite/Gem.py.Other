#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Simple_Statement_V7 - Implementation of simple tree statements, Version 7.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Versions 1..7.
#
#       Version 1:
#
#           Tree Statements implement `Tree_Statement`.
#
#       Version 2..6:
#
#           Do not exist.
#
#       Version 7:
#
#           Tree Statements implement `Tree_Statement`; and ...
#
#           ... in addition also implement `Tree_Suite`, and `Tree_Suite_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Operator             import  fact_is_tree_operator
    from    Z.Tree.Parameter            import  fact_is_tree_parameters_all
    from    Z.Tree.Target               import  fact_is__native_none__OR__tree_store_target
    from    Z.Tree.Target               import  fact_is_tree_store_target


#
#   Tree: Keyword Statement - Base class of `break` and `pass` statement.
#
class Tree_Keyword_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column):
        self.line_number = line_number
        self.column      = column


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.line('<{} @{}:{}>', self.keyword, self.line_number, self.column)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{}>', self.__class__.__name__, self.line_number, self.column)


@creator
def create_Tree_Keyword_Statement(Meta, line_number, column):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    return Meta(line_number, column)


#
#   Tree: Assert Statement
#
class Tree_Assert_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_value_expression                  (test)
    assert fact_is__native_none__OR__tree_value_expression(message)

    return Tree_Assert_Statement(line_number, column, test, message)


#
#   Tree: Assign Statement
#
#   Example:
#
#       [a, b, c] = d = e
#
#   In the above example the targets will be `NativeList` with two elements:
#
#       `[ [a, b, c], d ]`
#
#   The value will be:
#
#       `e`
#
class Tree_Assign_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'targets',                      #   NativeList of Tree_Store_Target
        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, targets, value):
        self.line_number = line_number
        self.column      = column

        self.targets = targets
        self.value   = value


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<assign @{}:{} ', self.line_number, self.column)

        for v in self.targets:
            v.dump_store_target_tokens(f)
            f.write(' = ')

        self.value.dump_value_expression_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Assign_Statement @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.targets, self.value)


@creator
def create_Tree_Assign_Statement(line_number, column, targets, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list     (targets)
    assert fact_is_tree_value_expression(value)

    return Tree_Assign_Statement(line_number, column, targets, value)


#
#   Tree: Break Statement
#
class Tree_Break_Statement(Tree_Keyword_Statement):
    __slots__ = (())


    keyword = 'break'


@creator
def create_Tree_Break_Statement(line_number, column):
    return create_Tree_Keyword_Statement(Tree_Break_Statement, line_number, column)


#
#   Tree: Continue Statement
#
class Tree_Continue_Statement(Tree_Keyword_Statement):
    __slots__ = (())


    keyword = 'continue'


@creator
def create_Tree_Continue_Statement(line_number, column):
    return create_Tree_Keyword_Statement(Tree_Continue_Statement, line_number, column)


#
#   Tree: Delete Statement
#
class Tree_Delete_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'targets',                      #   FullNativeList of Tree_Target
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, targets):
        self.line_number = line_number
        self.column      = column

        self.targets = targets


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        first = True

        f.arrange('<delete @{}:{}', self.line_number, self.column)

        for v in self.targets:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            v.dump_delete_target_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Delete_Statement @{}:{} {!r}>', self.line_number, self.column, self.targets)


@creator
def create_Tree_Delete_Statement(line_number, column, targets):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(targets)

    return Tree_Delete_Statement(line_number, column, targets)


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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_value_expression                  (body)
    assert fact_is__native_none__OR__tree_value_expression(globals)
    assert fact_is__native_none__OR__tree_value_expression(locals)

    if globals is None:
        assert fact_is_native_none(locals)

    return Tree_Execute_Statement(line_number, column, body, globals, locals)


#
#   Tree: Expression Statement
#
#       Example:
#
#           f(a)
#
#       The above will be a `Tree_Expression_Statement`, the expression will be a `Tree_Call` (i.e.: a function call).
#
class Tree_Expression_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value):
        self.line_number = line_number
        self.column      = column

        self.value = value


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<expression-statement @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Expression_Statement @{}:{} {!r}>',
                       self.line_number, self.column, self.value)


@creator
def create_Tree_Expression_Statement(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_value_expression(value)

    return Tree_Expression_Statement(line_number, column, value)


#
#   Tree: Modify Statement
#
#       (i.e.: a `+=`, `*=`, etc. statement).
#
class Tree_Modify_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'left',                         #   Tree_Value_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, left, operator, right):
        self.line_number = line_number
        self.column      = column

        self.left     = left
        self.operator = operator
        self.right    = right


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<modify-statement @{}:{} ', self.line_number, self.column)
        self.left.dump_store_target_tokens(f)
        f.space()
        self.operator.dump_operator_token(f)
        f.space()
        self.right.dump_value_expression_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Modify_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.left, self.operator, self.right)


@creator
def create_Tree_Modify_Statement(line_number, column, left, operator, right):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_store_target    (left)
    assert fact_is_tree_operator        (operator)
    assert fact_is_tree_value_expression(right)

    return Tree_Modify_Statement(line_number, column, left, operator, right)


#
#   Tree: Pass statement
#
class Tree_Pass_Statement(Tree_Keyword_Statement):
    __slots__ = (())


    keyword = 'pass'


@creator
def create_Tree_Pass_Statement(line_number, column):
    return create_Tree_Keyword_Statement(Tree_Pass_Statement, line_number, column)


#
#   Tree: Print Statement
#
class Tree_Print_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'destination',                  #   None | Tree_Value_Expression
        'values',                       #   SomeNativeList of Tree_Value_Expression
        'newline',                      #   NativeBoolean
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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_value_expression(destination)
    assert fact_is_some_native_list                       (values)
    assert fact_is_native_boolean                         (newline)

    return Tree_Print_Statement(line_number, column, destination, values, newline)


#
#   Tree: Return Statement
#
class Tree_Return_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   None | Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value):
        self.line_number = line_number
        self.column      = column

        self.value = value


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<return @{}:{}', self.line_number, self.column)

        if self.value is not None:
            f.space()
            self.value.dump_value_expression_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Return_Statement @{}:{} {!r}>', self.line_number, self.column, self.value)



@creator
def create_Tree_Return_Statement(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_value_expression(value)

    return Tree_Return_Statement(line_number, column, value)


#
#   Tree: Raise Statement
#
class Tree_Raise_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_value_expression(type)
    assert fact_is__native_none__OR__tree_value_expression(instance)
    assert fact_is__native_none__OR__tree_value_expression(traceback)

    if type is None:
        assert fact_is_native_none(instance)

    if instance is None:
        assert fact_is_native_none(traceback)

    return Tree_Raise_Statement(line_number, column, type, instance, traceback)