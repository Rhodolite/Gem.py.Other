#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Expression - Interface to tree classes that represent expressions.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Value_Expression
#       documentation
#           Interface to tree classes that represent expressions.
#
#       method
#           dump_value_expression_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_value_expression := true
#
class TRAIT_Tree_Value_Expression(object):
    __slots__ = (())


    if __debug__:
        is_tree_value_expression = True


#
#   USAGE:
#
#       v.is_tree_value_expression              #   Test if `v` is a tree expression.
#
#       v.dump_value_expression_tokens(f)       #   Dump the tokens representing the tree expression to `f`.
#
#       assert fact_is__native_none__OR__tree_value_expression(v)
#                                               #   Assert that `v` is either `None` or a tree value expression.
#
#       assert fact_is_tree_value_expression(v) #   Assert that `v` is a tree value expression.
#


#
#   fact_is__native_none__OR__tree_value_expression(v)
#
#       Assert that `v` is either `None` or a tree value expression.
#
if __debug__:
    def fact_is__native_none__OR__tree_value_expression(v):
        if v is None:
            return True

        assert v.is_tree_value_expression

        return True


#
#   fact_is_tree_value_expression(v) - Assert that `v` is a tree value expression.
#
if __debug__:
    def fact_is_tree_value_expression(v):
        assert v.is_tree_value_expression

        return True
