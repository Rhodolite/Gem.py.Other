#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Integer - Integer Interface.  Integer are Unique.
#
#       By "Unique" we mean is only one integer for each unique value.
#
#       In addition to being unique, strings are currently classified into five groups.  The first three gruops are
#       quite familiar:
#
#           negative    - A value less    than 0.
#           positive    - A value greater than 0.
#           zero        - A value of           0.
#
#       In addition, there are two other groups:
#
#           avid        - A value greater than or equal to 0 (i.e.: non-negative).
#           contrary    - A value less    than or equal to 0 (i.e.: non-positive).
#
#       The verb "avid"     was chosen for lack of a better verb; it sounds "positive"; and at least it sound better
#       than "non-negative".
#
#       The verb "contrary" was chosen for lack of a better verb; it sounds "negative"; at at least is sounds better
#       than "non-positive".
#
#       Testing for these groups is done with:
#
#           .is_avid_integer
#           .is_contrary_integer
#           .is_negative_integer
#           .is_positive_integer
#           .is_zero_integer
#
#       In debug mode, testing can also be done for a `Integer` with:
#
#           .is_integer
#
#       Testing is *NOT* done with the python `type` builtin.
#


from    Capital.Core                    import  export


#
#   interface Integer
#       method
#           python_code() => Full_Native_String
#
#       attribute
#           is_avid_integer     : Boolean
#           is_contrary_integer : Boolean
#           is_negative_integer : Boolean
#           is_positive_integer : Boolean
#           is_zero_integer     : Boolean
#
#           native_integer_subclass : Native_Integer
#
#       debug
#           is_integer : Boolean
#
class TRAIT_Integer(object):
    __slots__ = (())


    if __debug__:
        is_integer = True


#
#   interface Zero
#       extends
#           Integer
#
#       attribute
#           is_zero_integer := true
#



#
#   interface Avid_Integer
#       extends
#           Integer, Zero
#
#       attribute
#           is_avid_integer := true
#


#
#   interface Contrary_Integer
#       extends
#           Integer, Zero
#
#       attribute
#           is_contrary_integer := true
#


#
#   interface Negative_Integer
#       extends
#           Integer
#
#       attribute
#           is_negative_integer := true
#


#
#   interface Positive_Integer
#       extends
#           Integer
#
#       attribute
#           is_positive_integer := true
#



#
#   USAGE:
#
#       v.is_avid_integer                   #   Test if `v` is a `Avid_Integer`     (greater than or equal to 0).
#
#       v.is_contrary_integer               #   Test if `v` is a `Contrary_Integer` (less    than or equal to 0).
#
#       v.is_negative_integer               #   Test if `v` is a `Negative_Integer` (less    than             0).
#
#       v.is_positive_integer               #   Test if `v` is a `Positive_Integer` (greater than             0).
#
#       v.is_zero_integer                   #   Test if `v` is the `zero_integer` singleton.
#
#       conjure_avid_integer(v)             #   Conjure a `Avid_Integer`.
#
#       conjure_contrary_integer(v)         #   Conjure a `Contrary_Integer`.
#
#       conjure_integer(v)                  #   Conjure a `Integer`.
#
#       conjure_negative_integer(v)         #   Conjure a `Negative_Integer`.
#
#       conjure_positive_integer(v)         #   Conjure a `Positive_Integer`.
#
#       zero_integer                        #   The zero integer singleton.
#
#       v.native_integer_subclass           #   The `Native_Integer` that `v` represents (may be a subclass of
#                                           #   `Native_Integer).
#
#       v.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `Native_Integer` with the same value as the
#                                           #   `Native_Integer` that `v` wraps.
#


#
#   USAGE (debug mode):
#
#       v.is_integer                        #   Test if `v` is an `Integer`.
#
#       assert fact_avid_integer(v)         #   Assert that `v` is an `Avid_Integer`.
#
#       assert fact_is_contrary_integer(v)  #   Assert that `v` is a  `Contrary_Integer`.
#
#       assert fact_is_integer(v)           #   Assert that `v` is an `Integer`.
#
#       assert fact_negative_integer(v)     #   Assert that `v` is a  `Negative_Integer`.
#
#       assert fact_positive_integer(v)     #   Assert that `v` is a  `Positive_Integer`.
#
#       assert fact_is_zero_integer(v)      #   Assert that `v` is the `zero_integer` singleton.
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           `zero_integer`      - In a boolean context, evaluates to `False`.
#           All other integers  - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           0                           - In a boolean context, evaluates to `False`.
#           any other native integer    - In a boolean context, evaluates to `True`.
#


#
#   fact_is_avid_integer(v) - Assert that `v` is an `Avid_Integer`.
#
if __debug__:
    def fact_is_avid_integer(v):
        assert v.is_avid_integer

        return True


#
#   fact_is_contrary_integer(v) - Assert that `v` is a `Contrary_Integer`.
#
if __debug__:
    def fact_is_contrary_integer(v):
        assert v.is_contrary_integer

        return True


#
#   fact_is_integer(v) - Assert that `v` is an `Integer`.
#
if __debug__:
    def fact_is_integer(v):
        assert v.is_integer

        return True


#
#   fact_is_negative_integer(v) - Assert that `v` is a `Negative_Integer`.
#
if __debug__:
    def fact_is_negative_integer(v):
        assert v.is_negative_integer

        return True


#
#   fact_is_positive_integer(v) - Assert that `v` is a `Positive_Integer`.
#
if __debug__:
    def fact_is_positive_integer(v):
        assert v.is_positive_integer

        return True


#
#   fact_is_zero_integer(v) - Assert that `v` is the `zero_integer` singleton.
#
if __debug__:
    def fact_is_zero_integer(v):
        assert v.is_zero_integer

        return True


#
#   Imports
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Private.Integer_V1  import  zero_integer
from    Capital.Private.Integer_V1  import  conjure_avid_integer
from    Capital.Private.Integer_V1  import  conjure_contrary_integer
from    Capital.Private.Integer_V1  import  conjure_integer
from    Capital.Private.Integer_V1  import  conjure_negative_integer
from    Capital.Private.Integer_V1  import  conjure_positive_integer


#
#   conjure_avid_integer(v) - Conjure a `Avid_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Integer` (i.e.: `int`), and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_avid_integer)


#
#   conjure_contrary_integer(v) - Conjure a `Contrary_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Integer` (i.e.: `int`), and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_integer)


#
#   conjure_integer(v) - Conjure a `Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Integer` (i.e.: `int`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
export(conjure_integer)


#
#   conjure_negative_integer(v) - Conjure a `Negative_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Integer` (i.e.: `int`), and less than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_integer)


#
#   conjure_positive_integer(v) - Conjure a `Positive_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Integer` (i.e.: `int`), and greater than 0.
#
#       `v` may *NOT* be an instance of a subclass of `Native_Integer` (i.e.: `int`).
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_integer)


#
#   zero_integer - The singleton `Integer` wrapper around the `Native_Integer` (i.e.: `int`) with a value of `0`.
#
export(zero_integer)
