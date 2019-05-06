#
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
#       debug
#           is_tree_statement := true
#
#       method
#           dump_statement_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Statement(object):
    __slots__ = (())

    if __debug__:
        is_tree_statement = True


#
#   USAGE:
#
#       v.dump_statement_tokens(f)          #   Dump the tokens representing the tree statement(s) to `f`.
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

#
#   Import the version of tree statements we want to use.
#
from    Z.Parser.Global                 import  parser_globals


statement_version = parser_globals.statement_version


if statement_version in ((1, 2)):
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Assert_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Assign_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Break_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Continue_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Delete_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Execute_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Expression_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_From_Import_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Global_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Import_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Modify_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Pass_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Print_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Raise_Statement
    from    Z.Tree.Simple_Statement_V1      import      create_Tree_Return_Statement
elif statement_version == 3:
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Assert_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Assign_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Break_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Continue_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Delete_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Execute_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Expression_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_From_Import_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Global_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Import_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Modify_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Pass_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Print_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Raise_Statement
    from    Z.Tree.Simple_Statement_V3      import      create_Tree_Return_Statement
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Statement.py: unknown tree statement version: {!r}', statement_version)
