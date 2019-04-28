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
from    Z.Tree.Global                   import  tree_globals


version = tree_globals.operator_version


if version == '1':
    from    Z.Tree.Operator_V1          import (
                tree_add_operator_v1                            as  tree_add_operator,
                tree_binary_and_operator_v1                     as  tree_binary_and_operator,
                tree_binary_exclusive_or_operator_v1            as  tree_binary_exclusive_or_operator,
                tree_compare_different_operator_v1              as  tree_compare_different_operator,
                tree_compare_equal_operator_v1                  as  tree_compare_equal_operator,
                tree_compare_greater_than_operator_v1           as  tree_compare_greater_than_operator,
                tree_compare_greater_than_or_equal_operator_v1  as  tree_compare_greater_than_or_equal_operator,
                tree_compare_identity_operator_v1               as  tree_compare_identity_operator,
                tree_compare_less_than_operator_v1              as  tree_compare_less_than_operator,
                tree_compare_less_than_or_equal_operator_v1     as  tree_compare_less_than_or_equal_operator,
                tree_compare_not_equal_operator_v1              as  tree_compare_not_equal_operator,
                tree_contains_operator_v1                       as  tree_contains_operator,
                tree_divide_operator_v1                         as  tree_divide_operator,
                tree_excludes_operator_v1                       as  tree_excludes_operator,
                tree_floor_divide_operator_v1                   as  tree_floor_divide_operator,
                tree_invert_operator_v1                         as  tree_invert_operator,
                tree_left_shift_operator_v1                     as  tree_left_shift_operator,
                tree_logical_and_operator_v1                    as  tree_logical_and_operator,
                tree_logical_or_operator_v1                     as  tree_logical_or_operator,
                tree_modify_subtract_operator_v1                as  tree_modify_subtract_operator,
                tree_modulus_operator_v1                        as  tree_modulus_operator,
                tree_multiply_operator_v1                       as  tree_multiply_operator,
                tree_negative_operator_v1                       as  tree_negative_operator,
                tree_not_operator_v1                            as  tree_not_operator,
                tree_positive_operator_v1                       as  tree_positive_operator,
                tree_power_operator_v1                          as  tree_power_operator,
                tree_right_shift_operator_v1                    as  tree_right_shift_operator,
                tree_subtract_operator_v1                       as  tree_subtract_operator,
            )
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Operator.py: not relevant for tree operator version: {!r}', version)


#
#   fact_is_tree_operator(v) - Assert that `v` is a tree operator.
#
if __debug__:
    def fact_is_tree_operator(v):
        assert v.is_tree_operator

        return True
