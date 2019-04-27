#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Target - Interface to tree classes that represent targets.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#
#   Explanation:
#
#       A "target" is subset of "expression" that can appear to the left of an `=` or in a `delete` statement.
#
#       There are only a few targets that can appear to the left of an `=`  or in a `delete` statement:
#
#           Tree_Name                       #   See "Z.Tree.Name"
#           Tree_Attribute_Expression
#           Tree_List_Expression
#           Tree_Subscript_Expression
#           Tree_Tuple_Expression
#
#
#   Examples:
#
#       The following shows the different types of targets:
#
#           a        = 1                            #   `a`        is a `Tree_Name`
#           b.c      = 2                            #   `a.b`      is a `Tree_Attribute_Expression`
#           e[7]     = 3                            #   `a[7]`     is a `Tree_Subscript_Expression`
#           [e, g.h] = [4, 5]                       #   `[a, a.b]` is a `Tree_List_Expression`
#           (i, j.k) = [6, 7]                       #   `(a, a.b)` is a `Tree_Tuple_Expression`
#
#
#   NOTE:
#
#       A "list comprehension" *CANNOT* appear to the left of an `=`:
#
#           #
#           #   Syntax Error: cannot assign to a list comprehension
#           #
#           [x[i * i]   for i in range(5)]  = [ 8,  9, 10, 11, 12]
#
#           #
#           #   This is valid though
#           #
#           [x[0], x[1], x[4], x[3], x[16]] = [13, 14, 15, 16, 17]
#


#
#   interface Tree_Delete_Target - Interface to tree classes that represent "delete" targets.
#       method
#           dump_delete_target_tokens(f : Build_DumpToken)
#
#       debug
#           is_tree_delete_target := true
#
#
#   interface Tree_Store_Target - Interface to tree classes that represent "store" targets.
#       method
#           dump_store_target_tokens (f : Build_DumpToken)
#
#       debug
#           is_tree_store_target := true
#


#
#   USAGE:
#
#       v.is_tree_delete_target                 #   Test if `v` is a tree "delete" target.
#
#       v.is_tree_store_target                  #   Test if `v` is a tree "store" target.
#
#       v.dump_delete_target_tokens(f)          #   Dump the tokens representing the tree target (used in a delete
#                                               #   statement) to `f`
#
#       v.dump_store_target_tokens(f)           #   Dump the tokens representing the tree target (used in an assign
#                                               #   statement) to `f`.
#
#       assert fact_is_tree_delete_target(v)    #   Assert that `v` is a tree "delete" target.
#
#       assert fact_is_tree_store_target(v)     #   Assert that `v` is a tree "store" target.
#


#
#<order>
#
#   NOTE:
#       Because "Z/Tree/target_1.py" needs facts, then it imports this file.
#
#   HENCE:
#       The "fact" functions *MUST* appear *BEFORE* the import of "Z.Tree.Target_1"
#


#
#   fact_is__native_none__OR__tree_store_target(v)
#
#       Assert that `v` is either `None` or a tree "store" target.
#
if __debug__:
    def fact_is__native_none__OR__tree_store_target(v):
        if v is None:
            return True

        assert v.is_tree_store_target

        return True


#
#   fact_is_tree_store_target(v) - Assert that `v` is a tree "store" target.
#
if __debug__:
    def fact_is_tree_store_target(v):
        assert v.is_tree_store_target

        return True
#</order>


#
#   Import the version of tree targets we want to use.
#
from    Z.Tree.Global                   import  tree_globals


target_version = tree_globals.target_version


if target_version in ((1, 2, 3)):
    from    Z.Tree.Many_V1              import  create_Tree_List_Expression
    from    Z.Tree.Many_V1              import  create_Tree_Tuple_Expression
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Target.py: unknown tree target version: {!r}', target_version)
