#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Expression_V1 - Implementation of `Tree_Expression`, Version 1.
#
#       Copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   NOTE:
#       
#       Some tree expressions are in other files:
#
#           Tree_Attribute_Expression   #   See "Z/Tree/Target_1.py"
#           Tree_List_Expression        #   See "Z/Tree/Target_1.py"
#           Tree_Name                   #   See "Z/Tree/Name.py"
#           Tree_Tuple_Expression       #   See "Z/Tree/Target_1.py"
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_some_native_string
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Operator             import  fact_is_tree_operator
    from    Z.Tree.Parameter            import  fact_is_tree_parameters_all


#
#   Tree: Value Comprehension, V1
#
#       Base of `Tree_Generator_Comprehension_V1`, `Tree_List_Comprehension_V1`, and `Tree_Set_Comprehension_V1`.
#
class Tree_Value_Comprehension_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'element',                      #   Tree_Expression
        'generators',                   #   FullNativeList of Tree_Comprehension
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, element, generators):
        self.line_number = line_number
        self.column      = column

        self.element    = element
        self.generators = generators


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        first = True

        f.arrange('<{} @{}:{} ', self.keyword, self.line_number, self.column)
        self.element.dump_evaluate_tokens(f)

        for v in self.generators:
            f.space()
            v.dump_comprehension_clause_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.element, self.generators)


def create_Tree_Value_Comprehension_V1(Meta, line_number, column, element, generators):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression (element)
    assert fact_is_full_native_list(generators)

    return Meta(line_number, column, element, generators)


#
#   Tree: Backquote Expression, Version 1
#
class Tree_Backquote_Expression_V1(object):
    #
    #   implements Tree_Expression
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
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<backquote @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Backquote_Expression_V1 @{}:{} {!r}>',
                       self.line_number, self.column, self.value)


def create_Tree_Backquote_Expression_V1(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(value)

    return Tree_Backquote_Expression_V1(line_number, column, value)


#
#   Tree: Binary Expression, Version 1
#
class Tree_Binary_Expression_V1(object):
    #
    #   implements Tree_Expression
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
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<binary @{}:{} ', self.line_number, self.column)
        self.left.dump_evaluate_tokens(f)
        f.space()
        self.operator.dump_operator_token(f)
        f.space()
        self.right.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Binary_Expression_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.left, self.operator, self.right)


def create_Tree_Binary_Expression_V1(line_number, column, left, operator, right):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(left)
    assert fact_is_tree_operator  (operator)
    assert fact_is_tree_expression(right)

    return Tree_Binary_Expression_V1(line_number, column, left, operator, right)


#
#   Tree_Call_V1
#
class Tree_Call_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'function',                     #   Tree_*_Expression
        'arguments',                    #   NativeList of Tree_*_Expression
        'keywords',                     #   NativeList of Tree_*_Expression
        'star_arguments',               #   None | Tree_*_Expression
        'keyword_arguments',            #   None | Tree_*_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, function, arguments, keywords, star_arguments, keyword_arguments):
        self.line_number = line_number
        self.column      = column

        self.function          = function
        self.arguments         = arguments
        self.keywords          = keywords
        self.star_arguments    = star_arguments
        self.keyword_arguments = keyword_arguments


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        first = True

        star_arguments    = self.star_arguments
        keyword_arguments = self.keyword_arguments

        f.arrange('<call @{}:{} ', self.line_number, self.column)
        self.function.dump_evaluate_tokens(f)

        f.write(' (')

        for v in self.arguments:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_evaluate_tokens(f)

        for v in self.keywords:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_argument_tokens(f)

        if star_arguments is not None:
            if first:
                first = False
            else:
                f.write(', ')

            f.write('*')
            star_arguments.dump_evaluate_tokens(f)

        if keyword_arguments is not None:
            if first:
                first = False
            else:
                f.write(', ')

            f.write('**')
            keyword_arguments.dump_evaluate_tokens(f)

        f.write(')>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Call_V1 @{}:{} {!r} {} {} {} {}>',
                       self.line_number, self.column,
                       self.function, self.arguments, self.keywords, self.star_arguments, self.keyword_arguments)


def create_Tree_Call_V1(
        line_number, column, function, arguments, keywords, star_arguments, keyword_arguments,
):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression                  (function)
    assert fact_is_some_native_list                 (arguments)
    assert fact_is_some_native_list                 (keywords)
    assert fact_is__native_none__OR__tree_expression(star_arguments)
    assert fact_is__native_none__OR__tree_expression(keyword_arguments)

    return Tree_Call_V1(
               line_number, column, function, arguments, keywords, star_arguments, keyword_arguments,
           )


