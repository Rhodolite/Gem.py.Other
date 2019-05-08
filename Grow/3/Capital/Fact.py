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
#   fact_is_empty_native_list(v)
#
#       Assert that `v` is a empty *DIRECT* `list` instance (i.e.: has zero elements).
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_empty_native_list(v):
        assert type(v) is list
        assert len(v) == 0

        return True


#
#   fact_is_full_native_list(v)
#
#       Assert that `v` is a *DIRECT* `list` instance, and is "full" (i.e.: is non-empty; i.e.: and has at
#       least one element).
#
#       `v` may *NOT* be an instance of a subclass of `list`.
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
#   fact_is_native_none(v) - Assert that `v` is `None`.
#
if __debug__:
    def fact_is_native_none(v):
        assert v is None

        return True


if 0:
    #
    #   DISABLED (not currently used, will be enabled & used in the future)
    #

    #
    #   fact_is__native_none__OR__some_native_integer(v)
    #
    #       Assert that `v` is either:
    #
    #           1)  `NONE`; OR
    #
    #           2)  a `NativeInteger` (i.e.: `int`).
    #
    if __debug__:
        def fact_is__native_none__OR__some_native_integer(v):
            assert (v is None) or (isinstance(v, int))

            return True


#
#   fact_is_not_native_none(v) - Assert that `v` is not `None`.
#
if __debug__:
    def fact_is_not_native_none(v):
        assert v is not None

        return True


#
#   fact_is_positive_integer(v)
#
#       Assert that `v` is a *DIRECT* `int` instance, and is greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
if __debug__:
    def fact_is_positive_integer(v):
        assert type(v) is int
        assert v > 0

        return True


#
#   fact_is_some_native_integer(v) - Assert that the `v` is an `int`.
#
if __debug__:
    def fact_is_some_native_integer(v):
        assert isinstance(v, int)

        return True


#
#   fact_is_some_native_list(v)
#
#       Assert that `v` is a *DIRECT* `list` instance.
#
#       `v` may *NOT* be an instance of a subclass of `list`.
#
if __debug__:
    def fact_is_some_native_list(v):
        assert type(v) is list

        return True


#
#   fact_is_some_native_string(s) - Assert that `s` is a *DIRECT* `str` instance.
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_some_native_string(s):
        assert type(s) is str

        return True


#
#   fact_is_substantial_integer(v)
#
#       Assert that `v` is a *DIRECT* `int` instance, and is greater than or equal to 0.
#
#   NOTE:
#       "substantial" was chosen to mean "positive" or "zero".
#
if __debug__:
    def fact_is_substantial_integer(v):
        assert isinstance(v, int)
        assert v >= 0

        return True
