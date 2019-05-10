#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Definition_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Decorator_V1         import  convert_some_list_of_decorators
from    Z.Tree.Convert_Expression_V1        import  convert_some_list_of_expressions
from    Z.Tree.Convert_Parameter_V1         import  convert_parameter_tuple_0
from    Z.Tree.Convert_Statement_V1         import  convert_full_list_of_statements
from    Z.Tree.Definition_V1                import  create_Tree_Class_Definition
from    Z.Tree.Definition_V1                import  create_Tree_Function_Definition


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Native_String               import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__all_parameters
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition


#
#   convert_class_definition(v)
#
#       Convert a `Native_AbstractSyntaxTree_Class_Definition` (i.e.: `_ast.ClassDef`) to a `Tree_Class_Definition`.
#
assert Native_AbstractSyntaxTree_Class_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Class_Definition._fields     == (('name', 'bases', 'body', 'decorator_list'))


def convert_class_definition(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string(v.name)
    assert fact_is_some_native_list  (v.bases)
    assert fact_is_full_native_list  (v.body)
    assert fact_is_some_native_list  (v.decorator_list)

    return create_Tree_Class_Definition(
               v.lineno,
               v.col_offset,

               v.name,
               convert_some_list_of_expressions(v.bases),
               convert_full_list_of_statements (v.body),
               convert_some_list_of_decorators (v.decorator_list),
           )


#
#   convert_function_definition(V)
#
#       Convert a `Native_AbstractSyntaxTree_Function_Definition` (i.e.: `_ast.FunctionDef`) to a
#       `Tree_Function_Definition`.
#
assert Native_AbstractSyntaxTree_Function_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Function_Definition._fields     == (('name', 'args', 'body', 'decorator_list'))


def convert_function_definition(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string                           (v.name)
    assert fact_is__native__abstract_syntax_tree__all_parameters(v.args)
    assert fact_is_full_native_list                             (v.body)
    assert fact_is_some_native_list                             (v.decorator_list)

    return create_Tree_Function_Definition(
               v.lineno,
               v.col_offset,

               v.name,
               convert_parameter_tuple_0      (v.args),
               convert_full_list_of_statements(v.body),
               convert_some_list_of_decorators(v.decorator_list),
           )
