#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Statement_V1 - Implementation of `Tree_Statement`, Version 1.
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
    from    Z.Tree.Target               import  fact_is__native_none__OR__tree_store_target
    from    Z.Tree.Target               import  fact_is_tree_store_target


#
#   Tree: Keyword Statement, Version 1 - Base class of `break` and `pass` statement.
#
class Tree_Keyword_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.line('<{} @{}:{}>', self.keyword, self.line_number, self.column)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{}>', self.__class__.__name__, self.line_number, self.column)


def create_Tree_Keyword_Statement_V1(Meta, line_number, column):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    return Meta(line_number, column)


#
#   Tree: "Test" Statement, Version 1
#
#       A "Test" Statement is either a `if` or `while` statement.
#
class Tree_Test_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'test',                         #   Tree_Expression
        'body',                         #   FullNativeList of Tree_Statement
        'else_many',                    #   SomeNativeList of Tree_Statement
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column, test, body, else_many):
        self.line_number = line_number
        self.column      = column

        self.test      = test
        self.body      = body
        self.else_many = else_many


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<{} @{}:{} ', self.keyword, self.line_number, self.column)
        self.test.dump_evaluate_tokens(f)
        f.line(' {')

        with f.indent():
            for v in self.body:
                v.dump_suite_tokens(f)

        if len(self.else_many) > 0:
            with f.indent('} else {'):
                for v in self.else_many:
                    v.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.test, self.body, self.else_many)


def create_Tree_Test_Statement_V1(Meta, line_number, column, test, body, else_many):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression (test)
    assert fact_is_full_native_list(body)
    assert fact_is_some_native_list(else_many)

    return Meta(line_number, column, test, body, else_many)


#
#   Tree: Assert Statement, Version 1
#
class Tree_Assert_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'test',                         #   Tree_Expression
        'message',                      #   None | Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<assert @{}:{} ', self.line_number, self.column)
        self.test.dump_evaluate_tokens(f)

        if self.message is not None:
            f.write(', ')
            self.message.dump_evaluate_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Assert_Statement_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.test, self.message)



def create_Tree_Assert_Statement_V1(line_number, column, test, message):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression                  (test)
    assert fact_is__native_none__OR__tree_expression(message)

    return Tree_Assert_Statement_V1(line_number, column, test, message)

 
#
#   Tree: Assign Statement, Version 1
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
class Tree_Assign_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'targets',                      #   NativeList of Tree_Expression
        'value',                        #   Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<assign @{}:{} ', self.line_number, self.column)

        for v in self.targets:
            v.dump_store_target_tokens(f)
            f.write(' = ')
            
        self.value.dump_evaluate_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Assign_Statement_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.targets, self.value)


def create_Tree_Assign_Statement_V1(line_number, column, targets, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(targets)
    assert fact_is_tree_expression (value)

    return Tree_Assign_Statement_V1(line_number, column, targets, value)

 
#
#   Tree: `break` statement, V1
#
class Tree_Break_Statement_V1(Tree_Keyword_Statement_V1):
    __slots__ = (())


    keyword = 'break'


def create_Tree_Break_Statement_V1(line_number, column):
    return create_Tree_Keyword_Statement_V1(Tree_Break_Statement_V1, line_number, column)


#
#   Tree: Class Definition, Version 1
#
class Tree_Class_Definition_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'name',                         #   NativeString
        'bases',                        #   NativeList of Tree_Expression
        'body',                         #   NativeList of Tree_Statement
        'decorator_list',               #   NativeList of Tree_Decorator
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, name, bases, body, decorator_list):
        self.line_number = line_number
        self.column      = column

        self.name           = name
        self.bases          = bases
        self.body           = body
        self.decorator_list = decorator_list


    def _dump_bases_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.bases:
                v.dump_evaluate_tokens(f)
                f.line()


    def _dump_body_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.body:
                v.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_evaluate_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        decorator_list = self.decorator_list

        header = arrange('<class-definition @{}:{} {}', self.line_number, self.column, self.name)

        with f.indent_2(header, '>'):
            self._dump_bases_tokens(f, 'bases: [', None)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, ']; body: [',           ']')
            else:
                self._dump_body_tokens     (f, ']; body: [',           None)
                self._dump_decorator_tokens(f, ']; decorator_list: [', ']')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Class_Definition_V1 @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.bases, self.body, self.decorator_list)


def create_Tree_Class_Definition_V1(line_number, column, name, bases, body, decorator_list):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string(name)
    assert fact_is_some_native_list  (bases)
    assert fact_is_full_native_list  (body)
    assert fact_is_some_native_list  (decorator_list)

    return Tree_Class_Definition_V1(line_number, column, name, bases, body, decorator_list)


