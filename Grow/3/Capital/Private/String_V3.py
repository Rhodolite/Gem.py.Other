#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V3 - Private implementation of the public `String` Interface, Version 3.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#
#           2.  Tracebacks due to MemoryError (out of memory);
#
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique
#       in later versions.
#


#
#   Difference between Version 1, Version 2, and Version 3
#
#       Version 1:
#
#           1)  Both empty & full strings are managed by `String_V1`;
#
#           2)  Implementation of `.is_empty_string` and `.is_full_string` is done by properties.
#
#       Version 2:
#
#           Identical to version 1.
#
#       Version 3:
#
#           There are seperate classes for empty & full strings:
#
#               1A)     `EmptyString` is used to handle the singleton `empty_string`; and
#
#               1B)     `FullString` is used to handle full strings.
#
#           And also:
#
#               2)      Implementation of `.is_empty_string` and `.is_full_stting done by members (which is much
#                       simplier & faster than properties used in version 1).
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.NativeString            import  intern_native_string
from    Capital.String                  import  TRAIT_String


if __debug__:
    from    Capital.NativeString        import  fact_is_empty_INTERNED_native_string
    from    Capital.NativeString        import  fact_is_full_INTERNED_native_string


#
#   BaseString - A very simple string wrapper, base class of `EmptyString` and `FullString`.
#
#       NOTE: Named `BaseString` instead of `String`, since the name "String" is reserved for `interface String`.
#
#             (even though in the current implementation python (which does not have interfaces in python) does not
#             actually have anything really named `interface String` -- conceptually it does, and thus the name
#             "String" is still reserved for `interface String`).
#
class BaseString(
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   NativeString
    ))


    #
    #   Private
    #
    def __init__(self, interned_s):
        self.interned_s = interned_s


    #
    #   Interface String
    #
    @property
    def native_string(self):
        return self.interned_s


    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
    #
    def __format__(self, format_specification):
        return self.interned_s.__format__(format_specification)


class EmptyString(BaseString):
    __slots__ = ((
    #   'interned_s',                   #   Inherited from `BaseString`; but type changes to `EmptyNativeString`.
    ))


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False


    #
    #   Public
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
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the same
    #       characters.
    #
    @staticmethod
    def python_code():
        return '""'



class FullString(BaseString):
    __slots__ = ((
    #   'interned_s',                   #   Inherited from `BaseString`; but type changes to `FullNativeString`.
    ))


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True


    #
    #   Public
    #


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
