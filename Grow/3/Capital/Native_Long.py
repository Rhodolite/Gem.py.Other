#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_Long - Native Long & methods (only applicable to python 2.*)
#


from    Capital.System                  import  is_python_2


if is_python_2:
    #
    #   Avid_Native_Long - Zero or a positive native long (i.e.: `long` with a value greater than or equal to 0).
    #
    Avid_Native_Long = long


    #
    #   Contrary_Native_Long - Zero or a negative native long (i.e.: `long` with a value less than or equal to 0).
    #
    Contrary_Native_Long = long


    #
    #   Native_Long - A native long (i.e.: `long`).
    #
    Native_Long = long


    #
    #   fact_is_avid_native_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a value greater than or equal to 0.
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_avid_native_long(v):
            assert type(v) is Native_Long
            assert v >= 0

            return True


    #
    #   fact_is_contrary_native_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a value less than or equal to 0.
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_contrary_native_long(v):
            assert type(v) is Native_Long
            assert v <= 0

            return True


    #
    #   fact_is_native_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`).
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_native_long(v):
            assert type(v) is Native_Long

            return True


    #
    #   fact_is_native_non_zero_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a negative or positive value.
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_native_non_zero_long(v):
            assert type(v) is Native_Long
            assert v != 0

            return True


    #
    #   fact_is_native_zero(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a value of 0.
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_native_zero(v):
            assert type(v) is Native_Long
            assert v == 0

            return True


    #
    #   fact_is_negative_native_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a negative value.
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    if __debug__:
        def fact_is_avid_negative_long(v):
            assert type(v) is Native_Long
            assert v < 0

            return True


    #
    #   fact_is_positive_native_long(v)
    #
    #       Assert that `v` is a `Native_Long` (i.e.: `long`), with a positive value (greater than 0).
    #
    #       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
    #
    #   NOTE:
    #
    #       By definition "positive" means greater than 0.
    #
    #       See: https://simple.wikipedia.org/wiki/Positive_number
    #
    if __debug__:
        def fact_is_positive_native_long(v):
            assert type(v) is Native_Long
            assert v > 0

            return True
