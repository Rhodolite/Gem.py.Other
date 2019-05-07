#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Operator_V2 - Convert Python Abstract Syntax Tree Operators to Tree classes, Version 2
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2          import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


#
#   convert_binary_operator(z, v)
#
#       Convert a `_ast.*` class that represents a binary operator to a `Tree_Operator`.
#
def convert_binary_operator(v):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator[type(v)]


#
#   convert_compare_operator(z, v)
#
#       Convert a `_ast.*` class that represents a compare operator to a `Tree_Operator`.
#
def convert_compare_operator(z, v):
    return z.map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator[type(v)]


#
#   convert_logical_operator(z, v)
#
#       Convert a `_ast.*` class that represents a logical operator to a `Tree_Operator`.
#
def convert_logical_operator(z, v):
    return z.map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator[type(v)]


#
#   convert_modify_operator(z, v)
#
#       Convert a `_ast.*` class that represents a modify operator to a `Tree_Operator`.
#
#       A "modify" operator is an operator is an operator that can appear in a modify statement
#       (i.e.: `+=`, `*=`, etc.).
#
def convert_modify_operator(z, v):
    return z.map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator[type(v)]


#
#   convert_unary_operator(z, v)
#
#       Convert a `_ast.*` class that represents a unary operator to a `Tree_Operator`.
#
def convert_unary_operator(z, v):
    return z.map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator[type(v)]


#
#   convert_full_list_of_compare_operarors
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Operator`.
#
#       Each of the elements must be a compare operator.
#
convert_full_list_of_compare_operators = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_compare_operator)
    )
