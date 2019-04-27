#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name - Interface to tree classes that represent a name (in a context).
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Explanation:
#
#       A Tree name is used to access a symbol (i.e.: a variable).#
#
#       It has a context that explains how it is accessed.
#
#   Furthur Explanation:
#
#       See "Z.Tree.Context" for an explanation of contexts.
#
#       To quote from there:
#
#           A "tree context" is used to indicate the context of another tree node:
#
#               A `Tree_Name` is used to access a symbol (i.e: a variable), it has a context that is either:
#
#                   `delete`            (to delete the symbol),
#                   `load`              (to get the value of the symbol),
#                   `parameter`         (to define a function parameter), or
#                   `store`             (to save a new value to the symbol).
#
#       (again see "Z.Tree.Context" for more details).
#


#
#   interface Tree_Name
#       documentation
#           Interface to tree classes that represent names.
#
#       extends Tree_Delete_Target,
#               Tree_Expression,
#               Tree_Parameter,
#               Tree_Store_Target
#


#
#   Import the version of tree names we want to use.
#
from    Z.Tree.Global                   import  tree_globals


version = tree_globals.name_version


if version == '1':
    from    Z.Tree.Name_V1              import  create_Tree_Name_V1     as  create_Tree_Name
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Name.py: unknown tree name version: {!r}', version)
