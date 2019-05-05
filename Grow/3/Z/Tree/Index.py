#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Index - Interface to tree classes that represent index clauses.
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
#   interface Tree_Index_Clause - Interface to tree classes that represent index clauses.
#       method
#           dump_index_clause_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_index_clause := true
#


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
#<order>
#
#   NOTE:
#       Because "Z/Tree/Index_1.py" needs facts, then it imports this file.
#
#   HENCE:
#       The "fact" functions *MUST* appear *BEFORE* the import of "Z.Tree/Index_1.py"
#


#
#   fact_is_tree_index_clause(v) - Assert that `v` is a tree index clause.
#
if __debug__:
    def fact_is_tree_index_clause(v):
        assert v.is_tree_index_clause

        return True
#</order>


#
#   Import the version of tree index clauses we want to use.
#
from    Z.Parser.Global                 import  parser_globals


version = parser_globals.index_version


if version == '1':
    from    Z.Tree.Index_V1         import  (
                create_Tree_Extended_Slice_Index_V1     as  create_Tree_Extended_Slice_Index,
                create_Tree_Simple_Index_V1             as  create_Tree_Simple_Index,
                create_Tree_Slice_Index_V1              as  create_Tree_Slice_Index,
                tree_ellipses_index_v1                  as  tree_ellipses_index,
        )
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Index.py: unknown tree index version: {!r}', version)
