#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.None - Interface to tree class that represents `None`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       `tree_none` is used to represent where `None` appears in `_ast.*`, and also to represent empty lists.
#


#
#   Tree: None
#
class Tree_None(object):
    #
    #   Implements Tree_Statement
    #
    __slots__ = (())


    #
    #   Interface Tree_Statement
    #
    if __debug__:
        is_tree_statement = True


    suite_estimate = 0


    @staticmethod
    def dump_suite_tokens(f):
        f.line('<statement-none>')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<tree-none>'


def create_Tree_None():
    return Tree_None()


tree_none = create_Tree_None()
