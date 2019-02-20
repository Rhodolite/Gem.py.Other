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


from    Z.BuiltIn           import  Python_Type


#
#   fact_is_empty_python_list(v)
#
#       Assert the fact that `v` is a empty *DIRECT* instance of `list`.
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_empty_python_list(v):
        assert type(v) is list
        assert len(v) == 0

        return True


#
#   fact_is_full_exact_python_list(v)
#
#       Assert the fact that `v` is a *DIRECT* instance of `list`,
#       and is "full" (i.e.: is non-empty and has at least one element).
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_full_exact_python_list(v):
        assert type(v) is list
        assert len(v) > 0

        return True


#
#   fact_is_full_python_string(s)
#
#       Assert the fact that `s` is a `str` instance, and has a length greater than 0.
#
if __debug__:
    def fact_is_full_python_string(s):
        assert type(s) is str
        assert len(s) > 0

        return True


#
#   fact_is_full_string(s)
#
#       Assert the fact that `s` is an instance of `FullString`.
#
if __debug__:
    def fact_is_full_string(s):
        assert type(s) is FullString

        return True


#
#   fact_is_python_integer(v)
#
#       Assert the fact that the `v` is an instance of `int`.
#
if __debug__:
    def fact_is_python_integer(v):
        assert type(v) is int

        return True


#
#   fact_is_python_list(v)
#
#       Assert the fact that `v` is an instance of `list`.
#
if __debug__:
    def fact_is_python_list(s):
        assert type(s) is list

        return True


#
#   fact_is_python_none(v) - Assert the fact that `v` is `None`.
#
if __debug__:
    def fact_is_python_none(v):
        assert v is None

        return True


#
#   fact_is__python_none__or__actual_string(s)
#
#       Assert the fact that `s` is either `python_none` or an instance of
#       `ActualString`.
#
if __debug__:
    def fact_is__python_none__or__actual_string(s):
        if s is python_none:
            return True

        assert type(s) is ActualString

        return True


#
#   fact_is_python_string(s)
#
#       Assert the fact that `s` is a *DIRECT* instance of `str`
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_python_string(s):
        assert type(s) is str

        return True


#
#   fact_is_not_python_none(v) - Assert the fact that `v` is not `python_none`
#
if __debug__:
    def fact_is_not_python_none(v):
        assert v is not None

        return True


#
#   fact_is_positive_integer(v) - Assert the fact that `v` is an integer greater than 0.
#
if __debug__:
    def fact_is_positive_integer(v):
        assert type(v) is int
        assert v > 0

        return True


#
#   fact_is_python_class(classification)
#
#       Assert the fact that `classification` is a python class
#       (i.e.: It's metaclass is an instance of `Python_Type` (i.e.: `type`))
#
if __debug__:
    def fact_is_python_class(classification):
        assert python_is_instance(type(classification), Python_Type)

        return True
