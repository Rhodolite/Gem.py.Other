#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Float - Float Interface.  `Float`s are Unique.
#
#       This is pretty much a copy of "Capital/Integer.py" -- See that file for comments.
#


from    Capital.Core                    import  export


#
#   interface Float
#       method
#           python_code() => Full_Native_String
#
#       attribute
#           is_avid_float     : Boolean
#           is_contrary_float : Boolean
#           is_negative_float : Boolean
#           is_positive_float : Boolean
#           is_zero_float     : Boolean
#
#           native_float_subclass : Native_Float
#
#       debug
#           is_float : Boolean
#
class TRAIT_Float(object):
    __slots__ = (())


    if __debug__:
        is_float = True


#
#   interface Zero
#       extends
#           Float
#
#       attribute
#           is_zero_float := true
#



#
#   interface Avid_Float
#       extends
#           Float, Zero
#
#       attribute
#           is_avid_float := true
#


#
#   interface Contrary_Float
#       extends
#           Float, Zero
#
#       attribute
#           is_contrary_float := true
#


#
#   interface Negative_Float
#       extends
#           Float
#
#       attribute
#           is_negative_float := true
#


#
#   interface Positive_Float
#       extends
#           Float
#
#       attribute
#           is_positive_float := true
#



#
#   USAGE:
#
#       v.is_avid_float                     #   Test if `v` is a `Avid_Float`     (greater than or equal to 0).
#
#       v.is_contrary_float                 #   Test if `v` is a `Contrary_Float` (less    than or equal to 0).
#
#       v.is_negative_float                 #   Test if `v` is a `Negative_Float` (less    than             0).
#
#       v.is_positive_float                 #   Test if `v` is a `Positive_Float` (greater than             0).
#
#       v.is_zero_float                     #   Test if `v` is the `zero_float` singleton.
#
#       conjure_avid_float(v)               #   Conjure a `Avid_Float`.
#
#       conjure_contrary_float(v)           #   Conjure a `Contrary_Float`.
#
#       conjure_float(v)                    #   Conjure a `Float`.
#
#       conjure_negative_float(v)           #   Conjure a `Negative_Float`.
#
#       conjure_positive_float(v)           #   Conjure a `Positive_Float`.
#
#       zero_float                          #   The zero float singleton.
#
#       v.native_float_subclass             #   The `Native_Float` that `v` represents (may be a subclass of
#                                           #   `Native_Float).
#
#       v.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `Native_Float` with the same value as the
#                                           #   `Native_Float` that `v` wraps.
#


#
#   USAGE (debug mode):
#
#       v.is_float                          #   Test if `v` is an `Float`.
#
#       assert fact_avid_float(v)           #   Assert that `v` is an `Avid_Float`.
#
#       assert fact_is_contrary_float(v)    #   Assert that `v` is a  `Contrary_Float`.
#
#       assert fact_is_float(v)             #   Assert that `v` is an `Float`.
#
#       assert fact_negative_float(v)       #   Assert that `v` is a  `Negative_Float`.
#
#       assert fact_positive_float(v)       #   Assert that `v` is a  `Positive_Float`.
#
#       assert fact_is_zero_float(v)        #   Assert that `v` is the `zero_float` singleton.
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           `zero_float`      - In a boolean context, evaluates to `False`.
#           All other floats  - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           0.0                         - In a boolean context, evaluates to `False`.
#           any other native float      - In a boolean context, evaluates to `True`.
#


#
#   fact_is_avid_float(v) - Assert that `v` is an `Avid_Float`.
#
if __debug__:
    def fact_is_avid_float(v):
        assert v.is_avid_float

        return True


#
#   fact_is_contrary_float(v) - Assert that `v` is a `Contrary_Float`.
#
if __debug__:
    def fact_is_contrary_float(v):
        assert v.is_contrary_float

        return True


#
#   fact_is_float(v) - Assert that `v` is an `Float`.
#
if __debug__:
    def fact_is_float(v):
        assert v.is_float

        return True


#
#   fact_is_negative_float(v) - Assert that `v` is a `Negative_Float`.
#
if __debug__:
    def fact_is_negative_float(v):
        assert v.is_negative_float

        return True


#
#   fact_is_positive_float(v) - Assert that `v` is a `Positive_Float`.
#
if __debug__:
    def fact_is_positive_float(v):
        assert v.is_positive_float

        return True


#
#   fact_is_zero_float(v) - Assert that `v` is the `zero_float` singleton.
#
if __debug__:
    def fact_is_zero_float(v):
        assert v.is_zero_float

        return True


#
#   Imports
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Private.Float_V1  import  zero_float
from    Capital.Private.Float_V1  import  conjure_avid_float
from    Capital.Private.Float_V1  import  conjure_contrary_float
from    Capital.Private.Float_V1  import  conjure_float
from    Capital.Private.Float_V1  import  conjure_negative_float
from    Capital.Private.Float_V1  import  conjure_positive_float


#
#   conjure_avid_float(v) - Conjure a `Avid_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_avid_float)


#
#   conjure_contrary_float(v) - Conjure a `Contrary_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_float)


#
#   conjure_float(v) - Conjure a `Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
export(conjure_float)


#
#   conjure_negative_float(v) - Conjure a `Negative_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and less than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_float)


#
#   conjure_positive_float(v) - Conjure a `Positive_Float`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Float` (i.e.: `float`), and greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Float` (i.e.: `float`).
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_float)


#
#   zero_float - The singleton `Float` wrapper around the `Native_Float` (i.e.: `float`) with a value of `0`.
#
export(zero_float)
