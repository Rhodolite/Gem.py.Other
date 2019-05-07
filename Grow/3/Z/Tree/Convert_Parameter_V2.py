#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Parameter_V2 - Convert Python Abstract Syntax Tree Parameters to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       The following conversions are done in this file:
#
#           For `Native_AbstractSyntaxTree_Parameters_All` (i.e.: `_ast.arguments`):
#
#               convert_tuple_parameter - "Converts" the `.varargs` member.
#
#                   The `.varargs` member is either `None` or a `Full_Native_String`.
#
#                   For version 1, no conversion is done, these are left as is.
#
#
#               convert_map_parameter - "Converts" the `.kwargs` member.
#
#                   The `.kwargs` member is either `None` or a `Full_Native_String`.
#
#                   For version 1, no conversion is done, these are left as is.
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
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Parameters_All


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
#   convert_tuple_parameter(z, v)
#
#       "Convert" `None` to `None`.
#
#       "Convert" a `Full_Native_String` to the [same] `Full_Native_String`.
#
#   FUTURE:
#       Will convert a `Full_Native_String` to `Tree_Tuple_Parameter`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`, and
#       a `Full_Native_String` to the [same] `Full_Native_String`.
#
def convert_tuple_parameter(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native_none__OR__full_native_string(v)

    return v


#
#   convert_parameters_all(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Parameters_All` (i.e.: `_ast.args`) to a `Tree_Parameters_All`.
#
assert Native_AbstractSyntaxTree_Parameters_All._attributes == (())
assert Native_AbstractSyntaxTree_Parameters_All._fields     == (('args', 'vararg', 'kwarg', 'defaults'))


def convert_parameters_all(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_some_native_list                    (v.args)
    assert fact_is__native_none__OR__full_native_string(v.vararg)
    assert fact_is__native_none__OR__full_native_string(v.kwarg)
    assert fact_is_some_native_list                    (v.defaults)

    return z.create_Tree_Parameters_All(
               z.convert_some_list_of_name_parameters(z, v.args),
               convert_tuple_parameter               (z, v.vararg),
               convert_map_parameter                 (z, v.kwarg),
               z.convert_some_list_of_expressions    (z, v.defaults),
           )
