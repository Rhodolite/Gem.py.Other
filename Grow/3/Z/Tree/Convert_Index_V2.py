#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Index_V2 - Convert Python Abstract Syntax Tree Index Clause to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#



#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Ellipsis_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Extended_Slice_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Simple_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Slice_Index


#
#   convert_ellipses_index(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Ellipses_Index` (i.e.: `_ast.Ellipses`) to the
#       `tree_ellipses_index` singleton
#
assert Native_AbstractSyntaxTree_Ellipsis_Index._attributes == (())
assert Native_AbstractSyntaxTree_Ellipsis_Index._fields     == (())


def convert_ellipses_index(z, v):
    assert fact_is_convert_zone(z)

    return z.tree_ellipses_index


#
#   convert_extended_slice_index(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Extended_Slice_Index` (i.e.: `_ast.ExtSlice`) to a
#       `Tree_Extended_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Extended_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Extended_Slice_Index._fields     == (('dims',))


def convert_extended_slice_index(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_full_native_list(v.dims)

    return z.create_Tree_Extended_Slice_Index(
               convert_full_list_of_index_clauses(z, v.dims),
           )


#
#   convert_simple_index(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Simple_Index` (i.e.: `_ast.Index`) to a `Tree_Simple_Index`.
#
assert Native_AbstractSyntaxTree_Simple_Index._attributes == (())
assert Native_AbstractSyntaxTree_Simple_Index._fields     == (('value',))


def convert_simple_index(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return z.create_Tree_Simple_Index(
               z.convert_expression(z, v.value),
           )


#
#   convert_slice_index(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Slice_Index` (i.e.: `_ast.Slice`) to a `Tree_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Slice_Index._fields     == (('lower', 'upper', 'step'))


def convert_slice_index(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.lower)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.upper)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.step)

    return z.create_Tree_Slice_Index(
               z.convert_none_OR_expression(z, v.lower),
               z.convert_none_OR_expression(z, v.upper),
               z.convert_none_OR_expression(z, v.step),
           )


#
#   convert_index_clause(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Subscript_Clause`.
#
def convert_index_clause(z, v):
    assert fact_is_convert_zone(z)

    convert_index_clause__function = (
            z.map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function[type(v)]
        )

    return convert_index_clause__function(z, v)


#
#   convert_full_list_of_index_clauses(sequence)
#
#       Convert `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Index_clause`.
#
convert_full_list_of_index_clauses = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_index_clause)
    )
