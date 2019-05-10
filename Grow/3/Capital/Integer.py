#"
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
#           keen        - A value greater than or equal to 0 (i.e.: non-negative).
#           contrary    - A value less    than or equal to 0 (i.e.: non-positive).
#
#       The verb "keen"     was chosen for lack of a better verb; and at least it sound better than "non-negative".
#
#       The verb "contrary" was chosen for lack of a better verb; at at least is sounds better than "non-positive".
#
#       Testing for these groups is done with:
#
#           .is_contrary_integer
#           .is_keen_integer
#           .is_negative_integer
#           .is_positive_integer
#           .is_zero
#
#       In debug mode, testing can also be done for a `Some_Integer` with:
#
#           .is_some_integer
#
#       Testing is *NOT* done with the python `type` builtin.
#


from    Capital.Core                    import  export


#
#   interface Some_Integer
#       method
#           python_code() => Full_Native_String
#
#       attribute
#           is_contrary_integer : Boolean
#           is_keen_integer     : Boolean
#           is_negative_integer : Boolean
#           is_positive_integer : Boolean
#           is_zero             : Boolean
#
#           native_integer_subclass : Some_Native_Integer
#
#       debug
#           is_some_integer : Boolean
#
class TRAIT_Some_Integer(object):
    __slots__ = (())


    if __debug__:
        is_some_integer = True


#
#   interface Zero
#       extends
#           Some_Integer
#
#       attribute
#           is_zero := true
#
class TRAIT_Zero(object):
    __slots__ = (())


    is_zero = False


#
#   interface Contrary_Integer
#       extends
#           Some_Integer, Zero
#
#       attribute
#           is_contrary_integer := true
#
class TRAIT_Contrary_Integer(object):
    __slots__ = (())


    is_contrary_integer = True


#
#   interface Keen_Integer
#       extends
#           Some_Integer, Zero
#
#       attribute
#           is_keen_integer := true
#
class TRAIT_Keen_Integer(object):
    __slots__ = (())


    is_keen_integer = True


#
#   interface Negative_Integer
#       extends
#           Some_Integer
#
#       attribute
#           is_negative_integer := true
#
class TRAIT_Negative_Integer(object):
    __slots__ = (())


    is_negative_integer = True


#
#   interface Positive_Integer
#       extends
#           Some_Integer
#
#       attribute
#           is_positive_integer := true
#
class TRAIT_Positive_Integer(object):
    __slots__ = (())


    is_positive_integer = True



#
#   USAGE:
#
#       v.is_zero                           #   Test if `v` is `Zero`.
#
#       v.is_contrary_integer               #   Test if `v` is a `Contrary_Integer` (less    than or equal to 0).
#
#       v.is_keen_integer                   #   Test if `v` is a `Keen_Integer`     (greater than or equal to 0).
#
#       v.is_negative_integer               #   Test if `v` is a `Negative_Integer` (less    than             0).
#
#       v.is_positive_integer               #   Test if `v` is a `Positive_Integer` (greater than             0).
#
#       conjure_contrary_integer(v)         #   Conjure a `Contrary_Integer`.
#
#       conjure_keen_integer(v)             #   Conjure a `Keen_Integer`.
#
#       conjure_negative_integer(v)         #   Conjure a `Negative_Integer`.
#
#       conjure_positive_integer(v)         #   Conjure a `Positive_Integer`.
#
#       conjure_some_integer(v)             #   Conjure a `Some_Integer`.
#
#       zero_integer                        #   The zero integer singleton.
#
#       v.native_integer_subclass           #   The `Some_Native_Integer` that `v` represents (may be a subclass of
#                                           #   `Some_Native_Integer).
#
#       v.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `Some_Native_Integer` with the same value as the
#                                           #   `Some_Native_Integer` that `v` wraps.
#


#
#   USAGE (debug mode):
#
#       v.is_some_integer                   #   Test if `v` is a `Some_Integer`.
#
#       assert fact_is_contrary_integer(v)  #   Assert that `v` is a `Contrary_Integer`.
#
#       assert fact_keen_integer(v)         #   Assert that `v` is a `Keen_Integer`.
#
#       assert fact_negative_integer(v)     #   Assert that `v` is a `Negative_Integer`.
#
#       assert fact_positive_integer(v)     #   Assert that `v` is a `Positive_Integer`.
#
#       assert fact_is_some_integer(v)      #   Assert that `v` is a `Some_Integer`.
#
#       assert fact_is_zero(v)              #   Assert that `v` is the `zero_integer` singleton.
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
#   fact_is_contrary_integer(v) - Assert that `v` is a `Contrary_Integer`.
#
if __debug__:
    def fact_is_contrary_integer(v):
        assert v.is_contrary_integer

        return True


#
#   fact_is_keen_integer(v) - Assert that `v` is a `Keen_Integer`.
#
if __debug__:
    def fact_is_keen_integer(v):
        assert v.is_keen_integer

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
#   fact_is_some_integer(v) - Assert that `v` is a `Some_Integer`.
#
if __debug__:
    def fact_is_some_integer(v):
        assert v.is_some_integer

        return True


#
#   fact_is_zero(v) - Assert that `v` is the `zero_integer` singleton.
#
if __debug__:
    def fact_is_zero(v):
        assert v.is_zero

        return True


#
#   Imports
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Private.Integer_V8  import  zero_integer
from    Capital.Private.Integer_V8  import  conjure_contrary_integer
from    Capital.Private.Integer_V8  import  conjure_keen_integer
from    Capital.Private.Integer_V8  import  conjure_negative_integer
from    Capital.Private.Integer_V8  import  conjure_positive_integer
from    Capital.Private.Integer_V8  import  conjure_some_integer


#
#   conjure_contrary_integer(v) - Conjure a `Contrary_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a *DIRECT* `int` instance, and less than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
#   EXCEPTIONS
#
#       If `v` is positive, throws a `ValueError`.
#
export(conjure_contrary_integer)


#
#   conjure_keen_integer(v) - Conjure a `Keen_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a *DIRECT* `int` instance, and greater than or equal to 0.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
#   EXCEPTIONS
#
#       If `v` is negative, throws a `ValueError`.
#
export(conjure_keen_integer)


#
#   conjure_negative_integer(v) - Conjure a `Negative_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a *DIRECT* `int` instance, and less than to 0.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
#   EXCEPTIONS
#
#       If `v` is positive or 0, throws a `ValueError`.
#
export(conjure_negative_integer


#
#   conjure_positive_integer(v) - Conjure a `Positive_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a *DIRECT* `int` instance, and greater than to 0.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
#   EXCEPTIONS
#
#       If `v` is negative or 0, throws a `ValueError`.
#
export(conjure_positive_integer)


#
#   conjure_some_integer(v) - Conjure a `Some_Integer`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a *DIRECT* `int` instance.
#
#       `v` may *NOT* be an instance of a subclass of `int`.
#
export(conjure_some_integer)


#
#   zero_integer - The singleton `Zero`.
#
export(zero_integer)
