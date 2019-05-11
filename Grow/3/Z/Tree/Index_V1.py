#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Index - Implementation of `Tree_Index_Clause`, Version 1.
#
#       Copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Index                    import  TRAIT_Tree_Index_Clause


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression


#
#   Tree: Ellipses Index
#
class Tree_Ellipses_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = (())


    #
    #   Interface Tree_Index_Clause
    #
    @staticmethod
    def dump_index_clause_tokens(f):
        f.write('...')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree_Ellipses_Index>'


@creator
def create_Tree_Ellipses_Index():
    return Tree_Ellipses_Index()


tree_ellipses_index = create_Tree_Ellipses_Index()


#
#   Tree: Extended Slice Index
#
class Tree_Extended_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'many',                         #   Full_Native_List of Tree_Index_Clause
    ))


    #
    #   Private
    #
    def __init__(self, many):
        self.many = many


    #
    #   Interface Tree_Index_Clause
    #
    def dump_index_clause_tokens(self, f):
        first = True

        f.write('<extended-slice-index ')

        for v in self.many:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_index_clause_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Extended_Slice_Index {!r}>', self.many)


@creator
def create_Tree_Extended_Slice_Index(many):
    assert fact_is_full_native_list(many)

    return Tree_Extended_Slice_Index(many)


#
#   Tree: Simple Index
#
class Tree_Simple_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, value):
        self.value = value


    #
    #   Interface Tree_Index_Clause
    #
    def dump_index_clause_tokens(self, f):
        f.write('<simple-index ')
        self.value.dump_value_expression_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Simple_Index {!r}>', self.value)


@creator
def create_Tree_Simple_Index(value):
    assert fact_is_tree_value_expression(value)

    return Tree_Simple_Index(value)


#
#   Tree: Slice Index
#
#   NOTE ON PYTHON PARSING:
#
#       The following two examples are slightly different:
#
#           a[1:2]          #   `step` is `None`
#           a[1:2:]         #   `step` is a `Tree_Name` (with the name being `None`).
#
#       The second `:` can be detected by whether the value of `step` is `None`, or in fact a `Tree_Name` (with the
#       name `None`).
#
class Tree_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'lower',                        #   None | Tree_Value_Expression
        'upper',                        #   None | Tree_Value_Expression
        'step',                         #   None | Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, lower, upper, step):
        self.lower = lower
        self.upper = upper
        self.step  = step


    #
    #   Interface Tree_Index_Clause
    #
    def dump_index_clause_tokens(self, f):
        lower = self.lower
        upper = self.upper
        step  = self.step

        f.write('<slice-index ')

        if lower is not None:
            lower.dump_value_expression_tokens(f)
            f.space()

        f.write(':')

        if upper is not None:
            f.space()
            upper.dump_value_expression_tokens(f)

        if step is not None:
            if upper is not None:
                f.space()

            f.write(': ')
            step.dump_value_expression_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Slice_Index {!r} {!r} {!r}>', self.lower, self.upper, self.step)


@creator
def create_Tree_Slice_Index(lower, upper, step):
    assert fact_is__native_none__OR__tree_value_expression(lower)
    assert fact_is__native_none__OR__tree_value_expression(upper)
    assert fact_is__native_none__OR__tree_value_expression(step)

    return Tree_Slice_Index(lower, upper, step)
