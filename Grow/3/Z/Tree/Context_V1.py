#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  enumeration


#
#   Z.Tree.Context_V1 - Implementation of `Tree_Context`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Tree_Context_Delete_V1 - A `delete` context in a Delete-Statement
#
class Tree_Context_Delete_V1(object):
    __slots__ = (())


    is_tree_context            = True
    is_tree_delete_context     = True
    is_tree_expression_context = False
    is_tree_load_context       = False
    is_tree_parameter_context  = False
    is_tree_store_context      = False


    @staticmethod
    def __repr__():
        return arrange('<Tree-Context-Delete>')


    @staticmethod
    def dump_context_token(f):
        f.write('<context-delete>')


@creator
def create_Tree_Context_Delete_V1():
    return Tree_Context_Delete_V1()


tree_context_delete_v1 = create_Tree_Context_Delete_V1()


#
#   Tree_Context_Load_V1 - A `load` context in an expression
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
class Tree_Context_Load_V1(object):
    __slots__ = (())


    is_tree_context            = True
    is_tree_delete_context     = False
    is_tree_expression_context = True
    is_tree_load_context       = True
    is_tree_parameter_context  = False
    is_tree_store_context      = False


    @staticmethod
    def __repr__():
        return arrange('<Tree-Context-Load>')


    @staticmethod
    def dump_context_token(f):
        f.write('<context-load>')


@creator
def create_Tree_Context_Load_V1():
    return Tree_Context_Load_V1()


tree_context_load_v1 = create_Tree_Context_Load_V1()


#
#   Tree_Context_Parameter_V1 - A "parameter" context in `Tree_Parameters_All`.
#
class Tree_Context_Parameter_V1(object):
    __slots__ = (())


    is_tree_context            = True
    is_tree_delete_context     = False
    is_tree_expression_context = False
    is_tree_load_context       = False
    is_tree_parameter_context  = True
    is_tree_store_context      = False


    @staticmethod
    def __repr__():
        return arrange('<Tree_Context_Parameter_V1>')


    @staticmethod
    def dump_context_token(f):
        f.write('<context-parameter>')


@creator
def create_Tree_Context_Parameter_V1():
    return Tree_Context_Parameter_V1()



tree_context_parameter_v1 = create_Tree_Context_Parameter_V1()


#
#   Tree_Context_Store_V1 - A `store` context in a statement.
#
class Tree_Context_Store_V1(object):
    __slots__ = (())


    is_tree_context            = True
    is_tree_delete_context     = False
    is_tree_expression_context = True
    is_tree_load_context       = False
    is_tree_parameter_context  = False
    is_tree_store_context      = True


    @staticmethod
    def __repr__():
        return arrange('<Tree-Context-Store>')


    @staticmethod
    def dump_context_token(f):
        f.write('<context-store>')


@creator
def create_Tree_Context_Store_V1():
    return Tree_Context_Store_V1()



tree_context_store_v1 = create_Tree_Context_Store_V1()
