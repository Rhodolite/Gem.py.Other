#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    _ast                            import  PyCF_ONLY_AST   as  python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE


#
#   Export the names in `_ast` as full names
#
#   NOTE:
#       No idea why it's `_ast.alias` (instead of `.Alias` with a capital `A`).
#
from    _ast                            import  alias       as  PythonTree_Alias
from    _ast                            import  Attribute   as  PythonTree_Attribute
from    _ast                            import  Call        as  PythonTree_Call
from    _ast                            import  Expr        as  PythonTree_Expression
from    _ast                            import  Import      as  PythonTree_Import
from    _ast                            import  Module      as  PythonTree_Module
from    _ast                            import  Load        as  PythonTree_Load
from    _ast                            import  Name        as  PythonTree_Name
from    _ast                            import  Str         as  PythonTree_String


#
#   fact_is_python_abstract_syntax_tree_alias(v)
#
#       Assert the fact that `v` is a `PythonTree_Alias` instance.
#
if __debug__:
    def fact_is_python_abstract_syntax_tree_alias(v):
        assert type(v) is PythonTree_Alias

        return v


#
#   fact_is_python_abstract_syntax_tree_load(v)
#
#       Assert the fact that `v` is a `PythonTree_Load` instance.
#
if __debug__:
    def fact_is_python_abstract_syntax_tree_load(v):
        assert type(v) is PythonTree_Load

        return v


#
#   fact_is_python_abstract_syntax_tree_module(v)
#
#       Assert the fact that `v` is a `PythonTree_Module` instance.
#
if __debug__:
    def fact_is_python_abstract_syntax_tree_module(v):
        assert type(v) is PythonTree_Module

        return v


def python__compile__to__python_abstract_syntax_tree(source, filename):
    return compile(                                 #   Call the python built-in `compile` function.
               source   = source,
               filename = filename,
               mode     = 'exec',
               flags    = python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE,
           )
