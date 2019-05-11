#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_Integer_V1 - Temporary Integer Implementation, Version 1.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_Integer          import  Native_Integer
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_native_non_zero_integer


#
#   method__Native_Integer__representation
#
#       The python implemention of `repr` for `Native_Integer` (i.e.: `int.__repr__`).
#
method__Native_Integer__representation = Native_Integer.__repr__


#
#   Temporary_Integer - Temporary Integer Implementation
#
class Temporary_Integer(
        Native_Integer,
        TRAIT_Maybe_Temporary_0,
        #
        #   NOTE:
        #       Does *NOT* implement the `Integer` interface.
        #
        #       This is *NOT* a `Integer`, but a temporary element (that *MIGHT* be transformed to a `Integer`).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.Integer_V7.{Negative,Positive}_Integer_Leaf`
    #   (which an instance of this class is transformed to).
    #
    __slots__ = (())


    #
    #   Interface Maybe_Temporary
    #
   #@replace
    definitively_not_temporary = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Temporary_Integer {!r}>', method__Native_Integer__representation(self))


@export
@creator
def create_temporary_integer(v):
    assert fact_is_native_non_zero_integer(v)

    return Temporary_Integer(v)
