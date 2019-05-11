#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_Float_V1 - Temporary Float Implementation, Version 1.
#
#       This is pretty much a copy of "Capital/Private/Temporary_Integer_V1.py" -- See that file for comments.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Float             import  Native_Float


if __debug__:
    from    Capital.Native_Float        import  fact_is__non_zero__native_float


#
#   method__Native_Float__representation
#
#       The python implemention of `repr` for `Native_Float` (i.e.: `float.__repr__`).
#
method__Native_Float__representation = Native_Float.__repr__


#
#   Temporary_Float - Temporary Float Implementation
#
class Temporary_Float(
        Native_Float,
        TRAIT_Maybe_Temporary_0,
        #
        #   NOTE:
        #       Does *NOT* implement the `Float` interface.
        #
        #       This is *NOT* a `Float`, but a temporary element (that *MIGHT* be transformed to a `Float`).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.Float_V7.{Negative,Positive}_Float_Leaf`
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
        return arrange('<Temporary_Float {!r}>', method__Native_Float__representation(self))


@export
@creator
def create_temporary_float(v):
    assert fact_is__non_zero__native_float(v)

    return Temporary_Float(v)
