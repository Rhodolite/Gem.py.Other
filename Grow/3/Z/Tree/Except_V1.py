#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Except_V1 - Implementation of `Tree_Except_Clause`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression


#
#   Tree: Except Handler, Version 1
#
class Tree_Except_Handler_V1(object):
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'type_expression',              #   None | Tree_Expression
        'name_expression',              #   None | Tree_Expression
        'body',                         #   FullNativeList of Tree_Statment
    ))


    def __init__(self, line_number, column, type_expression, name_expression, body):
        self.line_number = line_number
        self.column      = column

        self.type_expression = type_expression
        self.name_expression = name_expression
        self.body            = body


    def __repr__(self):
        return arrange('<Tree_Except_Handler_V1 @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.type_expression, self.name_expression, self.body)


    def dump_except_clause_tokens(self, f):
        f.arrange('<except @{}:{}', self.line_number, self.column)

        if self.type_expression is not None:
            f.space()
            self.type_expression.dump_evaluate_tokens(f)

            if self.name_expression is not None:
                f.write(' as ')
                self.name_expression.dump_store_target_tokens(f)

        f.line(' {')

        with f.indent_2():
            for v in self.body:
                v.dump_token(f)

        f.line('}>')


def create_Tree_Except_Handler_V1(line_number, column, type_expression, name_expression, body):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is__native_none__OR__tree_expression(type_expression)
    assert fact_is__native_none__OR__tree_expression(name_expression)
    assert fact_is_full_native_list                 (body)

    if type_expression is None:
        assert fact_is_native_none(name_expression)

    return Tree_Except_Handler_V1(line_number, column, type_expression, name_expression, body) 
