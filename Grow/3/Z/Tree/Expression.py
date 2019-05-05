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


#
#   Import the version of tree expressions we want to use (must be after the "facts" above)
#
from    Z.Parser.Global                 import  parser_globals


version = parser_globals.expression_version


if version == '1':
    from    Z.Tree.Expression_V1        import  (
                create_Tree_Backquote_Expression_V1     as  create_Tree_Backquote_Expression,
                create_Tree_Binary_Expression_V1        as  create_Tree_Binary_Expression,
                create_Tree_Call_V1                     as  create_Tree_Call,
                create_Tree_Compare_Expression_V1       as  create_Tree_Compare_Expression,
                create_Tree_Generator_Comprehension_V1  as  create_Tree_Generator_Comprehension,
                create_Tree_If_Expression_V1            as  create_Tree_If_Expression,
                create_Tree_Lambda_Expression_V1        as  create_Tree_Lambda_Expression,
                create_Tree_List_Comprehension_V1       as  create_Tree_List_Comprehension,
                create_Tree_Map_Comprehension_V1        as  create_Tree_Map_Comprehension,
                create_Tree_Map_Expression_V1           as  create_Tree_Map_Expression,
                create_Tree_Number_V1                   as  create_Tree_Number,
                create_Tree_Set_Comprehension_V1        as  create_Tree_Set_Comprehension,
                create_Tree_Set_Expression_V1           as  create_Tree_Set_Expression,
                create_Tree_String_V1                   as  create_Tree_String,
                create_Tree_Unary_Expression_V1         as  create_Tree_Unary_Expression,
                create_Tree_Logical_Expression_V1       as  create_Tree_Logical_Expression,
                create_Tree_Yield_Expression_V1         as  create_Tree_Yield_Expression,
        )
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Expression.py: unknown tree expression version: {!r}', version)
