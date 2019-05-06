#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#

assert 0

#
#   Z.Tree.Convert_Statement_V1 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


#
#<order>
#
#   NOTE:
#       TO avoid import loops, the following have to appear *before* other imports:
#
#           convert_full_list_of_statements
#           convert_some_list_of_statements
#           convert_statement
#
#       This is so other files can import the functions below from this file.
#


#
#   convert_statement(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) instance to an instance of a class that implements
#       `Tree_Statement`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_statement(v):
    convert_statement__pseudo_method = (
            map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method[type(v)]
        )

    return convert_statement__pseudo_method(v)


#
#   convert_full_list_of_statements(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `NativeList of Tree_Statement`.
#
convert_full_list_of_statements = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_statement)


#
#   convert_some_list_of_statements(sequence)
#
#       Convert a `NativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `NativeList of Tree_Statement`.
#
convert_some_list_of_statements = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_statement)


#</order>


from    Capital.Core                        import  FATAL
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer


#
#   Import the version of tree statements we want to use.
#
from    Z.Parser.Global                 import  parser_globals


statement_version = parser_globals.statement_version


if statement_version == 1:
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_assert_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_assign_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_break_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_continue_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_delete_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_execute_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_expression_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_global_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_from_import_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_import_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_modify_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_pass_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_print_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_raise_statement
    from    Z.Tree.Convert_Simple_Statement_V1      import  convert_return_statement
elif statement_version in ((2, 3, 4)):
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_assert_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_assign_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_break_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_continue_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_delete_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_execute_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_expression_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_global_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_from_import_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_import_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_modify_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_pass_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_print_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_raise_statement
    from    Z.Tree.Convert_Simple_Statement_V2      import  convert_return_statement
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Statement.py: unknown tree statement version: {}', statement_version)


if statement_version == 1:
    from    Z.Tree.Convert_Definition_V1            import  convert_class_definition
    from    Z.Tree.Convert_Definition_V1            import  convert_function_definition
elif statement_version == 2:
    from    Z.Tree.Convert_Definition_V2            import  convert_class_definition
    from    Z.Tree.Convert_Definition_V2            import  convert_function_definition
elif statement_version == 3:
    from    Z.Tree.Convert_Definition_V3            import  convert_class_definition
    from    Z.Tree.Convert_Definition_V3            import  convert_function_definition
elif statement_version == 4:
    from    Z.Tree.Convert_Definition_V4            import  convert_class_definition
    from    Z.Tree.Convert_Definition_V4            import  convert_function_definition
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Statement.py: unknown tree statement version: {}', statement_version)


if statement_version == 1:
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_for_statement
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_if_statement
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_try_except_statement
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_try_finally_statement
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_while_statement
    from    Z.Tree.Convert_Compound_Statement_V1    import  convert_with_statement
elif statement_version in ((2, 3)):
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_for_statement
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_if_statement
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_try_except_statement
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_try_finally_statement
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_while_statement
    from    Z.Tree.Convert_Compound_Statement_V2    import  convert_with_statement
elif statement_version == 4:
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_for_statement
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_if_statement
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_try_except_statement
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_try_finally_statement
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_while_statement
    from    Z.Tree.Convert_Compound_Statement_V4    import  convert_with_statement
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Statement.py: unknown tree statement version: {}', statement_version)


#
#   map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_statement" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method = {
        Native_AbstractSyntaxTree_Assert_Statement      : convert_assert_statement,
        Native_AbstractSyntaxTree_Assign_Statement      : convert_assign_statement,
        Native_AbstractSyntaxTree_Break_Statement       : convert_break_statement,
        Native_AbstractSyntaxTree_Class_Definition      : convert_class_definition,
        Native_AbstractSyntaxTree_Continue_Statement    : convert_continue_statement,
        Native_AbstractSyntaxTree_Delete_Statement      : convert_delete_statement,
        Native_AbstractSyntaxTree_Execute_Statement     : convert_execute_statement,
        Native_AbstractSyntaxTree_Expression_Statement  : convert_expression_statement,
        Native_AbstractSyntaxTree_For_Statement         : convert_for_statement,
        Native_AbstractSyntaxTree_From_Import_Statement : convert_from_import_statement,
        Native_AbstractSyntaxTree_Function_Definition   : convert_function_definition,
        Native_AbstractSyntaxTree_Global_Statement      : convert_global_statement,
        Native_AbstractSyntaxTree_If_Statement          : convert_if_statement,
        Native_AbstractSyntaxTree_Import_Statement      : convert_import_statement,
        Native_AbstractSyntaxTree_Modify_Statement      : convert_modify_statement,
        Native_AbstractSyntaxTree_Pass_Statement        : convert_pass_statement,
        Native_AbstractSyntaxTree_Print_Statement       : convert_print_statement,
        Native_AbstractSyntaxTree_Raise_Statement       : convert_raise_statement,
        Native_AbstractSyntaxTree_Return_Statement      : convert_return_statement,
        Native_AbstractSyntaxTree_Try_Except_Statement  : convert_try_except_statement,
        Native_AbstractSyntaxTree_Try_Finally_Statement : convert_try_finally_statement,
        Native_AbstractSyntaxTree_While_Statement       : convert_while_statement,
        Native_AbstractSyntaxTree_With_Statement        : convert_with_statement,
    }
