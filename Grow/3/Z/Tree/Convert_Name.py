#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Name - Convert Python Abstract Syntax Tree Expressions to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Import the version of tree names we want to use.
#
from    Z.Tree.Global                   import  tree_globals


name_version = tree_globals.name_version


if name_version == 1:
    from    Z.Tree.Convert_Name_V1      import  convert_name_expression
    from    Z.Tree.Convert_Name_V1      import  convert_name_parameter
elif name_version == 2:
    from    Z.Tree.Convert_Name_V2      import  convert_name_expression
    from    Z.Tree.Convert_Name_V2      import  convert_name_parameter
elif name_version == 3:
    from    Z.Tree.Convert_Name_V3      import  convert_name_expression
    from    Z.Tree.Convert_Name_V3      import  convert_name_parameter
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Name.py: unknown tree name version: {!r}', name_version)
