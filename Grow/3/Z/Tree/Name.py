#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name - Interface to tree classes that represent a name.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#
#   Explanation:
#
#       A Tree name is used to access a symbol (i.e.: a variable).
#
#       In Version 1 & 2 implementation, `Tree_Name` has a context that explains how it is accessed.
#
#       In Version 3 implementation, different classes are derived from `Tree_Name` for the different ways they are
#       accessed.
#
#
#   Furthur Explanation:
#
#       See "Z.Tree.Context" for an explanation of contexts.
#
#       To quote from there:
#
#           A "tree context" is used to indicate the context of another tree node:
#
#               A `Tree_Name` (Version 1 & 2 implementation) is used to access a symbol (i.e: a variable), it has a
#               context that is either:
#
#                   `delete`            (to delete the symbol),
#                   `load`              (to get the value of the symbol),
#                   `parameter`         (to define a function parameter), or
#                   `store`             (to save a new value to the symbol).
#
#       (again see "Z.Tree.Context" for more details).
#


#
#   Import the version of tree names we want to use.
#
from    Z.Parser.Global                 import  parser_globals


name_version = parser_globals.name_version


if name_version in ((1, 2)):
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
    pass
elif name_version == 3:
    #
    #   interface Tree_Name
    #       documentation
    #           Interface to tree classes that represent names.
    #
    pass
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Name.py: unknown tree name version: {!r}', name_version)
