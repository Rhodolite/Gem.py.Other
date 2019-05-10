#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Literal_V2 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_native_integer
    from    Capital.Fact                        import  fact_is_substantial_native_integer
    from    Capital.Native_String               import  fact_is_some_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String_Literal


#
#   convert_string_literal(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_String_Literal` (i.e.: `_ast.Str`) to a `Tree_String`.
#
assert Native_AbstractSyntaxTree_String_Literal._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String_Literal._fields     == (('s',))


def convert_string_literal(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_some_native_string(v.s)

    return z.create_Tree_String(v.lineno, v.col_offset, v.s)
