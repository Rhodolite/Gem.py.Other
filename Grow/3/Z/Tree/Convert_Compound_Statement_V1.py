#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Compound_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Class_Definition
from    Z.Tree.Compound_Statement_V1        import  create_Tree_For_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Function_Definition
from    Z.Tree.Compound_Statement_V1        import  create_Tree_If_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Try_Except_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_Try_Finally_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_While_Statement
from    Z.Tree.Compound_Statement_V1        import  create_Tree_With_Statement
from    Z.Tree.Convert_Decorator            import  convert_some_list_of_decorators
from    Z.Tree.Convert_Except               import  convert_full_list_of_except_clauses
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Parameter            import  convert_parameters_all
from    Z.Tree.Convert_Statement            import  convert_full_list_of_statements
from    Z.Tree.Convert_Statement            import  convert_some_list_of_statements
from    Z.Tree.Convert_Target               import  convert_none_OR_target
from    Z.Tree.Convert_Target               import  convert_target
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all
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

               convert_expression             (self.test),
               convert_full_list_of_statements(self.body),
               convert_some_list_of_statements(self.orelse),
           )


#
#   convert_class_definition
#
#       Convert a `Native_AbstractSyntaxTree_Class_Definition` (i.e.: `_ast.ClassDef`) to a `Tree_Class_Definition`.
#
assert Native_AbstractSyntaxTree_Class_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Class_Definition._fields     == (('name', 'bases', 'body', 'decorator_list'))


def convert_class_definition(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string(self.name)
    assert fact_is_some_native_list  (self.bases)
    assert fact_is_full_native_list  (self.body)
    assert fact_is_some_native_list  (self.decorator_list)

    return create_Tree_Class_Definition(
               self.lineno,
               self.col_offset,

               self.name,
               convert_some_list_of_expressions(self.bases),
               convert_full_list_of_statements (self.body),
               convert_some_list_of_decorators (self.decorator_list),
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

               convert_target                 (self.target),
               convert_expression             (self.iter),
               convert_full_list_of_statements(self.body),
               convert_some_list_of_statements(self.orelse),
           )


#
#   convert_function_definition
#
#       Convert a `Native_AbstractSyntaxTree_Function_Definition` (i.e.: `_ast.FunctionDef`) to a
#       `Tree_Function_Definition`.
#
assert Native_AbstractSyntaxTree_Function_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Function_Definition._fields     == (('name', 'args', 'body', 'decorator_list'))


def convert_function_definition(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string                           (self.name)
    assert fact_is__native__abstract_syntax_tree__parameters_all(self.args)
    assert fact_is_full_native_list                             (self.body)
    assert fact_is_some_native_list                             (self.decorator_list)

    return create_Tree_Function_Definition(
               self.lineno,
               self.col_offset,

               self.name,
               convert_parameters_all         (self.args),
               convert_full_list_of_statements(self.body),
               convert_some_list_of_decorators(self.decorator_list),
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

               convert_full_list_of_statements    (self.body),
               convert_full_list_of_except_clauses(self.handlers),
               convert_some_list_of_statements    (self.orelse),
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

               convert_full_list_of_statements(self.body),
               convert_full_list_of_statements(self.finalbody),
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

               convert_expression             (self.context_expr),
               convert_none_OR_target         (self.optional_vars),
               convert_full_list_of_statements(self.body),
           )
