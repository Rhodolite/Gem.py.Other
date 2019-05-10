#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Literal_V1 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Literal_V1                   import  create_Tree_String


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Native_String               import  fact_is_some_native_string
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String_Literal


#
#   convert_string_literal(v)
#
#       Convert a `Native_AbstractSyntaxTree_String_Literal` (i.e.: `_ast.Str`) to a `Tree_String`.
#
assert Native_AbstractSyntaxTree_String_Literal._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String_Literal._fields     == (('s',))


def convert_string_literal(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_some_native_string(v.s)

    return create_Tree_String(v.lineno, v.col_offset, v.s)
