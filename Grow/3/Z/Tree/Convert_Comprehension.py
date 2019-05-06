#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Comprehension - Convert Python Abstract Syntax Tree Comprehension to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   See "Z/Tree/Comprehension.py" for an explanation of "Comprehensions".
#


from    Capital.Core                        import  trace
from    Z.Tree.Comprehension                import  create_Tree_Comprehension_Clause
from    Z.Tree.Convert_Target               import  convert_target
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Comprehension_Clause
from    Z.Tree.Produce_Convert_List         import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET


#
#   convert_comprehension(self)
#
#       Convert a `Native_AbstractSyntaxTree_Comprehension_Clause` (i.e.: `_ast.comprehension` to a
#       `Tree_Comprehension_Clause`.
#
assert Native_AbstractSyntaxTree_Comprehension_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Comprehension_Clause._fields     == (('target', 'iter', 'ifs'))


def convert_comprehension_clause(self):
    assert fact_is__ANY__native__abstract_syntax_tree__TARGET    (self.target)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(self.iter)
    assert fact_is_some_native_list                              (self.ifs)

    return create_Tree_Comprehension_Clause(
               convert_target                  (self.target),
               convert_expression              (self.iter),
               convert_some_list_of_expressions(self.ifs),
           )


#
#   convert_full_list_of_comprehensions(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Comprehension_Clause`
#       (i.e.: `list of _ast.Comprehension`) to a `FullNativeList of Tree_Comprehension_Clause`.
#
convert_full_list_of_comprehensions = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_comprehension_clause)
    )
