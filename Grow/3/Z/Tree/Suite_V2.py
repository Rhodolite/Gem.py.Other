#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Suite_V2 - Implementation of `Tree_Suite`, Version 2.
#
#       A `Tree_Suite` is two or more statements (python calls more than one statement a "suite").
#
#       All other tree statements implement themselves *as* *if* they are a "suite" of exactly one statement.
#


#
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           Does not exist.
#
#       Version 2:
#
#           Exists.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  replace
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list


#
#   Tree: Suite
#
class Tree_Suite_Implementation(
        tuple,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Suite
    #
   #@replace
    suite_estimate = 7                  #   `7` is not a very good estimate ...  but good enough ;-)


    @replace
    def dump_suite_tokens(self, f):
        for v in self:
            v.dump_statement_tokens(f)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Suite_Implementation {}>', ','.join(repr(v)    for v in self))


@creator
def create_Tree_Suite(sequence):
    assert fact_is_full_native_list(sequence)

    assert len(sequence) >= 2

    return Tree_Suite_Implementation(sequence)
