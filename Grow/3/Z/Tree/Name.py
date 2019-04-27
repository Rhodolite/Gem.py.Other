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
