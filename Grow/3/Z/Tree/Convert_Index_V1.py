#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Index_V1 - Convert Python Abstract Syntax Tree Index Clause to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Expression_V1        import  convert_value_expression
from    Z.Tree.Convert_Expression_V1        import  convert_value_expression_0
from    Z.Tree.Index_Clause_V1              import  create_Tree_Extended_Slice_Index
from    Z.Tree.Index_Clause_V1              import  create_Tree_Simple_Index
from    Z.Tree.Index_Clause_V1              import  create_Tree_Slice_Index
from    Z.Tree.Index_Clause_V1              import  tree_ellipses_index
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Ellipsis_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Extended_Slice_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Simple_Index
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Slice_Index


#
#   convert_ellipses_index(v)
#
#       Convert a `Native_AbstractSyntaxTree_Ellipses_Index` (i.e.: `_ast.Ellipses`) to the
#       `tree_ellipses_index` singleton
#
assert Native_AbstractSyntaxTree_Ellipsis_Index._attributes == (())
assert Native_AbstractSyntaxTree_Ellipsis_Index._fields     == (())


def convert_ellipses_index(v):
    return tree_ellipses_index


#
#   convert_extended_slice_index(v)
#
#       Convert a `Native_AbstractSyntaxTree_Extended_Slice_Index` (i.e.: `_ast.ExtSlice`) to a
#       `Tree_Extended_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Extended_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Extended_Slice_Index._fields     == (('dims',))


def convert_extended_slice_index(v):
    assert fact_is_full_native_list(v.dims)

    return create_Tree_Extended_Slice_Index(
               convert_full_list_of_index_clauses(v.dims),
           )


#
#   convert_simple_index(v)
#
#       Convert a `Native_AbstractSyntaxTree_Simple_Index` (i.e.: `_ast.Index`) to a `Tree_Simple_Index`.
#
assert Native_AbstractSyntaxTree_Simple_Index._attributes == (())
assert Native_AbstractSyntaxTree_Simple_Index._fields     == (('value',))


def convert_simple_index(v):
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.value)

    return create_Tree_Simple_Index(
               convert_value_expression(v.value),
           )


#
#   convert_slice_index(v)
#
#       Convert a `Native_AbstractSyntaxTree_Slice_Index` (i.e.: `_ast.Slice`) to a `Tree_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Slice_Index._fields     == (('lower', 'upper', 'step'))


def convert_slice_index(v):
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.lower)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.upper)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.step)

    return create_Tree_Slice_Index(
               convert_value_expression_0(v.lower),
               convert_value_expression_0(v.upper),
               convert_value_expression_0(v.step),
           )


#
#<convert_index_clause>
#
#   map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_index" function.
#
map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function = {
        Native_AbstractSyntaxTree_Ellipsis_Index       : convert_ellipses_index,
        Native_AbstractSyntaxTree_Extended_Slice_Index : convert_extended_slice_index,
        Native_AbstractSyntaxTree_Simple_Index         : convert_simple_index,
        Native_AbstractSyntaxTree_Slice_Index          : convert_slice_index,
    }


#
#   convert_index_clause(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Subscript_Clause`.
#
def convert_index_clause(v):
    convert_index_clause__function = (
            map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__function[type(v)]
        )

    return convert_index_clause__function(v)
#</convert_index_clause>


#
#   convert_full_list_of_index_clauses(sequence)
#
#       Convert `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Index_clause`.
#
convert_full_list_of_index_clauses = (
        produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_index_clause)
    )
