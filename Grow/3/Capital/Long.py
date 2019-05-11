#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Long - Long Interface.  `Long`s are Unique.
#
#       This is pretty much a copy of "Capital/Integer.py" -- See that file for comments.
#


from    Capital.Core                    import  export
from    Capital.System                  import  is_python_2


#
#   `Native_Long` is only implemented in Python 2.*
#
#   Hence, Inteface `Long` is also only implemented in Python 2.*
#
assert is_python_2


#
#   interface Long
#       method
#           python_code() => Full_Native_String
#
#       attribute
#           is_avid_long     : Boolean
#           is_contrary_long : Boolean
#           is_negative_long : Boolean
#           is_positive_long : Boolean
#           is_zero_long     : Boolean
#
#           native_long_subclass : Native_Long
#
#       debug
#           is_long : Boolean
#
class TRAIT_Long(object):
    __slots__ = (())


    if __debug__:
        is_long = True


#
#   interface Avid_Long
#       extends
#           Long, Zero_Long
#
#       attribute
#           is_avid_long := true
#


#
#   interface Contrary_Long
#       extends
#           Long, Zero_Long
#
#       attribute
#           is_contrary_long := true
#


#
#   interface Negative_Long
#       extends
#           Long
#
#       attribute
#           is_negative_long := true
#


#
#   interface Positive_Long
#       extends
#           Long
#
#       attribute
#           is_positive_long := true
#


#
#   interface Zero_Long
#       extends
#           Long
#
#       attribute
#           is_zero_long := true
#


#
#   USAGE:
#
#       v.is_avid_long                      #   Test if `v` is a `Avid_Long`     (greater than or equal to 0).
#
#       v.is_contrary_long                  #   Test if `v` is a `Contrary_Long` (less    than or equal to 0).
#
#       v.is_negative_long                  #   Test if `v` is a `Negative_Long` (less    than             0).
#
#       v.is_positive_long                  #   Test if `v` is a `Positive_Long` (greater than             0).
#
#       v.is_zero_long                      #   Test if `v` is the `zero_long` singleton.
#
#       conjure_avid_long(v)                #   Conjure a `Avid_Long`.
#
#       conjure_contrary_long(v)            #   Conjure a `Contrary_Long`.
#
#       conjure_long(v)                     #   Conjure a `Long`.
#
#       conjure_negative_long(v)            #   Conjure a `Negative_Long`.
#
#       conjure_positive_long(v)            #   Conjure a `Positive_Long`.
#
#       zero_long                           #   The zero long singleton.
#
#       v.native_long_subclass              #   The `Native_Long` that `v` represents (may be a subclass of
#                                           #   `Native_Long).
#
#       v.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `Native_Long` with the same value as the
#                                           #   `Native_Long` that `v` wraps.
#


#
#   USAGE (debug mode):
#
#       v.is_long                           #   Test if `v` is an `Long`.
#
#       assert fact_avid_long(v)            #   Assert that `v` is an `Avid_Long`.
#
#       assert fact_is_contrary_long(v)     #   Assert that `v` is a  `Contrary_Long`.
#
#       assert fact_is_long(v)              #   Assert that `v` is an `Long`.
#
#       assert fact_negative_long(v)        #   Assert that `v` is a  `Negative_Long`.
#
#       assert fact_positive_long(v)        #   Assert that `v` is a  `Positive_Long`.
#
#       assert fact_is_zero_long(v)         #   Assert that `v` is the `zero_long` singleton.
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           `zero_long`      - In a boolean context, evaluates to `False`.
#           All other longs  - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           0L                          - In a boolean context, evaluates to `False`.
#           any other native long       - In a boolean context, evaluates to `True`.
#


#
#   fact_is_avid_long(v) - Assert that `v` is an `Avid_Long`.
#
if __debug__:
    def fact_is_avid_long(v):
        assert v.is_avid_long

        return True


#
#   fact_is_contrary_long(v) - Assert that `v` is a `Contrary_Long`.
#
if __debug__:
    def fact_is_contrary_long(v):
        assert v.is_contrary_long

        return True


#
#   fact_is_long(v) - Assert that `v` is an `Long`.
#
if __debug__:
    def fact_is_long(v):
        assert v.is_long

        return True


#
#   fact_is_negative_long(v) - Assert that `v` is a `Negative_Long`.
#
if __debug__:
    def fact_is_negative_long(v):
        assert v.is_negative_long

        return True


#
#   fact_is_positive_long(v) - Assert that `v` is a `Positive_Long`.
#
if __debug__:
    def fact_is_positive_long(v):
        assert v.is_positive_long

        return True


#
#   fact_is_zero_long(v) - Assert that `v` is the `zero_long` singleton.
#
if __debug__:
    def fact_is_zero_long(v):
        assert v.is_zero_long

        return True


#
#   Imports
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Private.Long_V1  import  zero_long
from    Capital.Private.Long_V1  import  conjure_avid_long
from    Capital.Private.Long_V1  import  conjure_contrary_long
from    Capital.Private.Long_V1  import  conjure_long
from    Capital.Private.Long_V1  import  conjure_negative_long
from    Capital.Private.Long_V1  import  conjure_positive_long


#
#   conjure_avid_long(v) - Conjure a `Avid_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_avid_long)


#
#   conjure_contrary_long(v) - Conjure a `Contrary_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_long)


#
#   conjure_long(v) - Conjure a `Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
export(conjure_long)


#
#   conjure_negative_long(v) - Conjure a `Negative_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and less than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_long)


#
#   conjure_positive_long(v) - Conjure a `Positive_Long`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Long` (i.e.: `long`), and greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Long` (i.e.: `long`).
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_long)


#
#   zero_long - The singleton `Long` wrapper around the `Native_Long` (i.e.: `long`) with a value of `0`.
#
export(zero_long)
