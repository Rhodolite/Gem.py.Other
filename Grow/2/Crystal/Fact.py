#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   "Facts" are only called in assertions (so they are removed when not in python debug mode).
    #
    #   Internally facts do their *own* assertions & always return `true`.
    #
    #       1.  Only these [internal] assertions trigger when the fact fails;
    #
    #       2.  [the initial] assert never triggers -- only the internal ones do.
    #
    #   Again, the purpose of [the initial] assert, is so they are removed when not in debug mode.
    #


    #
    #   fact_is_actual_string(s)
    #
    #       Assert the fact that `s` is an `ActualString` (that is a non-empty python string).
    #
    #   NOTE:
    #       Defined in "Crystal.py"
    #


    #
    #   fact_is_interned_actual_string(s)
    #
    #       Assert that `s` is an actual string (a non empty string) that has been interned.
    #
    #   NOTE:
    #       Defined in "Crystal/Share.py"
    #


    #
    #   fact_is_none(v)                 - Assert the fact that `v` is `none`
    #
    if python_debug_mode:
        @share
        def fact_is_none(v):
            assert v is none

            return true


    #
    #   fact_is__none__or__actual_string(s)
    #
    #       Assert the fact that `s` is either `none` or an `ActualString` (that is a non-empty python string).
    #
    if python_debug_mode:
        @share
        def fact_is__none__or__actual_string(s):
            if s is not none:
                assert python_type(s) is ActualString
                assert length(s) > 0

            return true


    #
    #   fact_is_not_none(v)             - Assert the fact that `v` is not `none`
    #
    if python_debug_mode:
        @share
        def fact_is_not_none(v):
            assert v is not none

            return true


    #
    #   fact_is_not_none(v)             - Assert the fact that `v` is an integer greater than 0
    #
    if python_debug_mode:
        @share
        def fact_is_positive_integer(v):
            assert python_type(v) is Python_Integer
            assert v > 0

            return true


    #
    #   fact_is_python_class(classification)
    #
    #       Assert the fact that `classification` is a python class
    #       (i.e.: It's metaclass is an instance of `Python_Type`)
    #
    if python_debug_mode:
        @share
        def fact_is_python_class(classification):
            assert python_is_instance(type(classification), Python_Type)

            return true


    #
    #   fact_is__python_class__or__python_function(v)
    #
    #       Assert the fact that `v` is a python class or a python function.
    #
    #   NOTE:
    #       Defined in "Crystal/Share.py"
    #


    #
    #   fact_is_python_string(s)
    #
    #       Assert the fact that `s` is a python string.
    #
    #   NOTE:
    #       Defined in "Crystal/Share.py"
    #


    #
    #   fact_is_python_tuple(v)
    #
    #       Assert the fact that `v` is a `Python_Tuple`.
    #
    if python_debug_mode:
        @share
        def fact_is_python_tuple(v):
            assert type(v) is Python_Tuple

            return true
