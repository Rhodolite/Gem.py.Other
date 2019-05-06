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
#   interface Tree_Module_Alias
#       documentation
#           Interface to tree classes that represent module aliases.
#
#       debug
#           is_tree_module_alias := true
#
#       method
#           dump_module_alias_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Module_Alias(object):
    __slots__ = (())


    if __debug__:
        is_tree_module_alias = True


#
#   interface Tree_Symbol_Alias
#       documentation
#           Interface to tree classes that represent symbol aliases.
#
#       debug
#           is_tree_symbol_alias := true
#
#       method
#           dump_symbol_alias_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Symbol_Alias(object):
    __slots__ = (())


    if __debug__:
        is_tree_symbol_alias = True



#
#   USAGE:
#
#       v.dump_module_alias_tokens(f)       #   Dump the tokens representing the tree module alias to `f`.
#
#       v.dump_symbol_alias_tokens(f)       #   Dump the tokens representing the tree symbol alias to `f`.
#


#
#   USAGE (debug mode):
#
#       v.is_tree_module_alias              #   Test if `v` is a tree module alias.
#
#       v.is_tree_symbol_alias              #   Test if `v` is a tree symbol alias.
#
#       assert fact_is_tree_module_alias(v) #   Assert that `v` is a tree module alias.
#
#       assert fact_is_tree_symbol_alias(v) #   Assert that `v` is a tree symbol alias.
#


if 0:
    #
    #   fact_is_tree_module_alias(v) - Assert the fact that `v` is a tree module alias.
    #
    if __debug__:
        def fact_is_tree_module_alias(v):
            assert v.is_tree_module_alias

            return True


if 0:
    #
    #   fact_is_tree_symbol_alias(v) - Assert the fact that `v` is a tree symbol alias.
    #
    if __debug__:
        def fact_is_tree_symbol_alias(v):
            assert v.is_tree_module_alias

            return True
