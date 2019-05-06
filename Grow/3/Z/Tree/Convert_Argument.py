#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Argument_V1 - Convert Python Abstract Syntax Tree [Function] Arguments to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Import the version of tree argument we want to use.
#
from    Z.Parser.Global                 import  parser_globals


argument_version = parser_globals.argument_version


if argument_version == 1:
    from    Z.Tree.Convert_Argument_V1  import  convert_keyword_argument
    from    Z.Tree.Convert_Argument_V1  import  convert_some_list_of_keyword_arguments
elif argument_version == 2:
    from    Z.Tree.Convert_Argument_V2  import  convert_keyword_argument
    from    Z.Tree.Convert_Argument_V2  import  convert_some_list_of_keyword_arguments
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Argument.py: unknown tree argument version: {!r}', argument_version)
