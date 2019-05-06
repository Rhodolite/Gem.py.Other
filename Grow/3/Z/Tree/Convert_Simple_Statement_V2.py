#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Simple_Statement_V2 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All convert functions take a `z` parameter of type `Convert_Zone.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Alias                import  convert_full_list_of_module_aliases
from    Z.Tree.Convert_Alias                import  convert_full_list_of_symbol_aliases
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_full_list_of_expressions
from    Z.Tree.Convert_Expression           import  convert_none_OR_expression
from    Z.Tree.Convert_Operator             import  convert_modify_operator
from    Z.Tree.Convert_Target               import  convert_full_list_of_targets
from    Z.Tree.Convert_Target               import  convert_target
from    Z.Tree.Convert_Zone                 import  convert_zone
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement
from    Z.Tree.Statement                    import  create_Tree_Assert_Statement
from    Z.Tree.Statement                    import  create_Tree_Assign_Statement
from    Z.Tree.Statement                    import  create_Tree_Break_Statement
from    Z.Tree.Statement                    import  create_Tree_Continue_Statement
from    Z.Tree.Statement                    import  create_Tree_Delete_Statement
from    Z.Tree.Statement                    import  create_Tree_Execute_Statement
from    Z.Tree.Statement                    import  create_Tree_Expression_Statement
from    Z.Tree.Statement                    import  create_Tree_From_Import_Statement
from    Z.Tree.Statement                    import  create_Tree_Global_Statement
from    Z.Tree.Statement                    import  create_Tree_Import_Statement
from    Z.Tree.Statement                    import  create_Tree_Modify_Statement
from    Z.Tree.Statement                    import  create_Tree_Pass_Statement
from    Z.Tree.Statement                    import  create_Tree_Print_Statement
from    Z.Tree.Statement                    import  create_Tree_Raise_Statement
from    Z.Tree.Statement                    import  create_Tree_Return_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_native_boolean
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
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
               convert_full_list_of_symbol_aliases(convert_zone, self.names),
               self.level,
           )



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

               convert_full_list_of_module_aliases(convert_zone, self.names),
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
