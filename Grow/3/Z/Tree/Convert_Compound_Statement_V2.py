#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Compound_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Uses `FullNativeList of Tree_Statement` for a suite of statements.
#
#       Version 2:
#
#           Uses `Tree_Suite` for a suite of statements.
#


from    Capital.Core                        import  trace
from    Z.Parser.None                       import  parser_none
from    Z.Tree.Compound_Statement_V2        import  create_Tree_For_Statement
from    Z.Tree.Compound_Statement_V2        import  create_Tree_If_Statement
from    Z.Tree.Compound_Statement_V2        import  create_Tree_Try_Except_Statement
from    Z.Tree.Compound_Statement_V2        import  create_Tree_Try_Finally_Statement
from    Z.Tree.Compound_Statement_V2        import  create_Tree_While_Statement
from    Z.Tree.Compound_Statement_V2        import  create_Tree_With_Statement
from    Z.Tree.Convert_Except               import  convert_full_list_of_except_clauses
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Statement            import  convert_statement
from    Z.Tree.Convert_Target               import  convert_none_OR_target
from    Z.Tree.Convert_Target               import  convert_target
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement
from    Z.Tree.Suite                        import  create_Tree_Suite


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET


#
#   convert_test_statement(self, create) - common code for `convert_if_statement` and `convert_while_statement`.
#
def convert_test_statement(self, create):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.test)
    assert fact_is_full_native_list                              (self.body)
    assert fact_is_some_native_list                              (self.orelse)

    return create(
               self.lineno,
               self.col_offset,

               convert_expression(self.test),
               convert_suite     (self.body),
               convert_suite_0   (self.orelse),
           )


#
#   convert_for_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_For_Statement` (i.e.: `_ast.For`) to a `Tree_Extended_For_Statement`.
#
assert Native_AbstractSyntaxTree_For_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_For_Statement._fields     == (('target', 'iter', 'body', 'orelse'))


def convert_for_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET    (self.target)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.iter)
    assert fact_is_full_native_list                              (self.body)
    assert fact_is_some_native_list                              (self.orelse)

    return create_Tree_For_Statement(
               self.lineno,
               self.col_offset,

               convert_target    (self.target),
               convert_expression(self.iter),
               convert_suite     (self.body),
               convert_suite_0   (self.orelse),
           )


#
#   convert_if_statement
#
#       Convert a `Native_AbstractSyntaxTree_If_Statement` (i.e.: `_ast.If`) to a `Tree_If_Statement`.
#
assert Native_AbstractSyntaxTree_If_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Statement._fields     == (('test', 'body', 'orelse'))


def convert_if_statement(self):
    return convert_test_statement(self, create_Tree_If_Statement)


#
#   convert_try_except_statement
#
#       Convert a `Native_AbstractSyntaxTree_Try_Except_Statement` (i.e.: `_ast.TryExcept`) to a
#       `Tree_Try_Except_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Except_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Except_Statement._fields     == (('body', 'handlers', 'orelse'))


def convert_try_except_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list(self.body)
    assert fact_is_full_native_list(self.handlers)
    assert fact_is_some_native_list(self.orelse)

    return create_Tree_Try_Except_Statement(
               self.lineno,
               self.col_offset,

               convert_suite                      (self.body),
               convert_full_list_of_except_clauses(self.handlers),
               convert_suite_0                    (self.orelse),
           )


#
#   convert_try_finally_statement
#
#       Convert a `Native_AbstractSyntaxTree_Try_Finally_Statement` (i.e.: `_ast.TryFinally`) to a
#       `Tree_Try_Finally_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Finally_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Finally_Statement._fields     == (('body', 'finalbody'))


def convert_try_finally_statement(self):
    if 0:
        #
        #   Copy this disabled code into a new convert method, to trace the attributes & fields and help write the new
        #   method.
        #
        #   This code was used to write most of the convert methods in the "Z/Test/Convert_*.py" files :)
        #
        function_name = 'convert_try_finally_statement'

        trace('{}:              {!r}', function_name, self)
        trace('{}._attributes:  {!r}', function_name, self._attributes)
        trace('{}._fields:      {!r}', function_name, self._fields)

        trace('{}.lineno        {!r}', function_name, self.lineno)
        trace('{}.col_offset    {!r}', function_name, self.col_offset)

        trace('{}.body:      {!r}', function_name, self.body)
        trace('{}.finalbody: {!r}', function_name, self.finalbody)

    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list(self.body)
    assert fact_is_full_native_list(self.finalbody)

    return create_Tree_Try_Finally_Statement(
               self.lineno,
               self.col_offset,

               convert_suite(self.body),
               convert_suite(self.finalbody),
           )


#
#   convert_while_statement
#
#       Convert a `Native_AbstractSyntaxTree_While_Statement` (i.e.: `_ast.While`) to a `Tree_While_Statement`.
#
assert Native_AbstractSyntaxTree_While_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_While_Statement._fields     == (('test', 'body', 'orelse'))


def convert_while_statement(self):
    return convert_test_statement(self, create_Tree_While_Statement)


#
#   convert_with_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_With_Statement` (i.e.: `_ast.With`) to a `Tree_Extended_With_Statement`.
#
assert Native_AbstractSyntaxTree_With_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_With_Statement._fields     == (('context_expr', 'optional_vars', 'body'))


def convert_with_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                (self.context_expr)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET(self.optional_vars)
    assert fact_is_full_native_list                                              (self.body)

    return create_Tree_With_Statement(
               self.lineno,
               self.col_offset,

               convert_expression    (self.context_expr),
               convert_none_OR_target(self.optional_vars),
               convert_suite         (self.body),
           )



#
#   convert_suite(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to either:
#
#           1)  a single statement; or
#           2)  a `Tree_Suite`.
#
def convert_suite(sequence):
    assert fact_is_full_native_list(sequence)

    if len(sequence) == 1:
        return convert_statement(sequence[0])

    return create_Tree_Suite([convert_statement(v)   for v in sequence])



#
#   convert_suite_0(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to either:
#
#           1)  `parser_none`;
#           2)  a single statement; or
#           3)  a `Tree_Suite`.
#
def convert_suite_0(sequence):
    assert fact_is_some_native_list(sequence)

    total = len(sequence)

    if total == 0:
        return parser_none

    if total == 1:
        return convert_statement(sequence[0])

    return create_Tree_Suite([convert_statement(v)   for v in sequence])
