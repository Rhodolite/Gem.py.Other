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
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Backquote_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Call_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Ellipsis_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Extended_Slice_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Generator_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Lambda_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Simple_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Slice_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression


class Convert_Zone(object):
    __slots__ = ((
        #
        #   Argument
        #
        'convert_some_list_of_keyword_arguments',   #   Function

        'create_Tree_Keyword_Argument',             #   Function


        #
        #   Alias
        #
        'convert_full_list_of_module_aliases',      #   Function
        'convert_full_list_of_symbol_aliases',      #   Function

        'create_Tree_Module_Alias',                 #   Function
        'create_Tree_Symbol_Alias',                 #   Function


        #
        #   Comprehension
        #
        'convert_full_list_of_comprehensions',      #   Function

        'create_Tree_Comprehension_Clause',         #   Function


        #
        #   Context
        #
        'convert_delete_load_OR_store_context',     #   None | Function
        'convert_parameter_context',                #   None | Function

        'tree_delete_context',                      #   None | Tree_Context
        'tree_parameter_context',                   #   None | Tree_Context

        'map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context',
                                                    #   None | Map { Native_AbstractSyntaxTree_* : Tree_Context }

        'map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context',
                                                    #   None | Map { Native_AbstractSyntaxTree_* : Tree_Context }


        #
        #   Decorator
        #
        'convert_some_list_of_decorators',          #   Function

        #
        #   Expression
        #
        'convert_full_list_of_expressions',         #   Function
        'convert_some_list_of_expressions',         #   Function
        'convert_expression',                       #   Function
        'convert_none_OR_expression',               #   Function

        'map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function',
                                                    #    Map { Native_AbstractSyntaxTree_* : Function }

        #
        #   Index
        #
        'convert_index_clause',                     #   Function

        'create_Tree_Extended_Slice_Index',         #   Function
        'create_Tree_Simple_Index',                 #   Function
        'create_Tree_Slice_Index',                  #   Function

        'tree_ellipses_index',                      #   Tree_Ellipses_Index

        'map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function',
                                                    #    Map { Native_AbstractSyntaxTree_* : Function }


        #
        #   Name
        #
        'convert_some_list_of_name_parameters',


        #
        #   Parameter
        #
        'convert_parameters_all',
        

        #
        #   Statement
        #
        'convert_full_list_of_except_clauses',      #   Function
        'convert_full_list_of_statements',          #   Function
        'convert_some_list_of_statements',          #   Function
        'convert_statement',                        #   Function

        'create_Tree_Assert_Statement',             #   Function
        'create_Tree_Assign_Statement',             #   Function
        'create_Tree_Break_Statement',              #   Function
        'create_Tree_Class_Definition',             #   Function
        'create_Tree_Continue_Statement',           #   Function
        'create_Tree_Delete_Statement',             #   Function
        'create_Tree_Except_Handler',               #   Function
        'create_Tree_Execute_Statement',            #   Function
        'create_Tree_Expression_Statement',         #   Function
        'create_Tree_For_Statement',                #   Function
        'create_Tree_From_Import_Statement',        #   Function
        'create_Tree_Function_Definition',          #   Function
        'create_Tree_Global_Statement',             #   Function
        'create_Tree_If_Statement',                 #   Function
        'create_Tree_Import_Statement',             #   Function
        'create_Tree_Modify_Statement',             #   Function
        'create_Tree_Pass_Statement',               #   Function
        'create_Tree_Print_Statement',              #   Function
        'create_Tree_Raise_Statement',              #   Function
        'create_Tree_Return_Statement',             #   Function
        'create_Tree_Try_Except_Statement',         #   Function
        'create_Tree_Try_Finally_Statement',        #   Function
        'create_Tree_While_Statement',              #   Function
        'create_Tree_With_Statement',               #   Function

        'map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function',
                                                    #    Map { Native_AbstractSyntaxTree_* : Function }


        #
        #   Suite
        #
        'create_Tree_Suite',                        #   None | Function


        #
        #   Target
        #
        'convert_full_list_of_targets',             #   Function
        'convert_none_OR_target',                   #   Function
        'convert_target',                           #   Function

        'create_Tree_Attribute',                    #   None | Function

        'map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function',
                                                    #    Map { Native_AbstractSyntaxTree_* : Function }
    ))


    is_convert_zone = True


