#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Integer_V8 - Private implementation of the public "Integer" Interfaces, Version 8.
#
#       Integers are Unique.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Integer                 import  TRAIT_Contrary_Integer
from    Capital.Integer                 import  TRAIT_Integer
from    Capital.Integer                 import  TRAIT_Keen_Integer
from    Capital.Integer                 import  TRAIT_Negative_Integer
from    Capital.Integer                 import  TRAIT_Positive_Integer
from    Capital.Integer                 import  TRAIT_Zero
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Cannot              import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot              import  raise__CANNOT__create__ERROR


#
#   Common Methods
#


@property
def property__Integer__native_integer_subclass(self):
    return self



#
#   Zero [Leaf] Integer - A singleton wrapper around `0`.
#
class Zero_Leaf(
        Some_Native_Integer,
        TRAIT_Contrary_Integer,
        TRAIT_Keen_Integer,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Integer,
        TRAIT_Zero,
):
    __slots__ = (())


    #
    #   Interface Some_Integer
    #
    is_negative_integer = False
    is_positive_integer = False


    native_integer_subclass = property__Integer__native_integer_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Some_Native_Integer`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Integer`
    #
    @staticmethod
    def __repr__():
        return '<0>'


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Integer`
    #       with the same value as the `Some_Native_Integer` that `self` wraps.
    #
    @staticmethod
    def python_code():
        return '0'


#
#   method__Native_String__representation - The python implemention of `repr` for `Native_String` (i.e.: `str.__repr__`).
#
method__Native_String__representation = Some_Native_Integer.__repr__


#
#   Negative Integer [Leaf] - A wrapper around a negative native integer (i.e.: `int` with a value less than 0).
#
class Negative_Integer_Leaf(
        Some_Native_Integer,
        TRAIT_Contrary_Integer,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Negative_Integer,
        TRAIT_Integer,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface String
    #
    is_empty_string = False


    native_string_subclass = property__String__native_string_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `str`.
    #   .__len__()                    - Inherited from `str`.
    #


    #
    #   .__repr__() - Return the representation of a `String`
    #
    #   CURRENT
    #
    #       Surround the the result of `.python_code` with angle brackets.
    #
    #       Example:
    #
    #           assert __repr__(conjure_string('hello')) == "<'hello'>"
    #
    #   FUTURE
    #
    #       See `.python_code` for an explanation of how `.python_code` will behave differently in the future.
    #
    def __repr__(self):
        return arrange('<{}>', self.python_code())


    #
    #   .python_code()
    #
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the same
    #       characters.
    #
    #   CURRENT
    #
    #       For now, we just use the `Native_Integer` representation (i.e: `int.__repr__`).
    #
    #   FUTURE:
    #
    #       We will use the function `portray_python_string` which does a really good job of a python
    #       represenation (much more readable than `str.__repr__` when presented with a "raw" string).
    #
    #       However, that code is quite large, so we are not including it for now.
    #
    #       Also, really, we want to code generate the `portray_python_string` ... so will wait until the
    #       code generator can generate that function, before using it.
    #
    python_code = method__Native_Integer__representation


@creator
def create_empty_string(s):
    assert fact_is_empty_native_string(s)

    return Empty_String_Leaf(s)


@export
@creator
def create_full_string(s):
    assert fact_is_full_native_string(interned_s)

    return Full_String_Leaf(s)


empty_string = create_empty_string("")


export(empty_string)
