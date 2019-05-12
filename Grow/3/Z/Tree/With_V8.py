#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.With_V8 - Implementation of `Tree_While_Statement`, Version 8.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 7 and Version 8.
#
#       Version 7:
#
#           `.target` is of type `None | Tree_Store_Target`.
#
#       Version 8:
#
#           `.target` is of type `Tree_Store_Target_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Suite                import  fact_is_tree_suite
    from    Z.Tree.Suite                import  fact_is_tree_suite_0
    from    Z.Tree.Target               import  fact_is_tree_store_target_0


#
#   Tree: With Statement
#
class Tree_With_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
        'target',                       #   None | Tree_Store_Target
        'body',                         #   Tree_Statement
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, value, target, body):
        self.line_number = line_number
        self.column      = column

        self.value  = value
        self.target = target
        self.body   = body


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<with @{}:{} ', self.line_number, self.column)
        self.value.dump_value_expression_tokens(f)

        if self.target.has_store_target:
            f.write(' as ')
            self.target.dump_store_target_tokens(f)

        f.line(' {')

        with f.indent_2():
            self.body.dump_suite_tokens(f)

        f.line('}>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_With_Statement @{}:{} {!r} {!r}>',
                       self.line_number, self.column, self.value, self.target)


@creator
def create_Tree_With_Statement(line_number, column, value, target, body):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression(value)
    assert fact_is_tree_store_target_0  (target)
    assert fact_is_tree_suite           (body)

    return Tree_With_Statement(line_number, column, value, target, body)
