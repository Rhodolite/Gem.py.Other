#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Literal_V1 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Literal_V1                   import  create_Tree_Number_Literal
from    Z.Tree.Literal_V1                   import  create_Tree_String_Literal


if __debug__:
    from    Capital.Fact                        import  fact_is_ANY_native_number
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Capital.Native_String               import  fact_is_native_string
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String_Literal


#
#   convert_number_literal(v)
#
#       Convert a `Native_AbstractSyntaxTree_Number` (i.e.: `_ast.Num`) to a `Tree_Number_Literal`.
#
assert Native_AbstractSyntaxTree_Number._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Number._fields     == (('n',))


def convert_number_literal(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_ANY_native_number(v.n)

    return create_Tree_Number_Literal(v.lineno, v.col_offset, v.n)


#
#   convert_string_literal(v)
#
#       Convert a `Native_AbstractSyntaxTree_String_Literal` (i.e.: `_ast.Str`) to a `Tree_String_Literal`.
#
assert Native_AbstractSyntaxTree_String_Literal._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_String_Literal._fields     == (('s',))


def convert_string_literal(v):
    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_native_string(v.s)

    return create_Tree_String_Literal(v.lineno, v.col_offset, v.s)
