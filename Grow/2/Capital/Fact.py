#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


def USED(f):
    return f

#
#   "Capital/Fact.py" - Facts for assetions.
#
#       "Facts" are only called in assertions (so they are removed when not in python debug mode).
#
#       Internally facts do their *own* assertions & always return `True`.
#
#           1.  Only these [internal] assertions trigger when the fact fails;
#
#           2.  [the initial] assert never triggers -- only the internal ones do.
#
#       Again, the purpose of [the initial] assert, is so they are removed when not in debug mode.
#
#   FUTURE
#
#       Facts will be integrated much more closely into the code generator.
#
#       For now, we just use `fact_*` as funtions, as placeholders, for when they become an intrinsic
#       part of the Crystal Language.
#


from    Capital.Types       import  Python_Type


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
#   fact_is_string(s) - Assert the fact that `s` supports the `String` interface.
#
if __debug__:
    def fact_is_string(s):
        assert s.is_string

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
