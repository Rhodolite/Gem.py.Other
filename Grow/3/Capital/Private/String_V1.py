#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V1 - Private implementation of the public `String` Interface, Version 1.
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


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_String           import  intern_native_string
from    Capital.Some_String             import  TRAIT_Some_String


if __debug__:
    from    Capital.Native_String       import  fact_is_empty_INTERNED_native_string
    from    Capital.Native_String       import  fact_is_full_INTERNED_native_string


#
#   String [Leaf] - A very simple string wrapper.
#
@export
class String_Leaf(
        TRAIT_Some_String,
):
    __slots__ = ((
        'interned_s',                   #   Some_Native_String
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
    def is_empty_string(self):
        return len(self.interned_s) == 0


    @property
    def is_full_string(self):
        return len(self.interned_s) != 0


    @property
    def native_string(self):
        return self.interned_s


    #
    #   Public
    #

    
    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `Some_Native_String` implementation via `.interned_s`.
    #
    def __format__(self, format_specification):
        return self.interned_s.__format__(format_specification)


    #
    #   .__len__()  - Return the length.
    #
    #       Delegated to the `Some_Native_String` implementation via `.interned_s`.
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
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the
    #       same characters.
    #
    #   CURRENT
    #
    #       For now, we just use the `Some_Native_String` representation (i.e: `str.__repr__` via `.interned_s`).
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

    return String_Leaf(interned_s)


@export
@creator
def create_full_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return String_Leaf(interned_s)


empty_string = create_empty_string(intern_native_string(""))


export(create_full_string)
export(empty_string)
