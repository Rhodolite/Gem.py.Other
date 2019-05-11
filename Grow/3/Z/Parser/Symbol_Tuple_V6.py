#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_Tuple_V6 - Interface to a tuple of `Parser_Symbol`, Version 6.
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
from    Z.Parser.Symbol_Tuple           import  TRAIT_Parser_Symbol_Tuple


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list


#
#   Parser: Symbol Tuple [Leaf]
#
class Parser_Symbol_Tuple_Leaf(
        tuple,
        TRAIT_Parser_Symbol_Tuple,
):
    __slots__ = (())


    #
    #   Interface TRAIT_Parser_Symbol_Tuple
    #
    tuple_estimate = 7                  #   `7` is not a very good estimate ...  but good enough ;-)


    def dump_symbol_tuple_tokens(self, f):
        f.write('<symbol-tuple')

        first = True

        for v in self:
            if first:
                first = False
            else:
                f.write(',')

            f.space()
            v.dump_symbol_token(f)

        f.write('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_Tuple_Leaf {}>', ','.join(repr(v)    for v in self))


@creator
def create_Parser_Symbol_Tuple(sequence):
    assert fact_is_full_native_list(sequence)

    assert len(sequence) >= 2

    return Parser_Symbol_Tuple_Leaf(sequence)
