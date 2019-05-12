#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Complex - Complex Interface.  `Complex`es are Unique.
#


from    Capital.Core                    import  export


#
#   interface Complex
#       method
#           python_code() => Full_Native_String
#
#       attribute
#           native_complex_subclass : Native_Complex
#
#       debug
#           is_complex : Boolean
#
class TRAIT_Complex(object):
    __slots__ = (())


    if __debug__:
        is_complex = True


#
#   USAGE:
#
#       conjure_complex(v)                  #   Conjure a `Complex`.
#
#       v.native_complex_subclass           #   The `Native_Complex` that `v` represents (may be a subclass of
#                                           #   `Native_Complex`).
#
#       v.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `Native_Complex` with the same value as the
#                                           #   `Native_Complex` that `v` wraps.
#


#
#   USAGE (debug mode):
#
#       v.is_complex                        #   Test if `v` is an `Complex`.
#
#       assert fact_is_complex(v)           #   Assert that `v` is an `Complex`.
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           <0j>                - In a boolean context, evaluates to `False`.
#           All other complexs  - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           0j                          - In a boolean context, evaluates to `False`.
#           any other native complex    - In a boolean context, evaluates to `True`.
#


#
#   fact_is_complex(v) - Assert that `v` is an `Complex`.
#
if __debug__:
    def fact_is_complex(v):
        assert v.is_complex

        return True

#
#   Imports
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Private.Complex_V1  import  conjure_complex


#
#   conjure_complex(v) - Conjure a `Complex`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a `Native_Complex` (i.e.: `complex`).
#
#       `v` may *NOT* be an instance of a subclass of `Native_Complex` (i.e.: `complex`).
#
export(conjure_complex)
