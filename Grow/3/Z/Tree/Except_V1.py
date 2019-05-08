#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Except_V1 - Implementation of `Tree_Except_Clause`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Except                   import  TRAIT_Tree_Except_Clause


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression


#
#   Tree: Except Handler
#
class Tree_Except_Handler(
        TRAIT_Tree_Except_Clause,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'type_expression',              #   None | Tree_Value_Expression
        'name_expression',              #   None | Tree_Value_Expression
        'body',                         #   FullNativeList of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, type_expression, name_expression, body):
        self.line_number = line_number
        self.column      = column

        self.type_expression = type_expression
        self.name_expression = name_expression
        self.body            = body


    #
    #   Interface Tree_Except_Clause
    #
    def dump_except_clause_tokens(self, f):
        f.arrange('<except @{}:{}', self.line_number, self.column)

        if self.type_expression is not None:
            f.space()
            self.type_expression.dump_value_expression_tokens(f)

            if self.name_expression is not None:
                f.write(' as ')
                self.name_expression.dump_store_target_tokens(f)

        f.line(' {')

        with f.indent_2():
            for v in self.body:
                v.dump_statement_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Except_Handler @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.type_expression, self.name_expression, self.body)



@creator
def create_Tree_Except_Handler(line_number, column, type_expression, name_expression, body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_value_expression(type_expression)
    assert fact_is__native_none__OR__tree_value_expression(name_expression)
    assert fact_is_full_native_list                       (body)

    if type_expression is None:
        assert fact_is_native_none(name_expression)

    return Tree_Except_Handler(line_number, column, type_expression, name_expression, body)
