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
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique
#       in later versions.
#


#
#   Difference between Version 2 & Version 3
#
#       Version 2:
#
#           Has a `BaseString` to avoid duplicate code.
#
#       Version 2:
#
#           Removes `BaseString`, and instead duplicates code (See below)
#


#
#   WHY DUPLICATE CODE IN REMOVING `BaseString`?
#
#   SUMMARY:
#
#       To avoid a limitation in python related to it's implementation of multiple inheritance, in version 4
#       of String Implementation, where we need to do class transformations using `.__class__` assignment.
#
#       (See "Capital.Private.ConjureString_V4.py" for details).
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
#           2)  When figuring out a if `.__class__` assignment is allowed, python typically only allows the
#               [non-empty] `__slots__` to be in the "same" place in the inheritance diagram.
#
#               EXAMPLE (what we want to do):
#
#                   class TRAIT_String(object):                                 __slots__ = (())
#                   class TRAIT_TemporaryElement(object):                       __slots__ = (())
#                   class TemporaryString(TRAIT_TemporaryElement):              __slots__ = (('interned_s',))
#                   class BaseString     (TRAIT_String):                        __slots__ = (('interned_s',))
#                   class FullString     (BaseString, TRAIT_TemporaryElement):  __slots__ = (())
#
#                   x = TemporaryString()
#                   x.__class__ = FullString
#
#               However, this fails with:
#
#                   Type Error: __class__ assignment: 'TemporaryString' and object layout diffes from 'FullString'.
#
#               Removing `BaseString`, allows us to simplfy this:
#
#                   class TRAIT_String(object):                                     __slots__ = (())
#                   class TRAIT_TemporaryElement(object):                           __slots__ = (())
#                   class TemporaryString(TRAIT_TemporaryElement):                  __slots__ = (('interned_s',))
#                   class FullString     (TRAIT_String, TRAIT_TemporaryElement):    __slots__ = (('interned_s',))
#
#                   x = TemporaryString()
#                   x.__class__ = FullString
#
#               ALTHOUGH, this still fails with the same error as above:
#
#                   Type Error: __class__ assignment: 'TemporaryString' and object layout diffes from 'FullString'.
#
#               However, we can now REVERSE the order we declare the multiple inheritance for `FullString`
#               (since we eliminated `BaseString`):
#
#                   class TRAIT_String(object):                                     __slots__ = (())
#                   class TRAIT_TemporaryElement(object):                           __slots__ = (())
#                   class TemporaryString(TRAIT_TemporaryElement):                  __slots__ = (('interned_s',))
#                   class FullString     (TRAIT_TemporaryElement, TRAIT_String):    __slots__ = (('interned_s',))
#
#                   x = TemporaryString()
#                   x.__class__ = FullString
#
#               NOW, Python happily accepts out transformation.
#
#   CONCLUSION:
#
#       To avoid a limitation in python related to it's implementation of multiple inheritance, we have to eliminate
#       `BaseString`, and duplicate a few lines of code.
#
#       This will allos us to use `.__class__` assignment in version 4 implementation.
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
#   BaseString methods - A very simple string wrapper, base calss of `EmptyString` and `FullString`.
#
#       As explained above we had to get rid of `BaseString`.
#
#       So instead we just list the [no longer existing] `BaseString` methods, and copy them into
#       `EmptyString` and `FullString` below.
#
def BaseString__constructor(self, interned_s):
    self.interned_s = interned_s


@property
def BaseString__native_subclass(self):
    return self.interned_s


#
#   Empty String - A singleton wrapper around the native empty string `""`.
#
class EmptyString(
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   EmptyNativeString
    ))


    #
    #   Private
    #
    __init__ = BaseString__constructor


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False
    native_subclass = BaseString__native_subclass


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


#
#   Full String - A wrapper around a full native string.
#
class FullString(
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   FullNativeString
    ))


    #
    #   Private
    #
    __init__ = BaseString__constructor


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True
    native_subclass = BaseString__native_subclass


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


empty_string = create_empty_string("")


export(empty_string)
