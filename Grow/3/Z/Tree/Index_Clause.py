#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Index_Clause - Interface to tree classes that represent index clauses.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Explanation:
#
#       In the statement:
#
#           x = a[1] + a[:2] + a[3, 4]
#
#       The following "index clauses" appear:
#
#           1       - A `Tree_Simple_Index`
#           :2      - A `Tree_Slice_Index`
#           3, 4    - A `Tree_Extended_Slice_Index`
#


#
#   interface Tree_Index_Clause
#       documentation
#           Interface to tree classes that represent index clauses.
#
#       method
#           dump_index_clause_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_index_clause := true
#
class TRAIT_Tree_Index_Clause(object):
    __slots__ = (())


    if __debug__:
        is_tree_index_clause = True


#
#   USAGE:
#
#       v.is_tree_index_clause              #   Test if `v` is a tree index clause.
#
#       v.dump_index_clause_tokens(f)       #   Dump the tokens representing the tree index clause to `f`.
#
#       assert fact_is_tree_index_clause(v) #   Assert that `v` is a tree index clause.
#


#
#   fact_is_tree_index_clause(v) - Assert that `v` is a tree index clause.
#
if __debug__:
    def fact_is_tree_index_clause(v):
        assert v.is_tree_index_clause

        return True
