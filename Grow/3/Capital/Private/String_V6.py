#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V6 - Private implementation of the public `String` Interface, Version 6.
#
#       Strings are Unique (always).
#
#       Uniqueness is implemented in "Capital.Private.ConjureString_V5.py" (which uses the interface
#       `TemporaryElement` to implement uniqueness).
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           String classes use `object` as their base class.
#
#       Version 6:
#
#           String classes use `NativeString` as their base class.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.NativeString            import  NativeString
from    Capital.String                  import  TRAIT_String
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.Fact                import  fact_is_empty_native_string
    from    Capital.Fact                import  fact_is_full_native_string


#
#<methods>
#   common methods of `EmptyString` and `FullString`.
#
#       As explained in "Capital.Private.String_V4.py" we had to get rid of `BaseString`.
#
#       So instead we just list the [no longer existing] `BaseString` methods, and copy them into
#       `EmptyString` and `FullString` below.
#


#
#   BaseString: Interface String
#
@property
def property__BaseString__native_subclass(self):
    return self
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class EmptyString(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_String,
):
    __slots__ = (())


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False
    native_subclass = property__BaseString__native_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `NativeString`.
    #


    #
    #   .__len__()  - Return the length.
    #
    #       Always returns `0` for an `EmptyString`.
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
    #       Return a `NativeString` that is the python code that python will compile to a `NativeString` with the same
    #       characters.
    #
    @staticmethod
    def python_code():
        return '""'


#
#   method__NativeString__representation - The python implemention of `repr` for `str` (i.e.: `str.__repr__`).
#
method__NativeString__representation = NativeString.__repr__


#
#   Full String - A wrapper around a full native string.
#
class FullString(
        NativeString,
        TRAIT_TemporaryElement,
        TRAIT_String,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL('{}: A FullString may not be created',
                  "Capital.Private.FullString_V5.FullString.operator new (`__new__`)")


    if __debug__:
        def __init__(self, s):
            FATAL('{}: A FullString may not be constructed',
                  "Capital.Private.FullString_V5.FullString.constructor (`__init__`)")


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True
    native_subclass = property__BaseString__native_subclass


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
    #       For now, we just use the `NativeString` representation (i.e: `str.__repr__`).
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
    python_code = method__NativeString__representation


@creator
def create_empty_string(s):
    assert fact_is_empty_native_string(s)

    return EmptyString(s)


@export
@creator
def create_full_string(s):
    assert fact_is_full_native_string(interned_s)

    return FullString(s)


empty_string = create_empty_string("")


export(empty_string)