#
#   Tree: `continue` statement, V1
#
class Tree_Continue_Statement_V1(Tree_Keyword_Statement_V1):
    __slots__ = (())


    keyword = 'continue'


def create_Tree_Continue_Statement_V1(line_number, column):
    return create_Tree_Keyword_Statement_V1(Tree_Continue_Statement_V1, line_number, column)


#
#   Tree: Delete Statement, Version 1
#
class Tree_Delete_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
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
        return arrange('<Tree_Delete_Statement_V1 @{}:{} {!r}>', self.line_number, self.column, self.targets)


def create_Tree_Delete_Statement_V1(line_number, column, targets):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(targets)

    return Tree_Delete_Statement_V1(line_number, column, targets)


#
#   Tree: Execute Statement, Version 1
#
#   Example:
#
#       exec a, b, c
#
#   The above will be a `Tree_Execute_Statement_V1`.
#
class Tree_Execute_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'body',                         #   Tree_Expression
        'globals',                      #   None | Tree_Expression
        'locals',                       #   None | Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<execute-statement @{}:{} ', self.line_number, self.column)
        self.body.dump_evaluate_tokens(f)

        if self.globals is not None:
            f.write(' in ')
            self.globals.dump_evaluate_tokens(f)

            if self.locals is not None:
                f.write(', ')
                self.locals.dump_evaluate_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Execute_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.globals, self.locals)


def create_Tree_Execute_Statement_V1(line_number, column, body, globals, locals):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression                  (body)
    assert fact_is__native_none__OR__tree_expression(globals)
    assert fact_is__native_none__OR__tree_expression(locals)

    if globals is None:
        assert fact_is_native_none(locals)

    return Tree_Execute_Statement_V1(line_number, column, body, globals, locals)


#
#   Tree: Expression Statement, Version 1
#
#   Example:
#
#       f(a)
#
#   The above will be a `Tree_Expression_Statement_V1`, the expression will be a `Tree_Call` (i.e.: a function call).
#
class Tree_Expression_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<expression-statement @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Expression_Statement_V1 @{}:{} {!r}>',
                       self.line_number, self.column, self.value)


def create_Tree_Expression_Statement_V1(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(value)

    return Tree_Expression_Statement_V1(line_number, column, value)


#
#   Tree: For Statement, Version 1
#
class Tree_For_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'target',                       #   Tree_Target
        'sequence',                     #   Tree_Expression
        'body',                         #   FullNativeList of Tree_Statement
        'else_many',                    #   SomeNativeList of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, target, sequence, body, else_many):
        self.line_number = line_number
        self.column      = column

        self.target    = target
        self.sequence  = sequence
        self.body      = body
        self.else_many = else_many


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<for @{}:{} ', self.line_number, self.column)
        self.target.dump_store_target_tokens(f)
        f.write(' in ')
        self.sequence.dump_evaluate_tokens(f)
        f.line(' {')

        with f.indent():
            for v in self.body:
                v.dump_suite_tokens(f)

        if len(self.else_many) > 0:
            with f.indent('} else {'):
                for v in self.else_many:
                    v.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_For_Statement_V1 @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.target, self.sequence, self.body, self.else_many)


def create_Tree_For_Statement_V1(line_number, column, target, sequence, body, else_many):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_store_target(target)
    assert fact_is_tree_expression  (sequence)
    assert fact_is_full_native_list (body)
    assert fact_is_some_native_list (else_many)

    return Tree_For_Statement_V1(line_number, column, target, sequence, body, else_many)


#
#   Tree: `if` statement, Version 1
#
class Tree_If_Statement_V1(Tree_Test_Statement_V1):
    __slots__ = (())

    keyword = 'if'


def create_Tree_If_Statement_V1(line_number, column, test, body, orelse):
    return create_Tree_Test_Statement_V1(Tree_If_Statement_V1, line_number, column, test, body, orelse)


#
#   Tree: `from ... import ...` statement, Version 1
#
class Tree_From_Import_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'module',                       #   NativeString
        'names',                        #   NativeList of Tree_Alias
        'level',                        #   SubstantialInteger
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, module, names, level):
        self.line_number = line_number
        self.column      = column

        self.module = module
        self.names  = names
        self.level  = level


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<from @{}:{} {} import ', self.line_number, self.column, self.module)

        #
        #<names>
        #
        f.write('[')

        first = True

        for v in self.names:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_alias_tokens(f)

        f.write(']')
        #</>

        if self.level:
            f.arrange('; level<{}>', self.level)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_From_Import_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column,
                       self.module, self.names, self.level)


def create_Tree_From_Import_Statement_V1(line_number, column, module, names, level):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string (module)
    assert fact_is_full_native_list   (names)
    assert fact_is_substantial_integer(level)

    return Tree_From_Import_Statement_V1(line_number, column, module, names, level)


