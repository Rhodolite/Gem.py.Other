#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Float_V1 - Private implementation of the public "Float" Interfaces, Version 1.
#
#       Floats are Unique.
#
#       This is pretty much a copy of "Capital/Integer_V1.py" -- See that file for comments.
#


from    Capital.Core                            import  arrange
from    Capital.Core                            import  creator
from    Capital.Core                            import  export
from    Capital.Float                           import  TRAIT_Float
from    Capital.Maybe_Temporary                 import  TRAIT_Maybe_Temporary_0
from    Capital.Native_Float                    import  Native_Float
from    Capital.Number                          import  TRAIT_Number
from    Capital.Private.Produce_ConjureNumber   import  produce_conjure_number_functions
from    Capital.Private.Temporary_Float_V1      import  create_temporary_float


if __debug__:
    from    Capital.Cannot                      import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot                      import  raise__CANNOT__create__ERROR
    from    Capital.Native_Float                import  fact_is_native_float
    from    Capital.Native_Float                import  fact_is_zero_native_float


#
#<methods>
#
#   Common Methods
#


#
#   method__Native_Float__representation
#
#       The python implemention of `repr` for `Native_Float` (i.e.: `float.__repr__`).
#
method__Native_Float__representation = Native_Float.__repr__


def method__Float__operator_representation(self):
    return arrange('<{}>', method__Native_Float__representation(self))


@property
def property__Float__native_float_subclass(self):
    return self


#</methods>


#
#   Zero [Leaf] Float - A singleton wrapper around the `Native_Float` (i.e.: `float`) with a value of `0`.
#
class Zero_Leaf(
        Native_Float,
        #
        #   Implements Contrary_Float
        #
        TRAIT_Float,
        #
        #   Implements Avid_Float
        #
        TRAIT_Maybe_Temporary_0,
        TRAIT_Number,
        #
        #   Implements Zero
        #
):
    __slots__ = (())


    #
    #   Interface Float
    #
    is_avid_float     = True
    is_contrary_float = True
    is_negative_float = False
    is_positive_float = False
    is_zero_float     = True


    native_float_subclass = property__Float__native_float_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Float`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Float`
    #
    __repr__ = method__Float__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Float`
    #       with the same value as the `Native_Float` that `self` wraps.
    #
    python_code = method__Native_Float__representation


#
#   Negative Float [Leaf] - A wrapper around a negative native float (i.e.: `float` with a value less than 0).
#
class Negative_Float_Leaf(
        Native_Float,
        #
        #   Implements Contrary_Float
        #
        TRAIT_Float,
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Negative_Float
        #
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
    #   Interface Float
    #
    is_avid_float     = False
    is_contrary_float = True
    is_negative_float = True
    is_positive_float = False
    is_zero_float     = False


    native_float_subclass = property__Float__native_float_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Float`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Float`
    #
    __repr__ = method__Float__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Float`
    #       with the same value as the `Native_Float` that `self` wraps.
    #
    python_code = method__Native_Float__representation



#
#   Positive Float [Leaf] - A wrapper around a positive native float (i.e.: `float` with a value greater than 0).
#
class Positive_Float_Leaf(
        Native_Float,
        TRAIT_Float,
        #
        #   Implements Avid_Float
        #
        TRAIT_Maybe_Temporary_0,
        TRAIT_Number,
        #
        #   Implements Positive_Float
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
    #   Interface Float
    #
    is_contrary_float = False
    is_avid_float     = True
    is_negative_float = False
    is_positive_float = True
    is_zero_float     = False


    native_float_subclass = property__Float__native_float_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Float`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Float`
    #
    __repr__ = method__Float__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Float`
    #       with the same value as the `Native_Float` that `self` wraps.
    #
    python_code = method__Native_Float__representation




@creator
def create_zero_float(v):
    assert fact_is_zero_native_float(v)

    return Zero_Leaf(v)


zero_float = create_zero_float(0.0)


#
#   zero_float - The singleton `Float` wrapper around the `Native_Float` (i.e.: `float`) with a value of `0`.
#
export(zero_float)


[
    conjure_avid_float,
    conjure_contrary_float,
    conjure_negative_float,
    conjure_float,
    conjure_positive_float,
] = (
        produce_conjure_number_functions(
            number_name             = 'float',
            fact_is_native_number   = fact_is_native_float,
            create_temporary_number = create_temporary_float,
            Negative_Number_Type    = Negative_Float_Leaf,
            Positive_Number_Type    = Positive_Float_Leaf,
            zero_number             = zero_float,
        )
    )


#
#   conjure_avid_float(v) - Conjure a `Avid_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_avid_float)


#
#   conjure_contrary_float(v) - Conjure a `Contrary_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_float)


#
#   conjure_float(v) - Conjure a `Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
export(conjure_float)


#
#   conjure_negative_float(v) - Conjure a `Negative_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and less than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_float)


#
#   conjure_positive_float(v) - Conjure a `Positive_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_float)
