#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Argument_V3 - Convert Python Abstract Syntax Tree [Function] Arguments to Tree classes, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2 & Version 3.
#
#       Version 2:
#
#           The first argument to `create_Tree_Keyword_Argument` is a `Full_Native_String`.
#
#       Version 3:
#
#           The first argument to `create_Tree_Keyword_Argument` is a `Parser_Symbol`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Keyword_Argument


#
#   convert_keyword_argument(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Keyword_Argument (i.e.: `_ast.keyword`) to a `Tree_Keyword_Argument`.
#
assert Native_AbstractSyntaxTree_Keyword_Argument._attributes == (())
assert Native_AbstractSyntaxTree_Keyword_Argument._fields     == (('arg', 'value'))


def convert_keyword_argument(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_string                                  (v.arg)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return z.create_Tree_Keyword_Argument(
               z.conjure_parser_symbol(z, v.arg),
               z.convert_expression   (z, v.value),
           )


#
#   convert_some_list_of_keywords(sequence)
#
#       Convert `Native_List of Native_AbstractSyntaxTree_Keyword_Argument` (i.e.: `list of _ast.keyword`) to a
#       `Native_List of Tree_Keyword_Argument`
#
convert_some_list_of_keyword_arguments = (
        produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_keyword_argument)
    )
