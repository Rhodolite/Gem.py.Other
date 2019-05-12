#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_Complex - Native Complex & methods.
#


#
#   Native_Complex - A native complex (i.e.: `complex`).
#
Native_Complex = complex


#
#   fact_is_native_complex(v)
#
#       Assert that `v` is a `Native_Complex` (i.e.: `complex`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Complex` (i.e.: `complex`).
#
if __debug__:
    def fact_is_native_complex(v):
        assert type(v) is Native_Complex

        return True
