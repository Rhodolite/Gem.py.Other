#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Statement - Interface to tree classes that represent statement.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Statement
#       documentation
#           Interface to tree classes that represent statements.
#
#       debug
#           is_tree_statement := true
#
#       method
#           dump_statement_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Statement(object):
    __slots__ = (())

    if __debug__:
        is_tree_statement = True


#
#   USAGE:
#
#       v.dump_statement_tokens(f)          #   Dump the tokens representing the tree statement(s) to `f`.
#


#
#   USAGE (debug mode):
#
#       v.is_tree_statement                 #   Test if `v` is a tree statement.
#
#       assert fact_is_tree_statement(v)    #   Assert that `v` is a tree statement.
#



#
#   fact_is_tree_statement(v) - Assert that `v` is a `Tree_Statement`.
#
if __debug__:
    def fact_is_tree_statement(v):
        assert v.is_tree_statement

        return True
