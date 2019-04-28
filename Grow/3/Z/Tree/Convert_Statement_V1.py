#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Alias                import  convert_full_list_of_alias_clauses
from    Z.Tree.Convert_Decorator            import  convert_some_list_of_decorators
from    Z.Tree.Convert_Except               import  convert_full_list_of_except_clauses
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_full_list_of_expressions
from    Z.Tree.Convert_Expression           import  convert_none_OR_expression
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Operator             import  convert_modify_operator
from    Z.Tree.Convert_Parameter            import  convert_parameters_all
from    Z.Tree.Convert_Target               import  convert_full_list_of_targets
from    Z.Tree.Convert_Target               import  convert_none_OR_target
from    Z.Tree.Convert_Target               import  convert_target
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement
from    Z.Tree.Statement                    import  create_Tree_Assert_Statement
from    Z.Tree.Statement                    import  create_Tree_Assign_Statement
from    Z.Tree.Statement                    import  create_Tree_Break_Statement
from    Z.Tree.Statement                    import  create_Tree_Class_Definition
from    Z.Tree.Statement                    import  create_Tree_Continue_Statement
from    Z.Tree.Statement                    import  create_Tree_Delete_Statement
from    Z.Tree.Statement                    import  create_Tree_Execute_Statement
from    Z.Tree.Statement                    import  create_Tree_Expression_Statement
from    Z.Tree.Statement                    import  create_Tree_For_Statement
from    Z.Tree.Statement                    import  create_Tree_From_Import_Statement
from    Z.Tree.Statement                    import  create_Tree_Function_Definition
from    Z.Tree.Statement                    import  create_Tree_Global_Statement
from    Z.Tree.Statement                    import  create_Tree_If_Statement
from    Z.Tree.Statement                    import  create_Tree_Import_Statement
from    Z.Tree.Statement                    import  create_Tree_Modify_Statement
from    Z.Tree.Statement                    import  create_Tree_Pass_Statement
from    Z.Tree.Statement                    import  create_Tree_Print_Statement
from    Z.Tree.Statement                    import  create_Tree_Raise_Statement
from    Z.Tree.Statement                    import  create_Tree_Return_Statement
from    Z.Tree.Statement                    import  create_Tree_Try_Except_Statement
from    Z.Tree.Statement                    import  create_Tree_Try_Finally_Statement
from    Z.Tree.Statement                    import  create_Tree_While_Statement
from    Z.Tree.Statement                    import  create_Tree_With_Statement
from    Z.Tree.Suite                        import  create_Tree_Suite


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_native_boolean
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET


#
#   create_keyword_statement(self)
#
#       Common code for `convert_break_statement`, `convert_continue_statement` and `convert_pass_statement`.
#
def convert_keyword_statement(self, create):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    return create(self.lineno, self.col_offset)



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
#   convert_assert_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_Assert_Statement` (i.e.: `_ast.Assert`) to a `Tree_Assert_Statement`.
#
assert Native_AbstractSyntaxTree_Assert_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assert_Statement._fields     == (('test', 'msg'))


def convert_assert_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (self.test)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.msg)

    return create_Tree_Assert_Statement(
               self.lineno,
               self.col_offset,

               convert_expression        (self.test),
               convert_none_OR_expression(self.msg),
           )


#
#   convert_assign_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_Assign_Statement` (i.e.: `_ast.Assign`) to a `Tree_Assign`.
#
assert Native_AbstractSyntaxTree_Assign_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assign_Statement._fields     == (('targets', 'value'))


def convert_assign_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list                              (self.targets)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Assign_Statement(
               self.lineno,
               self.col_offset,

               convert_full_list_of_targets(self.targets),
               convert_expression          (self.value),
           )


#
#   convert_break_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_Break_Statement` (i.e.: `_ast.Break`) to a `Tree_Break_Statement`.
#
assert Native_AbstractSyntaxTree_Break_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Break_Statement._fields     == (())


def convert_break_statement(self):
    return convert_keyword_statement(self, create_Tree_Break_Statement)


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
#   convert_continue_statement
#
#       Convert a `Native_AbstractSyntaxTree_Continue_Statement` (i.e.: `_ast.Continue`) to a
#       `Tree_Continue_Statement`.
#
assert Native_AbstractSyntaxTree_Continue_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Continue_Statement._fields     == (())


def convert_continue_statement(self):
    return convert_keyword_statement(self, create_Tree_Continue_Statement)


