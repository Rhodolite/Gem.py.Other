#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Suite - Interface to tree classes that represent a suite.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       A "Suite" is a one or more tree statements (this is the definition used by python).
#


from    Capital.Core                    import  virtual


#
#   interface Tree_Suite
#       documentation
#           Interface to tree classes that represent a suite.
#
#           A "Suite" is a one or more tree statements (this is the definition used by python).
#
#       debug
#           is_tree_suite := true
#
#       attribute
#           suite_estimate : integer { 1, 7 }
#               documentation
#                   A suite estimate of 0 means 0 statements.
#                   A suite estimate of 1 means 1 statement.
#                   A suite estimate of 7 means 2 or more statements.
#
#       method
#           dump_suite_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Suite(object):
    __slots__ = (())


    if __debug__:
        is_tree_suite = True


   #@virtual
    suite_estimate = 1


    @virtual
    def dump_suite_tokens(self, f):
        self.dump_statement_tokens(f)


#
#   interface Tree_Suite_0
#       documentation
#           Interface to tree classes that represent a suite OR none.
#
#           A "Suite" is a one or more tree statements (this is the definition used by python).
#
#       attribute
#           suite_estimate : integer { 0, 1, 7 }
#               documentation
#                   A suite estimate of 0 means 0 statements.
#                   A suite estimate of 1 means 1 statement.
#                   A suite estimate of 7 means 2 or more statements.
#
#       if suite_estimate
#           implements Tree_Suite
#
#       debug
#           is_tree_suite_0 := true
#
class TRAIT_Tree_Suite_0(object):
    __slots__ = (())


    if __debug__:
        is_tree_suite_0 = True


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
#       v.is_tree_suite                     #   Test if `v` is a tree suite.
#
#       v.is_tree_suite_0                   #   Test if `v` is a `Tree_Suite_0`.
#
#       assert fact_is_tree_suite(v)        #   Assert that `v` is a tree suite.
#
#       assert fact_is_tree_suite_0(v)      #   Assert that `v` is a `Tree_Suite_0`.
#



#
#   fact_is_tree_suite(v) - Assert that `v` is a tree suite.
#
if __debug__:
    def fact_is_tree_suite(v):
        assert v.is_tree_suite

        return True


#
#   fact_is_tree_suite_0(v) - Assert that `v` is a `Tree_Suite_0`.
#
if __debug__:
    def fact_is_tree_suite_0(v):
        assert v.is_tree_suite_0

        return True


#
#   Import the version of tree suite we want to use.
#
from    Z.Parser.Global                 import  parser_globals


statement_version = parser_globals.statement_version


if statement_version in ((1, 2, 3)):
    #
    #   A "Suite" does not exist in statement versions 1 or 2.
    #
    pass
elif statement_version == 4:
    from    Z.Tree.Suite_V2             import  create_Tree_Suite
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Suite.py: unknown tree statement version: {}', statement_version)
