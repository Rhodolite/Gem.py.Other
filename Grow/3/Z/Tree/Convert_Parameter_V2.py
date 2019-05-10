#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Parameter_V2 - Convert Python Abstract Syntax Tree Parameters to Tree classes, Version 2.
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


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Native_Integer              import  fact_is_positive_native_integer
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Native_String               import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_All_Parameters
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name


#
#   convert_map_parameter(z, v)
#
#       "Convert" `None` to `None`.
#
#       "Convert" a `Full_Native_String` to the [same] `Full_Native_String`.
#
#   FUTURE:
#       Will convert a `Full_Native_String` to a `Tree_Map_Parameter`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`, and
#       a `Full_Native_String` to the [same] `Full_Native_String`.
#
def convert_map_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native_none__OR__full_native_string(v)

    return v


#
#   convert_name_parameter(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) to `Tree_Name`
#
#       The context (`.ctx` member) MUST BE a `Native_AbstractSyntaxTree_Parameter_Context`.
#
#       To handle other contexts, please see `convert_name_expression`.
#
assert Native_AbstractSyntaxTree_Name._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Name._fields     == (('id', 'ctx'))


def convert_name_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_native_integer(v.lineno)
    assert fact_is_avid_native_integer    (v.col_offset)

    assert fact_is_full_native_string                              (v.id)
    assert fact_is__native__abstract_syntax_tree__parameter_context(v.ctx)

    return z.create_Tree_Name(
               v.lineno,
               v.col_offset,

               v.id,
               z.convert_parameter_context(z, v.ctx),
           )


#
#   convert_parameter_tuple_0(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_All_Parameters` (i.e.: `_ast.args`) to a `Tree_All_Parameters`.
#
assert Native_AbstractSyntaxTree_All_Parameters._attributes == (())
assert Native_AbstractSyntaxTree_All_Parameters._fields     == (('args', 'vararg', 'kwarg', 'defaults'))


def convert_parameter_tuple_0(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_some_native_list                    (v.args)
    assert fact_is__native_none__OR__full_native_string(v.vararg)
    assert fact_is__native_none__OR__full_native_string(v.kwarg)
    assert fact_is_some_native_list                    (v.defaults)

    return z.create_Tree_All_Parameters(
               convert_some_list_of_name_parameters(z, v.args),
               convert_star_parameter              (z, v.vararg),
               convert_map_parameter               (z, v.kwarg),
               z.convert_some_list_of_expressions  (z, v.defaults),
           )


#
#   convert_star_parameter(z, v)
#
#       "Convert" `None` to `None`.
#
#       "Convert" a `Full_Native_String` to the [same] `Full_Native_String`.
#
#   FUTURE:
#       Will convert a `Full_Native_String` to `Tree_Star_Parameter`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`, and
#       a `Full_Native_String` to the [same] `Full_Native_String`.
#
def convert_star_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native_none__OR__full_native_string(v)

    return v


#
#   convert_some_list_of_name_parameters(z, v)
#
#       Convert a `Some_Native_List of Native_AbstractSyntaxTree_Name` (i.e.: `list of _ast.Name`) to a
#       `Some_Native_List of SyntaxTree_Name`.
#
#       Each of the `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) must have a context (i.e.: `.ctx` member)
#       of type `Native_AbstractSyntaxTree_Parameter`.
#
convert_some_list_of_name_parameters = (
        produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_name_parameter)
    )
