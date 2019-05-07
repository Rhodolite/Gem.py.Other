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
class TRAIT_Tree_Argument(object):
    __slots__ = (())


    if __debug__:
        is_tree_argument = True


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
#   fact_is_tree_argument(v) - Assert the fact that `v` is a `Tree_Argument`.
#
if __debug__:
    def fact_is_tree_argument(v):
        assert v.is_tree_argument

        return True
