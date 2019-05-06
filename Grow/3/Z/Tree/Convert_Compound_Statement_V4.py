#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Compound_Statement_V4 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2, Version 3, and Version 4.
#
#       Version 2:
#
#           Uses `FullNativeList of Tree_Statement` for a suite of statements.
#
#       Version 3:
#
#           Does not exist.
#
#       Version 4:
#
#           Uses `Tree_Suite` for a suite of statements.
#


from    Z.Parser.None                       import  parser_none
from    Z.Tree.Convert_Except_V2            import  convert_full_list_of_except_clauses
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Target               import  convert_none_OR_target
from    Z.Tree.Convert_Target               import  convert_target


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement


#
#   convert_test_statement(z, v, create) - common code for `convert_{if,while}_statement`.
#
def convert_test_statement(z, v, create):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.test)
    assert fact_is_full_native_list                              (v.body)
    assert fact_is_some_native_list                              (v.orelse)

    return create(
               v.lineno,
               v.col_offset,

               convert_expression(v.test),
               convert_suite     (z, v.body),
               convert_suite_0   (z, v.orelse),
           )


#
#   convert_for_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_For_Statement` (i.e.: `_ast.For`) to a `Tree_Extended_For_Statement`.
#
assert Native_AbstractSyntaxTree_For_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_For_Statement._fields     == (('target', 'iter', 'body', 'orelse'))


def convert_for_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET    (v.target)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.iter)
    assert fact_is_full_native_list                              (v.body)
    assert fact_is_some_native_list                              (v.orelse)

    return z.create_Tree_For_Statement(
               v.lineno,
               v.col_offset,

               convert_target    (v.target),
               convert_expression(v.iter),
               convert_suite     (z, v.body),
               convert_suite_0   (z, v.orelse),
           )


#
#   convert_if_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_If_Statement` (i.e.: `_ast.If`) to a `Tree_If_Statement`.
#
assert Native_AbstractSyntaxTree_If_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_If_Statement._fields     == (('test', 'body', 'orelse'))


def convert_if_statement(z, v):
    assert fact_is_convert_zone(z)

    return convert_test_statement(z, v, z.create_Tree_If_Statement)


#
#   convert_try_except_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Try_Except_Statement` (i.e.: `_ast.TryExcept`) to a
#       `Tree_Try_Except_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Except_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Except_Statement._fields     == (('body', 'handlers', 'orelse'))


def convert_try_except_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.body)
    assert fact_is_full_native_list(v.handlers)
    assert fact_is_some_native_list(v.orelse)

    return z.create_Tree_Try_Except_Statement(
               v.lineno,
               v.col_offset,

               convert_suite                      (z, v.body),
               convert_full_list_of_except_clauses(z, v.handlers),
               convert_suite_0                    (z, v.orelse),
           )


#
#   convert_try_finally_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Try_Finally_Statement` (i.e.: `_ast.TryFinally`) to a
#       `Tree_Try_Finally_Statement`.
#
assert Native_AbstractSyntaxTree_Try_Finally_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Try_Finally_Statement._fields     == (('body', 'finalbody'))


def convert_try_finally_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.body)
    assert fact_is_full_native_list(v.finalbody)

    return z.create_Tree_Try_Finally_Statement(
               v.lineno,
               v.col_offset,

               convert_suite(z, v.body),
               convert_suite(z, v.finalbody),
           )


#
#   convert_while_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_While_Statement` (i.e.: `_ast.While`) to a `Tree_While_Statement`.
#
assert Native_AbstractSyntaxTree_While_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_While_Statement._fields     == (('test', 'body', 'orelse'))


def convert_while_statement(z, v):
    assert fact_is_convert_zone(z)

    return convert_test_statement(z, v, z.create_Tree_While_Statement)


#
#   convert_with_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_With_Statement` (i.e.: `_ast.With`) to a `Tree_Extended_With_Statement`.
#
assert Native_AbstractSyntaxTree_With_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_With_Statement._fields     == (('context_expr', 'optional_vars', 'body'))


def convert_with_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                (v.context_expr)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET(v.optional_vars)
    assert fact_is_full_native_list                                              (v.body)

    return z.create_Tree_With_Statement(
               v.lineno,
               v.col_offset,

               convert_expression    (v.context_expr),
               convert_none_OR_target(v.optional_vars),
               convert_suite         (z, v.body),
           )


#
#   convert_suite(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to either:
#
#           1)  a single statement; or
#
#           2)  a `Tree_Suite`.
#
def convert_suite(z, sequence):
    assert fact_is_convert_zone    (z)
    assert fact_is_full_native_list(sequence)

    if len(sequence) == 1:
        return z.convert_statement(z, sequence[0])

    return z.create_Tree_Suite([z.convert_statement(z, v)   for v in sequence])



#
#   convert_suite_0(z, sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to either:
#
#           1)  `parser_none`;
#
#           2)  a single statement; or
#
#           3)  a `Tree_Suite`.
#
def convert_suite_0(z, sequence):
    assert fact_is_convert_zone    (z)
    assert fact_is_some_native_list(sequence)

    total = len(sequence)

    if total == 0:
        return parser_none

    if total == 1:
        return z.convert_statement(z, sequence[0])

    return z.create_Tree_Suite([z.convert_statement(z, v)   for v in sequence])
