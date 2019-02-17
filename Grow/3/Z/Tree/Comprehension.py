
#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Comprehension - Interface to tree classes that represent comprehension clauses.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Example:
#
#       In the following statement:
#
#           multiply = [x * y   for x in range(10)   if x   if x * y != 7   for y in range(7)]#
#
#       Has the following:
#
#           1)  What python calls a "list comprehension" (and we call a `Tree_List_Comprehension`).
#
#               The following is a "list comprehension":
#
#                   [x * y   for x in range(10)   if x   if x * y != 7   for y in range(7)]
#
#               (i.e.: a `list` created with one or more "comprehension" clauses).
#
#           2)  What python calls a "comprehension" (and we call a `Tree_Comprehension_Clause`):
#
#               The following is a "comprehension clause":
#
#                   for x in range(10)   if x   if x * y != 7
#
#               The following is another "comprehension clause":
#
#                   for y in range(7)
#
#   THUS:
#
#       A "list comprehension" consists of an "expression" and one or more "comprehension clauses"; and
#
#       A "comprehension clause" consists of a single `for`, and zero or more `if`s.
#


#
#   interface Tree_Comprehension_Clause - Interface to tree classes that represent comprehension clauses.
#       method
#           dump_comprehension_clause_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_comprehension_clause := true
#


#
#   USAGE:
#
#       v.is_tree_comprehension_clause                  #   Test if `v` is a tree comprehension clause.
#
#       v.dump_comprehension_clause_tokens(f)           #   Dump the tokens representing the tree comprehension clause
#                                                       #   to `f`.
#
#       assert fact_is_tree_comprehension_clause(v)     #   Assert that `v` is a tree comprehension clause.
#



#
#<order>
#
#   NOTE:
#       Because "Z/Tree/Comprehension_V1.py" needs facts, then it imports this file.
#
#   HENCE:
#       The "fact" functions *MUST* appear *BEFORE* the import of "Z.Tree.Comprehension_V1"
#


#
#   fact_is_tree_comprehension_clause(v) - Assert that `v` is a tree comprehension clause.
#
if __debug__:
    def fact_is_tree_comprehension_clause(v):
        assert v.is_tree_comprehension_clause

        return True
#</order>


#
#   Import the version of tree comprehension clauses we want to use.
#
from    Z.Tree.Global                   import  tree_globals


tree_version = tree_globals.tree_version


if tree_version in (('1', '2')):
    from    Z.Tree.Comprehension_V1     import  (
                create_Tree_Comprehension_Clause_V1     as  create_Tree_Comprehension_Clause,
        )
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Comprehension.py: unknown tree version: {}', tree_version)