#
#   Tree: Compare Expression, Version 1
#
class Tree_Compare_Expression_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'left',                         #   Tree_Expression
        'operators',                    #   FullNativeList of Tree_Operator
        'comparators',                  #   FullNativeList of Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, left, operators, comparators):
        self.line_number = line_number
        self.column      = column

        self.left        = left
        self.operators   = operators
        self.comparators = comparators


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<compare @{}:{} ', self.line_number, self.column)
        self.left.dump_evaluate_tokens(f)

        for [operator, right] in zip(self.operators, self.comparators):
            f.space()
            operator.dump_operator_token(f)
            f.space()
            right.dump_evaluate_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Compare_Expression_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.left, self.operators, self.comparators)


def create_Tree_Compare_Expression_V1(line_number, column, left, operators, comparators):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression (left)
    assert fact_is_full_native_list(operators)
    assert fact_is_full_native_list(comparators)

    return Tree_Compare_Expression_V1(line_number, column, left, operators, comparators)


#
#   Tree: Generator Comprehension, V1
#
class Tree_Generator_Comprehension_V1(Tree_Value_Comprehension_V1):
    __slots__ = (())

    keyword = 'generator-comprehension'


def create_Tree_Generator_Comprehension_V1(line_number, column, element, generators):
    return create_Tree_Value_Comprehension_V1(Tree_Generator_Comprehension_V1, line_number, column, element, generators)


#
#   Tree: If Expression, Version 1
#
class Tree_If_Expression_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'test',                         #   Tree_Expression
        'body',                         #   Tree_Expression
        'else_expression',              #   Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, test, body, else_expression):
        self.line_number = line_number
        self.column      = column

        self.test            = test
        self.body            = body
        self.else_expression = else_expression


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<if-expression @{}:{} ', self.line_number, self.column)
        self.body.dump_evaluate_tokens(f)
        f.write(' if ')
        self.test.dump_evaluate_tokens(f)
        f.write(' else ')
        self.else_expression.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_If_Expression_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.test, self.body, self.else_expression)


def create_Tree_If_Expression_V1(line_number, column, test, body, else_expression):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression(test)
    assert fact_is_tree_expression(body)
    assert fact_is_tree_expression(else_expression)

    return Tree_If_Expression_V1(line_number, column, test, body, else_expression)


#
#   Tree: Logical Expression, Version 1
#
class Tree_Logical_Expression_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'operator',                     #   Tree_Operator
        'values',                       #   NativeList of Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, operator, values):
        self.line_number = line_number
        self.column      = column

        self.operator = operator
        self.values   = values


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        first = True

        f.arrange('<logical @{}:{} ', self.line_number, self.column)

        for v in self.values:
            if first:
                first = False
            else:
                f.space()
                self.operator.dump_operator_token(f)
                f.space()

            v.dump_evaluate_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Logical_Expression_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.operator, self.values)


def create_Tree_Logical_Expression_V1(line_number, column, operator, values):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_operator   (operator)
    assert fact_is_full_native_list(values)

    return Tree_Logical_Expression_V1(line_number, column, operator, values)


#
#   Tree: Map Expression, V1
#
class Tree_Map_Expression_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'keys',                         #   SomeNativeList of Tree_Expression
        'values',                       #   SomeNativeList of Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, keys, values):
        self.line_number = line_number
        self.column      = column

        self.keys   = keys
        self.values = values


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<map @{}:{}', self.line_number, self.column)

        if len(self.keys) == 0:
            f.greater_than_sign()
            return

        first = True

        for [k, v] in zip(self.keys, self.values):
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            k.dump_evaluate_tokens(f)
            f.write(' : ')
            v.dump_evaluate_tokens(f)

        f.write(' >')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Map_Expression_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.keys, self.values)


def create_Tree_Map_Expression_V1(line_number, column, keys, values):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_list(keys)
    assert fact_is_some_native_list(values)

    assert len(keys) == len(values)

    return Tree_Map_Expression_V1(line_number, column, keys, values)


#
#   Tree: Lambda Expression, Version 1
#
class Tree_Lambda_Expression_V1(object):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, parameters, body):
        self.line_number = line_number
        self.column      = column

        self.parameters = parameters
        self.body       = body


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        header = arrange('<lambda @{}:{}', self.line_number, self.column)

        f.line()

        with f.indent_2():
            with f.indent_2(header, '>'):
                self.parameters.dump_parameter_tokens(f)
                self.body.dump_evaluate_tokens(f)
                f.line()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Lambda_Expression_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.parameters, self.body)


