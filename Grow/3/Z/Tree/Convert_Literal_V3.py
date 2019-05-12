#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Literal_V3 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2 & Version 3.
#
#       Version 1:
#
#           1)  The third parameter to `z.create_Tree_Number_Literal` is a
#               `Native_Float | Native_Integer | Native_Long`.
#
#           2)  The third parameter to `z.create_Tree_String_Literal` is a `Native_String`.
#
#       Version 2:
#
#           1)  The third parameter to `z.create_Tree_Number_Literal` is a `Number`.
#
#           2)  The third parameter to `z.create_Tree_String_Literal` is a `String`.
#


from    Capital.Conjure_Number                  import  conjure_number
from    Capital.String                          import  conjure_string


if __debug__:
    from    Capital.Fact                        import  fact_is_ANY_native_number
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Capital.Native_String               import  fact_is_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String_Literal


#
#   convert_number_literal(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Number` (i.e.: `_ast.Num`) to a `Tree_Number_Literal`.
#
assert Native_AbstractSyntaxTree_Number._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Number._fields     == (('n',))


def convert_number_literal(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_ANY_native_number(v.n)

    return z.create_Tree_Number_Literal(
               v.lineno,
               v.col_offset,

               conjure_number(v.n),
           )


#
#   convert_string_literal(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_String_Literal` (i.e.: `_ast.Str`) to a `Tree_String_Literal`.
#
assert Native_AbstractSyntaxTree_String_Literal._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String_Literal._fields     == (('s',))


def convert_string_literal(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_native_string(v.s)

    return z.create_Tree_String_Literal(
               v.lineno,
               v.col_offset,

               conjure_string(v.s),
           )
