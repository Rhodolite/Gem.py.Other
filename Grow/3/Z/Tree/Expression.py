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
#           Interface to tree classes that represent value expressions.
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
#   interface Tree_Value_Expression_0
#       documentation
#           Interface to `parser_none` or tree classes that represent value expressions.
#
#       attribute
#           has_tree_value_expression : Boolean
#
#       if has_tree_value_expression:
#           implements Tree_Value_Expression
#
#       debug
#           is_tree_value_expression_0 := true
#
class TRAIT_Tree_Value_Expression_0(object):
    __slots__ = (())


    has_tree_value_expression = True


    if __debug__:
        is_tree_value_expression_0 = True


#
#   USAGE:
#
#       v.is_tree_value_expression                  #   Test if `v` is a `Tree_Value_Expression`.
#
#       v.is_tree_value_expression_0                #   Test if `v` is a `Tree_Value_Expression_0`.
#
#       v.dump_value_expression_tokens(f)           #   Dump the tokens representing the `Tree_Value_Expression` to `f`.
#
#       assert fact_is__native_none__OR__tree_value_expression(v)
#                                                   #   Assert that `v` is either `None` or a tree value expression.
#
#       assert fact_is_tree_value_expression(v)     #   Assert that `v` is a `Tree_Value_Expression`.
#
#       assert fact_is_tree_value_expression_0(v)   #   Assert that `v` is a `Tree_Value_Expression_0`.
#


#
#   fact_is__native_none__OR__tree_value_expression(v)
#
#       Assert that `v` is either `None` or a `Tree_Value_Expression`.
#
if __debug__:
    def fact_is__native_none__OR__tree_value_expression(v):
        if v is None:
            return True

        assert v.is_tree_value_expression

        return True


#
#   fact_is_tree_value_expression(v) - Assert that `v` is a `Tree_Value_Expression`.
#
if __debug__:
    def fact_is_tree_value_expression(v):
        assert v.is_tree_value_expression

        return True


#
#   fact_is_tree_value_expression_0(v) - Assert that `v` is a `Tree_Value_Expression_0`.
#
if __debug__:
    def fact_is_tree_value_expression_0(v):
        assert v.is_tree_value_expression_0

        return True
