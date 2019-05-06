#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Definition_V3 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           The class or function name is `FullNativeList`.
#
#       Version 3:
#
#           The class or function name is `Parser_Symbol`.
#


from    Z.Parser.Symbol                     import  conjure_parser_symbol
from    Z.Tree.Convert_Decorator            import  convert_some_list_of_decorators
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Parameter            import  convert_parameters_all
from    Z.Tree.Convert_Statement            import  convert_full_list_of_statements
from    Z.Tree.Definition_V2                import  create_Tree_Class_Definition
from    Z.Tree.Definition_V2                import  create_Tree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all


#
#   convert_class_definition
#
#       Convert a `Native_AbstractSyntaxTree_Class_Definition` (i.e.: `_ast.ClassDef`) to a `Tree_Class_Definition`.
#
assert Native_AbstractSyntaxTree_Class_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Class_Definition._fields     == (('name', 'bases', 'body', 'decorator_list'))


def convert_class_definition(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string(self.name)
    assert fact_is_some_native_list  (self.bases)
    assert fact_is_full_native_list  (self.body)
    assert fact_is_some_native_list  (self.decorator_list)

    return create_Tree_Class_Definition(
               self.lineno,
               self.col_offset,

               conjure_parser_symbol           (self.name),
               convert_some_list_of_expressions(self.bases),
               convert_full_list_of_statements (self.body),
               convert_some_list_of_decorators (self.decorator_list),
           )


#
#   convert_function_definition
#
#       Convert a `Native_AbstractSyntaxTree_Function_Definition` (i.e.: `_ast.FunctionDef`) to a
#       `Tree_Function_Definition`.
#
assert Native_AbstractSyntaxTree_Function_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Function_Definition._fields     == (('name', 'args', 'body', 'decorator_list'))


def convert_function_definition(self):
    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is_full_native_string                           (self.name)
    assert fact_is__native__abstract_syntax_tree__parameters_all(self.args)
    assert fact_is_full_native_list                             (self.body)
    assert fact_is_some_native_list                             (self.decorator_list)

    return create_Tree_Function_Definition(
               self.lineno,
               self.col_offset,

               conjure_parser_symbol          (self.name),
               convert_parameters_all         (self.args),
               convert_full_list_of_statements(self.body),
               convert_some_list_of_decorators(self.decorator_list),
           )
