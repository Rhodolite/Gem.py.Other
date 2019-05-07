#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Except - Interface to tree classes that represent except clauses.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   Explanation:
#
#       In the following statement:
#
#           try:
#               a()
#           except T as e:
#               b()
#           except:
#               c()
#
#       There are two "except clauses":
#
#           1)  except T as e: b()
#           2)  except       : c()
#


#
#   interface Tree_Except_Clause - Interface to tree classes that represent except clauses.
#       method
#           dump_except_clause_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_except_clause := true
#
class TRAIT_Tree_Except_Clause(object):
    __slots__ = (())


    if __debug__:
        is_tree_except_clause = True


#
#   USAGE:
#
#       v.is_tree_except_clause                 #   Test if `v` is a tree except clause.
#
#       v.dump_except_clause_tokens(f)          #   Dump the tokens representing the tree except clause to `f`.
#
#       assert fact_is_tree_except_clause(v)    #   Assert that `v` is a tree except clause.
#



#
#<order>
#
#   NOTE:
#       Because "Z.Tree.Except_1" needs facts, then it imports this file.
#
#   HENCE:
#       The "fact" functions *MUST* appear *BEFORE* the import of "Z.Tree.Except_1"
#


#
#   fact_is_tree_except_clause(v) - Assert that `v` is a tree except clause.
#
if __debug__:
    def fact_is_tree_except_clause(v):
        assert v.is_tree_except_clause

        return True
#</order>
