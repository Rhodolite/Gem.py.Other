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


from    Capital.Types       import  Python_Type


#
#   fact_is_empty_python_list(v)
#
#       Assert the fact that `v` is a empty *DIRECT* `list` instance.
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_empty_python_list(v):
        assert type(v) is list
        assert len(v) == 0

        return True


#
#   fact_is_full_python_list(v)
#
#       Assert the fact that `v` is a *DIRECT* `list` instance, and is "full" (i.e.: is non-empty and has at least one
#       element).
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_full_python_list(v):
        assert type(v) is list
        assert len(v) > 0

        return True


#
#   fact_is_full_python_string(s)
#
#       Assert the fact that `s` is a *DIRECT* `str` instance, and has a length greater than 0.
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_full_python_string(s):
        assert type(s) is str
        assert len(s) > 0

        return True


#
#   fact_is_python_integer(v) - Assert the fact that the `v` is an `int` instance.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
if __debug__:
    def fact_is_python_integer(v):
        assert type(v) is int

        return True


#
#   fact_is_python_none(v) - Assert the fact that `v` is `None`.
#
if __debug__:
    def fact_is_python_none(v):
        assert v is None

        return True


#
#   fact_is_python_string(s) - Assert the fact that `s` is a *DIRECT* `str` instance.
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_python_string(s):
        assert type(s) is str

        return True
