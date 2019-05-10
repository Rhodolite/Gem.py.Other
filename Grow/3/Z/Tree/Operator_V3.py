#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Operator_V3 - Implementation of `Tree_Operator`, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1, Version 2, and Version 3.
#
#       Version 1:
#
#           One class per operator (so as to do a 1-1 emulation of `_ast`).
#
#       Version 2:
#
#           Does not exist.
#
#       Version 3:
#
#           A single enumeration named `Tree_Operator_Enumeration`.
#
#           See "Z.Tree.Context_V3.py" for an explanation of "enumeration".
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  enumeration
from    Capital.String                  import  conjure_full_string
from    Z.Tree.Operator                 import  TRAIT_Tree_Operator


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string


#
#   Tree: Operator Enumeration
#
@enumeration
class Tree_Operator_Enumeration(
        TRAIT_Tree_Operator,
):
    __slots__ = ((
        'operator_token',               #   Full_String
    ))


    #
    #   Private
    #
    def __init__(self, operator_token):
        self.operator_token = operator_token


    #
    #   Interface Tree_Operator
    #
    def dump_operator_token(self, f):
        f.write(self.operator_token.native_string_subclass)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Operator_Enumeration {}>', self.operator_token)




#
#   create_TOE(name, operator_token) - Create a `Tree_Operator_Enumeration`.
#
#       The `name` argument is ignored -- is just exists for documentation purposes.
#
@creator
def create_TOE(name, operator_token):
    assert fact_is_full_native_string(name)
    assert fact_is_full_native_string(operator_token)

    return Tree_Operator_Enumeration(
               conjure_full_string(operator_token),
           )


TOE = Tree_Operator_Enumeration


TOE.tree_add_operator                           = create_TOE('Tree_Add_Operator',                           '{+}'     )
TOE.tree_binary_and_operator                    = create_TOE('Tree_Binary_And_Operator',                    '{&}'     )
TOE.tree_binary_exclusive_or_operator           = create_TOE('Tree_Binary_Exclusive_Or_Operator',           '{^}'     )
TOE.tree_compare_different_operator             = create_TOE('Tree_Compare_Different_Operator',             '{is-not}')
TOE.tree_compare_equal_operator                 = create_TOE('Tree_Compare_Equal_Operator',                 '{==}'    )
TOE.tree_compare_greater_than_operator          = create_TOE('Tree_Compare_Greater_Than_Operator',          '{>}'     )
TOE.tree_compare_greater_than_or_equal_operator = create_TOE('Tree_Compare_Greater_Than_Or_Equal_Operator', '{>=}'    )
TOE.tree_compare_identity_operator              = create_TOE('Tree_Compare_Identity_Operator',              '{is}'    )
TOE.tree_compare_less_than_operator             = create_TOE('Tree_Compare_Less_Than_Operator',             '{<}'     )
TOE.tree_compare_less_than_or_equal_operator    = create_TOE('Tree_Compare_Less_Than_Or_Equal_Operator',    '{<=}'    )
TOE.tree_compare_not_equal_operator             = create_TOE('Tree_Compare_Not_Equal_Operator',             '{!=}'    )
TOE.tree_contains_operator                      = create_TOE('Tree_Contains_Operator',                      '{in}'    )
TOE.tree_divide_operator                        = create_TOE('Tree_Divide_Operator',                        '{/}'     )
TOE.tree_excludes_operator                      = create_TOE('Tree_Excludes_Operator',                      '{not-in}')
TOE.tree_floor_divide_operator                  = create_TOE('Tree_Floor_Divide_Operator',                  '{//}'    )
TOE.tree_invert_operator                        = create_TOE('Tree_Invert_Operator',                        '{~}'     )
TOE.tree_left_shift_operator                    = create_TOE('Tree_Left_Shift_Operator',                    '{<<}'    )
TOE.tree_logical_and_operator                   = create_TOE('Tree_Logical_And_Operator',                   '{and}'   )
TOE.tree_logical_or_operator                    = create_TOE('Tree_Logical_Or_Operator',                    '{or}'    )
TOE.tree_modulus_operator                       = create_TOE('Tree_Modulus_Operator',                       '{%}'     )
TOE.tree_multiply_operator                      = create_TOE('Tree_Multiply_Operator',                      '{*}'     )
TOE.tree_negative_operator                      = create_TOE('Tree_Negative_Operator',                      '{-}'     )
TOE.tree_not_operator                           = create_TOE('Tree_Not_Operator',                           '{not}'   )
TOE.tree_positive_operator                      = create_TOE('Tree_Positive_Operator',                      '{+}'     )
TOE.tree_power_operator                         = create_TOE('Tree_Power_Operator',                         '{**}'    )
TOE.tree_right_shift_operator                   = create_TOE('Tree_Right_Shift_Operator',                   '{>>}'    )
TOE.tree_subtract_operator                      = create_TOE('Tree_Subtract_Operator',                      '{-}'     )


del TOE, create_TOE
