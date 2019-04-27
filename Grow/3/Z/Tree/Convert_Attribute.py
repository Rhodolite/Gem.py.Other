#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Attribute - Convert Python Abstract Syntax Tree Expressions to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Import the version of tree names we want to use.
#
from    Z.Tree.Global                   import  tree_globals


target_version = tree_globals.target_version


if target_version == 1:
    from    Z.Tree.Convert_Attribute_V1     import  convert_attribute_expression
elif target_version == 2:
    from    Z.Tree.Convert_Attribute_V2     import  convert_attribute_expression
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Attribute.py: unknown tree target version: {!r}', target_version)
