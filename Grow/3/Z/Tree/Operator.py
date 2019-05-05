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
#   Import the version of tree operators we want to use
#
from    Z.Parser.Global                 import  parser_globals


operator_version = parser_globals.operator_version


if operator_version == 1:
    from    Z.Tree.Operator_V1          import  tree_add_operator
    from    Z.Tree.Operator_V1          import  tree_binary_and_operator
    from    Z.Tree.Operator_V1          import  tree_binary_exclusive_or_operator
    from    Z.Tree.Operator_V1          import  tree_compare_different_operator
    from    Z.Tree.Operator_V1          import  tree_compare_equal_operator
    from    Z.Tree.Operator_V1          import  tree_compare_greater_than_operator
    from    Z.Tree.Operator_V1          import  tree_compare_greater_than_or_equal_operator
    from    Z.Tree.Operator_V1          import  tree_compare_identity_operator
    from    Z.Tree.Operator_V1          import  tree_compare_less_than_operator
    from    Z.Tree.Operator_V1          import  tree_compare_less_than_or_equal_operator
    from    Z.Tree.Operator_V1          import  tree_compare_not_equal_operator
    from    Z.Tree.Operator_V1          import  tree_contains_operator
    from    Z.Tree.Operator_V1          import  tree_divide_operator
    from    Z.Tree.Operator_V1          import  tree_excludes_operator
    from    Z.Tree.Operator_V1          import  tree_floor_divide_operator
    from    Z.Tree.Operator_V1          import  tree_invert_operator
    from    Z.Tree.Operator_V1          import  tree_left_shift_operator
    from    Z.Tree.Operator_V1          import  tree_logical_and_operator
    from    Z.Tree.Operator_V1          import  tree_logical_or_operator
    from    Z.Tree.Operator_V1          import  tree_modulus_operator
    from    Z.Tree.Operator_V1          import  tree_multiply_operator
    from    Z.Tree.Operator_V1          import  tree_negative_operator
    from    Z.Tree.Operator_V1          import  tree_not_operator
    from    Z.Tree.Operator_V1          import  tree_positive_operator
    from    Z.Tree.Operator_V1          import  tree_power_operator
    from    Z.Tree.Operator_V1          import  tree_right_shift_operator
    from    Z.Tree.Operator_V1          import  tree_subtract_operator
elif operator_version == 2:
    from    Z.Tree.Operator_V2          import  Tree_Operator_Enumeration   as  TOE

    tree_add_operator                           = TOE.tree_add_operator
    tree_binary_and_operator                    = TOE.tree_binary_and_operator
    tree_binary_exclusive_or_operator           = TOE.tree_binary_exclusive_or_operator
    tree_compare_different_operator             = TOE.tree_compare_different_operator
    tree_compare_equal_operator                 = TOE.tree_compare_equal_operator
    tree_compare_greater_than_operator          = TOE.tree_compare_greater_than_operator
    tree_compare_greater_than_or_equal_operator = TOE.tree_compare_greater_than_or_equal_operator
    tree_compare_identity_operator              = TOE.tree_compare_identity_operator
    tree_compare_less_than_operator             = TOE.tree_compare_less_than_operator
    tree_compare_less_than_or_equal_operator    = TOE.tree_compare_less_than_or_equal_operator
    tree_compare_not_equal_operator             = TOE.tree_compare_not_equal_operator
    tree_contains_operator                      = TOE.tree_contains_operator
    tree_divide_operator                        = TOE.tree_divide_operator
    tree_excludes_operator                      = TOE.tree_excludes_operator
    tree_floor_divide_operator                  = TOE.tree_floor_divide_operator
    tree_invert_operator                        = TOE.tree_invert_operator
    tree_left_shift_operator                    = TOE.tree_left_shift_operator
    tree_logical_and_operator                   = TOE.tree_logical_and_operator
    tree_logical_or_operator                    = TOE.tree_logical_or_operator
    tree_modulus_operator                       = TOE.tree_modulus_operator
    tree_multiply_operator                      = TOE.tree_multiply_operator
    tree_negative_operator                      = TOE.tree_negative_operator
    tree_not_operator                           = TOE.tree_not_operator
    tree_positive_operator                      = TOE.tree_positive_operator
    tree_power_operator                         = TOE.tree_power_operator
    tree_right_shift_operator                   = TOE.tree_right_shift_operator
    tree_subtract_operator                      = TOE.tree_subtract_operator

    del TOE
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Operator.py: not relevant for tree operator version: {}', operator_version)


#
#   fact_is_tree_operator(v) - Assert that `v` is a tree operator.
#
if __debug__:
    def fact_is_tree_operator(v):
        assert v.is_tree_operator

        return True
