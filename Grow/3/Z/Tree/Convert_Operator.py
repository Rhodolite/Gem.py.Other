#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Operator - Convert Python Abstract Syntax Tree Operators to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Add_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Binary_And_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Different_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Greater_Than_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Greater_Than_Or_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Identity_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Less_Than_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Less_Than_Or_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Compare_Not_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Contains_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Divide_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Excludes_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Floor_Divide_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Invert_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Left_Shift_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Logical_And_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Logical_Or_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Modulus_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Multiply_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Negative_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Not_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Positive_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Power_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Right_Shift_Operator
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Subtract_Operator
from    Z.Tree.Operator                         import  tree_add_operator
from    Z.Tree.Operator                         import  tree_binary_and_operator
from    Z.Tree.Operator                         import  tree_binary_exclusive_or_operator
from    Z.Tree.Operator                         import  tree_compare_different_operator
from    Z.Tree.Operator                         import  tree_compare_equal_operator
from    Z.Tree.Operator                         import  tree_compare_greater_than_operator
from    Z.Tree.Operator                         import  tree_compare_greater_than_or_equal_operator
from    Z.Tree.Operator                         import  tree_compare_identity_operator
from    Z.Tree.Operator                         import  tree_compare_less_than_operator
from    Z.Tree.Operator                         import  tree_compare_less_than_or_equal_operator
from    Z.Tree.Operator                         import  tree_compare_not_equal_operator
from    Z.Tree.Operator                         import  tree_contains_operator
from    Z.Tree.Operator                         import  tree_divide_operator
from    Z.Tree.Operator                         import  tree_excludes_operator
from    Z.Tree.Operator                         import  tree_floor_divide_operator
from    Z.Tree.Operator                         import  tree_invert_operator
from    Z.Tree.Operator                         import  tree_left_shift_operator
from    Z.Tree.Operator                         import  tree_logical_and_operator
from    Z.Tree.Operator                         import  tree_logical_or_operator
from    Z.Tree.Operator                         import  tree_modulus_operator
from    Z.Tree.Operator                         import  tree_multiply_operator
from    Z.Tree.Operator                         import  tree_negative_operator
from    Z.Tree.Operator                         import  tree_not_operator
from    Z.Tree.Operator                         import  tree_positive_operator
from    Z.Tree.Operator                         import  tree_power_operator
from    Z.Tree.Operator                         import  tree_right_shift_operator
from    Z.Tree.Operator                         import  tree_subtract_operator
from    Z.Tree.Produce_Convert_List_V1          import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list


#
#   assert_no_operator_fields(map)
#
#       Assert that all the keys of `map` have empty `._attribute` and `._fields` members.
#
if __debug__:
    def assert_no_operator_fields(map):
        for k in map:
            assert k._attributes == (())
            assert k._fields     == (())


#
#   convert_binary_operator
#
#       Convert a `_ast.*` class that represents a binary operator to a `Tree_Operator`.
#
map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator = {
        Native_AbstractSyntaxTree_Add_Operator                 : tree_add_operator,
        Native_AbstractSyntaxTree_Binary_And_Operator          : tree_binary_and_operator,
        Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator : tree_binary_exclusive_or_operator,
        Native_AbstractSyntaxTree_Divide_Operator              : tree_divide_operator,
        Native_AbstractSyntaxTree_Floor_Divide_Operator        : tree_floor_divide_operator,
        Native_AbstractSyntaxTree_Left_Shift_Operator          : tree_left_shift_operator,
        Native_AbstractSyntaxTree_Modulus_Operator             : tree_modulus_operator,
        Native_AbstractSyntaxTree_Multiply_Operator            : tree_multiply_operator,
        Native_AbstractSyntaxTree_Power_Operator               : tree_power_operator,
        Native_AbstractSyntaxTree_Right_Shift_Operator         : tree_right_shift_operator,
        Native_AbstractSyntaxTree_Subtract_Operator            : tree_subtract_operator,
    }


if __debug__:
    assert_no_operator_fields(map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator)


def convert_binary_operator(self):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator[type(self)]


#
#   convert_compare_operator
#
#       Convert a `_ast.*` class that represents a compare operator to a `Tree_Operator`.
#
map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator = {
        Native_AbstractSyntaxTree_Compare_Different_Operator             : tree_compare_different_operator,
        Native_AbstractSyntaxTree_Compare_Equal_Operator                 : tree_compare_equal_operator,
        Native_AbstractSyntaxTree_Compare_Greater_Than_Or_Equal_Operator : tree_compare_greater_than_or_equal_operator,
        Native_AbstractSyntaxTree_Compare_Greater_Than_Operator          : tree_compare_greater_than_operator,
        Native_AbstractSyntaxTree_Compare_Identity_Operator              : tree_compare_identity_operator,
        Native_AbstractSyntaxTree_Compare_Less_Than_Or_Equal_Operator    : tree_compare_less_than_or_equal_operator,
        Native_AbstractSyntaxTree_Compare_Less_Than_Operator             : tree_compare_less_than_operator,
        Native_AbstractSyntaxTree_Compare_Not_Equal_Operator             : tree_compare_not_equal_operator,
        Native_AbstractSyntaxTree_Contains_Operator                      : tree_contains_operator,
        Native_AbstractSyntaxTree_Excludes_Operator                      : tree_excludes_operator,
    }


if __debug__:
    assert_no_operator_fields(map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator)


def convert_compare_operator(self):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator[type(self)]


#
#   convert_logical_operator
#
#       Convert a `_ast.*` class that represents a logical operator to a `Tree_Operator`.
#
map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator = {
        Native_AbstractSyntaxTree_Logical_And_Operator : tree_logical_and_operator,
        Native_AbstractSyntaxTree_Logical_Or_Operator  : tree_logical_or_operator,
    }


if __debug__:
    assert_no_operator_fields(map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator)


def convert_logical_operator(self):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator[type(self)]


#
#   convert_modify_operator
#
#       Convert a `_ast.*` class that represents a modify operator to a `Tree_Operator`.
#
#       A "modify" operator is an operator is an operator that can appear in a modify statement
#       (i.e.: `+=`, `*=`, etc.).
#
#       The following conversions are preformed:
#
#           python type                                     converted to
#           -----------                                     ------------
#           Native_AbstractSyntaxTree_Subtract_Operator     tree_subtract_operator
#
map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator = {
        Native_AbstractSyntaxTree_Subtract_Operator : tree_subtract_operator,
    }


if __debug__:
    assert_no_operator_fields(map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator)


def convert_modify_operator(self):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator[type(self)]


#
#   convert_unary_operator
#
#       Convert a `_ast.*` class that represents a unary operator to a `Tree_Operator`.
#
map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator = {
        Native_AbstractSyntaxTree_Invert_Operator   : tree_invert_operator,
        Native_AbstractSyntaxTree_Negative_Operator : tree_negative_operator,
        Native_AbstractSyntaxTree_Positive_Operator : tree_positive_operator,
        Native_AbstractSyntaxTree_Not_Operator      : tree_not_operator,
    }


if __debug__:
    assert_no_operator_fields(map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator)


def convert_unary_operator(self):
    return map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator[type(self)]


#
#   convert_full_list_of_compare_operarors
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Operator`.
#
#       Each of the elements must be a compare operator.
#
convert_full_list_of_compare_operators = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_compare_operator)
    )
