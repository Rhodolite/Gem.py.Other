#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Complex_V1 - Private implementation of the public `Complex` Interface, Version 1.
#
#       `Complex`es are Unique.
#


from    Capital.Complex                         import  TRAIT_Complex
from    Capital.Core                            import  arrange
from    Capital.Core                            import  creator
from    Capital.Core                            import  export
from    Capital.Maybe_Temporary                 import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Complex                  import  Native_Complex
from    Capital.Number                          import  TRAIT_Number
from    Capital.Private.Produce_ConjureComplex  import  produce_conjure_complex


if __debug__:
    from    Capital.Cannot                      import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot                      import  raise__CANNOT__create__ERROR


#
#   method__Native_Complex__representation
#
#       The python implemention of `repr` for `Native_Complex` (i.e.: `complex.__repr__`).
#
method__Native_Complex__representation = Native_Complex.__repr__


#
#   Complex [Leaf] - A wrapper around a native complex (i.e.: `complex`).
#
class Complex_Leaf(
        Native_Complex,
        TRAIT_Complex,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Number,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Complex
    #
    @property
    def native_complex_subclass(self):
        return self



    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Complex`.
    #


    #
    #   .__repr__() - Return the representation of a `Complex`
    #
    def __repr__(self):
        return arrange('<{}>', method__Native_Complex__representation(self))


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Complex`
    #       with the same value as the `Native_Complex` that `self` wraps.
    #
    python_code = method__Native_Complex__representation


conjure_complex = produce_conjure_complex(Complex_Leaf)


#
#   conjure_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Complex` (i.e.: `complex`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `complex`).
#
export(conjure_complex)
