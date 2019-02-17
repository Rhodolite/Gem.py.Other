#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Index_V1 - Implementation of `Tree_Index_Clause`, Version 1.
#
#       Copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression


#
#   Tree: Ellipses Index, Version 1
#
class Tree_Ellipses_Index_V1(object):
    #
    #   implements Tree_Index_Clause
    #
    __slots__ = (())


    #
    #   Interface Tree_Index_Clause
    #
    if __debug__:
        is_tree_index_clause = True


    @staticmethod
    def dump_index_clause_tokens(f):
        f.write('...')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree_Ellipses_Index_V1>'


def create_Tree_Ellipses_Index_V1():
    return Tree_Ellipses_Index_V1()


tree_ellipses_index_v1 = create_Tree_Ellipses_Index_V1()


#
#   Tree: Extended Slice Index, Version 1
#
class Tree_Extended_Slice_Index_V1(object):
    #
    #   implements Tree_Index_Clause
    #
    __slots__ = ((
        'many',                         #   NativeList of Tree_Index_Clause
    ))


    #
    #   Private
    #
    def __init__(self, many):
        self.many = many


    #
    #   Interface Tree_Index_Clause
    #
    if __debug__:
        is_tree_index_clause = True


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
        return arrange('<Tree_Extended_Slice_Index_V1 {!r}>', self.many)


def create_Tree_Extended_Slice_Index_V1(many):
    assert fact_is_full_native_list(many)

    return Tree_Extended_Slice_Index_V1(many)


#
#   Tree: Simple Index, Version 1
#
class Tree_Simple_Index_V1(object):
    #
    #   implements Tree_Index_Clause
    #
    __slots__ = ((
        'value',                        #   Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, value):
        self.value = value


    #
    #   Interface Tree_Index_Clause
    #
    if __debug__:
        is_tree_index_clause = True


    def dump_index_clause_tokens(self, f):
        f.write('<simple-index ')
        self.value.dump_evaluate_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Simple_Index_V1 {!r}>', self.value)


def create_Tree_Simple_Index_V1(value):
    assert fact_is_tree_expression(value)

    return Tree_Simple_Index_V1(value)


#
#   Tree: Slice Index, Version 1
#
#   NOTE ON PYTHON PARSING:
#
#       The following two examples are slightly different:
#
#           a[1:2]          #   `step` is `None`
#           a[1:2:]         #   `step` is a `Tree_Name` (with the name being `None`).
#
#       The second `:` can be detected by whether the value of `step` is `None`, or in fact a `Tree_Name` (with the name `None`).
#
class Tree_Slice_Index_V1(object):
    #
    #   implements Tree_Index_Clause
    #
    __slots__ = ((
        'lower',                        #   None | Tree_Expression
        'upper',                        #   None | Tree_Expression
        'step',                         #   None | Tree_Expression
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
    if __debug__:
        is_tree_index_clause = True


    def dump_index_clause_tokens(self, f):
        lower = self.lower
        upper = self.upper
        step  = self.step

        f.write('<slice-index ')

        if lower is not None:
            lower.dump_evaluate_tokens(f)
            f.space()

        f.write(':')

        if upper is not None:
            f.space()
            upper.dump_evaluate_tokens(f)

        if step is not None:
            if upper is not None:
                f.space()

            f.write(': ')
            step.dump_evaluate_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Slice_Index_V1 {!r} {!r} {!r}>', self.lower, self.upper, self.step)


def create_Tree_Slice_Index_V1(lower, upper, step):
    assert fact_is__native_none__OR__tree_expression(lower)
    assert fact_is__native_none__OR__tree_expression(upper)
    assert fact_is__native_none__OR__tree_expression(step)

    return Tree_Slice_Index_V1(lower, upper, step)
