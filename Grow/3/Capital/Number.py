#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Number - Number Interface.  `Number`s are Unique.
#
#       A `Number` is a `Float`,   an `Integer`, or a `Long` (python 2.*).
#
#       A `Number` is a `Float` or an `Integer`              (python 3.*).
#   
#


from    Capital.Core                    import  export


#
#   interface Number
#       debug
#           is_number : Boolean
#
class TRAIT_Number(object):
    __slots__ = (())


    if __debug__:
        is_number = True


#
#   USAGE (debug mode):
#
#       v.is_number                         #   Test if `v` is a `Number`.
#
#       assert fact_is_number(v)            #   Assert that `v` is an `Number`.
#
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           `zero_float`        - In a boolean context, evaluates to `False`.
#           `zero_integer`      - In a boolean context, evaluates to `False`.
#           `zero_long`         - In a boolean context, evaluates to `False`.
#           All other numbers   - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           0                           - In a boolean context, evaluates to `False`.
#           0L                          - In a boolean context, evaluates to `False`.
#           0.0                         - In a boolean context, evaluates to `False`.
#           any other native number     - In a boolean context, evaluates to `True`.
#


#
#   fact_is_number(v) - Assert that `v` is a `Number`.
#
if __debug__:
    def fact_is_number(v):
        assert v.is_number

        return True
