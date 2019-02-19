#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    _ast                            import  PyCF_ONLY_AST   as  python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE


#
#   Export the names in `_ast` as full names
#
from    _ast                            import  Expr    as  Python_AbstractSyntaxTree_Expression
from    _ast                            import  Import  as  Python_AbstractSyntaxTree_Import
from    _ast                            import  Module  as  Python_AbstractSyntaxTree_Module


python_compile = compile                #   python builtin `compile`


def python__compile__to__python_abstract_syntax_tree(source, filename):
    return python_compile(
               source   = source,
               filename = filename,
               mode     = 'exec',
               flags    = python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE,
           )
