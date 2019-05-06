#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Zone - Functions to convert Python Abstract Syntax Tree Statements to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  creator
from    Capital.Core                        import  export
from    Capital.Core                        import  FATAL
from    Z.Parser.Global                     import  parser_globals
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


class Convert_Zone(object):
    __slots__ = ((
        #
        #   Aliases
        #
        'convert_full_list_of_module_aliases',      #   Function
        'convert_full_list_of_symbol_aliases',      #   Function
        'create_Tree_Module_Alias',                 #   Function
        'create_Tree_Symbol_Alias',                 #   Function

        #
        #   Statements
        #
        'convert_full_list_of_statements',          #   Function
        'convert_some_list_of_statements',          #   Function
        'convert_statement',                        #   Function

        'map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method',
                                                    #    Map { Native_AbstractSyntaxTree_* : Function }
    ))


    is_convert_zone = True


#
#   fact_is_convert_zone(v)     - Assert that `v` is a convert zone.
#
if __debug__:
    def fact_is_convert_zone(v):
        assert v.is_convert_zone

        return True



def FATAL_unknown_version(name, version):
    FATAL('Z/Tree/Convert_Zone.py: unknown tree {} version: {}', name, version)


def fill_convert_zone():
    alias_version         = parser_globals.alias_version
    argument_version      = parser_globals.argument_version
    comprehension_version = parser_globals.comprehension_version
    context_version       = parser_globals.context_version
    except_version        = parser_globals.except_version
    expression_version    = parser_globals.expression_version
    index_version         = parser_globals.index_version
    module_name_version   = parser_globals.module_name_version
    name_version          = parser_globals.name_version
    operator_version      = parser_globals.operator_version
    parameter_version     = parser_globals.parameter_version
    statement_version     = parser_globals.statement_version
    symbol_version        = parser_globals.symbol_version
    target_version        = parser_globals.target_version


    #
    #   Alias Version
    #
    if alias_version == 2:
        #
        #   Next two lines use "_V1" on purpose
        #
        from    Z.Tree.Alias_V1             import  create_Tree_Alias_Clause            as  create_Tree_Module_Alias
        from    Z.Tree.Alias_V1             import  create_Tree_Alias_Clause            as  create_Tree_Symbol_Alias

        from    Z.Tree.Convert_Alias_V2     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V2     import  convert_full_list_of_symbol_aliases
    elif alias_version == 3:
        from    Z.Tree.Alias_V3             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V3             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V3     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V3     import  convert_full_list_of_symbol_aliases
    elif alias_version == 4:
        from    Z.Tree.Alias_V4             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V4             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V4     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V4     import  convert_full_list_of_symbol_aliases
    elif alias_version == 5:
        from    Z.Tree.Alias_V5             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V5             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V5     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V5     import  convert_full_list_of_symbol_aliases
    elif alias_version == 6:
        from    Z.Tree.Alias_V6             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V6             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V6     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V6     import  convert_full_list_of_symbol_aliases
    else:
        FATAL_unknown_version('alias', alias_version)


    #
    #   Statements
    #
    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Statement_V2             import  convert_statement
        from    Z.Tree.Convert_Statement_V2             import  convert_full_list_of_statements
        from    Z.Tree.Convert_Statement_V2             import  convert_some_list_of_statements
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
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
        FATAL_unknown_version('statement', statement_version)


    if statement_version == 2:
        from    Z.Tree.Convert_Definition_V2            import  convert_class_definition
        from    Z.Tree.Convert_Definition_V2            import  convert_function_definition
    elif statement_version == 3:
        from    Z.Tree.Convert_Definition_V3            import  convert_class_definition
        from    Z.Tree.Convert_Definition_V3            import  convert_function_definition
    elif statement_version == 4:
        from    Z.Tree.Convert_Definition_V4            import  convert_class_definition
        from    Z.Tree.Convert_Definition_V4            import  convert_function_definition
    else:
        FATAL_unknown_version('statement', statement_version)

    if statement_version in ((2, 3)):
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
        FATAL_unknown_version('statement', statement_version)


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


    #
    #   ========================================  z  ========================================
    #
    z = convert_zone


    #
    #   Aliases
    #
    z.convert_full_list_of_module_aliases = convert_full_list_of_module_aliases
    z.convert_full_list_of_symbol_aliases = convert_full_list_of_symbol_aliases
    z.create_Tree_Module_Alias            = create_Tree_Module_Alias
    z.create_Tree_Symbol_Alias            = create_Tree_Symbol_Alias


    #
    #  Statements
    #
    z.convert_full_list_of_statements = convert_full_list_of_statements
    z.convert_some_list_of_statements = convert_some_list_of_statements
    z.convert_statement               = convert_statement

    z.map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method = (
            map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__pseudo_method
        )


    #
    #   Done
    #
    return z


@creator
def create_convert_zone():
    return Convert_Zone()


convert_zone = create_convert_zone()
