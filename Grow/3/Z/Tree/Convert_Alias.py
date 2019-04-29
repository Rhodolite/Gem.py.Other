#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias - Convert Python Abstract Syntax Tree Alias to `Tree_Alias`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Import the version of tree aliases we want to use.
#
from    Z.Tree.Global                   import  tree_globals


alias_version = tree_globals.alias_version


if alias_version == 1:
    from    Z.Tree.Convert_Alias_V1     import  convert_full_list_of_module_aliases
    from    Z.Tree.Convert_Alias_V1     import  convert_full_list_of_symbol_aliases
elif alias_version == 2:
    from    Z.Tree.Convert_Alias_V2     import  convert_full_list_of_module_aliases
    from    Z.Tree.Convert_Alias_V1     import  convert_full_list_of_symbol_aliases
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Alias.py: unknown tree alias version: {!r}', alias_version)
