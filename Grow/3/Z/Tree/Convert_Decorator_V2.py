#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Decorator_V2 - Convert Python Abstract Syntax Tree Decorators to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__list__OF__Native_AbstractSyntaxTree_STAR


#
#   convert_decorator(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) to a `Tree_Value_Expression`.
#
#   CURRENT:
#
#       For now (since this is a 1-1 translation of `_ast`) a decorator is simply a `Tree_Value_Expression`.
#
#       Hence, all we do is call `z.convert_value_expression`.
#
#   FUTURE:
#
#       We will have a special class for a decorator.
#
def convert_decorator(z, v):
    return z.convert_value_expression(z, v)


#
#   convert_list_of_decorators(z, v)
#
#       Convert some `Native_List of Native_AbstractSyntaxTree_Decorator` (i.e.: `list of _ast.decorator`) to a
#       `Native_List of Tree_Decorator`.
#
convert_list_of_decorators = produce__convert__list__OF__Native_AbstractSyntaxTree_STAR(convert_decorator)
