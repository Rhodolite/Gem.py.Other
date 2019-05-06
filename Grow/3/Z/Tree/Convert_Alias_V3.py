#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V3 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 3.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           1)  `z.create_Tree_Module_Alias`        maps to `Z.Tree.Alias_1.create_Tree_Alias_Clause`.
#
#           2)  `z.create_Tree_Symbol_Alias` *ALSO* maps to `Z.Tree.Alias_1.create_Tree_Alias_Clause`.
#
#           Hence for both module & symbol aliases it creates a `Tree_Alias_Clause`
#
#       Version 3:
#
#           1)  `z.create_Tree_Module_Alias`        maps to `Z.Tree.Alias_3.create_Tree_Module_Alias`.
#
#           2)  `z.create_Tree_Symbol_Alias` *ALSO* maps to `Z.Tree.Alias_3.create_Tree_Symbol_Alias`.
#
#           Hence for module alias it creates a `Tree_Module_Alias`,
#           while for symbol alias it creates a `Tree_Symbol_Alias`.
#
#           Uses all the code from version 2, since the only difference is in the `z` parameter.
#


from    Z.Tree.Convert_Alias_V2             import  convert_full_list_of_module_aliases
from    Z.Tree.Convert_Alias_V2             import  convert_full_list_of_symbol_aliases
