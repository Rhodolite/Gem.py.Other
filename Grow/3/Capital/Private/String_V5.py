#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V5 - Private implementation of the public `String` Interface, Version 5.
#
#       Strings are Unique (always).
#
#       Uniqueness is implemented in "Capital.Private.ConjureString_V5.py" (which uses the interface
#       `TemporaryElement` to implement uniqueness).
#


#
#   Difference between Version 4 & Version 5.
#
#       Version 4:
#
#           1)  Strings are unique (in normal cases).
#
#           2)  Has creator function `create_full_string` for `FullString`.
#
#       Version 5:
#
#           1)  Strings are unique (always).
#
#           2)  Does *NOT* have creator function for `FullString` (since `FullString` cannot be created, but
#               only transformed from a `Capital.Private.TemporaryString_V3.TemporaryString`).
#
#               Also in debug mode, `FullString` has disabled the create (`__new__`) and construct (`__init__`)
#               methods.
#
#           3)  `FullString` implements interface `TemporaryElement` (needed to make strings unique always).
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.NativeString            import  intern_native_string
from    Capital.String                  import  TRAIT_String
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.NativeString        import  fact_is_empty_INTERNED_native_string


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
def property__BaseString__native_string(self):
    return self.interned_s


#
#   BaseString.__format__ (format_specification)  - Format `String`
#
#       Delegated to the `NativeString` implementation via `.interned_s`.
#
def method__BaseString__operator_format(self, format_specification):
    return self.interned_s.__format__(format_specification)
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class EmptyString(
        TRAIT_TemporaryElement,
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   EmptyNativeString
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
    native_string   = property__BaseString__native_string


    #
    #   Public
    #


    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
    #
    __format__ = method__BaseString__operator_format


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
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the same
    #       characters.
    #
    @staticmethod
    def python_code():
        return '""'


#
#   Full String - A wrapper around a full native string.
#
class FullString(
        TRAIT_TemporaryElement,
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   FullNativeString
    ))


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
    native_string   = property__BaseString__native_string


    #
    #   Public
    #


    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
    #
    __format__ = method__BaseString__operator_format


    #
    #   .__len__()  - Return the length.
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
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
    #       For now, we just use the `NativeString` representation (i.e: `str.__repr__` via `.interned_s`).
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

    return EmptyString(interned_s)


@export
@creator
def create_full_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return FullString(interned_s)


empty_string = create_empty_string(intern_native_string(""))


export(empty_string)
