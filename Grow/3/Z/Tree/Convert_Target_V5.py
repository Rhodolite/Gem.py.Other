#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Target_V5 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 5.
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


#
#   Differences between Version 2 & Version 5.
#
#       Version 2:
#
#           `convert_store_target_0` returns `None` or `Tree_Target`
#
#       Versions 3..4:
#
#           Do not exist.
#
#       Version 2:
#
#           `convert_store_target_0` returns `None` or `Tree_Target_0`.
#


from    Z.Parser.None                       import  parser_none
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR


#
#   convert_delete_target(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Delete_Target`.
#
def convert_delete_target(z, v):
    convert_delete_target__function = (
            z.map__Native_AbstractSyntaxTree_TARGET__to__convert_delete_target__function[type(v)]
        )

    return convert_delete_target__function(z, v)


#
#   convert_store_target(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_{Delete,Store}_Target`.
#
def convert_store_target(z, v):
    convert_store_target__function = (
            z.map__Native_AbstractSyntaxTree_TARGET__to__convert_store_target__function[type(v)]
        )

    return convert_store_target__function(z, v)


#
#   convert_store_target_0(z, v)
#
#       1.  Convert `None` to a `Tree_Store_Target_0` (specifically to `parser_none`); or
#
#       2.  Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Store_Target_0`.
#
def convert_store_target_0(z, v):
    if v is None:
        return parser_none

    return z.convert_store_target(z, v)


#
#   convert_full_list_of_delete_targets(sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Delete_Target`.
#
convert_full_list_of_delete_targets = (
        produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_delete_target)
    )


#
#   convert_full_list_of_store_targets(sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Store_Target`.
#
convert_full_list_of_store_targets = (
        produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_store_target)
    )