#
#   fact_is_convert_zone(v)     - Assert that `v` is a convert zone.
#
if __debug__:
    @export
    def fact_is_convert_zone(v):
        assert v.is_convert_zone

        return True



def FATAL_unknown_version(name, version):
    FATAL('Z/Tree/Convert_Zone.py: unknown tree {} version: {}', name, version)


@export
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
    #   Argument
    #
    if argument_version == 2:
        from    Z.Tree.Convert_Argument_V2  import  convert_some_list_of_keyword_arguments
    elif argument_version == 3:
        from    Z.Tree.Convert_Argument_V3  import  convert_some_list_of_keyword_arguments
    else:
        FATAL_unknown_version('argument', argument_version)


    if argument_version == 2:
        from    Z.Tree.Argument_V1          import  create_Tree_Keyword_Argument
    elif argument_version == 3:
        from    Z.Tree.Argument_V3          import  create_Tree_Keyword_Argument
    else:
        FATAL_unknown_version('argument', argument_version)
        

    #
    #   Alias
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
    #   Comprehension
    #
    from    Z.Tree.Convert_Comprehension_V2 import  convert_full_list_of_comprehensions

    from    Z.Tree.Comprehension_V1         import  create_Tree_Comprehension_Clause        #   "_V1" on purpose.

    
    #
    #   Context
    #
    if context_version == 0:
        tree_delete_context    = None
        tree_parameter_context = None
    elif context_version == 2:
        from    Z.Tree.Context_V1       import  tree_delete_context
        from    Z.Tree.Context_V1       import  tree_load_context
        from    Z.Tree.Context_V1       import  tree_parameter_context
        from    Z.Tree.Context_V1       import  tree_store_context
    elif context_version == 3:
        from    Z.Tree.Context_V3       import  Tree_Context_Enumeration

        tree_delete_context    = Tree_Context_Enumeration.delete
        tree_load_context      = Tree_Context_Enumeration.load
        tree_parameter_context = Tree_Context_Enumeration.parameter
        tree_store_context     = Tree_Context_Enumeration.store
    else:
        FATAL_unknown_version('context', context_version)


    if context_version == 0:
        convert_delete_load_OR_store_context = None
        convert_parameter_context            = None
    elif context_version in ((2, 3)):
        from    Z.Tree.Convert_Context_V2   import  convert_delete_load_OR_store_context
        from    Z.Tree.Convert_Context_V2   import  convert_parameter_context
    else:
        FATAL_unknown_version('context', context_version)


    if context_version == 0:
        map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = None
        map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context        = None
    elif context_version in ((2, 3)):
        map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
                Native_AbstractSyntaxTree_Delete_Context : tree_delete_context,
                Native_AbstractSyntaxTree_Load_Context   : tree_load_context,
                Native_AbstractSyntaxTree_Store_Context  : tree_store_context,
            }

        map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
                Native_AbstractSyntaxTree_Load_Context  : tree_load_context,
                Native_AbstractSyntaxTree_Store_Context : tree_store_context,
            }


        if __debug__:
            def assert_no_context_fields(mapping):
                for k in mapping:
                    assert k._attributes == (())
                    assert k._fields     == (())


            assert_no_context_fields(map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context)
            assert_no_context_fields(map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context)
    else:
        FATAL_unknown_version('context', context_version)


    #
    #   Decorator
    #
    from    Z.Tree.Convert_Decorator_V2     import  convert_some_list_of_decorators


    #
    #   Expressions
    #
    if expression_version == 2:
        from    Z.Tree.Convert_Expression_V2    import  convert_backquote_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_binary_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_call_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_compare_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_full_list_of_expressions
        from    Z.Tree.Convert_Expression_V2    import  convert_generator_comprehension
        from    Z.Tree.Convert_Expression_V2    import  convert_if_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_lambda_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_list_comprehension
        from    Z.Tree.Convert_Expression_V2    import  convert_logical_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_map_comprehension
        from    Z.Tree.Convert_Expression_V2    import  convert_map_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_none_OR_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_number
        from    Z.Tree.Convert_Expression_V2    import  convert_set_comprehension
        from    Z.Tree.Convert_Expression_V2    import  convert_set_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_some_list_of_expressions
        from    Z.Tree.Convert_Expression_V2    import  convert_string
        from    Z.Tree.Convert_Expression_V2    import  convert_unary_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_yield_expression
    else:
        FATAL_unknown_version('expression', expression_version)


    #
    #   Index
    #
    if index_version == 2:
        from    Z.Tree.Convert_Index_V2     import  convert_ellipses_index
        from    Z.Tree.Convert_Index_V2     import  convert_extended_slice_index
        from    Z.Tree.Convert_Index_V2     import  convert_index_clause
        from    Z.Tree.Convert_Index_V2     import  convert_simple_index
        from    Z.Tree.Convert_Index_V2     import  convert_slice_index
    else:
        FATAL_unknown_version('index', index_version)


    if index_version == 2:
        from    Z.Tree.Index_V1             import  create_Tree_Extended_Slice_Index
        from    Z.Tree.Index_V1             import  create_Tree_Simple_Index
        from    Z.Tree.Index_V1             import  create_Tree_Slice_Index
        from    Z.Tree.Index_V1             import  tree_ellipses_index
    else:
        FATAL_unknown_version('index', index_version)


    #
    #   Name
    #
    if name_version == 2:
        from    Z.Tree.Convert_Name_V2      import  convert_name_expression
        from    Z.Tree.Convert_Name_V2      import  convert_some_list_of_name_parameters
    elif name_version == 3:
        from    Z.Tree.Convert_Name_V3      import  convert_name_expression
        from    Z.Tree.Convert_Name_V3      import  convert_some_list_of_name_parameters
    elif name_version == 4:
        from    Z.Tree.Convert_Name_V4      import  convert_name_expression
        from    Z.Tree.Convert_Name_V4      import  convert_some_list_of_name_parameters
    else:
        FATAL_unknown_version('name', name_version)


    #
    #   Parameter
    #
    from    Z.Tree.Convert_Parameter_V2     import  convert_parameters_all


    #
    #   Statements
    #
    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Except_V2    import  convert_full_list_of_except_clauses
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3)):
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_For_Statement           #   "_V1" on purpose
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_If_Statement            #   "_V1" on purpose
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_Try_Except_Statement    #   "_V1" on purpose
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_Try_Finally_Statement   #   "_V1" on purpose
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_While_Statement         #   "_V1" on purpose
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_With_Statement          #   "_V1" on purpose
    elif statement_version == 4:
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_For_Statement
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_If_Statement
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_Try_Except_Statement
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_Try_Finally_Statement
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_While_Statement
        from    Z.Tree.Compound_Statement_V4    import  create_Tree_With_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Statement_V2     import  convert_statement
        from    Z.Tree.Convert_Statement_V2     import  convert_full_list_of_statements
        from    Z.Tree.Convert_Statement_V2     import  convert_some_list_of_statements
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_assert_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_assign_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_break_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_continue_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_delete_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_execute_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_expression_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_global_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_from_import_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_import_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_modify_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_pass_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_print_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_raise_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_return_statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version == 2:
        from    Z.Tree.Convert_Definition_V2    import  convert_class_definition
        from    Z.Tree.Convert_Definition_V2    import  convert_function_definition
    elif statement_version == 3:
        from    Z.Tree.Convert_Definition_V3    import  convert_class_definition
        from    Z.Tree.Convert_Definition_V3    import  convert_function_definition
    elif statement_version == 4:
        from    Z.Tree.Convert_Definition_V4    import  convert_class_definition
        from    Z.Tree.Convert_Definition_V4    import  convert_function_definition
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


    if statement_version == 2:
        from    Z.Tree.Definition_V1    import  create_Tree_Class_Definition    #   "_V1" on purpose
        from    Z.Tree.Definition_V1    import  create_Tree_Function_Definition #   "_V1" on purpose
    elif statement_version == 3:
        from    Z.Tree.Definition_V3    import  create_Tree_Class_Definition
        from    Z.Tree.Definition_V3    import  create_Tree_Function_Definition
    elif statement_version == 4:
        from    Z.Tree.Definition_V4    import  create_Tree_Class_Definition
        from    Z.Tree.Definition_V4    import  create_Tree_Function_Definition
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Except_V1        import  create_Tree_Except_Handler
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((1, 2, 3)):
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Assert_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Assign_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Break_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Continue_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Delete_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Execute_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Expression_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_From_Import_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Global_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Import_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Modify_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Pass_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Print_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Raise_Statement
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Return_Statement
    elif statement_version == 4:
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Assert_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Assign_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Break_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Continue_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Delete_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Execute_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Expression_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_From_Import_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Global_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Import_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Modify_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Pass_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Print_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Raise_Statement
        from    Z.Tree.Simple_Statement_V3      import  create_Tree_Return_Statement
    else:
        FATAL_unknown_version('statement', statement_version)

    
    #
    #   Suite
    #
    if statement_version in ((1, 2, 3)):
        #
        #   A "Suite" does not exist in statement versions 1 or 2.
        #
        create_Tree_Suite = None
    elif statement_version == 4:
        from    Z.Tree.Suite_V4         import  create_Tree_Suite
    else:
        FATAL_unknown_version('statement', statement_version)


    #
    #   Target
    #
    if target_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Target_V2    import  convert_full_list_of_targets
        from    Z.Tree.Convert_Target_V2    import  convert_none_OR_target
        from    Z.Tree.Convert_Target_V2    import  convert_target
    else:
        FATAL_unknown_version('target', target_version)


    if target_version == 2:
        from    Z.Tree.Convert_Attribute_V2     import  convert_attribute_expression
        from    Z.Tree.Convert_Many_V2          import  convert_list_expression
        from    Z.Tree.Convert_Many_V2          import  convert_tuple_expression
        from    Z.Tree.Convert_Subscript_V2     import  convert_subscript_expression
    elif target_version == 3:
        from    Z.Tree.Convert_Attribute_V3     import  convert_attribute_expression
        from    Z.Tree.Convert_Many_V2          import  convert_list_expression         #   "_V2" on purpose.
        from    Z.Tree.Convert_Many_V2          import  convert_tuple_expression        #   "_V2" on purpose.
        from    Z.Tree.Convert_Subscript_V2     import  convert_subscript_expression    #   "_V2" on purpose.
    elif target_version == 4:
        from    Z.Tree.Convert_Attribute_V4     import  convert_attribute_expression
        from    Z.Tree.Convert_Many_V4          import  convert_list_expression
        from    Z.Tree.Convert_Many_V4          import  convert_tuple_expression
        from    Z.Tree.Convert_Subscript_V4     import  convert_subscript_expression
    else:
        FATAL_unknown_version('target', target_version)


    if target_version == 2:
        from    Z.Tree.Attribute_V1     import  create_Tree_Attribute                   #   "_V1" on purpose.
    elif target_version == 3:
        from    Z.Tree.Attribute_V3     import  create_Tree_Attribute
    elif target_version == 4:
        create_Tree_Attribute = None
    else:
        FATAL_unknown_version('target', target_version)


    #
    #   map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_expression" psuedo method
    #       (actually to a function).
    #
    map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function = {
            Native_AbstractSyntaxTree_Attribute_Expression    : convert_attribute_expression,
            Native_AbstractSyntaxTree_Backquote_Expression    : convert_backquote_expression,
            Native_AbstractSyntaxTree_Binary_Expression       : convert_binary_expression,
            Native_AbstractSyntaxTree_Call_Expression         : convert_call_expression,
            Native_AbstractSyntaxTree_Compare_Expression      : convert_compare_expression,
            Native_AbstractSyntaxTree_Generator_Comprehension : convert_generator_comprehension,
            Native_AbstractSyntaxTree_If_Expression           : convert_if_expression,
            Native_AbstractSyntaxTree_Lambda_Expression       : convert_lambda_expression,
            Native_AbstractSyntaxTree_List_Comprehension      : convert_list_comprehension,
            Native_AbstractSyntaxTree_List_Expression         : convert_list_expression,
            Native_AbstractSyntaxTree_Logical_Expression      : convert_logical_expression,
            Native_AbstractSyntaxTree_Map_Comprehension       : convert_map_comprehension,
            Native_AbstractSyntaxTree_Map_Expression          : convert_map_expression,
            Native_AbstractSyntaxTree_Name                    : convert_name_expression,
            Native_AbstractSyntaxTree_Number                  : convert_number,
            Native_AbstractSyntaxTree_Set_Comprehension       : convert_set_comprehension,
            Native_AbstractSyntaxTree_Set_Expression          : convert_set_expression,
            Native_AbstractSyntaxTree_String                  : convert_string,
            Native_AbstractSyntaxTree_Subscript_Expression    : convert_subscript_expression,
            Native_AbstractSyntaxTree_Tuple_Expression        : convert_tuple_expression,
            Native_AbstractSyntaxTree_Unary_Expression        : convert_unary_expression,
            Native_AbstractSyntaxTree_Yield_Expression        : convert_yield_expression,
    }


    #
    #   map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_index" function.
    #
    map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function = {
            Native_AbstractSyntaxTree_Ellipsis_Index       : convert_ellipses_index,
            Native_AbstractSyntaxTree_Extended_Slice_Index : convert_extended_slice_index,
            Native_AbstractSyntaxTree_Simple_Index         : convert_simple_index,
            Native_AbstractSyntaxTree_Slice_Index          : convert_slice_index,
        }


    #
    #   map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_statement" psuedo method
    #       (actually to a function).
    #
    map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function = {
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
    #   map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_target" function.
    #
    map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function = {
            Native_AbstractSyntaxTree_Attribute_Expression : convert_attribute_expression,
            Native_AbstractSyntaxTree_List_Expression      : convert_list_expression,
            Native_AbstractSyntaxTree_Name                 : convert_name_expression,
            Native_AbstractSyntaxTree_Subscript_Expression : convert_subscript_expression,
            Native_AbstractSyntaxTree_Tuple_Expression     : convert_tuple_expression,
        }

    #
    #   ========================================  z  ========================================
    #
    z = convert_zone


    #
    #   Argument
    #
    z.convert_some_list_of_keyword_arguments = convert_some_list_of_keyword_arguments

    z.create_Tree_Keyword_Argument           = create_Tree_Keyword_Argument


    #
    #   Alias
    #
    z.convert_full_list_of_module_aliases = convert_full_list_of_module_aliases
    z.convert_full_list_of_symbol_aliases = convert_full_list_of_symbol_aliases

    z.create_Tree_Module_Alias            = create_Tree_Module_Alias
    z.create_Tree_Symbol_Alias            = create_Tree_Symbol_Alias


    #
    #   Comprehension
    #
    z.convert_full_list_of_comprehensions = convert_full_list_of_comprehensions

    z.create_Tree_Comprehension_Clause = create_Tree_Comprehension_Clause


    #
    #   Context
    #
    z.convert_delete_load_OR_store_context = convert_delete_load_OR_store_context
    z.convert_parameter_context            = convert_parameter_context

    z.tree_delete_context    = tree_delete_context
    z.tree_parameter_context = tree_parameter_context

    z.map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = (
            map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context
        )

    z.map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context = (
            map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context
        )


    #
    #   Decorator
    #
    z.convert_some_list_of_decorators = convert_some_list_of_decorators


    #
    #   Expression
    #
    z.convert_expression               = convert_expression
    z.convert_full_list_of_expressions = convert_full_list_of_expressions
    z.convert_none_OR_expression       = convert_none_OR_expression
    z.convert_some_list_of_expressions = convert_some_list_of_expressions

    z.map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function = (
            map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function
        )


    #
    #   Index
    #
    z.convert_index_clause = convert_index_clause

    z.create_Tree_Extended_Slice_Index = create_Tree_Extended_Slice_Index
    z.create_Tree_Simple_Index         = create_Tree_Simple_Index
    z.create_Tree_Slice_Index          = create_Tree_Slice_Index

    z.tree_ellipses_index = tree_ellipses_index

    z.map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function = (
            map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function
        )


    #
    #   Name
    #
    z.convert_some_list_of_name_parameters = convert_some_list_of_name_parameters

    
    #
    #   Parameter
    #
    z.convert_parameters_all = convert_parameters_all


    #
    #  Statement
    #
    z.convert_full_list_of_except_clauses = convert_full_list_of_except_clauses
    z.convert_full_list_of_statements     = convert_full_list_of_statements
    z.convert_some_list_of_statements     = convert_some_list_of_statements
    z.convert_statement                   = convert_statement

    z.create_Tree_Assert_Statement      = create_Tree_Assert_Statement
    z.create_Tree_Assign_Statement      = create_Tree_Assign_Statement
    z.create_Tree_Break_Statement       = create_Tree_Break_Statement
    z.create_Tree_Class_Definition      = create_Tree_Class_Definition
    z.create_Tree_Continue_Statement    = create_Tree_Continue_Statement
    z.create_Tree_Delete_Statement      = create_Tree_Delete_Statement
    z.create_Tree_Except_Handler        = create_Tree_Except_Handler
    z.create_Tree_Execute_Statement     = create_Tree_Execute_Statement
    z.create_Tree_Expression_Statement  = create_Tree_Expression_Statement
    z.create_Tree_For_Statement         = create_Tree_For_Statement
    z.create_Tree_From_Import_Statement = create_Tree_From_Import_Statement
    z.create_Tree_Function_Definition   = create_Tree_Function_Definition
    z.create_Tree_Global_Statement      = create_Tree_Global_Statement
    z.create_Tree_If_Statement          = create_Tree_If_Statement
    z.create_Tree_Import_Statement      = create_Tree_Import_Statement
    z.create_Tree_Modify_Statement      = create_Tree_Modify_Statement
    z.create_Tree_Pass_Statement        = create_Tree_Pass_Statement
    z.create_Tree_Print_Statement       = create_Tree_Print_Statement
    z.create_Tree_Raise_Statement       = create_Tree_Raise_Statement
    z.create_Tree_Return_Statement      = create_Tree_Return_Statement
    z.create_Tree_Try_Except_Statement  = create_Tree_Try_Except_Statement
    z.create_Tree_Try_Finally_Statement = create_Tree_Try_Finally_Statement
    z.create_Tree_While_Statement       = create_Tree_While_Statement
    z.create_Tree_With_Statement        = create_Tree_With_Statement

    z.map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function = (
            map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function
        )


    #
    #   Suite
    #
    z.create_Tree_Suite = create_Tree_Suite


    #
    #   Target
    #
    z.convert_full_list_of_targets = convert_full_list_of_targets
    z.convert_none_OR_target       = convert_none_OR_target
    z.convert_target               = convert_target

    z.create_Tree_Attribute = create_Tree_Attribute

    z.map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function = (
            map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function
        )


    #
    #   Done
    #
    return z


@creator
def create_convert_zone():
    return Convert_Zone()


convert_zone = create_convert_zone()
