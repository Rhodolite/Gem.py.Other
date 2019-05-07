#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Parameter_V1 - Convert Python Abstract Syntax Tree Parameters to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       The following conversions are done in this file:
#
#           For `Native_AbstractSyntaxTree_Parameters_All` (i.e.: `_ast.arguments`):
#
#               convert_tuple_parameter - "Converts" the `.varargs` member.
#
#                   The `.varargs` member is either `None` or a `NativeString`.
#
#                   For version 1, no conversion is done, these are left as is.
#
#
#               convert_map_parameter - "Converts" the `.kwargs` member.
#
#                   The `.kwargs` member is either `None` or a `NativeString`.
#
#                   For version 1, no conversion is done, these are left as is.
#


from    Capital.Core                        import  FATAL
from    Capital.Core                        import  trace
from    Z.Tree.Convert_Expression_V1        import  convert_some_list_of_expressions
from    Z.Tree.Convert_Name_V1              import  convert_name_parameter
from    Z.Tree.Parameter                    import  create_Tree_Parameters_All
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Parameters_All


#
#   convert_map_parameter(v)
#
#       "Convert" `None` to `None`.
#
#       "Convert" a full `NativeString` to the [same] full `NativeString`
#
#   FUTURE:
#       Will convert `NativeString` to `Tree_Map_Parameter`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`, and
#       a full `NativeString` to the [same] full `NativeString`.
#
def convert_map_parameter(v):
    assert fact_is__native_none__OR__full_native_string(v)

    return v


#
#   convert_tuple_parameter(v)
#
#       "Convert" `None` to `None`.
#
#       "Convert" a full `NativeString` to the [same] full `NativeString`
#
#   FUTURE:
#       Will convert `NativeString` to `Tree_Tuple_Parameter`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`, and
#       a full `NativeString` to the [same] full `NativeString`.
#
def convert_tuple_parameter(v):
    assert fact_is__native_none__OR__full_native_string(v)

    return v


#
#   convert_list_of_name_parameters(v)
#
#       Convert a `list of Native_AbstractSyntaxTree_Name` (i.e.: `list of _ast.Name`) to a `list of SyntaxTree_Name`.
#
#       Each of the `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) must have a context (i.e.: `.ctx` member)
#       of type `Native_AbstractSyntaxTree_Parameter`.
#
convert_list_of_name_parameters = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_name_parameter)
    )


#
#   convert_parameters_all(v)
#
#       Convert a `Native_AbstractSyntaxTree_Parameters_All` (i.e.: `_ast.args`) to a `Tree_Parameters_All`.
#
assert Native_AbstractSyntaxTree_Parameters_All._attributes == (())
assert Native_AbstractSyntaxTree_Parameters_All._fields     == (('args', 'vararg', 'kwarg', 'defaults'))


def convert_parameters_all(v):
    assert fact_is_some_native_list                    (v.args)
    assert fact_is__native_none__OR__full_native_string(v.vararg)
    assert fact_is__native_none__OR__full_native_string(v.kwarg)
    assert fact_is_some_native_list                    (v.defaults)

    return create_Tree_Parameters_All(
               convert_list_of_name_parameters (v.args),
               convert_tuple_parameter         (v.vararg),
               convert_map_parameter           (v.kwarg),
               convert_some_list_of_expressions(v.defaults),
           )
