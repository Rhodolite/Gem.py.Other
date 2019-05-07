#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Expression - Interface to tree classes that represent expressions.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Expression
#       documentation
#           Interface to tree classes that represent expressions.
#
#       method
#           dump_evaluate_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_expression := true
#


#
#   USAGE:
#
#       v.is_tree_expression                    #   Test if `v` is a tree expression.
#
#       v.dump_evaluate_tokens(f)               #   Dump the tokens representing the tree expression to `f`.
#                                               #
#                                               #   The expression is being "evaluated" in a "load" context, hence
#                                               #   the name is `dump_evaluate_tokens` instead of
#                                               #   `dump_expression_tokens`.
#                                               #
#                                               #   See "Z/Tree/Context" for for an explanation of a "load" context).
#
#       assert fact_is__native_none__OR__tree_expression(v)
#                                               #   Assert that `v` is either `None` or a tree expression.
#
#       assert fact_is_tree_expression(v)       #   Assert that `v` is a tree expression.
#



#
#   fact_is__native_none__OR__tree_expression(v)
#
#       Assert that `v` is either `None` or a `Tree_Expression`.
#
if __debug__:
    def fact_is__native_none__OR__tree_expression(v):
        if v is None:
            return True

        assert v.is_tree_expression

        return True


#
#   fact_is_tree_expression(v) - Assert that `v` is a `Tree_Expression`.
#
if __debug__:
    def fact_is_tree_expression(v):
        assert v.is_tree_expression

        return True
