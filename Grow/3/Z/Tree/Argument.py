#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Argument - Interface to tree classes that represent tree [function] argments.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Argument - Interface to tree classes that represent [function] arguments.
#
#       interface Tree_Argument
#           method
#               dump_argument_tokens(f : Build_DumpToken)
#
#           debug
#               is_tree_argument := true
#


#
#   USAGE:
#
#       v.is_tree_argument                  #   Test if `v` is a `Tree_Argument`.
#
#       v.dump_argument_tokens(f)           #   Dump the tokens representing the tree [function] arguments to `f`.
#
#       assert fact_is_tree_argument(v)     #   Assert that `v` is a tree [function] argument.
#


#
#   Import the version of tree aliases we want to use
#
from    Z.Tree.Global                   import  tree_globals


tree_version = tree_globals.tree_version


if tree_version in (('1', '2')):
    from    Z.Tree.Argument_1               import  create_Tree_Keyword_Argument_V1     as  create_Tree_Keyword_Argument
else:
    from    Capital.Core                    import  FATAL

    FATAL('Z/Tree/Argument.py: unknown tree version: {}', tree_version)


#
#   fact_is_tree_argument(v) - Assert the fact that `v` is a `Tree_Argument`.
#
if __debug__:
    def fact_is_tree_argument(v):
        assert v.is_tree_argument

        return True
