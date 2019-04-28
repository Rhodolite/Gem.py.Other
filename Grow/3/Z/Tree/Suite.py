#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Suite - Implementation of `Tree_Suite`
#
#       A `Tree_Suite` is two or more statements (python calls more than one statement a "suite").
#
#       All other tree statements implement themselves *as* *if* they are a "suite" of exactly one statement.
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list


#
#   Tree: Suite
#
class Tree_Suite(tuple):
    #
    #   implements Tree_Statement,
    #              Tree_Statement_0
    #
    __slots__ = (())


    #
    #   Interface Tree_Statement,
    #             Tree_Statement_0
    #
    if __debug__:
        is_tree_statement   = True
        is_tree_statement_0 = True


    is_tree_statement_none = False
    suite_estimate         = 7          #   `7` is not a very good estimate ...  but good enough ;-)


    def dump_suite_tokens(self, f):
        for v in self:
            v.dump_suite_tokens(f)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Suite {}>', ','.join(repr(v)    for v in self))


def create_Tree_Suite(sequence):
    assert fact_is_full_native_list(sequence)

    assert len(sequence) >= 2

    return Tree_Suite(sequence)
