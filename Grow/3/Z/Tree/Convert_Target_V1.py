#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Target_V1 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 1.
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


from    Z.Tree.Convert_Attribute_V1         import  convert_attribute_expression
from    Z.Tree.Convert_Many_V1              import  convert_list_expression
from    Z.Tree.Convert_Many_V1              import  convert_tuple_expression
from    Z.Tree.Convert_Name_V1              import  convert_name_expression
from    Z.Tree.Convert_Subscript_V1         import  convert_subscript_expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR



if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list


#
#   convert_store_target_0(v)
#
#       1.  Convert `None` to `None; OR
#
#       2.  convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Store_Target`.
#
def convert_store_target_0(v):
    if v is None:
        return None

    return convert_target(v)


#
#<convert_target>
#
#   map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_target" function.
#
map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function = {
        Native_AbstractSyntaxTree_Attribute_Expression : convert_attribute_expression,
        Native_AbstractSyntaxTree_List_Expression      : convert_list_expression,
        Native_AbstractSyntaxTree_Name                 : convert_name_expression,
        Native_AbstractSyntaxTree_Subscript_Expression : convert_subscript_expression,
        Native_AbstractSyntaxTree_Tuple_Expression     : convert_tuple_expression,
    }


#
#   convert_target(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_{Delete,Store}_Target`.
#
def convert_target(v):
    convert_target__function = (
            map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function[type(v)]
        )

    return convert_target__function(v)
#</convert_target>


#
#   convert_full_list_of_targets(sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Value_Expression`.
#
#       Each of the expressions must be a target expresion.
#
convert_full_list_of_targets = produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_target)
