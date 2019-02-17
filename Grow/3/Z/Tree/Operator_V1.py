#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  enumeration


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   Z.Tree.Operator_V1 - Implementation of `Tree_Operator`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Tree: Operator, Version 1
#
class Tree_Operator_V1(object):
    __slots__ = ((
        'name',                         #   NativeString
        'operator_token',               #   NativeString
    ))


    def __init__(self, name, operator_token):
        self.name           = name
        self.operator_token = operator_token


    is_tree_operator = True


    def __repr__(self):
        return arrange('<Tree_Operator_V1 {}>', self.operator_token)


    def dump_operator_token(self, f):
        f.write(self.operator_token)


def create_Tree_Operator_V1(name, operator_token):
    assert fact_is_full_native_string(name)
    assert fact_is_full_native_string(operator_token)

    return Tree_Operator_V1(name, operator_token)


tree_add_operator_v1                           = create_Tree_Operator_V1('add',                   '{+}'     )
tree_binary_and_operator_v1                    = create_Tree_Operator_V1('binary-and',            '{&}'     )
tree_binary_exclusive_or_operator_v1           = create_Tree_Operator_V1('binary-exclusive-or',   '{^}'     )
tree_compare_different_operator_v1             = create_Tree_Operator_V1('different',             '{is-not}')
tree_compare_equal_operator_v1                 = create_Tree_Operator_V1('equal',                 '{==}'    )
tree_compare_greater_than_operator_v1          = create_Tree_Operator_V1('greater-than',          '{>}'     )
tree_compare_greater_than_or_equal_operator_v1 = create_Tree_Operator_V1('greater-than-or-equal', '{>=}'    )
tree_compare_identity_operator_v1              = create_Tree_Operator_V1('identity',              '{is}'    )
tree_compare_less_than_operator_v1             = create_Tree_Operator_V1('less-than',             '{<}'     )
tree_compare_less_than_or_equal_operator_v1    = create_Tree_Operator_V1('less-than-or-equal',    '{<=}'    )
tree_compare_not_equal_operator_v1             = create_Tree_Operator_V1('not-equal',             '{!=}'    )
tree_contains_operator_v1                      = create_Tree_Operator_V1('in',                    '{in}'    )
tree_divide_operator_v1                        = create_Tree_Operator_V1('divide',                '{/}'     )
tree_excludes_operator_v1                      = create_Tree_Operator_V1('not-in',                '{not-in}')
tree_floor_divide_operator_v1                  = create_Tree_Operator_V1('floor-divide',          '{//}'    )
tree_invert_operator_v1                        = create_Tree_Operator_V1('invert',                '{~}'     )
tree_left_shift_operator_v1                    = create_Tree_Operator_V1('left-shift',            '{<<}'    )
tree_logical_and_operator_v1                   = create_Tree_Operator_V1('and',                   '{and}'   )
tree_logical_or_operator_v1                    = create_Tree_Operator_V1('or',                    '{or}'    )
tree_modify_subtract_operator_v1               = create_Tree_Operator_V1('modify-subtract',       '{-=}'    )
tree_modulus_operator_v1                       = create_Tree_Operator_V1('modulus',               '{%}'     )
tree_multiply_operator_v1                      = create_Tree_Operator_V1('multiply',              '{*}'     )
tree_negative_operator_v1                      = create_Tree_Operator_V1('negative',              '{-}'     )
tree_not_operator_v1                           = create_Tree_Operator_V1('not',                   '{not}'   )
tree_positive_operator_v1                      = create_Tree_Operator_V1('positive',              '{+}'     )
tree_power_operator_v1                         = create_Tree_Operator_V1('power',                 '{**}'    )
tree_right_shift_operator_v1                   = create_Tree_Operator_V1('right-shift',           '{>>}'    )
tree_subtract_operator_v1                      = create_Tree_Operator_V1('subtract',              '{-}'     )
