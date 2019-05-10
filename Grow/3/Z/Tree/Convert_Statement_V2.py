#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Statement_V2 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 2.
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
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   convert_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) instance to an instance of a class that implements
#       `Tree_Statement`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_statement(z, v):
    assert fact_is_convert_zone(z)

    convert_statement_function = (
            z.map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function[type(v)]
        )

    return convert_statement_function(z, v)


#
#   convert_full_list_of_statements(z, sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Statement`.
#
convert_full_list_of_statements = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_statement)


#
#   convert_some_list_of_statements(z, sequence)
#
#       Convert a `Some_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Some_Native_List of Tree_Statement`.
#
convert_some_list_of_statements = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_statement)
