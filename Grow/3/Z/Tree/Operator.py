#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Operator - Interface to tree classes that represent operators>
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Operator - Interface to tree classes that represent operators.
#
#       interface Tree_Operator
#           method
#               dump_operator_token (f : Build_DumpToken)
#
#           debug
#               is_tree_operator := true
#
class TRAIT_Tree_Operator(object):
    __slots__ = (())


    if __debug__:
        is_tree_operator = True


#
#   USAGE:
#
#       v.dump_oprator_token(f)                     #   Dump the token representing the tree operator to `f`.
#


#
#   USAGE (debug mode):
#
#       v.is_tree_operator                          #   Test if `v` is a tree operator.
#
#       assert fact_is_tree_operator(v)             #   Assert that `v` is a tree operator.
#


#
#   fact_is_tree_operator(v) - Assert that `v` is a tree operator.
#
if __debug__:
    def fact_is_tree_operator(v):
        assert v.is_tree_operator

        return True
