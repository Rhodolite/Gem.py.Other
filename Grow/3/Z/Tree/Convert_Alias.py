#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias - Convert Python Abstract Syntax Tree Alias to `Tree_Alias`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Alias                        import  create_Tree_Alias_Clause
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list


#
#   convert_alias_clause(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Alias`.
#
#   NOTE:
#       Currently, can only handle non-aliased names (i.e.: does not have a `as` clause in the `from` or `import`
#       statement).
#
#       Does, not yet, handle aliased names (i.e.: has a `as` claues in the `from` or `import` statement).
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_alias_clause(self):
    return create_Tree_Alias_Clause(self.name, self.asname)


#
#   convert_full_list_of_alias_clauses
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Alias`.
#
def convert_full_list_of_alias_clauses(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_alias_clause(v)   for v in sequence]
