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
from    Capital.Core                        import  trace
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Add_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Backquote_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_And_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Binary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Call_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Different_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Greater_Than_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Greater_Than_Or_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Identity_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Less_Than_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Less_Than_Or_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Compare_Not_Equal_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Contains_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Divide_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Ellipsis_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Excludes_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Extended_Slice_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Floor_Divide_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_For_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Generator_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_If_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Invert_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Lambda_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Left_Shift_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_And_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Logical_Or_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modulus_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Multiply_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Negative_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Not_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Number
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Positive_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Power_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Right_Shift_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Comprehension
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Set_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Simple_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Slice_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_String_Literal
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subtract_Operator
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Except_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Try_Finally_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_While_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_With_Statement
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Yield_Expression


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer


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
        'convert_load_OR_store_context',            #   None | Function
        'convert_parameter_context',                #   None | Function

        'tree_delete_context',                      #   None | Tree_Context
        'tree_parameter_context',                   #   None | Tree_Context

        'map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context',
                                                    #   None | Map { Native_AbstractSyntaxTree_* : Tree_Context }

        'map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context',
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

        'create_Tree_Backquote_Expression',         #   Function
        'create_Tree_Binary_Expression',            #   Function
        'create_Tree_Call_Expression',              #   Function
        'create_Tree_Compare_Expression',           #   Function
        'create_Tree_Generator_Comprehension',      #   Function
        'create_Tree_If_Expression',                #   Function
        'create_Tree_Lambda_Expression',            #   Function
        'create_Tree_List_Comprehension',           #   Function
        'create_Tree_Logical_Expression',           #   Function
        'create_Tree_Map_Comprehension',            #   Function
        'create_Tree_Map_Expression',               #   Function
        'create_Tree_Number',                       #   Function
        'create_Tree_Set_Comprehension',            #   Function
        'create_Tree_Set_Expression',               #   Function
        'create_Tree_String',                       #   Function
        'create_Tree_Unary_Expression',             #   Function
        'create_Tree_Yield_Expression',             #   Function

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
        #   Module
        #
        'create_Tree_Module',                       #   Function


        #
        #   Module_Name
        #
        'conjure_parser_module_name',               #   None | Function
        'conjure_parser_module_name_with_dot',      #   None | Function


        #
        #   Name
        #
        'create_Tree_Name',                         #   None | Function

        'map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function',
                                                    #   None |  Map { Native_AbstractSyntaxTree_* : Function }

        #
        #   Operator
        #
        'convert_binary_operator',                      #   Function
        'convert_full_list_of_compare_operators',       #   Function
        'convert_logical_operator',                     #   Function
        'convert_modify_operator',                      #   Function
        'convert_unary_operator',                       #   Function

        'map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator',
                                                        #    Map { Native_AbstractSyntaxTree_* : Tree_Opertor }

        'map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator',
                                                        #    Map { Native_AbstractSyntaxTree_* : Tree_Opertor }

        'map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator',
                                                        #    Map { Native_AbstractSyntaxTree_* : Tree_Opertor }

        'map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator',
                                                        #    Map { Native_AbstractSyntaxTree_* : Tree_Opertor }

        'map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator',
                                                        #    Map { Native_AbstractSyntaxTree_* : Tree_Opertor }


        #
        #   Parameter
        #
        'convert_parameter_tuple_0',                #   None | Function

        'create_Tree_All_Parameters',               #   None | Function
        'create_Tree_Keyword_Parameter',            #   None | Function
        'create_Tree_Map_Parameter',                #   None | Function
        'create_Tree_Normal_Parameter',             #   None | Function
        'create_Tree_Parameter_Tuple',              #   None | Function
        'create_Tree_Star_Parameter',               #   None | Function


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
        'convert_suite',                            #   None | Function
        'convert_suite_0',                          #   None | Function

        'create_Tree_Suite',                        #   None | Function


        #
        #   Symbol
        #
        'conjure_parser_symbol',                    #   Function
        'conjure_parser_symbol_0',                  #   Function

        'create_Parser_Symbol_Tuple',               #   None | Function


        #
        #   Target
        #
        'convert_full_list_of_targets',             #   Function
        'convert_none_OR_target',                   #   Function
        'convert_target',                           #   Function

        'create_Tree_Attribute',                    #   None | Function
        'create_Tree_List_Expression',              #   None | Function
        'create_Tree_Subscript_Expression',         #   None | Function
        'create_Tree_Tuple_Expression',             #   None | Function

        'map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function',
                                                    #   None |  Map { Native_AbstractSyntaxTree_* : Function }

        'map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function',
                                                    #   None |  Map { Native_AbstractSyntaxTree_* : Function }

        'map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function',
                                                    #   None |  Map { Native_AbstractSyntaxTree_* : Function }

        'map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function',
                                                    #   None |  Map { Native_AbstractSyntaxTree_* : Function }

        'map__Native_AbstractSyntaxTree_TARGET__to__convert_target__function',
                                                    #   Map { Native_AbstractSyntaxTree_* : Function }
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
def fill_convert_zone(version):
    assert fact_is_positive_native_integer(version)

    assert 2 <= version <= 21


    #
    #   Version 1
    #
    alias_version         = 1       #   1..6
    argument_version      = 1       #   1..3
    comprehension_version = '1'
    context_version       = 1       #   1..3, 0
    except_version        = '1'
    expression_version    = 1       #   1..3
    index_version         = 1       #   1..2
    module_name_version   = 0       #   0, 2..3 (no version 1)
    name_version          = 1       #   1..4
    operator_version      = 1       #   1, 3    (no version 2)
    parameter_version     = 1       #   1..6
    statement_version     = 1       #   1..7
    symbol_version        = 0       #   0, 2..6 (no version 1)
    target_version        = 1       #   1..4


    #
    #   Version 2: Introduce `Convert_Zone`
    #
    if version >= 2:
        alias_version      = 2
        argument_version   = 2
        context_version    = 2
        expression_version = 2
        index_version      = 2
        name_version       = 2
        parameter_version  = 2
        statement_version  = 2
        target_version     = 2


    #
    #   Version 3 & 4: Introduce Enumerations
    #
    #       3:  Enumeration for `Tree_Context`
    #       4:  Enumeration for `Tree_Operator`
    #
    if version >= 3:
        context_version = 3

    if version >= 4:
        operator_version = 3


    #
    #   Version 5: Split `Tree_Alias_Clause` into `Tree_{Module,Symbol}_Alias_Leaf`.
    #
    if version >= 5:
        alias_version = 3


    #
    #   Version 6, 7, 8, & 9: Introduce `Parser_Symbol`
    #
    #       6:  `Tree_Keyword_Argument`            uses symbols.
    #
    #       7:  `Tree_Name`                        uses symbols.
    #
    #       8:  `Tree_Target`                      uses symbols (affects `Tree_Attribute`).
    #
    #       9:  `Tree_{Class,Function}_Definition` uses symbols.
    #
    if version >= 6:
        argument_version = 3            #   `Tree_Keyword_Argument` uses symbols.
        symbol_version   = 2            #   Enable `Parser_Symbol`

    if version >= 7:
        name_version      = 3           #   `Tree_Name` uses symbols.
        parameter_version = 3           #   `Tree_Name` uses symbols (affects `convert_name_parameter`).

    if version >= 8:
        target_version = 3              #   `Tree_Target` uses symbols (affects `Tree_Attribute`).

    if version >= 9:
        statement_version = 3           #   `Tree_{Class,Function}_Definition` uses symbols.


    #
    #   Version 10 & 11: Introduce `Parser_Module_Name`
    #
    #       10: `Tree_From_Import.module`     is a `Parser_Module_Name`.
    #
    #       11: `Tree_Module_Alias_Leaf.name` is a `Parser_Module_Name`.
    #
    if version >= 10:
        module_name_version = 2     #   Enable                        `Parser_Module_Name`.
        statement_version   = 4     #   `Tree_From_Import.module`is a `Parser_Module_Name`.
        symbol_version      = 3     #   Symbol version 3 implements   `Parser_Module_Name`.

    if version >= 11:
        alias_version       = 4     #   `Tree_Module_Alias_Leaf.name` is a `Parser_Module_Name`.


    #
    #   Version 12 & 13: Improve `Tree_{Module,Symbol}_Alias_Leaf`.
    #
    #       12: `Tree_{Module,Symbol}_Alias_Leaf` use `Parser_Symbol` and `Parser_Symbol_0`.
    #
    #       13: Only use `Tree_{Module,Symbol}_Alias.as_name` when it has a value.
    #
    if version >= 12:
        alias_version  = 5          #   `Tree_{Module,Symbol}_Alias` use `Parser_Symbol` and `Parser_Symbol_0`.
        symbol_version = 4          #   Symbol version 4 implements `Parser_Symbol_0`

    if version >= 13:
        alias_version       = 6     #   Only use `Tree_{Module,Symbol}_Alias.as_name` when it has a value.
        module_name_version = 3     #   `Parser_Module_Name_With_Dot` implements `Tree_Module_Alias`.
        symbol_version      = 5     #   Symbol version 6 implements `Tree_{Module,Symbol}_Alias`.


    #
    #   Version 14: `Tree_Global_Statement` uses `Parser_Symbol` & `Parser_Symbol_Tuple`
    #
    #       14: `Tree_Global_Statement` uses `Parser_Symbol`
    #
    #       15: `Tree_Global_Statement` uses `Parser_Symbol_Tuple`
    #
    if version >= 14:
        statement_version = 5       #   `Tree_Global_Statement` uses `Parser_Symbol`

    if version >= 15:
        symbol_version    = 6       #   `Parser_Symbol` implements `Parser_Symbol_Tuple`.
        statement_version = 6       #   `Tree_Global_Statement` uses `Parser_Symbol`

    #
    #   Version 16 & 17: No longer use contexts
    #
    #       16: `Tree_Name`    no longer uses contexts.
    #
    #       17: `Tree_Target`  no longer uses contexts (affects `Tree_Attribute`, `Tree_{List,Tuple}_Expression`, and
    #                          `Tree_Subscript`).
    #
    if version >= 16:
        name_version      = 4           #   `Tree_Name` no longer uses contexts
        parameter_version = 4           #   Implement `Tree_Name_Parameter`

    if version >= 17:
        context_version = 0             #   Nothing uses contexts anymore ... so totally disable tree contexts
        target_version  = 4


    #
    #   Version 18: `Tree_String` uses `String`
    #
    if version >= 18:
        expression_version = 3          #   `Tree_String` uses `String`

    #
    #   Version 19 & 20: Improve `Tree_Parameter`
    #
    #       19: Implement `Tree_{Map,Tuple}_Parameter`.
    #
    #       20: Add `Tree_Parameter_Tuple_Leaf`.  Remove `Tree_All_Parameters`.
    #
    if version >= 19:
        parameter_version = 5           #   Add `Tree_{Map,Tuple}_Parameter`

    if version >= 20:
        parameter_version = 6           #   Add `Tree_Parameter_Tuple_Leaf`.  Remove `Tree_All_Parameters`.


    #
    #   Version 21: Add `Tree_Suite` & `Tree_Suite_0`
    #
    if version >= 21:
        statement_version = 7


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
    #   Verify verions
    #
    assert fact_is_positive_native_integer   (version)
    assert fact_is_positive_native_integer   (alias_version)
    assert fact_is_positive_native_integer   (argument_version)
    assert fact_is_full_native_string        (comprehension_version)
    assert fact_is_substantial_native_integer(context_version)
    assert fact_is_full_native_string        (except_version)
    assert fact_is_positive_native_integer   (index_version)
    assert fact_is_substantial_native_integer(module_name_version)
    assert fact_is_positive_native_integer   (name_version)
    assert fact_is_positive_native_integer   (operator_version)
    assert fact_is_positive_native_integer   (parameter_version)
    assert fact_is_positive_native_integer   (expression_version)
    assert fact_is_positive_native_integer   (statement_version)
    assert fact_is_substantial_native_integer(symbol_version)
    assert fact_is_positive_native_integer   (target_version)

    assert 2   <= version               <= 21
    assert 1   <= alias_version         <= 6
    assert 1   <= argument_version      <= 3
    assert '1' == comprehension_version == '1'
    assert 0   <= context_version       <= 3
    assert '1' == except_version        == '1'
    assert 1   <= expression_version    <= 3
    assert 1   <= index_version         <= 2
    assert 0   <= module_name_version   <= 3
    assert 1   <= name_version          <= 4
    assert 1   <= operator_version      <= 3
    assert 1   <= parameter_version     <= 6
    assert 1   <= statement_version     <= 7
    assert 0   <= symbol_version        <= 6
    assert 1   <= target_version        <= 4


    #
    #   Trace versions
    #
    trace('Versions: version={} alias={} argument={} comprehension={!r} context={} except={!r} ...',
          version, alias_version, argument_version, comprehension_version, context_version, except_version)

    trace('... expression={} index={} module_name={} name={} statement={} operator={} parameter={}',
          expression_version, index_version, module_name_version, name_version, statement_version, operator_version,
          parameter_version)

    trace('... symbol={} target={}',
          symbol_version, target_version)


    #
    #   Alias
    #
    if alias_version == 2:
        #
        #   Next two lines use "_V1" on purpose.
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
        convert_load_OR_store_context        = None
        convert_parameter_context            = None
    elif context_version in ((2, 3)):
        from    Z.Tree.Convert_Context_V2   import  convert_delete_load_OR_store_context
        from    Z.Tree.Convert_Context_V2   import  convert_load_OR_store_context
        from    Z.Tree.Convert_Context_V2   import  convert_parameter_context
    else:
        FATAL_unknown_version('context', context_version)


    #
    #   Decorator
    #
    from    Z.Tree.Convert_Decorator_V2     import  convert_some_list_of_decorators


    #
    #   Expressions
    #
    if expression_version in ((2, 3)):
        from    Z.Tree.Convert_Expression_V2    import  convert_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_full_list_of_expressions
        from    Z.Tree.Convert_Expression_V2    import  convert_none_OR_expression
        from    Z.Tree.Convert_Expression_V2    import  convert_some_list_of_expressions
    else:
        FATAL_unknown_version('expression', expression_version)


    if expression_version == 2:
        from    Z.Tree.Convert_Literal_V2               import  convert_string_literal
    elif expression_version == 3:
        from    Z.Tree.Convert_Literal_V3               import  convert_string_literal
    else:
        FATAL_unknown_version('expression', expression_version)


    if expression_version in ((2, 3)):
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_backquote_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_binary_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_call_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_compare_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_generator_comprehension
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_if_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_lambda_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_list_comprehension
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_logical_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_map_comprehension
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_map_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_number
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_set_comprehension
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_set_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_unary_expression
        from    Z.Tree.Convert_Specific_Expression_V2   import  convert_yield_expression
    else:
        FATAL_unknown_version('expression', expression_version)


    if expression_version in ((2, 3)):
        from    Z.Tree.Expression_V1    import  create_Tree_Backquote_Expression        #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Binary_Expression           #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Call_Expression             #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Compare_Expression          #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Generator_Comprehension     #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_If_Expression               #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Lambda_Expression           #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_List_Comprehension          #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Logical_Expression          #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Map_Comprehension           #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Map_Expression              #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Number                      #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Set_Comprehension           #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Set_Expression              #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Unary_Expression            #   "_V1" on purpose.
        from    Z.Tree.Expression_V1    import  create_Tree_Yield_Expression            #   "_V1" on purpose.
    else:
        FATAL_unknown_version('expression', expression_version)


    if expression_version == 2:
        from    Z.Tree.Literal_V1       import  create_Tree_String                      #   "_V1" on purpose.
    elif expression_version == 3:
        from    Z.Tree.Literal_V3       import  create_Tree_String
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
        from    Z.Tree.Index_V1         import  create_Tree_Extended_Slice_Index    #   "_V1" on purpose.
        from    Z.Tree.Index_V1         import  create_Tree_Simple_Index            #   "_V1" on purpose.
        from    Z.Tree.Index_V1         import  create_Tree_Slice_Index             #   "_V1" on purpose.
        from    Z.Tree.Index_V1         import  tree_ellipses_index                 #   "_V1" on purpose.
    else:
        FATAL_unknown_version('index', index_version)


    #
    #   Module
    #
    from    Z.Tree.Module               import  create_Tree_Module


    #
    #   Module_Name
    #
    if module_name_version == 0:
        conjure_parser_module_name = None
    elif module_name_version in ((2, 3)):
        from    Z.Parser.Conjure_Module_Name    import  conjure_parser_module_name
    else:
        FATAL_unknown_version('module_name', module_name_version)


    if module_name_version == 0:
        conjure_parser_module_name_with_dot = None
    elif module_name_version == 2:
        from    Z.Parser.Module_Name_V2     import  conjure_parser_module_name_with_dot
    elif module_name_version == 3:
        from    Z.Parser.Module_Name_V3     import  conjure_parser_module_name_with_dot
    else:
        FATAL_unknown_version('module_name', module_name_version)


    #
    #   Name
    #
    if name_version == 2:
        from    Z.Tree.Convert_Name_V2      import  convert_name_expression
    elif name_version == 3:
        from    Z.Tree.Convert_Name_V3      import  convert_name_expression
    elif name_version == 4:
        from    Z.Tree.Convert_Name_V4      import  convert_name_expression
    else:
        FATAL_unknown_version('name', name_version)


    if name_version == 2:
        from    Z.Tree.Name_V1          import  create_Tree_Name            #   "_V1" on purpose.
    elif name_version == 3:
        from    Z.Tree.Name_V3          import  create_Tree_Name
    elif name_version == 4:
        create_Tree_Name = None
    else:
        FATAL_unknown_version('name', name_version)


    if name_version in ((2, 3)):
        #
        #    No need to define these, leave them vacant (i.e.: uninitialized).
        #
       #create_Tree_Delete_Name   = VACANT
       #create_Tree_Evaluate_Name = VACANT
       #create_Tree_Store_Name    = VACANT

        pass
    elif name_version == 4:
        from    Z.Tree.Name_V4          import  create_Tree_Delete_Name
        from    Z.Tree.Name_V4          import  create_Tree_Evaluate_Name
        from    Z.Tree.Name_V4          import  create_Tree_Store_Name
    else:
        FATAL_unknown_version('target', target_version)



    #
    #   Operator (version 1 or 3.  Version 2 does not exist).
    #
    from        Z.Tree.Convert_Operator_V2  import  convert_binary_operator
    from        Z.Tree.Convert_Operator_V2  import  convert_full_list_of_compare_operators
    from        Z.Tree.Convert_Operator_V2  import  convert_logical_operator
    from        Z.Tree.Convert_Operator_V2  import  convert_modify_operator
    from        Z.Tree.Convert_Operator_V2  import  convert_unary_operator


    if operator_version == 1:
        from    Z.Tree.Operator_V1          import  tree_add_operator
        from    Z.Tree.Operator_V1          import  tree_binary_and_operator
        from    Z.Tree.Operator_V1          import  tree_binary_exclusive_or_operator
        from    Z.Tree.Operator_V1          import  tree_compare_different_operator
        from    Z.Tree.Operator_V1          import  tree_compare_equal_operator
        from    Z.Tree.Operator_V1          import  tree_compare_greater_than_operator
        from    Z.Tree.Operator_V1          import  tree_compare_greater_than_or_equal_operator
        from    Z.Tree.Operator_V1          import  tree_compare_identity_operator
        from    Z.Tree.Operator_V1          import  tree_compare_less_than_operator
        from    Z.Tree.Operator_V1          import  tree_compare_less_than_or_equal_operator
        from    Z.Tree.Operator_V1          import  tree_compare_not_equal_operator
        from    Z.Tree.Operator_V1          import  tree_contains_operator
        from    Z.Tree.Operator_V1          import  tree_divide_operator
        from    Z.Tree.Operator_V1          import  tree_excludes_operator
        from    Z.Tree.Operator_V1          import  tree_floor_divide_operator
        from    Z.Tree.Operator_V1          import  tree_invert_operator
        from    Z.Tree.Operator_V1          import  tree_left_shift_operator
        from    Z.Tree.Operator_V1          import  tree_logical_and_operator
        from    Z.Tree.Operator_V1          import  tree_logical_or_operator
        from    Z.Tree.Operator_V1          import  tree_modulus_operator
        from    Z.Tree.Operator_V1          import  tree_multiply_operator
        from    Z.Tree.Operator_V1          import  tree_negative_operator
        from    Z.Tree.Operator_V1          import  tree_not_operator
        from    Z.Tree.Operator_V1          import  tree_positive_operator
        from    Z.Tree.Operator_V1          import  tree_power_operator
        from    Z.Tree.Operator_V1          import  tree_right_shift_operator
        from    Z.Tree.Operator_V1          import  tree_subtract_operator
    elif operator_version == 3:
        from    Z.Tree.Operator_V3          import  Tree_Operator_Enumeration   as  TOE

        tree_add_operator                           = TOE.tree_add_operator
        tree_binary_and_operator                    = TOE.tree_binary_and_operator
        tree_binary_exclusive_or_operator           = TOE.tree_binary_exclusive_or_operator
        tree_compare_different_operator             = TOE.tree_compare_different_operator
        tree_compare_equal_operator                 = TOE.tree_compare_equal_operator
        tree_compare_greater_than_operator          = TOE.tree_compare_greater_than_operator
        tree_compare_greater_than_or_equal_operator = TOE.tree_compare_greater_than_or_equal_operator
        tree_compare_identity_operator              = TOE.tree_compare_identity_operator
        tree_compare_less_than_operator             = TOE.tree_compare_less_than_operator
        tree_compare_less_than_or_equal_operator    = TOE.tree_compare_less_than_or_equal_operator
        tree_compare_not_equal_operator             = TOE.tree_compare_not_equal_operator
        tree_contains_operator                      = TOE.tree_contains_operator
        tree_divide_operator                        = TOE.tree_divide_operator
        tree_excludes_operator                      = TOE.tree_excludes_operator
        tree_floor_divide_operator                  = TOE.tree_floor_divide_operator
        tree_invert_operator                        = TOE.tree_invert_operator
        tree_left_shift_operator                    = TOE.tree_left_shift_operator
        tree_logical_and_operator                   = TOE.tree_logical_and_operator
        tree_logical_or_operator                    = TOE.tree_logical_or_operator
        tree_modulus_operator                       = TOE.tree_modulus_operator
        tree_multiply_operator                      = TOE.tree_multiply_operator
        tree_negative_operator                      = TOE.tree_negative_operator
        tree_not_operator                           = TOE.tree_not_operator
        tree_positive_operator                      = TOE.tree_positive_operator
        tree_power_operator                         = TOE.tree_power_operator
        tree_right_shift_operator                   = TOE.tree_right_shift_operator
        tree_subtract_operator                      = TOE.tree_subtract_operator

        del TOE
    else:
        FATAL_unknown_version('operator', operator_version)


    #
    #   Parameter
    #
    if parameter_version == 2:
        from    Z.Tree.Convert_Parameter_V2     import  convert_parameter_tuple_0
    elif parameter_version == 3:
        from    Z.Tree.Convert_Parameter_V3     import  convert_parameter_tuple_0
    elif parameter_version == 4:
        from    Z.Tree.Convert_Parameter_V4     import  convert_parameter_tuple_0
    elif parameter_version == 5:
        from    Z.Tree.Convert_Parameter_V5     import  convert_parameter_tuple_0
    elif parameter_version == 6:
        from    Z.Tree.Convert_Parameter_V6     import  convert_parameter_tuple_0
    else:
        FATAL_unknown_version('parameter', parameter_version)


    if parameter_version in ((2, 3)):
        create_Tree_Keyword_Parameter = None
        create_Tree_Map_Parameter     = None
        create_Tree_Normal_Parameter  = None
        create_Tree_Star_Parameter = None
    elif parameter_version == 4:
        create_Tree_Keyword_Parameter = None
        create_Tree_Map_Parameter     = None

        from    Z.Tree.Parameter_V4         import  create_Tree_Normal_Parameter

        create_Tree_Star_Parameter = None
    elif parameter_version == 5:
        create_Tree_Keyword_Parameter = None

        from    Z.Tree.Parameter_V5         import  create_Tree_Map_Parameter
        from    Z.Tree.Parameter_V5         import  create_Tree_Normal_Parameter
        from    Z.Tree.Parameter_V5         import  create_Tree_Star_Parameter
    elif parameter_version == 6:
        from    Z.Tree.Parameter_V6         import  create_Tree_Keyword_Parameter
        from    Z.Tree.Parameter_V6         import  create_Tree_Map_Parameter
        from    Z.Tree.Parameter_V6         import  create_Tree_Normal_Parameter
        from    Z.Tree.Parameter_V6         import  create_Tree_Star_Parameter
    else:
        FATAL_unknown_version('parameter', parameter_version)


    if parameter_version in ((2, 3, 4)):
        from    Z.Tree.Parameter_Tuple_V1   import  create_Tree_All_Parameters
        
        create_Tree_Parameter_Tuple = None
    elif parameter_version == 5:
        from    Z.Tree.Parameter_Tuple_V5   import  create_Tree_All_Parameters
        
        create_Tree_Parameter_Tuple = None
    elif parameter_version == 6:
        create_Tree_All_Parameters = None

        from    Z.Tree.Parameter_Tuple_V6   import  create_Tree_Parameter_Tuple
    else:
        FATAL_unknown_version('parameter', parameter_version)


    #
    #   Statements
    #
    if statement_version in ((2, 3, 4, 5, 6, 7)):
        from    Z.Tree.Convert_Except_V2    import  convert_full_list_of_except_clauses
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3)):
        from    Z.Tree.Convert_From_Import_V2   import  convert_from_import_statement
    elif statement_version in ((4, 5, 6, 7)):
        from    Z.Tree.Convert_From_Import_V4   import  convert_from_import_statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6, 7)):
        from    Z.Tree.Convert_Import_V2    import  convert_import_statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6)):
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_For_Statement           #   "_V1" on purpose.
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_If_Statement            #   "_V1" on purpose.
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_Try_Except_Statement    #   "_V1" on purpose.
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_Try_Finally_Statement   #   "_V1" on purpose.
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_While_Statement         #   "_V1" on purpose.
        from    Z.Tree.Compound_Statement_V1    import  create_Tree_With_Statement          #   "_V1" on purpose.
    elif statement_version == 7:
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_For_Statement
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_If_Statement
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_Try_Except_Statement
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_Try_Finally_Statement
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_While_Statement
        from    Z.Tree.Compound_Statement_V7    import  create_Tree_With_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Global_V2    import  convert_global_statement
    elif statement_version == 5:
        from    Z.Tree.Convert_Global_V5    import  convert_global_statement
    elif statement_version in ((6, 7)):
        from    Z.Tree.Convert_Global_V6    import  convert_global_statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6, 7)):
        from    Z.Tree.Convert_Statement_V2     import  convert_statement
        from    Z.Tree.Convert_Statement_V2     import  convert_full_list_of_statements
        from    Z.Tree.Convert_Statement_V2     import  convert_some_list_of_statements
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6, 7)):
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_assert_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_assign_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_break_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_continue_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_delete_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_execute_statement
        from    Z.Tree.Convert_Simple_Statement_V2  import  convert_expression_statement
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
    elif statement_version in ((3, 4, 5, 6)):
        from    Z.Tree.Convert_Definition_V3    import  convert_class_definition
        from    Z.Tree.Convert_Definition_V3    import  convert_function_definition
    elif statement_version == 7:
        from    Z.Tree.Convert_Definition_V7    import  convert_class_definition
        from    Z.Tree.Convert_Definition_V7    import  convert_function_definition
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6)):
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_for_statement
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_if_statement
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_try_except_statement
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_try_finally_statement
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_while_statement
        from    Z.Tree.Convert_Compound_Statement_V2    import  convert_with_statement
    elif statement_version == 7:
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_for_statement
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_if_statement
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_try_except_statement
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_try_finally_statement
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_while_statement
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_with_statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version == 2:
        from    Z.Tree.Definition_V1    import  create_Tree_Class_Definition        #   "_V1" on purpose.
        from    Z.Tree.Definition_V1    import  create_Tree_Function_Definition     #   "_V1" on purpose.
    elif statement_version in ((3, 4, 5, 6)):
        from    Z.Tree.Definition_V3    import  create_Tree_Class_Definition
        from    Z.Tree.Definition_V3    import  create_Tree_Function_Definition
    elif statement_version == 7:
        from    Z.Tree.Definition_V7    import  create_Tree_Class_Definition
        from    Z.Tree.Definition_V7    import  create_Tree_Function_Definition
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6, 7)):
        from    Z.Tree.Except_V1        import  create_Tree_Except_Handler          #   "_V1" on purpose.
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3)):
        from    Z.Tree.From_Import_V1   import  create_Tree_From_Import_Statement   #   "_V1" on purpose.
    elif statement_version in ((4, 5, 6)):
        from    Z.Tree.From_Import_V4   import  create_Tree_From_Import_Statement
    elif statement_version == 7:
        from    Z.Tree.From_Import_V7   import  create_Tree_From_Import_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6)):
        from    Z.Tree.Import_V1        import  create_Tree_Import_Statement        #   "_V1" on purpose.
    elif statement_version == 7:
        from    Z.Tree.Import_V7        import  create_Tree_Import_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4)):
        from    Z.Tree.Global_V1        import  create_Tree_Global_Statement        #   "_V1" on purpose.
    elif statement_version == 5:
        from    Z.Tree.Global_V5        import  create_Tree_Global_Statement
    elif statement_version == 6:
        from    Z.Tree.Global_V6        import  create_Tree_Global_Statement
    elif statement_version == 7:
        from    Z.Tree.Global_V7        import  create_Tree_Global_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6)):
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Assert_Statement        #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Assign_Statement        #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Break_Statement         #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Continue_Statement      #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Delete_Statement        #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Execute_Statement       #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Expression_Statement    #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Modify_Statement        #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Pass_Statement          #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Print_Statement         #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Raise_Statement         #   "_V1" on purpose.
        from    Z.Tree.Simple_Statement_V1      import  create_Tree_Return_Statement        #   "_V1" on purpose.
    elif statement_version == 7:
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Assert_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Assign_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Break_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Continue_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Delete_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Execute_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Expression_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Modify_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Pass_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Print_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Raise_Statement
        from    Z.Tree.Simple_Statement_V7      import  create_Tree_Return_Statement
    else:
        FATAL_unknown_version('statement', statement_version)


    #
    #   Suite (only used in statement version 7)
    #
    if statement_version in ((2, 3, 4, 5, 6)):
        convert_suite   = None
        convert_suite_0 = None
    elif statement_version == 7:
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_suite
        from    Z.Tree.Convert_Compound_Statement_V7    import  convert_suite_0
    else:
        FATAL_unknown_version('statement', statement_version)


    if statement_version in ((2, 3, 4, 5, 6)):
        create_Tree_Suite = None
    elif statement_version == 7:
        from    Z.Tree.Suite_V7         import  create_Tree_Suite
    else:
        FATAL_unknown_version('statement', statement_version)


    #
    #   Symbol
    #
    if symbol_version == 0:
        conjure_parser_symbol = None
    elif symbol_version == 2:
        from    Z.Parser.Symbol_V2          import  conjure_parser_symbol
    elif symbol_version == 3:
        from    Z.Parser.Symbol_V3          import  conjure_parser_symbol
    elif symbol_version == 4:
        from    Z.Parser.Symbol_V4          import  conjure_parser_symbol
    elif symbol_version == 5:
        from    Z.Parser.Symbol_V5          import  conjure_parser_symbol
    elif symbol_version == 6:
        from    Z.Parser.Symbol_V6          import  conjure_parser_symbol
    else:
        FATAL_unknown_version('symbol', symbol_version)


    if symbol_version in ((0, 2, 3)):
        conjure_parser_symbol_0 = None
    elif symbol_version == 4:
        from    Z.Parser.Symbol_V4          import  conjure_parser_symbol_0
    elif symbol_version in ((5, 6)):
        conjure_parser_symbol_0 = None
    else:
        FATAL_unknown_version('symbol', symbol_version)


    if symbol_version in ((0, 2, 3, 4, 5)):
        create_Parser_Symbol_Tuple = None
    elif symbol_version == 6:
        from    Z.Parser.Symbol_Tuple_V6    import  create_Parser_Symbol_Tuple
    else:
        FATAL_unknown_version('symbol', symbol_version)


    #
    #   Target
    #
    if target_version in ((2, 3)):
        #
        #    No need to define these, leave them vacant (i.e.: uninitialized).
        #
       #create_Tree_Delete_Attribute   = VACANT
       #create_Tree_Evaluate_Attribute = VACANT
       #create_Tree_Store_Attribute    = VACANT

        pass
    elif target_version == 4:
        from    Z.Tree.Attribute_V4                 import  create_Tree_Delete_Attribute
        from    Z.Tree.Attribute_V4                 import  create_Tree_Evaluate_Attribute
        from    Z.Tree.Attribute_V4                 import  create_Tree_Store_Attribute
    else:
        FATAL_unknown_version('target', target_version)


    if target_version == 2:
        from    Z.Tree.Convert_Attribute_V2     import  convert_attribute_expression
    elif target_version == 3:
        from    Z.Tree.Convert_Attribute_V3     import  convert_attribute_expression
    elif target_version == 4:
        from    Z.Tree.Convert_Attribute_V4     import  convert_attribute_expression
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        from    Z.Tree.Convert_Many_V2          import  convert_list_expression
        from    Z.Tree.Convert_Many_V2          import  convert_tuple_expression
    elif target_version == 4:
        from    Z.Tree.Convert_Many_V4          import  convert_list_expression
        from    Z.Tree.Convert_Many_V4          import  convert_tuple_expression
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        from    Z.Tree.Convert_Subscript_V2     import  convert_subscript_expression
    elif target_version == 4:
        from    Z.Tree.Convert_Subscript_V4     import  convert_subscript_expression
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3, 4)):
        from    Z.Tree.Convert_Target_V2    import  convert_full_list_of_targets
        from    Z.Tree.Convert_Target_V2    import  convert_none_OR_target
        from    Z.Tree.Convert_Target_V2    import  convert_target
    else:
        FATAL_unknown_version('target', target_version)


    if target_version == 2:
        from    Z.Tree.Attribute_V1     import  create_Tree_Attribute           #   "_V1" on purpose.
    elif target_version == 3:
        from    Z.Tree.Attribute_V3     import  create_Tree_Attribute
    elif target_version == 4:
        create_Tree_Attribute = None
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        from    Z.Tree.Many_V1          import  create_Tree_List_Expression     #   "_V1" on purpose.
        from    Z.Tree.Many_V1          import  create_Tree_Tuple_Expression    #   "_V1" on purpose.
    elif target_version == 4:
        create_Tree_List_Expression  = None
        create_Tree_Tuple_Expression = None
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        #
        #    No need to define these, leave them vacant (i.e.: uninitialized).
        #
       #create_Tree_Evaluate_List  = VACANT
       #create_Tree_Evaluate_Tuple = VACANT
       #create_Tree_Store_List     = VACANT
       #create_Tree_Store_Tuple    = VACANT

        pass
    elif target_version == 4:
        from    Z.Tree.Many_V4          import  create_Tree_Evaluate_List
        from    Z.Tree.Many_V4          import  create_Tree_Evaluate_Tuple
        from    Z.Tree.Many_V4          import  create_Tree_Store_List
        from    Z.Tree.Many_V4          import  create_Tree_Store_Tuple
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        from    Z.Tree.Subscript_V1     import  create_Tree_Subscript_Expression    #   "_V1" on purpose.
    elif target_version == 4:
        create_Tree_Subscript_Expression = None
    else:
        FATAL_unknown_version('target', target_version)


    if target_version in ((2, 3)):
        #
        #    No need to define these, leave them vacant (i.e.: uninitialized).
        #
       #create_Tree_Delete_Subscript   = VACANT
       #create_Tree_Evaluate_Subscript = VACANT
       #create_Tree_Store_Subscript    = VACANT

        pass
    elif target_version == 4:
        from    Z.Tree.Subscript_V4                 import  create_Tree_Delete_Subscript
        from    Z.Tree.Subscript_V4                 import  create_Tree_Evaluate_Subscript
        from    Z.Tree.Subscript_V4                 import  create_Tree_Store_Subscript
    else:
        FATAL_unknown_version('target', target_version)


    #
    #   fact_no_context_fields
    #
    if __debug__:
        def fact_no_context_fields(mapping):
            for k in mapping:
                assert k._attributes == (())
                assert k._fields     == (())

            return True


    #
    #   (Used by context, versions 2 & 3)
    #
    #   1)  map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Context }
    #
    #       Map a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a `Tree_Context`.
    #
    #   2)  map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Context }
    #
    #       Map a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a `Tree_Context`.
    #
    if context_version == 0:
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = None
        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context        = None
    elif context_version in ((2, 3)):
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
                Native_AbstractSyntaxTree_Delete_Context : tree_delete_context,
                Native_AbstractSyntaxTree_Load_Context   : tree_load_context,
                Native_AbstractSyntaxTree_Store_Context  : tree_store_context,
            }

        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
                Native_AbstractSyntaxTree_Load_Context  : tree_load_context,
                Native_AbstractSyntaxTree_Store_Context : tree_store_context,
            }


        assert fact_no_context_fields(map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context)
        assert fact_no_context_fields(map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context)
    else:
        FATAL_unknown_version('context', context_version)


    #
    #   (Used by expression)
    #
    #   map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_expression" function.
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
            Native_AbstractSyntaxTree_String_Literal          : convert_string_literal,
            Native_AbstractSyntaxTree_Subscript_Expression    : convert_subscript_expression,
            Native_AbstractSyntaxTree_Tuple_Expression        : convert_tuple_expression,
            Native_AbstractSyntaxTree_Unary_Expression        : convert_unary_expression,
            Native_AbstractSyntaxTree_Yield_Expression        : convert_yield_expression,
        }


    #
    #   (Used by index)
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
    #   (Used by name, version 4)
    #
    #   map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "create_name" function.
    #
    if name_version in ((2, 3)):
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function      = None
    elif name_version == 4:
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function = {
                Native_AbstractSyntaxTree_Delete_Context : create_Tree_Delete_Name,
                Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Name,
                Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Name,
            }

        assert fact_no_context_fields(
                map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function,
            )
    else:
        FATAL_unknown_version('name', name_version)


    #
    #   (Used by operator)
    #
    #   1)  map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Operator }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) that represents a binary operator to a
    #           `Tree_Operator`.
    #
    #   2)  map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Operator }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) that represents a compare operator to a
    #           `Tree_Operator`.
    #
    #   3)  map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Operator }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) that represents a logical operator to a
    #           `Tree_Operator`.
    #
    #   4)  map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Operator }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) that represents a modify operator to a
    #           `Tree_Operator`.
    #
    #           A "modify" operator is an operator is an operator that can appear in a modify statement
    #           (i.e.: `+=`, `*=`, etc.).
    #
    #   5)  map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator
    #               : Map { Native_AbstractSyntaxTree_* : Tree_Operator }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) that represents a unary operator to a
    #           `Tree_Operator`.
    #
    map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator = {
            Native_AbstractSyntaxTree_Add_Operator                 : tree_add_operator,
            Native_AbstractSyntaxTree_Binary_And_Operator          : tree_binary_and_operator,
            Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator : tree_binary_exclusive_or_operator,
            Native_AbstractSyntaxTree_Divide_Operator              : tree_divide_operator,
            Native_AbstractSyntaxTree_Floor_Divide_Operator        : tree_floor_divide_operator,
            Native_AbstractSyntaxTree_Left_Shift_Operator          : tree_left_shift_operator,
            Native_AbstractSyntaxTree_Modulus_Operator             : tree_modulus_operator,
            Native_AbstractSyntaxTree_Multiply_Operator            : tree_multiply_operator,
            Native_AbstractSyntaxTree_Power_Operator               : tree_power_operator,
            Native_AbstractSyntaxTree_Right_Shift_Operator         : tree_right_shift_operator,
            Native_AbstractSyntaxTree_Subtract_Operator            : tree_subtract_operator,
        }

    map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator = {
            Native_AbstractSyntaxTree_Compare_Different_Operator : tree_compare_different_operator,
            Native_AbstractSyntaxTree_Compare_Equal_Operator     : tree_compare_equal_operator,

            Native_AbstractSyntaxTree_Compare_Greater_Than_Or_Equal_Operator:
                tree_compare_greater_than_or_equal_operator,

            Native_AbstractSyntaxTree_Compare_Greater_Than_Operator       : tree_compare_greater_than_operator,
            Native_AbstractSyntaxTree_Compare_Identity_Operator           : tree_compare_identity_operator,
            Native_AbstractSyntaxTree_Compare_Less_Than_Or_Equal_Operator : tree_compare_less_than_or_equal_operator,
            Native_AbstractSyntaxTree_Compare_Less_Than_Operator          : tree_compare_less_than_operator,
            Native_AbstractSyntaxTree_Compare_Not_Equal_Operator          : tree_compare_not_equal_operator,
            Native_AbstractSyntaxTree_Contains_Operator                   : tree_contains_operator,
            Native_AbstractSyntaxTree_Excludes_Operator                   : tree_excludes_operator,
        }

    map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator = {
            Native_AbstractSyntaxTree_Logical_And_Operator : tree_logical_and_operator,
            Native_AbstractSyntaxTree_Logical_Or_Operator  : tree_logical_or_operator,
        }

    map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator = {
            Native_AbstractSyntaxTree_Subtract_Operator : tree_subtract_operator,
        }

    map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator = {
            Native_AbstractSyntaxTree_Invert_Operator   : tree_invert_operator,
            Native_AbstractSyntaxTree_Negative_Operator : tree_negative_operator,
            Native_AbstractSyntaxTree_Positive_Operator : tree_positive_operator,
            Native_AbstractSyntaxTree_Not_Operator      : tree_not_operator,
        }


    #
    #   (Used by statement)
    #
    #   map__Native_AbstractSyntaxTree_STATEMENT__to__convert_statement__function
    #           : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_statement" function.
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
    #   (Used by target, version 4)
    #
    #   1)  map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function
    #               : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "create_attribute" function.
    #
    #   2)  map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function
    #               : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "create_subscript" function.
    #
    #   3)  map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_list_function
    #               : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "create_list" function.
    #
    #   4)  map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_tuple_function
    #               : Map { Native_AbstractSyntaxTree_* : Function }
    #
    #           This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "create_tuple" function.
    #
    if target_version in ((2, 3)):
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function = None
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function = None
        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function             = None
        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function            = None
    elif target_version == 4:
        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function = {
                Native_AbstractSyntaxTree_Delete_Context : create_Tree_Delete_Attribute,
                Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Attribute,
                Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Attribute,
            }


        map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function = {
                Native_AbstractSyntaxTree_Delete_Context : create_Tree_Delete_Subscript,
                Native_AbstractSyntaxTree_Load_Context   : create_Tree_Evaluate_Subscript,
                Native_AbstractSyntaxTree_Store_Context  : create_Tree_Store_Subscript,
            }

        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function = {
                Native_AbstractSyntaxTree_Load_Context  : create_Tree_Evaluate_List,
                Native_AbstractSyntaxTree_Store_Context : create_Tree_Store_List,
            }

        map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function = {
                Native_AbstractSyntaxTree_Load_Context  : create_Tree_Evaluate_Tuple,
                Native_AbstractSyntaxTree_Store_Context : create_Tree_Store_Tuple,
            }

        for mapping in ((
               map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function,
               map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function,
               map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function,
               map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function,
        )):
            assert fact_no_context_fields(mapping)
    else:
        FATAL_unknown_version('target', target_version)


    #
    #   (Used by target)
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

    z.create_Tree_Keyword_Argument = create_Tree_Keyword_Argument


    #
    #   Alias
    #
    z.convert_full_list_of_module_aliases = convert_full_list_of_module_aliases
    z.convert_full_list_of_symbol_aliases = convert_full_list_of_symbol_aliases

    z.create_Tree_Module_Alias = create_Tree_Module_Alias
    z.create_Tree_Symbol_Alias = create_Tree_Symbol_Alias


    #
    #   Comprehension
    #
    z.convert_full_list_of_comprehensions = convert_full_list_of_comprehensions

    z.create_Tree_Comprehension_Clause = create_Tree_Comprehension_Clause


    #
    #   Context
    #
    z.convert_delete_load_OR_store_context = convert_delete_load_OR_store_context
    z.convert_load_OR_store_context        = convert_load_OR_store_context
    z.convert_parameter_context            = convert_parameter_context

    z.tree_delete_context    = tree_delete_context
    z.tree_parameter_context = tree_parameter_context

    z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = (
            map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context
        )

    z.map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context = (
            map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__to__Tree_Context
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

    z.create_Tree_Backquote_Expression    = create_Tree_Backquote_Expression
    z.create_Tree_Binary_Expression       = create_Tree_Binary_Expression
    z.create_Tree_Call_Expression         = create_Tree_Call_Expression
    z.create_Tree_Compare_Expression      = create_Tree_Compare_Expression
    z.create_Tree_Generator_Comprehension = create_Tree_Generator_Comprehension
    z.create_Tree_If_Expression           = create_Tree_If_Expression
    z.create_Tree_Lambda_Expression       = create_Tree_Lambda_Expression
    z.create_Tree_List_Comprehension      = create_Tree_List_Comprehension
    z.create_Tree_Logical_Expression      = create_Tree_Logical_Expression
    z.create_Tree_Map_Comprehension       = create_Tree_Map_Comprehension
    z.create_Tree_Map_Expression          = create_Tree_Map_Expression
    z.create_Tree_Number                  = create_Tree_Number
    z.create_Tree_Set_Comprehension       = create_Tree_Set_Comprehension
    z.create_Tree_Set_Expression          = create_Tree_Set_Expression
    z.create_Tree_String                  = create_Tree_String
    z.create_Tree_Unary_Expression        = create_Tree_Unary_Expression
    z.create_Tree_Yield_Expression        = create_Tree_Yield_Expression

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
    #   Module
    #
    z.create_Tree_Module = create_Tree_Module


    #
    #   Module_Name
    #
    z.conjure_parser_module_name          = conjure_parser_module_name
    z.conjure_parser_module_name_with_dot = conjure_parser_module_name_with_dot


    #
    #   Name
    #
    z.create_Tree_Name             = create_Tree_Name

    z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function = (
            map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_name__function
        )

    #
    #   Operator (version 1 or 3.  Version 2 does not exist).
    #
    z.convert_binary_operator                = convert_binary_operator
    z.convert_full_list_of_compare_operators = convert_full_list_of_compare_operators
    z.convert_logical_operator               = convert_logical_operator
    z.convert_modify_operator                = convert_modify_operator
    z.convert_unary_operator                 = convert_unary_operator

    z.map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator = (
            map__Native_AbstractSyntaxTree_OPERATOR__to__BINARY__Tree_Operator
        )

    z.map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator = (
            map__Native_AbstractSyntaxTree_OPERATOR__to__COMPARE__Tree_Operator
        )

    z.map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator = (
            map__Native_AbstractSyntaxTree_OPERATOR__to__LOGICAL__Tree_Operator
        )

    z.map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator = (
            map__Native_AbstractSyntaxTree_OPERATOR__to__MODIFY__Tree_Operator
        )

    z.map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator = (
            map__Native_AbstractSyntaxTree_OPERATOR__to__UNARY__Tree_Operator
        )


    #
    #   Parameter
    #
    z.convert_parameter_tuple_0 = convert_parameter_tuple_0

    z.create_Tree_All_Parameters    = create_Tree_All_Parameters
    z.create_Tree_Keyword_Parameter = create_Tree_Keyword_Parameter
    z.create_Tree_Map_Parameter     = create_Tree_Map_Parameter
    z.create_Tree_Normal_Parameter  = create_Tree_Normal_Parameter
    z.create_Tree_Parameter_Tuple   = create_Tree_Parameter_Tuple
    z.create_Tree_Star_Parameter    = create_Tree_Star_Parameter


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
    z.convert_suite   = convert_suite
    z.convert_suite_0 = convert_suite_0

    z.create_Tree_Suite = create_Tree_Suite


    #
    #   Symbol
    #
    z.conjure_parser_symbol   = conjure_parser_symbol
    z.conjure_parser_symbol_0 = conjure_parser_symbol_0

    z.create_Parser_Symbol_Tuple = create_Parser_Symbol_Tuple


    #
    #   Target
    #
    z.convert_full_list_of_targets = convert_full_list_of_targets
    z.convert_none_OR_target       = convert_none_OR_target
    z.convert_target               = convert_target

    z.create_Tree_Attribute            = create_Tree_Attribute
    z.create_Tree_List_Expression      = create_Tree_List_Expression
    z.create_Tree_Subscript_Expression = create_Tree_Subscript_Expression
    z.create_Tree_Tuple_Expression     = create_Tree_Tuple_Expression

    z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function = (
            map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_attribute__function
        )

    z.map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function = (
            map__Native_AbstractSyntaxTree__DELETE_LOAD_OR_STORE_CONTEXT__TO__create_subscript__function
        )

    z.map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function = (
            map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_list__function
        )

    z.map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function = (
            map__Native_AbstractSyntaxTree__LOAD_OR_STORE_CONTEXT__TO__create_tuple__function
        )

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