#
#   convert_delete_statement(self)
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Statement` (i.e.: `_ast.Delete`) to a `Tree_Extended_Delete_Statement`.
#
assert Native_AbstractSyntaxTree_Delete_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Delete_Statement._fields     == (('targets',))


def convert_delete_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list(self.targets)

    return create_Tree_Delete_Statement(
               self.lineno,
               self.col_offset,

               convert_full_list_of_targets(self.targets),
           )


#
#   convert_execute_statement
#
#       Convert a `Native_AbstractSyntaxTree_Execute_Statement` (i.e.: `_ast.Exec`) to a
#       `Tree_Execute_Statement`.
#
assert Native_AbstractSyntaxTree_Execute_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Execute_Statement._fields     == (('body', 'globals', 'locals'))


def convert_execute_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (self.body)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.globals)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.locals)

    return create_Tree_Execute_Statement(
               self.lineno,
               self.col_offset,

               convert_expression        (self.body),
               convert_none_OR_expression(self.globals),
               convert_none_OR_expression(self.locals),
           )


#
#   convert_expression_statement
#
#       Convert a `Native_AbstractSyntaxTree_Expression_Statement` (i.e.: `_ast.Expr`) to a
#       `Tree_Expression_Statement`.
#
assert Native_AbstractSyntaxTree_Expression_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Expression_Statement._fields     == (('value',))


def convert_expression_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Expression_Statement(
               self.lineno,
               self.col_offset,

               convert_expression(self.value),
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
#   convert_global_statement
#
#       Convert a `Native_AbstractSyntaxTree_Global_Statement` (i.e.: `_ast.Global`) to a
#       `Tree_Global_Statement`.
#
assert Native_AbstractSyntaxTree_Global_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Global_Statement._fields     == (('names',))


def convert_global_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list(self.names)

    return create_Tree_Global_Statement(
               self.lineno,
               self.col_offset,

               self.names,
           )


#
#   convert_from_import_statement
#
#       Convert a `Native_AbstractSyntaxTree_From_Import_Statement` (i.e.: `_ast.ImportFrom`) to a
#       `Tree_From_Import_Statement`.
#
assert Native_AbstractSyntaxTree_From_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_From_Import_Statement._fields     == (('module', 'names', 'level'))


def convert_from_import_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string (self.module)
    assert fact_is_full_native_list   (self.names)
    assert fact_is_substantial_integer(self.level)

    return create_Tree_From_Import_Statement(
               self.lineno,
               self.col_offset,

               self.module,
               convert_full_list_of_alias_clauses(self.names),
               self.level,
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
#   convert_import_statement
#
#       Convert a `Native_AbstractSyntaxTree_Import_Statement` (i.e.: `_ast.Import`) to a `Tree_Import_Statement`.
#
assert Native_AbstractSyntaxTree_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Import_Statement._fields     == (('names',))


def convert_import_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_list(self.names)

    return create_Tree_Import_Statement(
               self.lineno,
               self.col_offset,

               convert_full_list_of_alias_clauses(self.names),
           )


#
#   convert_modify_statement
#
#       Convert a `Native_AbstractSyntaxTree_Modify_Statement` (i.e.: `_ast.AugAssign`) to a `Tree_Modify_Statement`.
#
assert Native_AbstractSyntaxTree_Modify_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Modify_Statement._fields     == (('target', 'op', 'value'))


def convert_modify_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET         (self.target)
    assert fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR(self.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (self.value)

    return create_Tree_Modify_Statement(
               self.lineno,
               self.col_offset,

               convert_target         (self.target),
               convert_modify_operator(self.op),
               convert_expression     (self.value),
           )


#
#   convert_pass_statement
#
#       Convert a `Native_AbstractSyntaxTree_Pass_Statement` (i.e.: `_ast.Pass`) to a `Tree_Pass_Statement`.
#
assert Native_AbstractSyntaxTree_Pass_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Pass_Statement._fields     == (())


def convert_pass_statement(self):
    return convert_keyword_statement(self, create_Tree_Pass_Statement)


#
#   convert_print_statement
#
#       Convert a `Native_AbstractSyntaxTree_Print_Statement` (i.e.: `_ast.Print`) to a `Tree_Print_Statement`.
#
assert Native_AbstractSyntaxTree_Print_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Print_Statement._fields     == (('dest', 'values', 'nl'))


def convert_print_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.dest)
    assert fact_is_full_native_list                                                  (self.values)
    assert fact_is_native_boolean                                                    (self.nl)

    return create_Tree_Print_Statement(
               self.lineno,
               self.col_offset,

               convert_none_OR_expression      (self.dest),
               convert_full_list_of_expressions(self.values),
               self.nl,
           )
    
           
#
#   convert_raise_statement
#
#       Convert a `Native_AbstractSyntaxTree_Raise_Statement` (i.e.: `_ast.Raise`) to a `Tree_Raise_Statement`.
#
assert Native_AbstractSyntaxTree_Raise_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Raise_Statement._fields     == (('type', 'inst', 'tback'))


def convert_raise_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.inst)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.tback)

    return create_Tree_Raise_Statement(
               self.lineno,
               self.col_offset,

               convert_none_OR_expression(self.type),
               convert_none_OR_expression(self.inst),
               convert_none_OR_expression(self.tback),
           )


#
#   convert_return_statement
#
#       Convert a `Native_AbstractSyntaxTree_Return_Statement` (i.e.: `_ast.Return`) to a `Tree_Return_Statement`.
#
assert Native_AbstractSyntaxTree_Return_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Return_Statement._fields     == (('value',))


def convert_return_statement(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Return_Statement(
               self.lineno,
               self.col_offset,

               convert_none_OR_expression(self.value),
           )


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
