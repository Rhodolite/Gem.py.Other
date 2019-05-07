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


#
#   The rest of the files refer to a `Tree_Name`, this means:
#
#       1)  `Tree_Name_Version_1`, or
#
#       2)  `Tree_Name_Version_4`
#
#   as determined by `name_version` (see "Z.Tree.Convert_Zone.py" for `name_version`).
#


#
#   interface Tree_Name_Version_1
#       documentation
#           Interface to tree classes that represent names.
#
#       extends Tree_Delete_Target,
#               Tree_Expression,
#               Tree_Parameter,
#               Tree_Store_Target
#
#   NOTE:
#       `Tree_Name_Version_1` is used if `1 <= name_version <= 3` (see "Z.Tree.Convert_Zone.py" for `name_version`).
#


#
#   interface Tree_Name_Version_4
#       documentation
#           Interface to tree classes that represent names.
#
#   NOTE:
#       `Tree_Name_Version_4` is used if `name_version == 4` (see "Z.Tree.Convert_Zone.py" for `name_version`).
#