#
#   Tree: Function Definition, Version 1
#
class Tree_Function_Definition_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'name',                         #   NativeString
        'parameters',                   #   Tree_Parameter
        'body',                         #   NativeList of Tree_Statement
        'decorator_list',               #   NativeList of Tree_Decorator
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, name, parameters, body, decorator_list):
        self.line_number = line_number
        self.column      = column

        self.name           = name
        self.parameters     = parameters
        self.body           = body
        self.decorator_list = decorator_list


    def _dump_body_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.body:
                v.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_evaluate_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        decorator_list = self.decorator_list

        header = arrange('<function-definition @{}:{} {}', self.line_number, self.column, self.name)

        with f.indent_2(header, '>'):
            self.parameters.dump_parameter_tokens(f)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, '[',                    ']')
            else:
                self._dump_body_tokens     (f, '[',                    None)
                self._dump_decorator_tokens(f, ']; decorator_list: [', ']')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Function_Definition_V1 @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.parameters, self.body, self.decorator_list)


def create_Tree_Function_Definition_V1(line_number, column, name, parameters, body, decorator_list):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string (name)
    assert fact_is_tree_parameters_all(parameters)
    assert fact_is_full_native_list   (body)
    assert fact_is_some_native_list   (decorator_list)

    return Tree_Function_Definition_V1(line_number, column, name, parameters, body, decorator_list)


#
#   Tree: Global Statement, Version 1
#
class Tree_Global_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'names',                        #   FullNativeList of FullNativeString
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, names):
        self.line_number = line_number
        self.column      = column

        self.names = names


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        first = True

        f.arrange('<global @{}:{} ', self.line_number, self.column)

        for s in self.names:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            f.write(s)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Global_Statement_V1 @{}:{} {!r}>', self.line_number, self.column, self.names)


def create_Tree_Global_Statement_V1(line_number, column, names):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(names)

    return Tree_Global_Statement_V1(line_number, column, names)


#
#   Tree: `import` statement, Version 1
#
class Tree_Import_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'aliases',                      #   NativeList of Tree_Alias
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, aliases):
        self.line_number = line_number
        self.column      = column

        self.aliases = aliases


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<import @{}:{} ', self.line_number, self.column)

        #
        #<aliases>
        #
        f.write('[')

        first = True

        for v in self.aliases:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_alias_tokens(f)

        f.write(']')
        #</>

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Import_Statement_V1 @{}:{} {!r}>', self.line_number, self.column, self.aliases)


def create_Tree_Import_Statement_V1(line_number, column, aliases):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(aliases)

    return Tree_Import_Statement_V1(line_number, column, aliases)


#
#   Tree: Modify Statement, Version 1
#
#       (i.e.: a `+=`, `*=`, etc. statement).
#
class Tree_Modify_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'left',                         #   Tree_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<modify-statement @{}:{} ', self.line_number, self.column)
        self.left.dump_store_target_tokens(f)
        f.space()
        self.operator.dump_operator_token(f)
        f.space()
        self.right.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Modify_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.left, self.operator, self.right)


def create_Tree_Modify_Statement_V1(line_number, column, left, operator, right):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_store_target(left)
    assert fact_is_tree_operator    (operator)
    assert fact_is_tree_expression  (right)

    return Tree_Modify_Statement_V1(line_number, column, left, operator, right)


#
#   Tree: `pass` statement, V1
#
class Tree_Pass_Statement_V1(Tree_Keyword_Statement_V1):
    __slots__ = (())


    keyword = 'pass'


def create_Tree_Pass_Statement_V1(line_number, column):
    return create_Tree_Keyword_Statement_V1(Tree_Pass_Statement_V1, line_number, column)


#
#   Tree: Print Statement, Version 1
#
class Tree_Print_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'destination',                  #   None | Tree_Expression
        'values',                       #   FullNativeList of Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        first = True

        f.arrange('<print @{}:{}', self.line_number, self.column)

        if self.destination is not None:
            first = False

            f.write(' {>>} ')
            self.destination.dump_evaluate_tokens(f)

        for v in self.values:
            if first:
                first = True
            else:
                f.write(',')

            f.space()
            v.dump_evaluate_tokens(f)

        if not self.newline:
            f.write(',')

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Print_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.destination, self.values, self.newline)


def create_Tree_Print_Statement_V1(line_number, column, destination, values, newline):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_expression(destination)
    assert fact_is_full_native_list                 (values)
    assert fact_is_native_boolean                   (newline)

    return Tree_Print_Statement_V1(line_number, column, destination, values, newline)

 
