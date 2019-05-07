#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Definition_V4 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           Uses `FullNativeList of Tree_Statement` for a suite of statements.
#
#       Version 4:
#
#           Uses `Tree_Suite` for a suite of statements.
#


from    Z.Parser.Symbol                         import  conjure_parser_symbol
from    Z.Tree.Convert_Compound_Statement_V4    import  convert_suite
from    Z.Tree.Convert_Parameter_V2             import  convert_parameters_all


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition


#
#   convert_class_definition(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Class_Definition` (i.e.: `_ast.ClassDef`) to a `Tree_Class_Definition`.
#
assert Native_AbstractSyntaxTree_Class_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Class_Definition._fields     == (('name', 'bases', 'body', 'decorator_list'))


def convert_class_definition(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string(v.name)
    assert fact_is_some_native_list  (v.bases)
    assert fact_is_full_native_list  (v.body)
    assert fact_is_some_native_list  (v.decorator_list)

    return z.create_Tree_Class_Definition(
               v.lineno,
               v.col_offset,

               conjure_parser_symbol             (v.name),
               z.convert_some_list_of_expressions(z, v.bases),
               convert_suite                     (z, v.body),
               z.convert_some_list_of_decorators (z, v.decorator_list),
           )


#
#   convert_function_definition(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Function_Definition` (i.e.: `_ast.FunctionDef`) to a
#       `Tree_Function_Definition`.
#
assert Native_AbstractSyntaxTree_Function_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Function_Definition._fields     == (('name', 'args', 'body', 'decorator_list'))


def convert_function_definition(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string                           (v.name)
    assert fact_is__native__abstract_syntax_tree__parameters_all(v.args)
    assert fact_is_full_native_list                             (v.body)
    assert fact_is_some_native_list                             (v.decorator_list)

    return z.create_Tree_Function_Definition(
               v.lineno,
               v.col_offset,

               conjure_parser_symbol            (v.name),
               convert_parameters_all           (v.args),
               convert_suite                    (z, v.body),
               z.convert_some_list_of_decorators(z, v.decorator_list),
           )
