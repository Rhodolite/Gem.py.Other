#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V5 - Private implementation of the public `String` Interface, Version 5.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique
#       in later versions.
#


#
#   Difference between Version 4 and Version 5:
#
#       Version 4:
#
#           Has a `Base_String` to avoid duplicate code.
#
#       Version 5:
#
#           Removes `Base_String`, and instead duplicates code (See below)
#


#
#   WHY DUPLICATE CODE IN REMOVING `Base_String`?
#
#   SUMMARY:
#
#       To avoid a limitation in python related to it's implementation of multiple inheritance, in version 6
#       of String Implementation, where we need to do class transformations using `.__class__` assignment.
#
#       (See "Capital.Private.ConjureString_V6.py" for details).
#
#   DETAILS:
#
#       Python has a few limitations with with it's implementation of multiple inheritance;
#
#           1)  Python does not allow multiple inheritance to have `__slots__` in multiple bases:
#
#               If you attempt to do this:
#
#                   class A(object): __slots__ = (('a',))
#                   class B(object): __slots__ = (('b',))
#                   class C(A, B): pass
#
#               You get the error:
#
#                   TypeError: Error when calling the metclass bases
#                       multiple bases have instance lay-out conflict
#
#               Which, interpreted, means:
#
#                   multiple bases (A & B) both have __slots__ that are non-empty.
#
#           2)  When figuring out if `.__class__` assignment is allowed, python typically only allows the
#               [non-empty] `__slots__` to be in the "same" place in the inheritance diagram.
#
#               EXAMPLE (what we want to do):
#
#                   class TRAIT_Some_String(object):                                __slots__ = (())
#                   class TRAIT_Maybe_Temporary_0(object):                          __slots__ = (())
#                   class Temporary_String(TRAIT_Maybe_Temporary_0):                __slots__ = (('interned_s',))
#                   class Full_String    (TRAIT_Some_String):                       __slots__ = (('interned_s',))
#                   class Full_String    (Base_String, TRAIT_Maybe_Temporary_0):    __slots__ = (())
#
#                   x = Temporary_String()
#                   x.__class__ = Full_String
#
#               However, this fails with:
#
#                   Type Error: __class__ assignment: 'Temporary_String' and object layout diffes from 'Full_String'.
#
#               Removing `Base_String`, allows us to simplfy this:
#
#                   class TRAIT_Some_String(object):                                    __slots__ = (())
#                   class TRAIT_Maybe_Temporary_0(object):                              __slots__ = (())
#                   class Temporary_String(TRAIT_Maybe_Temporary_0):                    __slots__ = (('interned_s',))
#                   class Full_String    (TRAIT_Some_String, TRAIT_Maybe_Temporary_0):  __slots__ = (('interned_s',))
#
#                   x = Temporary_String()
#                   x.__class__ = Full_String
#
#               ALTHOUGH, this still fails with the same error as above:
#
#                   Type Error: __class__ assignment: 'Temporary_String' and object layout diffes from 'Full_String'.
#
#               However, we can now REVERSE the order we declare the multiple inheritance for `Full_String`
#               (since we eliminated `Base_String`):
#
#                   class TRAIT_Some_String(object):                                    __slots__ = (())
#                   class TRAIT_Maybe_Temporary_0(object):                              __slots__ = (())
#                   class Temporary_String(TRAIT_Maybe_Temporary_0):                    __slots__ = (('interned_s',))
#                   class Full_String    (TRAIT_Maybe_Temporary_0, TRAIT_Some_String):  __slots__ = (('interned_s',))
#
#                   x = Temporary_String()
#                   x.__class__ = Full_String
#
#               NOW, python accepts out transformation.
#
#   CONCLUSION:
#
#       To avoid a limitation in python related to it's implementation of multiple inheritance, we have to eliminate
#       `Base_String`, and duplicate a few lines of code.
#
#       This will allos us to use `.__class__` assignment in version 4 implementation.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_String           import  intern_native_string
from    Capital.String                  import  TRAIT_Some_String


if __debug__:
    from    Capital.Native_String       import  fact_is_empty_INTERNED_native_string
    from    Capital.Native_String       import  fact_is_full_INTERNED_native_string


#
#<methods>
#   Base_String methods - A very simple string wrapper, common methods of `Empty_String` and `Full_String`.
#
#       As explained above we had to get rid of `Base_String`.
#
#       So instead we just list the [no longer existing] `Base_String` methods, and copy them into
#       `Empty_String` and `Full_String` below.
#


#
#   Base_String: contructor
#
def method__Base_String__constructor(self, interned_s):
    self.interned_s = interned_s


#
#   Base_String: Interface String
#
@property
def property__Base_String__native_string(self):
    return self.interned_s


#
#   Base_String.__format__ (format_specification)  - Format `String`
#
#       Delegated to the `Some_Native_String` implementation via `.interned_s`.
#
def method__Base_String__operator_format(self, format_specification):
    return self.interned_s.__format__(format_specification)
#</methods>


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class Empty_String(
        TRAIT_Some_String,
):
    __slots__ = ((
        'interned_s',                   #   Empty_Native_String
    ))


    #
    #   Private
    #
    __init__ = method__Base_String__constructor


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
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `Empty_Native_String` implementation via `.interned_s`.
    #
    __format__ = method__Base_String__operator_format


    #
    #   .__len__()  - Return the length.
    #
    #       Always returns `0` for an `Empty_String`.
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
class Full_String(
        TRAIT_Some_String,
):
    __slots__ = ((
        'interned_s',                   #   Full_Native_String
    ))


    #
    #   Private
    #
    __init__ = method__Base_String__constructor


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
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `Full_Native_String` implementation via `.interned_s`.
    #
    __format__ = method__Base_String__operator_format


    #
    #   .__len__()  - Return the length.
    #
    #       Delegated to the `Full_Native_String` implementation via `.interned_s`.
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
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the same
    #       characters.
    #
    #   CURRENT
    #
    #       For now, we just use the `Full_Native_String` representation (i.e: `str.__repr__` via `.interned_s`).
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

    return Empty_String(interned_s)


@export
@creator
def create_full_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return Full_String(interned_s)


empty_string = create_empty_string(intern_native_string(""))


export(empty_string)