#
#   Tree: Return Statement, Version 1
#
class Tree_Return_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<return @{}:{}', self.line_number, self.column)

        if self.value is not None:
            f.space()
            self.value.dump_evaluate_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Return_Statement_V1 @{}:{} {!r}>', self.line_number, self.column, self.value)



def create_Tree_Return_Statement_V1(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_expression(value)

    return Tree_Return_Statement_V1(line_number, column, value)


#
#   Tree: Raise Statement, Version 1
#
class Tree_Raise_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'type',                         #   None | Tree_Expression
        'instance',                     #   None | Tree_Expression
        'traceback',                    #   None | Tree_Expression
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<raise @{}:{}', self.line_number, self.column)

        if self.type is None:
            assert instance is traceback is None
        else:
            f.space()
            self.type.dump_evaluate_tokens(f)

            if self.instance is None:
                assert self.traceback is None
            else:
                f.write(', ')
                self.instance.dump_evaluate_tokens(f)

                if self.traceback is not None:   
                    f.write(', ')
                    self.traceback.dump_evaluate_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Raise_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.type, self.instance, self.traceback)


def create_Tree_Raise_Statement_V1(line_number, column, type, instance, traceback):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_expression(type)
    assert fact_is__native_none__OR__tree_expression(instance)
    assert fact_is__native_none__OR__tree_expression(traceback)

    if type is None:
        assert fact_is_native_none(instance)

    if instance is None:
        assert fact_is_native_none(traceback)

    return Tree_Raise_Statement_V1(line_number, column, type, instance, traceback)


#
#   Tree: Try Except Statement, Version 1
#
class Tree_Try_Except_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'body',                         #   FullNativeList of Tree_Statement
        'except_handlers',              #   FullNativeList of Tree_Except_Handler
        'else_many',                    #   SomeNativeList of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, body, except_handlers, else_many):
        self.line_number = line_number
        self.column      = column

        self.body            = body
        self.except_handlers = except_handlers
        self.else_many       = else_many


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.line('<try @{}:{} {{', self.line_number, self.column)

        with f.indent_2():
            with f.indent_2():
                for v in self.body:
                    v.dump_suite_tokens(f)

            f.line('}')

            for v in self.except_handlers:
                v.dump_except_clause_tokens(f)

            if len(self.else_many) > 0:
                with f.indent('else {', '}'):
                    for v in self.else_many:
                        v.dump_suite_tokens(f)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Try_Except_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.except_handlers, self.else_many)


def create_Tree_Try_Except_Statement_V1(line_number, column, body, except_handlers, else_many):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(body)
    assert fact_is_full_native_list(except_handlers)
    assert fact_is_some_native_list(else_many)

    return Tree_Try_Except_Statement_V1(line_number, column, body, except_handlers, else_many)


#
#   Tree: Try Finally Statement, Version 1
#
class Tree_Try_Finally_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'body',                         #   FullNativeList of Tree_Statement
        'finally_body',                 #   FullNativeList of Tree_Statement
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        header = arrange('<try @{}:{} {{', self.line_number, self.column)

        with f.indent_2(header):
            for v in self.body:
                v.dump_suite_tokens(f)

        with f.indent_2('} finally {'):
            for v in self.finally_body:
                v.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Try_Finally_Statement_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.body, self.finally_body)


def create_Tree_Try_Finally_Statement_V1(line_number, column, body, finally_body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(body)
    assert fact_is_full_native_list(finally_body)

    return Tree_Try_Finally_Statement_V1(line_number, column, body, finally_body)


#
#   Tree: `while` statement, Version 1
#
class Tree_While_Statement_V1(Tree_Test_Statement_V1):
    __slots__ = (())

    keyword = 'while'


def create_Tree_While_Statement_V1(line_number, column, test, body, orelse):
    return create_Tree_Test_Statement_V1(Tree_While_Statement_V1, line_number, column, test, body, orelse)


#
#   Tree: With Statement, Version 1
#
class Tree_With_Statement_V1(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
        'target',                       #   None | Tree_Target
        'body',                         #   FullNativeList of Tree_Statement
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
    if __debug__:
        is_tree_statement = True


    suite_estimate = 1


    def dump_suite_tokens(self, f):
        f.arrange('<with @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)

        if self.target is not None:
            f.write(' as ')
            self.target.dump_store_target_tokens(f)

        f.line(' {')

        with f.indent():
            for v in self.body:
                v.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_With_Statement_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.value, self.target, self.body.else_many)


def create_Tree_With_Statement_V1(line_number, column, value, target, body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression                    (value)
    assert fact_is__native_none__OR__tree_store_target(target)
    assert fact_is_full_native_list                   (body)

    return Tree_With_Statement_V1(line_number, column, value, target, body)
