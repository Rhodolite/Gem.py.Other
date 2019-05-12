#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Conjure_Number - Conjure a `Number`.
#
#       A `Number` is a `Complex`, a `Float`,   an `Integer`, or a `Long` (python 2.*).
#
#       A `Number` is a `Commplex, a `Float` or an `Integer`              (python 3.*).
#
#   NOTE:
#
#       Has to be seperate from `Capital.Number` to avoid import loops:
#
#           conjure_number      needs   conjure_integer
#           conjure_integer     needs   Integer         needs   Trait_Number
#
#       If `conjure_number` and `TRAIT_Number` are in the same file, it causes import loops.
#


from    Capital.Complex                 import  conjure_complex
from    Capital.Core                    import  export
from    Capital.Float                   import  conjure_float
from    Capital.Integer                 import  conjure_integer
from    Capital.Native_Float            import  Native_Float
from    Capital.Native_Integer          import  Native_Integer
from    Capital.System                  import  is_python_2


if is_python_2:
    from    Capital.Native_Long         import  Native_Long
    from    Capital.Long                import  conjure_long


if __debug__:
    from    Capital.Fact                import  fact_is_ANY_native_number


#
#   conjure_number(v) - Conjure a `Number`, based on `v`.  Guarantees Uniqueness.
#
#       `v` must be a:
#
#           1)  `Native_Complex` (i.e.: `complex`),
#
#           2)  `Native_Float`   (i.e.: `float`),
#
#           3)  `Native_Integer` (i.e.: `int`), or a
#
#           4)  `Native_Long`    (i.e: `long`).                 #   Python 2.* only
#
#       `v` may *NOT* be an instance of a subclass of:
#
#           1)  `Native_Complex` (i.e.: `complex`),
#
#           2)  `Native_Float`   (i.e.: `float`),
#
#           3)  `Native_Integer` (i.e.: `int`), or
#
#           4)  `Native_Long` (i.e.: `long`).                   #   Python 2.* only
#
if is_python_2:
    @export
    def conjure_number(v):
        assert fact_is_ANY_native_number(v)

        v_type = type(v)

        if v_type is Native_Integer:
            return conjure_integer(v)

        if v_type is Native_Long:
            return conjure_long(v)

        if v_type is Native_Float:
            return conjure_float(v)

        return conjure_complex(v)
else:
    #
    #   Python 3.* does not have a `Native_Long` (i.e.: `long`) type.
    #
    @export
    def conjure_number(v):
        assert fact_is_ANY_native_number(v)

        v_type = type(v)

        if v_type is Native_Integer:
            return conjure_integer(v)

        if v_type is Native_Float:
            return conjure_float(v)

        return conjure_complex(v)
