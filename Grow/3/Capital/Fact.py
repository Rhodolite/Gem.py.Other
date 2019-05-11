#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   "Facts" are only called in assertions (so they are removed when not in
#   python debug mode).
#
#   Internally facts do their *own* assertions & always return `True`.
#
#       1.  Only these [internal] assertions trigger when the fact fails;
#
#       2.  [the initial] assert never triggers -- only the internal ones do.
#
#   Again, the purpose of [the initial] assert, is so they are removed when
#   not in debug mode.
#


from    Capital.Types       import  Native_Function
from    Capital.Types       import  Native_Built_In_Method
from    Capital.Types       import  Python_Type


#
#   fact_is_empty_native_list(v)
#
#       Assert that `v` is a `Native_List`, and is "empty" (i.e.: `list` with zero elements).
#
#       `v` may *NOT* be an instance of a subclass of `Native_List`.
#
if __debug__:
    def fact_is_empty_native_list(v):
        assert type(v) is list
        assert len(v) == 0

        return True


#
#   fact_is_full_native_list(v)
#
#       Assert that `v` is a `Native_List`, and is "full" (i.e.: `list` with at least one element).
#
#       `v` may *NOT* be an instance of a subclass of `Native_List`.
#
if __debug__:
    def fact_is_full_native_list(v):
        assert type(v) is list
        assert len(v) > 0

        return True


#
#   fact_is_native_boolean(v) - Assert that `v` is a `bool`.
#
if __debug__:
    def fact_is_native_boolean(v):
        assert type(v) is bool

        return True


#
#   fact_is_native_built_in_method(method) - Assert that `method` is a `Native_Built_In_Method`.
#
if __debug__:
    def fact_is_native_built_in_method(f):
        assert type(f) is Native_Built_In_Method

        return True


#
#   fact_is_native_function(f) - Assert that `f` is a `Native_Function`.
#
if __debug__:
    def fact_is_native_function(f):
        assert type(f) is Native_Function

        return True


#
#   fact_is_native_list(v)
#
#       Assert that `v` is a `Native_List` (i.e.: `list`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_List` (i.e.: `list`).
#
if __debug__:
    def fact_is_native_list(v):
        assert type(v) is list

        return True


#
#   fact_is_native_none(v) - Assert that `v` is `None`.
#
if __debug__:
    def fact_is_native_none(v):
        assert v is None

        return True


#
#   fact_is_native_type(v) - Assert that `v` is a `Type` (i.e.: probably a `class`).
#
if __debug__:
    def fact_is_native_type(v):
        assert isinstance(type(v), Python_Type)

        return True


if 0:
    #
    #   DISABLED (not currently used, will be enabled & used in the future)
    #

    #
    #   fact_is__native_none__OR__native_integer(v)
    #
    #       Assert that `v` is either:
    #
    #           1)  `NONE`; OR
    #
    #           2)  a `NativeInteger` (i.e.: `int`).
    #
    if __debug__:
        def fact_is__native_none__OR__native_integer(v):
            assert (v is None) or (type(v) is int)

            return True


#
#   fact_is_not_native_none(v) - Assert that `v` is not `None`.
#
if __debug__:
    def fact_is_not_native_none(v):
        assert v is not None

        return True
