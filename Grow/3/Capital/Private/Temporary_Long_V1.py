#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_Long_V1 - Temporary Long Implementation, Version 1.
#
#       This is pretty much a copy of "Capital/Private/Temporary_Integer_V1.py" -- See that file for comments.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Long             import  Native_Long
from    Capital.System                  import  is_python_2


if __debug__:
    from    Capital.Fact                import  fact_is__non_zero__ANY_native_INTEGRAL_number


#
#   `Native_Long` is only implemented in Python 2.*
#
#   Hence, Inteface `Long` is also only implemented in Python 2.*
#
assert is_python_2


#
#   method__Native_Long__representation
#
#       The python implemention of `repr` for `Native_Long` (i.e.: `long.__repr__`).
#
method__Native_Long__representation = Native_Long.__repr__


#
#   Temporary_Long - Temporary Long Implementation
#
class Temporary_Long(
        Native_Long,
        TRAIT_Maybe_Temporary_0,
        #
        #   NOTE:
        #       Does *NOT* implement the `Long` interface.
        #
        #       This is *NOT* a `Long`, but a temporary element (that *MIGHT* be transformed to a `Long`).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.Long_V7.{Negative,Positive}_Long_Leaf`
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
        return arrange('<Temporary_Long {!r}>', method__Native_Long__representation(self))


@export
@creator
def create_temporary_long(v):
    assert fact_is__non_zero__ANY_native_INTEGRAL_number(v)

    return Temporary_Long(v)
