#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   percentage__with_considering_0_of_0_as_100(top, bottom):
#       Calcuate `top / bottom` as a percentage with rounding.
#
#       Calculate a percentage without rouding: *ONLY* using integers.
#
#       This avoids the whole quagmire of the unsual behavior of `round` in python.
#
#       NOTE:
#           `top` and `bottom` are used instead of numerator & denominator as they are easier nouns to remember.
#
def percentage__with_considering_0_of_0_as_100(top, bottom):
    assert (type(top)    is int) and (0 <= top <= bottom)
    assert (type(bottom) is int) and (bottom >= 0)

    if bottom is 0:
        return 100

    return ((top * 1000) / bottom + 5) / 10


#
#   Exports
#
__all__ = ((
    'percentage__with_considering_0_of_0_as_100',
))
