#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V6 - Private implementation of the public `String` Interface, Version 6.
#
#       Strings are Unique (always).
#
#       Uniqueness is implemented in "Capital.Private.ConjureString_V5.py" (which uses the interface
#       `Maybe_Temporary` to implement uniqueness).
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           1)  Strings are unique (in normal cases).
#
#           2)  Has creator function `create_full_string` for `Full_String_Leaf`.
#
#       Version 6:
#
#           1)  Strings are unique (always).
#
#           2)  Does *NOT* have creator function for `Full_String_Leaf` (since `Full_String_Leaf` cannot be created,
#               but only transformed from a `Capital.Private.Temporary_String_V6.Temporary_String`).
#
#               Also in debug mode, `Full_String_Leaf` has disabled the create (`__new__`) and construct (`__init__`)
#               methods.
#
#           3)  `Full_String_Leaf` implements interface `Maybe_Temporary` (needed to make strings unique always).
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_String           import  intern_native_string
from    Capital.String                  import  TRAIT_String
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Cannot              import  raise__CANNOT__create__ERROR
    from    Capital.Cannot              import  raise__CANNOT__construct__ERROR
    from    Capital.Native_String       import  fact_is_empty_INTERNED_native_string


#
#<methods>
#
#   Common methods of `{Empty,Full}_String_Leaf`.
#


#
#   Interface String
#
@property
def property__String__native_string_subclass(self):
    return self.interned_s


#
#   .__format__ (format_specification)  - Format `String`
#
#       Delegated to the `Native_String` (i.e.: `str`) implementation via `.interned_s`.
#
def method__String__operator_format(self, format_specification):
    return self.interned_s.__format__(format_specification)
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class Empty_String_Leaf(
        #
        #   Implements Empty_String
        #
        TRAIT_Maybe_Temporary_0,
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   Empty_Native_String
    ))


    #
    #   Private
    #
    def __init__(self, interned_s):
        self.interned_s = interned_s


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False


    native_string_subclass = property__String__native_string_subclass


    #
    #   Public
    #


    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `Native_String` implementation via `.interned_s`.
    #
    __format__ = method__String__operator_format


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
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the same
    #       characters.
    #
    @staticmethod
    def python_code():
        return '""'


#
#   Full String - A wrapper around a full native string.
#
class Full_String_Leaf(
        #
        #   Implements Full_String
        #
        TRAIT_Maybe_Temporary_0,
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   Full_Native_String
    ))


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
    is_full_string  = True


    native_string_subclass = property__String__native_string_subclass


    #
    #   Public
    #


    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `Native_String` implementation via `.interned_s`.
    #
    __format__ = method__String__operator_format


    #
    #   .__len__()  - Return the length.
    #
    #       Delegated to the `Native_String` implementation via `.interned_s`.
    #
    def __len__(self):
        return self.interned_s.__len__()


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
    #       For now, we just use the `Native_String` representation (i.e: `str.__repr__`) via `.interned_s`.
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
    def python_code(self):
        return repr(self.interned_s)


@creator
def create_empty_string(interned_s):
    assert fact_is_empty_INTERNED_native_string(interned_s)

    return Empty_String_Leaf(interned_s)


@export
@creator
def create_full_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return Full_String_Leaf(interned_s)


empty_string = create_empty_string(intern_native_string(""))


#
#   empty_string - The empty string singleton.
#
export(empty_string)
