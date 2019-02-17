#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Decorator - Convert Python Abstract Syntax Tree Decorators to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Expression           import  convert_expression


if __debug__:
    from    Capital.Fact                    import  fact_is_some_native_list


#
#   convert_decorator
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) to a `Tree_Expression`.
#
#   CURRENT:
#
#       For now (since this is a 1-1 translation of `_ast`) a decorator is simply a `Tree_Expresion`.
#
#       Hence, all we do is call `convert_expression`.
#
#   FUTURE:
#
#       We will have a special class for a decorator.
#
def convert_decorator(self):
    return convert_expression(self)


#
#   convert_some_list_of_decorators
#
#       Convert some `NativeList of Native_AbstractSyntaxTree_Decorator` (i.e.: `list of _ast.decorator`) to a
#       `NativeList of Tree_Decorator`.
#
def convert_some_list_of_decorators(sequence):
    assert fact_is_some_native_list(sequence)

    return [convert_decorator(v)   for v in sequence]
