#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_Complex_V1 - Temporary Complex Implementation, Version 1.
#
#       This is pretty much a copy of "Capital/Private/Temporary_Integer_V1.py" -- See that file for comments.
#
#       NOTE:
#
#           One small difference:
#
#               `Temporary_Integer` does NOT allow the `0` value.
#
#               `Temporary_Complex` does     allow the `0j` value.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Complex          import  Native_Complex


if __debug__:
    from    Capital.Native_Complex      import  fact_is_native_complex


#
#   method__Native_Complex__representation
#
#       The python implemention of `repr` for `Native_Complex` (i.e.: `complex.__repr__`).
#
method__Native_Complex__representation = Native_Complex.__repr__


#
#   Temporary_Complex - Temporary Complex Implementation
#
class Temporary_Complex(
        Native_Complex,
        TRAIT_Maybe_Temporary_0,
        #
        #   NOTE:
        #       Does *NOT* implement the `Complex` interface.
        #
        #       This is *NOT* a `Complex`, but a temporary element (that *MIGHT* be transformed to a `Complex`).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.Complex_V7.{Negative,Positive}_Complex_Leaf`
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
        return arrange('<Temporary_Complex {!r}>', method__Native_Complex__representation(self))


@export
@creator
def create_temporary_complex(v):
    assert fact_is_native_complex(v)

    return Temporary_Complex(v)
