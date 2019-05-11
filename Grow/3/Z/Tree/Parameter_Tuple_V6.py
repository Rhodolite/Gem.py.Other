#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_Tuple_V6 - Interface to a tuple of `Parser_Symbol`, Version 6.
#


#
#   Differences between Version 1..6.
#
#       Version 1..5:
#
#           Do not exist.
#
#       Version 6:
#
#           Exists.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  replace
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list


#
#   Tree: Parameter Tuple [Leaf]
#
class Tree_Parameter_Tuple_Leaf(
        tuple,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0
):
    __slots__ = (())


    #
    #   Interface TRAIT_Tree_Parameter_Tuple
    #
   #@replace
    tuple_estimate = 7                  #   `7` is not a very good estimate ...  but good enough ;-)


    def dump_parameter_tuple_tokens(self, f):
        with f.indent_2('<parameter-tuple', '>'):
            for v in self:
                v.dump_parameter_tokens(f)
                f.line(',')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Parameter_Tuple_Leaf {}>', ','.join(repr(v)    for v in self))


@creator
def create_Tree_Parameter_Tuple(sequence):
    assert fact_is_full_native_list(sequence)

    assert len(sequence) >= 2

    return Tree_Parameter_Tuple_Leaf(sequence)
