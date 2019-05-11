#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Long_V1 - Private implementation of the public "Long" Interfaces, Version 1.
#
#       Longs are Unique.
#
#       This is pretty much a copy of "Capital/Integer_V1.py" -- See that file for comments.
#


from    Capital.Core                            import  arrange
from    Capital.Core                            import  creator
from    Capital.Core                            import  export
from    Capital.Long                            import  TRAIT_Long
from    Capital.Maybe_Temporary                 import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Long                     import  Native_Long
from    Capital.Private.Produce_ConjureNumber   import  produce_conjure_number_functions
from    Capital.Private.Temporary_Long_V1       import  create_temporary_long
from    Capital.System                          import  is_python_2


if __debug__:
    from    Capital.Cannot                      import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot                      import  raise__CANNOT__create__ERROR
    from    Capital.Fact                        import  fact_is_ANY_native_INTEGRAL_number
    from    Capital.Native_Long                 import  fact_is_zero_native_long


#
#   `Native_Long` is only implemented in Python 2.*
#
#   Hence, Inteface `Long` is also only implemented in Python 2.*
#
assert is_python_2


#
#<methods>
#
#   Common Methods
#


#
#   method__Native_Long__representation
#
#       The python implemention of `repr` for `Native_Long` (i.e.: `long.__repr__`).
#
method__Native_Long__representation = Native_Long.__repr__


def method__Long__operator_representation(self):
    return arrange('<{}>', method__Native_Long__representation(self))


@property
def property__Long__native_long_subclass(self):
    return self


#</methods>


#
#   Zero [Leaf] Long - A singleton wrapper around the `Native_Long` (i.e.: `long`) with a value of `0`.
#
class Zero_Leaf(
        Native_Long,
        #
        #   Implements Contrary_Long
        #
        TRAIT_Long,
        #
        #   Implements Avid_Long
        #
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Zero
        #
):
    __slots__ = (())


    #
    #   Interface Long
    #
    is_avid_long     = True
    is_contrary_long = True
    is_negative_long = False
    is_positive_long = False
    is_zero_long     = True


    native_long_subclass = property__Long__native_long_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Long`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Long`
    #
    __repr__ = method__Long__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Long`
    #       with the same value as the `Native_Long` that `self` wraps.
    #
    python_code = method__Native_Long__representation


#
#   Negative Long [Leaf] - A wrapper around a negative native long (i.e.: `long` with a value less than 0).
#
class Negative_Long_Leaf(
        Native_Long,
        #
        #   Implements Contrary_Long
        #
        TRAIT_Long,
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Negative_Long
        #
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Long
    #
    is_avid_long     = False
    is_contrary_long = True
    is_negative_long = True
    is_positive_long = False
    is_zero_long     = False


    native_long_subclass = property__Long__native_long_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Long`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Long`
    #
    __repr__ = method__Long__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Long`
    #       with the same value as the `Native_Long` that `self` wraps.
    #
    python_code = method__Native_Long__representation



#
#   Positive Long [Leaf] - A wrapper around a positive native long (i.e.: `long` with a value greater than 0).
#
class Positive_Long_Leaf(
        Native_Long,
        TRAIT_Long,
        #
        #   Implements Avid_Long
        #
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Positive_Long
        #
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Long
    #
    is_contrary_long = False
    is_avid_long     = True
    is_negative_long = False
    is_positive_long = True
    is_zero_long     = False


    native_long_subclass = property__Long__native_long_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Long`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Long`
    #
    __repr__ = method__Long__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Long`
    #       with the same value as the `Native_Long` that `self` wraps.
    #
    python_code = method__Native_Long__representation




@creator
def create_zero_long(v):
    assert fact_is_zero_native_long(v)

    return Zero_Leaf(v)


zero_long = create_zero_long(0L)


#
#   zero_long - The singleton `Long` wrapper around the `Native_Long` (i.e.: `long`) with a value of `0`.
#
export(zero_long)


[
    conjure_avid_long,
    conjure_contrary_long,
    conjure_negative_long,
    conjure_long,
    conjure_positive_long,
] = (
        produce_conjure_number_functions(
            number_name             = 'long',
            fact_is_native_number   = fact_is_ANY_native_INTEGRAL_number,
            create_temporary_number = create_temporary_long,
            Negative_Number_Type    = Negative_Long_Leaf,
            Positive_Number_Type    = Positive_Long_Leaf,
            zero_number             = zero_long,
        )
    )


#
#   conjure_avid_long(v) - Conjure a `Avid_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_avid_long)


#
#   conjure_contrary_long(v) - Conjure a `Contrary_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_long)


#
#   conjure_long(v) - Conjure a `Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
export(conjure_long)


#
#   conjure_negative_long(v) - Conjure a `Negative_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and less than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_long)


#
#   conjure_positive_long(v) - Conjure a `Positive_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_long)
