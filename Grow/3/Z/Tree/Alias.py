#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias - Interface to tree classes that represent tree aliases.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       Explanation:
#
#           A "tree alias" is used to indicate an [aliased or unaliased] `import` statement (or `from` statement).
#
#       Example:
#
#           In the following statements:
#
#               import              a, b as c
#               from    d   import  e, f as g
#
#           There are four aliases:
#
#               `a`         - Import of module `a` (not aliased, so member `.as_name` is `None`).
#
#               `b as c`    - Import of module `b`, aliased to symbol `c`.
#
#               `e`         - Import of symbol `e` (not aliased, so member `.as_name` is `None`).
#
#               `f as g`    - Import of symbol `f`, aliased to symbol `g`.
#


#
#   interface Tree_Alias - Interface to tree classes that represent aliases.
#
#       interface Tree_Alias
#           debug
#               is_tree_alias := true
#
#           method
#               dump_alias_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Alias(object):
    __slots__ = (())


    if __debug__:
        is_tree_alias = True



#
#   USAGE:
#
#       v.is_tree_alias                     #   Test if `v` is a `Tree_Alias`.
#
#       v.dump_alias_tokens(f)              #   Dump the tokens representing the tree alias to `f`.
#
#       assert fact_is_tree_alias(v) )      #   Assert that `v` is a tree alias.
#



#
#   fact_is_tree_alias(v) - Assert the fact that `v` is a `Tree_Alias`.
#
if __debug__:
    def fact_is_tree_alias(v):
        assert v.is_tree_alias

        return True