def create_Tree_Lambda_Expression_V1(line_number, column, parameters, body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_parameters_all(parameters)
    assert fact_is_tree_expression    (body)

    return Tree_Lambda_Expression_V1(line_number, column, parameters, body)


#
#   Tree: List Comprehension, V1
#
class Tree_List_Comprehension_V1(Tree_Value_Comprehension_V1):
    __slots__ = (())

    keyword = 'list-comprehension'


def create_Tree_List_Comprehension_V1(line_number, column, element, generators):
    return create_Tree_Value_Comprehension_V1(Tree_List_Comprehension_V1, line_number, column, element, generators)


#
#   Tree: Map Comprehension, V1
#
class Tree_Map_Comprehension_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'key',                          #   Tree_Expression
        'value',                        #   Tree_Expression
        'generators',                   #   FullNativeList of Tree_Comprehension
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, key, value, generators):
        self.line_number = line_number
        self.column      = column

        self.key        = key
        self.value      = value
        self.generators = generators


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        first = True

        f.arrange('<map-comprehension @{}:{} ', self.line_number, self.column)
        self.key.dump_evaluate_tokens(f)
        f.write(' : ')
        self.value.dump_evaluate_tokens(f)

        for v in self.generators:
            f.space()
            v.dump_comprehension_clause_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Map_Comprehension_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.key, self.value, self.generators)


def create_Tree_Map_Comprehension_V1(line_number, column, key, value, generators):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression (key)
    assert fact_is_tree_expression (value)
    assert fact_is_full_native_list(generators)

    return Tree_Map_Comprehension_V1(line_number, column, key, value, generators)


#
#   Tree: Number, Version 1
#
class Tree_Number_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'n',                            #   int
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, n):
        self.line_number = line_number
        self.column      = column

        self.n = n


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<number @{}:{} {}>', self.line_number, self.column, self.n)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Number_V1 @{}:{} {!r}>', self.line_number, self.column, self.n)


def create_Tree_Number_V1(line_number, column, n):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_integer(n)

    return Tree_Number_V1(line_number, column, n)


#
#   Tree: Set Comprehension, V1
#
class Tree_Set_Comprehension_V1(Tree_Value_Comprehension_V1):
    __slots__ = (())

    keyword = 'set-comprehension'


def create_Tree_Set_Comprehension_V1(line_number, column, element, generators):
    return create_Tree_Value_Comprehension_V1(Tree_Set_Comprehension_V1, line_number, column, element, generators)


#
#   Tree: Set Expression, V1
#
class Tree_Set_Expression_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'values',                       #   SomeNativeList of Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, values):
        self.line_number = line_number
        self.column      = column

        self.values = values


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<set @{}:{}', self.line_number, self.column)

        first = True

        for v in self.values:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            v.dump_evaluate_tokens(f)

        f.write('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Set_Expression_V1 @{}:{} {!r}>', self.line_number, self.column, self.values)


def create_Tree_Set_Expression_V1(line_number, column, values):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_list(values)

    return Tree_Set_Expression_V1(line_number, column, values)


#
#   Tree: String, Version 1
#
class Tree_String_V1(object):
    #
    #   Implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        's',                            #   NativeString
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, s):
        self.line_number = line_number
        self.column      = column

        self.s = s


    #
    #   Interface Tree_Expression
    #
    is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<string @{}:{} ', self.line_number, self.column)
        f.write(repr(self.s))
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_String_V1 @{}:{} {!r}>', self.line_number, self.column, self.s)


def create_Tree_String_V1(line_number, column, s):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_string(s)

    return Tree_String_V1(line_number, column, s)


#
#   Tree: Unary Expression, Version 1
#
class Tree_Unary_Expression_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, operator, right):
        self.line_number = line_number
        self.column      = column

        self.operator = operator
        self.right    = right


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<unary @{}:{} ', self.line_number, self.column)
        self.operator.dump_operator_token(f)
        f.space()
        self.right.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Unary_Expression_V1 @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.operator, self.right)


def create_Tree_Unary_Expression_V1(line_number, column, operator, right):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_operator  (operator)
    assert fact_is_tree_expression(right)

    return Tree_Unary_Expression_V1(line_number, column, operator, right)


#
#   Tree: Yield Expression, Version 1
#
class Tree_Yield_Expression_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   None | Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value):
        self.line_number = line_number
        self.column      = column

        self.value = value


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        f.arrange('<yield @{}:{}', self.line_number, self.column)

        if self.value is not None:
            f.space()
            self.value.dump_evaluate_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Yield_Expression_V1 @{}:{} {!r}>',
                       self.line_number, self.column, self.value)


def create_Tree_Yield_Expression_V1(line_number, column, value):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_expression(value)

    return Tree_Yield_Expression_V1(line_number, column, value)
