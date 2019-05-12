#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Except_V8 - Implementation of `Tree_Except_Clause`, Version 8.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 1..8:
#
#       Version 1:
#
#           `.target_expression` is of type `None | Tree_Store_Target`.
#
#       Versions 2..7:
#
#           Do not exist.
#
#       Version 8:
#
#           `.target_expression` is of type `Tree_Store_Target_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Except                   import  TRAIT_Tree_Except_Clause


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression
    from    Z.Tree.Target               import  fact_is_tree_store_target_0


#
#   Tree: Except Handler
#
class Tree_Except_Handler(
        TRAIT_Tree_Except_Clause,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'type_expression',              #   None | Tree_Value_Expression
        'target_expression',            #   Tree_Store_Target_0
        'body',                         #   Full_Native_List of Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, type_expression, target_expression, body):
        self.line_number = line_number
        self.column      = column

        self.type_expression   = type_expression
        self.target_expression = target_expression
        self.body              = body


    #
    #   Interface Tree_Except_Clause
    #
    def dump_except_clause_tokens(self, f):
        f.arrange('<except @{}:{}', self.line_number, self.column)

        if self.type_expression is not None:
            f.space()
            self.type_expression.dump_value_expression_tokens(f)

            if self.target_expression.has_store_target:
                f.write(' as ')
                self.target_expression.dump_store_target_tokens(f)

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
                       self.line_number, self.column, self.type_expression, self.target_expression, self.body)



@creator
def create_Tree_Except_Handler(line_number, column, type_expression, target_expression, body):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is__native_none__OR__tree_value_expression(type_expression)
    assert fact_is_tree_store_target_0                    (target_expression)
    assert fact_is_full_native_list                       (body)

    if type_expression is None:
        assert not target_expression.has_store_target

    return Tree_Except_Handler(line_number, column, type_expression, target_expression, body)
