#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   "Facts" are only called in assertions (so they are removed when not in
#   python debug mode).
#
#   Internally facts do their *own* assertions & always return `python_true`.
#
#       1.  Only these [internal] assertions trigger when the fact fails;
#
#       2.  [the initial] assert never triggers -- only the internal ones do.
#
#   Again, the purpose of [the initial] assert, is so they are removed when
#   not in debug mode.
#


from    Z.BuiltIn           import  python_debug_mode
from    Z.BuiltIn           import  python_type
from    Z.BuiltIn           import  python_true
from    Z.BuiltIn           import  Python_Integer
from    Z.BuiltIn           import  Python_List


#
#   fact_is_full_string(s)
#
#       Assert the fact that `s` is an instance of `FullString`.
#
if python_debug_mode:
    def fact_is_full_string(s):
        assert python_type(s) is FullString

        return python_true


#
#   fact_is_python_integer(v)
#
#       Assert the fact that the `v` is an instance of `Python_Integer` (i.e.: `int`).
#
if python_debug_mode:
    def fact_is_python_integer(v):
        assert python_type(v) is Python_Integer

        return python_true


#
#   fact_is_python_list(v)
#
#       Assert the fact that `v` is an instance of `Python_List` (i.e.: `list`).
#
if python_debug_mode:
    def fact_is_python_list(s):
        assert python_type(s) is Python_List

        return python_true


#
#   fact_is_python_none(v) - Assert the fact that `v` is `python_none` (i.e.: `None`).
#
if python_debug_mode:
    def fact_is_python_none(v):
        assert v is none

        return python_true


#
#   fact_is__python_none__or__actual_string(s)
#
#       Assert the fact that `s` is either `python_none` or an instance of
#       `ActualString`.
#
if python_debug_mode:
    def fact_is__python_none__or__actual_string(s):
        if s is python_none:
            return python_true

        assert python_type(s) is ActualString

        return python_true


#
#   fact_is_not_python_none(v) - Assert the fact that `v` is not `python_none`
#
if python_debug_mode:
    def fact_is_not_python_none(v):
        assert v is not none

        return python_true


#
#   fact_is_not_none(v)             - Assert the fact that `v` is an integer greater than 0
#
if python_debug_mode:
    def fact_is_positive_integer(v):
        assert python_type(v) is Python_Integer
        assert v > 0

        return python_true


#
#   fact_is_python_class(classification)
#
#       Assert the fact that `classification` is a python class
#       (i.e.: It's metaclass is an instance of `Python_Type`)
#
if python_debug_mode:
    def fact_is_python_class(classification):
        assert python_is_instance(type(classification), Python_Type)

        return python_true
