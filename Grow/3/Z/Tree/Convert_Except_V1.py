#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Except_V1 - Convert Python Abstract Syntax Tree Except Handler to `Tree_Except_Handler`, Version 1
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Expression_V1        import  convert_none_OR_expression
from    Z.Tree.Convert_Statement_V1         import  convert_full_list_of_statements
from    Z.Tree.Except_V1                    import  create_Tree_Except_Handler
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_none
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Except_Handler


#
#   convert_except_handler(v)
#
#       Convert a `Native_AbstractSyntaxTree_Except_Handler` (i.e.: `_ast.ExceptHandler`) to a
#       `Tree_Except_Handler`.
#
assert Native_AbstractSyntaxTree_Except_Handler._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Except_Handler._fields     == (('type', 'name', 'body'))


def convert_except_handler(v):
    if 0:
        #
        #   Copy this disabled code into a new convert method, to trace the attributes & fields and help write the new
        #   method.
        #
        #   This code was used to write most of the convert methods in the "Z/Test/Convert_*.py" files :)
        #
        function_name = 'convert_except_handler'

        trace('{}:              {!r}', function_name, v)
        trace('{}._attributes:  {!r}', function_name, v._attributes)
        trace('{}._fields:      {!r}', function_name, v._fields)

        trace('{}.lineno        {!r}', function_name, v.lineno)
        trace('{}.col_offset    {!r}', function_name, v.col_offset)

        trace('{}.type: {!r}', function_name, v.type)
        trace('{}.name: {!r}', function_name, v.name)
        trace('{}.body: {!r}', function_name, v.body)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.name)
    assert fact_is_full_native_list                                                  (v.body)

    if v.type is None:
        assert fact_is_native_none(v.name)

    return create_Tree_Except_Handler(
               v.lineno,
               v.col_offset,

               convert_none_OR_expression     (v.type),
               convert_none_OR_expression     (v.name),
               convert_full_list_of_statements(v.body),
           )


#
#   convert_except_clause(v)
#
#       Currently there is only one type of "except clause", the "except handler".
#
#       Hence this routine just calls `convert_except_handler`.
#
convert_except_clause = convert_except_handler


#
#   convert_full_list_of_except_clauses
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Except_Handler` (i.e.: `list of _ast.ExceptHandler`) to
#       a `NativeList of Tree_Except_Clause`.
#
convert_full_list_of_except_clauses = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_except_clause)
    )
