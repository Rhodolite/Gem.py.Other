#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_Integer - Native Integer & methods.
#


#
#   Avid_Native_Integer - Zero or a positive native integer (i.e.: `int` with a value greater than or equal to 0).
#
Avid_Native_Integer = int


#
#   Contrary_Native_Integer - Zero or a negative native integer (i.e.: `int` with a value less than or equal to 0).
#
Contrary_Native_Integer = int


#
#   Native_Integer - A native integer (i.e.: `int`).
#
Native_Integer = int


#
#   fact_is_avid_native_integer(v)
#
#       Assert that `v` is a `Native_Integer` (i.e.: `int`), with a value greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
if __debug__:
    def fact_is_avid_native_integer(v):
        assert type(v) is Native_Integer
        assert v >= 0

        return True


#
#   fact_is_contrary_native_integer(v)
#
#       Assert that `v` is a `Native_Integer` (i.e.: `int`), with a value less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
if __debug__:
    def fact_is_contrary_native_integer(v):
        assert type(v) is Native_Integer
        assert v <= 0

        return True


#
#   fact_is_native_integer(v)
#
#       Assert that `v` is a `Native_Integer` (i.e.: `int`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
if __debug__:
    def fact_is_native_integer(v):
        assert type(v) is Native_Integer

        return True


#
#   fact_is_negative_native_integer(v)
#
#       Assert that `v` is a `Native_Integer` (i.e.: `int`), with a negative value.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
if __debug__:
    def fact_is_avid_negative_integer(v):
        assert type(v) is Native_Integer
        assert v < 0

        return True


#
#   fact_is_positive_native_integer(v)
#
#       Assert that `v` is a `Native_Integer` (i.e.: `int`), with a positive value (greater than 0).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
#   NOTE:
#       
#       By definition "positive" means greater than 0.
#
#       See: https://simple.wikipedia.org/wiki/Positive_number
#
if __debug__:
    def fact_is_positive_native_integer(v):
        assert type(v) is Native_Integer
        assert v > 0

        return True
