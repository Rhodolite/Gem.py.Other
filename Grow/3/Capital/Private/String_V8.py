#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V8 - Private implementation of the public `String` Interface, Version 8.
#
#       Strings are Unique (always).
#
#       Uniqueness is implemented in "Capital.Private.ConjureString_V6.py" (which uses the interface
#       `Maybe_Temporary` to implement uniqueness).
#


#
#   Difference between Version 7 & Version 8.
#
#       Version 7:
#
#           1)  `Empty_String_Leaf` does not implement `Empty_String`.
#
#           2)  `Full_String_Leaf`  does not implement `Full_String`.
#
#       Version 8:
#
#           1)  `Empty_String_Leaf` implements `Empty_String`.
#
#           2)  `Full_String_Leaf`  implements `Full_String`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0
from    Capital.Native_String           import  Native_String
from    Capital.String                  import  TRAIT_Empty_String
from    Capital.String                  import  TRAIT_Full_String
from    Capital.String                  import  TRAIT_String



if __debug__:
    from    Capital.Cannot              import  raise__CANNOT__create__ERROR
    from    Capital.Cannot              import  raise__CANNOT__construct__ERROR
    from    Capital.Native_String       import  fact_is_empty_native_string
    from    Capital.Native_String       import  fact_is_full_native_string


#
#<methods>
#
#   Common methods of `{Empty,Full}_String_Leaf`.
#


#
#   Base_String: Interface String
#
@property
def property__String__native_string_subclass(self):
    return self
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class Empty_String_Leaf(
        Native_String,
        TRAIT_Empty_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_String,
):
    __slots__ = (())


    #
    #   Interface String
    #
    is_full_string = False


    native_string_subclass = property__String__native_string_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_String`.
    #


    #
    #   .__len__()  - Return the length.
    #
    #       Always returns `0` for an `Empty_String_Leaf`.
    #
    @staticmethod
    def __len__():
        return 0


    #
    #   .__repr__() - Return the representation of a `String`
    #
    @staticmethod
    def __repr__():
        return '<"">'


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_String`
    #       with the same characters.
    #
    @staticmethod
    def python_code():
        return '""'


#
#   method__Native_String__representation - The python implemention of `repr` for `Native_String` (i.e.: `str.__repr__`).
#
method__Native_String__representation = Native_String.__repr__


#
#   Full String - A wrapper around a full native string.
#
class Full_String_Leaf(
        Native_String,
        TRAIT_Full_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_String,
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
    #       For now, we just use the `Native_String` representation (i.e: `str.__repr__`).
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
    python_code = method__Native_String__representation


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
