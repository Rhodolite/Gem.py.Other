#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Expression_V1 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#<order>
#
#   To avoid import loops:
#
#           1)  `convert_expression`,
#
#           2)  `convert_full_list_of_expressions`, and
#
#           3)  `convert_some_list_of_expressions`
#
#   must be defined first, since lots of other modules (that we import) need to import these functions.
#


from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


#
#   convert_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Value_Expression`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_expression(v):
    convert_expression__function = (
            map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function[type(v)]
        )

    return convert_expression__function(v)


#
#   convert_none_OR_expression(v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a
#       `Tree_Value_Expression`.
#
def convert_none_OR_expression(v):
    if v is None:
        return None

    return convert_expression(v)


#
#   convert_full_list_of_expressions(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Value_Expression`.
#
convert_full_list_of_expressions = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#
#   convert_some_list_of_expressions(sequence)
#
#       Convert a `SomeNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `SomeNativeList of Tree_Value_Expression`.
#
convert_some_list_of_expressions = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#</order>


from    Z.Tree.Convert_Attribute_V1             import  convert_attribute_expression
from    Z.Tree.Convert_Many_V1                  import  convert_list_expression
from    Z.Tree.Convert_Many_V1                  import  convert_tuple_expression
from    Z.Tree.Convert_Name_V1                  import  convert_name_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_backquote_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_binary_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_call_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_compare_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_generator_comprehension
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_if_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_lambda_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_list_comprehension
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_logical_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_map_comprehension
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_map_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_number
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_set_comprehension
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_set_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_string
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_unary_expression
from    Z.Tree.Convert_Specific_Expression_V1   import  convert_yield_expression
from    Z.Tree.Convert_Subscript_V1             import  convert_subscript_expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Backquote_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Binary_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Call_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Generator_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_If_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Lambda_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_List_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Logical_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Map_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Number
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Set_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Set_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_String
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Yield_Expression


#
#   USED BY: convert_expression (at top of file).
#
#   map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_expression" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function = {
        Native_AbstractSyntaxTree_Attribute_Expression    : convert_attribute_expression,
        Native_AbstractSyntaxTree_Backquote_Expression    : convert_backquote_expression,
        Native_AbstractSyntaxTree_Binary_Expression       : convert_binary_expression,
        Native_AbstractSyntaxTree_Call_Expression         : convert_call_expression,
        Native_AbstractSyntaxTree_Compare_Expression      : convert_compare_expression,
        Native_AbstractSyntaxTree_Generator_Comprehension : convert_generator_comprehension,
        Native_AbstractSyntaxTree_If_Expression           : convert_if_expression,
        Native_AbstractSyntaxTree_Lambda_Expression       : convert_lambda_expression,
        Native_AbstractSyntaxTree_List_Comprehension      : convert_list_comprehension,
        Native_AbstractSyntaxTree_List_Expression         : convert_list_expression,
        Native_AbstractSyntaxTree_Logical_Expression      : convert_logical_expression,
        Native_AbstractSyntaxTree_Map_Comprehension       : convert_map_comprehension,
        Native_AbstractSyntaxTree_Map_Expression          : convert_map_expression,
        Native_AbstractSyntaxTree_Name                    : convert_name_expression,
        Native_AbstractSyntaxTree_Number                  : convert_number,
        Native_AbstractSyntaxTree_Set_Comprehension       : convert_set_comprehension,
        Native_AbstractSyntaxTree_Set_Expression          : convert_set_expression,
        Native_AbstractSyntaxTree_String                  : convert_string,
        Native_AbstractSyntaxTree_Subscript_Expression    : convert_subscript_expression,
        Native_AbstractSyntaxTree_Tuple_Expression        : convert_tuple_expression,
        Native_AbstractSyntaxTree_Unary_Expression        : convert_unary_expression,
        Native_AbstractSyntaxTree_Yield_Expression        : convert_yield_expression,
    }