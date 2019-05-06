#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Index - Convert Python Abstract Syntax Tree Index Clause to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  trace
from    Z.Tree.Convert_Expression           import  convert_expression
from    Z.Tree.Convert_Expression           import  convert_none_OR_expression
from    Z.Tree.Index                        import  create_Tree_Extended_Slice_Index
from    Z.Tree.Index                        import  create_Tree_Simple_Index
from    Z.Tree.Index                        import  create_Tree_Slice_Index
from    Z.Tree.Index                        import  tree_ellipses_index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Ellipsis_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Extended_Slice_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Simple_Index
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Slice_Index
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION


#
#   convert_ellipses_index(self)
#
#       Convert a `Native_AbstractSyntaxTree_Ellipses_Index` (i.e.: `_ast.Ellipses`) to the
#       `tree_ellipses_index` singleton
#
assert Native_AbstractSyntaxTree_Ellipsis_Index._attributes == (())
assert Native_AbstractSyntaxTree_Ellipsis_Index._fields     == (())


def convert_ellipses_index(self):
    return tree_ellipses_index


#
#   convert_extended_slice_index(self)
#
#       Convert a `Native_AbstractSyntaxTree_Extended_Slice_Index` (i.e.: `_ast.ExtSlice`) to a
#       `Tree_Extended_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Extended_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Extended_Slice_Index._fields     == (('dims',))


def convert_extended_slice_index(self):
    assert fact_is_full_native_list(self.dims)

    return create_Tree_Extended_Slice_Index(
               convert_full_list_of_index_clauses(self.dims),
           )


#
#   convert_simple_index(self)
#
#       Convert a `Native_AbstractSyntaxTree_Simple_Index` (i.e.: `_ast.Index`) to a `Tree_Simple_Index`.
#
assert Native_AbstractSyntaxTree_Simple_Index._attributes == (())
assert Native_AbstractSyntaxTree_Simple_Index._fields     == (('value',))


def convert_simple_index(self):
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.value)

    return create_Tree_Simple_Index(
               convert_expression(self.value),
           )


#
#   convert_slice_index(self)
#
#       Convert a `Native_AbstractSyntaxTree_Slice_Index` (i.e.: `_ast.Slice`) to a `Tree_Slice_Index`.
#
assert Native_AbstractSyntaxTree_Slice_Index._attributes == (())
assert Native_AbstractSyntaxTree_Slice_Index._fields     == (('lower', 'upper', 'step'))


def convert_slice_index(self):
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.lower)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.upper)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(self.step)

    return create_Tree_Slice_Index(
               convert_none_OR_expression(self.lower),
               convert_none_OR_expression(self.upper),
               convert_none_OR_expression(self.step),
           )


#
#<convert_index_clause>
#
#   map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__pseudo_method
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_index" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__pseudo_method = {
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
    convert_index_clause__pseudo_method = (
            map__Native_AbstractSyntaxTree_INDEX_CLAUSE__to__convert_index_clause__pseudo_method[type(v)]
        )

    return convert_index_clause__pseudo_method(v)
#</convert_target>


#
#   convert_full_list_of_index_clauses(sequence)
#
#       Convert `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Index_clause`.
#
convert_full_list_of_index_clauses = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_index_clause)
    )
