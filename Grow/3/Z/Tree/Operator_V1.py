#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Operator_V1 - Implementation of `Tree_Operator`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Some_String             import  conjure_some_string
from    Z.Tree.Operator                 import  TRAIT_Tree_Operator


#
#   Create_TOE(MetaName, operator_token)
#
#       Create a class with the name [in the parameter] `MetaName`:
#
#           With a `.dump_operator_token` that writes [the value in the parameter] `operator_token`.
#
#       Then return a singleton of that class
#
#   Example:
#
#       Given the call `Create_TOE("Add", "{+}")
#
#   It will create the following class:
#
#       #
#       #   Tree: Add Operator
#       #
#       class Tree_Add_Operator(
#               TRAIT_Tree_Operator,
#       ):
#           __slots__ = (())
#
#
#           #
#           #  Interface Tree_Operator
#           #
#           @staticmethod
#           def dump_operator_token(f):
#               f.write('+')                    #   This is `operator` in the code below.
#
#
#           @staticmethod
#           def __repr__(f):
#               return '<Tree_Add_Operator>'    #   This is `portrait` in the code below.
#
#   Then return a singleton of that class.
#
@creator
def create_TOE(MetaName, operator_token):
    operator = conjure_some_string(operator_token)
    portrait = arrange('<{}>', MetaName)


    #
    #   Tree: MetaName Operator
    #
    class X_Operator(
            TRAIT_Tree_Operator,
    ):
        __slots__ = (())


        #
        #  Interface Tree_Operator
        #
        @staticmethod
        def dump_operator_token(f):
            f.write(operator.native_string)


        @staticmethod
        def __repr__(f):
            return portrait


    #
    #   Rename class `X_Operator` to have the name [in the parameter] `MetaName`
    #
    X_Operator.__name__ = MetaName


    return X_Operator()


tree_add_operator                           = create_TOE('Tree_Add_Operator',                           '{+}'     )
tree_binary_and_operator                    = create_TOE('Tree_Binary_And_Operator',                    '{&}'     )
tree_binary_exclusive_or_operator           = create_TOE('Tree_Binary_Exclusive_Or_Operator',           '{^}'     )
tree_compare_different_operator             = create_TOE('Tree_Compare_Different_Operator',             '{is-not}')
tree_compare_equal_operator                 = create_TOE('Tree_Compare_Equal_Operator',                 '{==}'    )
tree_compare_greater_than_operator          = create_TOE('Tree_Compare_Greater_Than_Operator',          '{>}'     )
tree_compare_greater_than_or_equal_operator = create_TOE('Tree_Compare_Greater_Than_Or_Equal_Operator', '{>=}'    )
tree_compare_identity_operator              = create_TOE('Tree_Compare_Identity_Operator',              '{is}'    )
tree_compare_less_than_operator             = create_TOE('Tree_Compare_Less_Than_Operator',             '{<}'     )
tree_compare_less_than_or_equal_operator    = create_TOE('Tree_Compare_Less_Than_Or_Equal_Operator',    '{<=}'    )
tree_compare_not_equal_operator             = create_TOE('Tree_Compare_Not_Equal_Operator',             '{!=}'    )
tree_contains_operator                      = create_TOE('Tree_Contains_Operator',                      '{in}'    )
tree_divide_operator                        = create_TOE('Tree_Divide_Operator',                        '{/}'     )
tree_excludes_operator                      = create_TOE('Tree_Excludes_Operator',                      '{not.in}')
tree_floor_divide_operator                  = create_TOE('Tree_Floor_Divide_Operator',                  '{//}'    )
tree_invert_operator                        = create_TOE('Tree_Invert_Operator',                        '{~}'     )
tree_left_shift_operator                    = create_TOE('Tree_Left_Shift_Operator',                    '{<<}'    )
tree_logical_and_operator                   = create_TOE('Tree_Logical_And_Operator',                   '{and}'   )
tree_logical_or_operator                    = create_TOE('Tree_Logical_Or_Operator',                    '{or}'    )
tree_modulus_operator                       = create_TOE('Tree_Modulus_Operator',                       '{%}'     )
tree_multiply_operator                      = create_TOE('Tree_Multiply_Operator',                      '{*}'     )
tree_negative_operator                      = create_TOE('Tree_Negative_Operator',                      '{-}'     )
tree_not_operator                           = create_TOE('Tree_Not_Operator',                           '{not}'   )
tree_positive_operator                      = create_TOE('Tree_Positive_Operator',                      '{+}'     )
tree_power_operator                         = create_TOE('Tree_Power_Operator',                         '{**}'    )
tree_right_shift_operator                   = create_TOE('Tree_Right_Shift_Operator',                   '{>>}'    )
tree_subtract_operator                      = create_TOE('Tree_Subtract_Operator',                      '{-}'     )



del create_TOE
