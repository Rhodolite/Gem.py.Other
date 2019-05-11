#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_Float - Native Float & methods.
#


#
#   Avid_Native_Float - Zero or a positive native float (i.e.: `float` with a value greater than or equal to 0).
#
Avid_Native_Float = float


#
#   Contrary_Native_Float - Zero or a negative native float (i.e.: `float` with a value less than or equal to 0).
#
Contrary_Native_Float = float


#
#   Native_Float - A native float (i.e.: `float`).
#
Native_Float = float


#
#   fact_is_avid_native_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a value greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_avid_native_float(v):
        assert type(v) is Native_Float
        assert v >= 0

        return True


#
#   fact_is_contrary_native_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a value less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_contrary_native_float(v):
        assert type(v) is Native_Float
        assert v <= 0

        return True


#
#   fact_is_native_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_native_float(v):
        assert type(v) is Native_Float

        return True


#
#   fact_is_native_non_zero_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a negative or positive value.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_native_non_zero_float(v):
        assert type(v) is Native_Float
        assert v != 0

        return True


#
#   fact_is_native_zero(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a value of 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_native_zero(v):
        assert type(v) is Native_Float
        assert v == 0

        return True


#
#   fact_is_negative_native_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a negative value.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
if __debug__:
    def fact_is_avid_negative_float(v):
        assert type(v) is Native_Float
        assert v < 0

        return True


#
#   fact_is_positive_native_float(v)
#
#       Assert that `v` is a `Native_Float` (i.e.: `float`), with a positive value (greater than 0).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   NOTE:
#
#       By definition "positive" means greater than 0.
#
#       See: https://simple.wikipedia.org/wiki/Positive_number
#
if __debug__:
    def fact_is_positive_native_float(v):
        assert type(v) is Native_Float
        assert v > 0

        return True
