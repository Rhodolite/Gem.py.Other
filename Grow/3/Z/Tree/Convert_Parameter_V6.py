#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Parameter_V6 - Convert Python Abstract Syntax Tree Parameters to Tree classes, Version 6.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 4:
#
#           `convert_parameter_tuple_0` converts to `Tree_All_Parameters`
#
#       Version 5:
#
#           `convert_parameter_tuple_0` converts to `Tree_Parameter_Tuple_0`
#


from    Z.Parser.None                       import  parser_none


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_native_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_native_integer
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Native_String               import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__name
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_All_Parameters
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name


#
#   convert_map_parameter(z, v, value)
#
#       Convert a `v` and `value` to `Tree_Keyword_Parameter`.
#
#       `v` must be a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`), and the context (`.ctx` member) MUST BE a
#       `Native_AbstractSyntaxTree_Parameter_Context`.
#
#   SEE ALSO
#
#       `convert_name_parameter` below, which is very similiar, but without a `value`.
#
def convert_keyword_parameter(z, v, value):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_full_native_string                                  (v.id)
    assert fact_is__native__abstract_syntax_tree__parameter_context    (v.ctx)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(value)

    return z.create_Tree_Keyword_Parameter(
               v.lineno,
               v.col_offset,

               z.conjure_parser_symbol(z, v.id),
               z.convert_expression   (z, value),
           )


#
#   convert_map_parameter(z, v)
#
#       Convert `v` to a `Tree_Parameter_0`.
#
#       Specifically:
#
#           1)  Convert `None` to `parser_none`.
#
#           2)  Convert a `Full_Native_String` to a `Tree_Map_Parameter`.
#
def convert_map_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native_none__OR__full_native_string(v)

    if v is None:
        return parser_none

    return z.create_Tree_Map_Parameter(
               z.conjure_parser_symbol(z, v),
           )


#
#   convert_name_parameter(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to `Tree_Normal_Parameter`
#
#       The context (`.ctx` member) MUST BE a `Native_AbstractSyntaxTree_Parameter_Context`.
#
#       To handle other contexts, please see `convert_name_expression`.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer   (v.lineno)
    assert fact_is_substantial_native_integer(v.col_offset)

    assert fact_is_full_native_string                              (v.id)
    assert fact_is__native__abstract_syntax_tree__parameter_context(v.ctx)

    return z.create_Tree_Normal_Parameter(
               v.lineno,
               v.col_offset,

               z.conjure_parser_symbol(z, v.id),
           )


#
#   convert_parameter_tuple_0(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_All_Parameters` (i.e.: `_ast.args`) to a `Tree_Parameter_Tuple_0`.
#
assert Native_AbstractSyntaxTree_All_Parameters._attributes == (())
assert Native_AbstractSyntaxTree_All_Parameters._fields     == (('args', 'vararg', 'kwarg', 'defaults'))


def convert_parameter_tuple_0(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_some_native_list                    (v.args)
    assert fact_is__native_none__OR__full_native_string(v.vararg)
    assert fact_is__native_none__OR__full_native_string(v.kwarg)
    assert fact_is_some_native_list                    (v.defaults)

    total = 0

    #
    #<name-parameters>
    #
    #   Also handles `Tree_Keyword_Parameter`
    #
    start_keywords = len(v.args) - len(v.defaults)

    for [index, w] in enumerate(v.args):
        if index < start_keywords:
            x = convert_name_parameter(z, w)
        else:
            x = convert_keyword_parameter(z, w, v.defaults[index - start_keywords])

        if total == 0:
            first = x
            total = 1
        elif total == 1:
            many  = [first, x]
            total = 2
        else:
            many.append(x)
    #</name-parameters>

    #
    #<star-parameter>
    #
    x = convert_star_parameter(z, v.vararg)

    if x.has_tree_parameter:
        if total == 0:
            first = x
            total = 1
        elif total == 1:
            many  = [first, x]
            total = 2
        else:
            many.append(x)
    #</star-parameter>


    #
    #<map-parameter>
    #
    x = convert_map_parameter(z, v.kwarg)

    if x.has_tree_parameter:
        if total == 0:
            total = 1
            first = x
        elif total == 1:
            many  = [first, x]
            total = 2
        else:
            many.append(x)
    #</map-parameter>

    if total == 0:
        return parser_none

    if total == 1:
        return first

    return z.create_Tree_Parameter_Tuple(many)


#
#   convert_star_parameter(z, v)
#
#       Convert `v` to a `Tree_Parameter_0`.
#
#       Specifically:
#
#           1)  Convert `None` to `parser_none`.
#
#           2)  Convert a `Full_Native_String` to a `Tree_Star_Parameter`.
#
def convert_star_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native_none__OR__full_native_string(v)

    if v is None:
        return parser_none

    return z.create_Tree_Star_Parameter(
               z.conjure_parser_symbol(z, v),
           )
