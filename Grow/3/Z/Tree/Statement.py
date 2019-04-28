#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Statement - Interface to tree classes that represent statement.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Statement
#       documentation
#           Interface to tree classes that represent statements.
#
#       method
#           dump_suite_tokens(f : Build_DumpToken)
#
#       attribute
#           suite_estimate : integer { 0, 1, 7 }
#               documentation
#                   A suite estimate of 0 means 0 statements.
#                   A suite estimate of 1 means 1 statement.
#                   A suite estimate of 7 means 2 or more statements.
#
#       debug
#           is_tree_statement := true
#


#
#   USAGE:
#
#       v.dump_suite_tokens(f)              #   Dump the tokens representing the tree statement(s) to `f`.
#
#       v.suite_estimate                    #   Estimate the number of statements in this suite.
#                                           #   (See documentation above for the estimate values).
#


#
#   USAGE (debug mode):
#
#       v.is_tree_statement                 #   Test if `v` is a tree statement.
#
#       assert fact_is_tree_statement(v)    #   Assert that `v` is a tree statement.
#



#
#   fact_is_tree_statement(v) - Assert that `v` is a `Tree_Statement`.
#
if __debug__:
    def fact_is_tree_statement(v):
        assert v.is_tree_statement

        return True
#</facts>


#
#   Import the version of tree statements we want to use.
#
from    Z.Tree.Global                   import  tree_globals


statement_version = tree_globals.statement_version


if statement_version in ((1, 2)):
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Assert_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Assign_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Break_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Continue_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Delete_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Execute_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Expression_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_From_Import_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Global_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Import_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Modify_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Pass_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Print_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Raise_Statement
    from    Z.Tree.Simple_Statement_V1  import      create_Tree_Return_Statement

    from    Z.Tree.Statement_V1         import      create_Tree_Class_Definition
    from    Z.Tree.Statement_V1         import      create_Tree_For_Statement
    from    Z.Tree.Statement_V1         import      create_Tree_Function_Definition
    from    Z.Tree.Statement_V1         import      create_Tree_If_Statement
    from    Z.Tree.Statement_V1         import      create_Tree_Try_Except_Statement
    from    Z.Tree.Statement_V1         import      create_Tree_Try_Finally_Statement
    from    Z.Tree.Statement_V1         import      create_Tree_While_Statement
    from    Z.Tree.Statement_V1         import      create_Tree_With_Statement
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Statement.py: unknown tree statement version: {!r}', statement_version)
