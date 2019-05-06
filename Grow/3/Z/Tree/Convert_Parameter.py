#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Parameter - Convert Python Abstract Syntax Tree Parameters to Tree classes.
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
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Name                 import  convert_name_parameter
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Parameters_All
from    Z.Tree.Parameter                    import  create_Tree_Parameters_All


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer


#
#   convert_map_parameter
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
def convert_map_parameter(self):
    assert fact_is__native_none__OR__full_native_string(self)

    return self


#
#   convert_tuple_parameter
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
def convert_tuple_parameter(self):
    assert fact_is__native_none__OR__full_native_string(self)

    return self


#
#   convert_list_of_name_parameters
#
#       Convert a `list of Native_AbstractSyntaxTree_Name` (i.e.: `list of _ast.Name`) to a `list of SyntaxTree_Name`.
#
#       Each of the `Native_AbstractSyntaxTree_Name` (i.e.: `_ast.Name`) must have a context (i.e.: `.ctx` member)
#       of type `Native_AbstractSyntaxTree_Parameter`.
#
def convert_list_of_name_parameters(sequence):
    assert fact_is_some_native_list(sequence)

    return [convert_name_parameter(v)   for v in sequence]


#
#   convert_parameters_all
#
#       Convert a `Native_AbstractSyntaxTree_Parameters_All` (i.e.: `_ast.args`) to a `Tree_Parameters_All`.
#
assert Native_AbstractSyntaxTree_Parameters_All._attributes == (())
assert Native_AbstractSyntaxTree_Parameters_All._fields     == (('args', 'vararg', 'kwarg', 'defaults'))


def convert_parameters_all(self):
    assert fact_is_some_native_list                    (self.args)
    assert fact_is__native_none__OR__full_native_string(self.vararg)
    assert fact_is__native_none__OR__full_native_string(self.kwarg)
    assert fact_is_some_native_list                    (self.defaults)

    return create_Tree_Parameters_All(
               convert_list_of_name_parameters (self.args),
               convert_tuple_parameter         (self.vararg),
               convert_map_parameter           (self.kwarg),
               convert_some_list_of_expressions(self.defaults),
           )
