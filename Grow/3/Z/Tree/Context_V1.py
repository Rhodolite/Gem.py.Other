#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  enumeration
from    Z.Tree.Context                  import  TRAIT_Tree_Context


#
#   Z.Tree.Context_V1 - Implementation of `Tree_Context`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Tree: Delete Context - A `delete` context in a Delete-Statement
#
class Tree_Delete_Context(
        TRAIT_Tree_Context,
):
    __slots__ = (())


    #
    #   Interface Tree_Context
    #
   #@replace
    is_tree_delete_context = True


    @staticmethod
    def dump_context_token(f):
        f.write('<context-delete>')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree-Context-Delete>'


@creator
def create_Tree_Delete_Context():
    return Tree_Delete_Context()


tree_delete_context = create_Tree_Delete_Context()


#
#   Tree: Load Context - A `load` context in an expression
#
#   Example:
#
#       In the statement:
#
#           f(a.b)
#
#       There will are three expressions that have a `load` context:
#
#           f       - A `Tree_Name` with a `load` context (to load the value of `f`, so as to call the function)
#
#           a       - A `Tree_Name` with a `load` context (to load the value of `a`, so as to access its `b` member)
#
#           a.b     - A `Tree_Attribute` with a `load` context (to load the value of `a.b`, as the first argument to
#                    `f`).
#
#       A call to `dump_token` on this Statement-Expression will output something like the following:
#
#           <Expression-Statement @7:0 <call @7:0 <Name f load> [<Attribute @7:2 <Name a load> b load>] []>>
#
class Tree_Load_Context(
        TRAIT_Tree_Context,
):
    __slots__ = (())


    #
    #   Interface Tree_Context
    #
   #@replace
    is_tree_load_context = True


    @staticmethod
    def dump_context_token(f):
        f.write('<context-load>')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree-Context-Load>'


@creator
def create_Tree_Load_Context():
    return Tree_Load_Context()


tree_load_context = create_Tree_Load_Context()


#
#   Tree: Parameter Context - A "parameter" context in `Tree_Parameters_All`.
#
class Tree_Parameter_Context(
        TRAIT_Tree_Context,
):
    __slots__ = (())


    #
    #   Interface Tree_Context
    #
   #@replace
    is_tree_parameter_context = True


    @staticmethod
    def dump_context_token(f):
        f.write('<context-parameter>')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree_Parameter_Context>'


@creator
def create_Tree_Parameter_Context():
    return Tree_Parameter_Context()



tree_parameter_context = create_Tree_Parameter_Context()


#
#   Tree: Store Context  - A `store` context in a statement.
#
class Tree_Store_Context(
        TRAIT_Tree_Context,
):
    __slots__ = (())


    #
    #   Interface Tree_Context
    #
   #@replace
    is_tree_store_context = True


    @staticmethod
    def dump_context_token(f):
        f.write('<context-store>')


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<Tree-Context-Store>'


@creator
def create_Tree_Store_Context():
    return Tree_Store_Context()



tree_store_context = create_Tree_Store_Context()
