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
from    Capital.Native_String           import  Empty_Native_String
from    Capital.Native_String           import  Full_Native_String
from    Capital.String                  import  TRAIT_Some_String
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Native_String       import  fact_is_empty_native_string
    from    Capital.Native_String       import  fact_is_full_native_string


#
#<methods>
#   common methods of `{Empty,Full}_String_Leaf`.
#
#       As explained in "Capital.Private.String_V5.py" we had to get rid of `Base_String`.
#
#       So instead we just list the [no longer existing] `Base_String` methods, and copy them into
#       `Empty_String_Leaf` and `Full_String_Leaf` below.
#


#
#   Base_String: Interface String
#
@property
def property__Base_String__native_string(self):
    return self
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class Empty_String_Leaf(
        Empty_Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Some_String,
):
    __slots__ = (())


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False
    native_string   = property__Base_String__native_string


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Empty_Native_String`.
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
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Empty_Native_String`
    #       with the same characters.
    #
    @staticmethod
    def python_code():
        return '""'


#
#   method__Full_Native_String__representation - The python implemention of `repr` for `str` (i.e.: `str.__repr__`).
#
method__Full_Native_String__representation = Full_Native_String.__repr__


#
#   Full String - A wrapper around a full native string.
#
class Full_String_Leaf(
        Full_Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Some_String,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL('{}: A Full_String_Leaf may not be {}',
                  "Capital.Private.FullString_V6.Full_String_Leaf.operator new (`__new__`)",
                  'created')


    if __debug__:
        def __init__(self, s):
            FATAL('{}: A Full_String_Leaf may not be {}',
                  "Capital.Private.FullString_V6.Full_String_Leaf.constructor (`__init__`)",
                  'constructed')


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True
    native_string   = property__Base_String__native_string


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
    #           assert __repr__(conjure_some_string('hello')) == "<'hello'>"
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
    #       For now, we just use the `Full_Native_String` representation (i.e: `str.__repr__`).
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
    python_code = method__Full_Native_String__representation


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
