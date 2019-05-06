#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V1 - Convert Python Abstract Syntax Tree Alias to `Tree_Alias_Clause`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Alias_V1                     import  create_Tree_Alias_Clause
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause
from    Z.Tree.Produce_Convert_List         import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list
    from    Capital.Fact                    import  fact_is_full_native_string
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


#
#   convert_alias_clause(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Alias_Clause`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_alias_clause(self):
    assert fact_is_full_native_string                  (self.name)
    assert fact_is__native_none__OR__full_native_string(self.asname)

    return create_Tree_Alias_Clause(self.name, self.asname)


#
#   convert_full_list_of_alias_clauses(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Alias_Clause`.
#
convert_full_list_of_alias_clauses = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_alias_clause)
    )


#
#   convert_full_list_of_module_aliases(sequence)
#
#       In Version 1, identical to `convert_full_list_of_alias_clauses`.
#
convert_full_list_of_module_aliases = convert_full_list_of_alias_clauses


#
#   convert_full_list_of_symbol_aliases(sequence)
#
#       In Version 1, identical to `convert_full_list_of_alias_clauses`.
#
convert_full_list_of_symbol_aliases = convert_full_list_of_alias_clauses
