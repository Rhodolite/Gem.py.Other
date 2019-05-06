#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Definition_V2 - Implementation of tree compound statements, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           1)  Tree Statements implement `Tree_Statement`.
#
#           2)  A           list of statements is stored as `FullNativeList of Tree_Statement`.
#
#           3)  An optional list of statements is stored as `SomeNativeList of Tree_Statement`.
#
#       Version 2:
#
#           1)  Tree Statements implement `Tree_Statement`; and ...
#
#               ... in addition also implement `Tree_Suite`, and `Tree_Suite_0`.
#
#           2)  A           list of statements is stored as `Tree_Suite`.
#
#           3)  An optional list of statements is stored as `Tree_Suite_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Parameter            import  fact_is_tree_parameters_all
    from    Z.Tree.Suite                import  fact_is_tree_suite


#
#   Tree: Class Definition
#
class Tree_Class_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'name',                         #   NativeString
        'bases',                        #   NativeList of Tree_Expression
        'body',                         #   Tree_Statement
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
            self.body.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_evaluate_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        decorator_list = self.decorator_list

        header = arrange('<class-definition @{}:{} {}', self.line_number, self.column, self.name)

        with f.indent_2(header, '>'):
            self._dump_bases_tokens(f, 'bases: {', None)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, '}; body: {',           '}')
            else:
                self._dump_body_tokens     (f, '}; body: {',           None)
                self._dump_decorator_tokens(f, '}; decorator_list: {', '}')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Class_Definition @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.bases, self.body, self.decorator_list)


@creator
def create_Tree_Class_Definition(line_number, column, name, bases, body, decorator_list):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string(name)
    assert fact_is_some_native_list  (bases)
    assert fact_is_tree_suite        (body)
    assert fact_is_some_native_list  (decorator_list)

    return Tree_Class_Definition(line_number, column, name, bases, body, decorator_list)


#
#   Tree: Function Definition
#
class Tree_Function_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'name',                         #   NativeString
        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_List
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
            self.body.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_evaluate_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        decorator_list = self.decorator_list

        header = arrange('<function-definition @{}:{} {}', self.line_number, self.column, self.name)

        with f.indent_2(header, '>'):
            self.parameters.dump_parameter_tokens(f)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, '{',                    '}')
            else:
                self._dump_body_tokens     (f, '{',                    None)
                self._dump_decorator_tokens(f, '}; decorator_list: {', '}')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Function_Definition @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.parameters, self.body, self.decorator_list)


@creator
def create_Tree_Function_Definition(line_number, column, name, parameters, body, decorator_list):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string (name)
    assert fact_is_tree_parameters_all(parameters)
    assert fact_is_tree_suite         (body)
    assert fact_is_some_native_list   (decorator_list)

    return Tree_Function_Definition(line_number, column, name, parameters, body, decorator_list)
