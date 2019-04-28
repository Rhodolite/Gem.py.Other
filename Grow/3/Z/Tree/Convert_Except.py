#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Except - Convert Python Abstract Syntax Tree Except Handler to `Tree_Except_Handler`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Statement            import  convert_full_list_of_statements
from    Z.Tree.Except                       import  create_Tree_Except_Handler
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Except_Handler


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_native_none
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Fact                        import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION


#
#   convert_except_handler
#
#       Convert a `Native_AbstractSyntaxTree_Except_Handler` (i.e.: `_ast.ExceptHandler`) to a
#       `Tree_Except_Handler`.
#
assert Native_AbstractSyntaxTree_Except_Handler._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Except_Handler._fields     == (('type', 'name', 'body'))


def convert_except_handler(self):
    if 0:
        #
        #   Copy this disabled code into a new convert method, to trace the attributes & fields and help write the new
        #   method.
        #
        #   This code was used to write most of the convert methods in the "Z/Test/Convert_*.py" files :)
        #
        function_name = 'convert_except_handler'

        trace('{}:              {!r}', function_name, self)
        trace('{}._attributes:  {!r}', function_name, self._attributes)
        trace('{}._fields:      {!r}', function_name, self._fields)

        trace('{}.lineno        {!r}', function_name, self.lineno)
        trace('{}.col_offset    {!r}', function_name, self.col_offset)

        trace('{}.type: {!r}', function_name, self.type)
        trace('{}.name: {!r}', function_name, self.name)
        trace('{}.body: {!r}', function_name, self.body)

    assert fact_is_positive_integer   (self.lineno)
    assert fact_is_substantial_integer(self.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.name)
    assert fact_is_full_native_list                                                  (self.body)

    if self.type is None:
        assert fact_is_native_none(self.name)
        
    return create_Tree_Except_Handler(
               self.lineno,
               self.col_offset,

               convert_none_OR_expression     (self.type),
               convert_none_OR_expression     (self.name),
               convert_full_list_of_statements(self.body),
           )


#
#   convert_except_clause(v)
#
#       Currently there is only one type of "except clause", the "except handler".
#
#       Hence this routine just calls `convert_except_handler`.
#
def convert_except_clause(v):
    return convert_except_handler(v)


#
#   convert_full_list_of_except_clauses
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Except_Handler` (i.e.: `list of _ast.ExceptHandler`) to
#       a `NativeList of Tree_Except_Clause`.
#
def convert_full_list_of_except_clauses(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_except_clause(v)   for v in sequence]
