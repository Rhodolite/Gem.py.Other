#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V2 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           1)  `convert_alias_clause` is used for both module aliases & symbol aliases (so as to do a 1-1 emulation
#                of `_ast`).
#
#           2)  Both `convert_full_list_of_module_aliases` and `convert_full_list_of_symbol_aliases` are mapped to
#               `convert_full_list_of_alias_clauses`.
#
#       Version 2:
#
#           1)  `convert_alias_clause` removed.
#
#           2)  `convert_module_alias` used for module aliases.
#
#           3)  `convert_symbol_alias` used for symbol aliases.
#
#           4)  `convert_full_list_of_module_aliases` becomes it's own routine (used for full list of module aliases)
#
#           5)  `convert_full_list_of_symbol_aliases` becomes it's own routine (used for full list of symbol aliases).
#


from    Z.Tree.Alias_V2                     import  create_Tree_Module_Alias
from    Z.Tree.Alias_V2                     import  create_Tree_Symbol_Alias
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list
    from    Capital.Fact                    import  fact_is_full_native_string
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


#
#   convert_module_alias(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Module_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_module_alias(self):
    assert fact_is_full_native_string                  (self.name)
    assert fact_is__native_none__OR__full_native_string(self.asname)

    return create_Tree_Module_Alias(self.name, self.asname)


#
#   convert_symbol_alias(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Symbol_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_symbol_alias(self):
    assert fact_is_full_native_string                  (self.name)
    assert fact_is__native_none__OR__full_native_string(self.asname)

    return create_Tree_Symbol_Alias(self.name, self.asname)


#
#   convert_full_list_of_module_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Module_Alias`.
#
def convert_full_list_of_module_aliases(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_module_alias(v)   for v in sequence]


#
#   convert_full_list_of_symbol_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Symbol_Alias`.
#
def convert_full_list_of_symbol_aliases(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_symbol_alias(v)   for v in sequence]
