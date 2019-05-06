#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Statement - Convert Python Abstract Syntax Tree Statements to Tree classes
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Import the version of tree statements we want to use.
#
from    Z.Parser.Global                 import  parser_globals


statement_version = parser_globals.statement_version


if statement_version == 1:
    from    Z.Tree.Convert_Statement_V1             import  convert_statement
    from    Z.Tree.Convert_Statement_V1             import  convert_full_list_of_statements
    from    Z.Tree.Convert_Statement_V1             import  convert_some_list_of_statements
elif statement_version in ((2, 3, 4)):
    from    Z.Tree.Convert_Statement_V2             import  convert_statement
    from    Z.Tree.Convert_Statement_V2             import  convert_full_list_of_statements
    from    Z.Tree.Convert_Statement_V2             import  convert_some_list_of_statements
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Statement.py: unknown tree statement version: {}', statement_version)
