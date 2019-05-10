#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Comprehension_V1 - Convert Python Abstract Syntax Tree Comprehension to Tree classes, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   See "Z/Tree/Comprehension.py" for an explanation of "Comprehensions".
#


from    Z.Tree.Comprehension_V1             import  create_Tree_Comprehension_Clause
from    Z.Tree.Convert_Expression_V1        import  convert_expression
from    Z.Tree.Convert_Expression_V1        import  convert_some_list_of_expressions
from    Z.Tree.Convert_Target_V1            import  convert_target
from    Z.Tree.Produce_Convert_List_V1      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Comprehension_Clause


#
#   convert_comprehension(v)
#
#       Convert a `Native_AbstractSyntaxTree_Comprehension_Clause` (i.e.: `_ast.comprehension` to a
#       `Tree_Comprehension_Clause`.
#
assert Native_AbstractSyntaxTree_Comprehension_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Comprehension_Clause._fields     == (('target', 'iter', 'ifs'))


def convert_comprehension_clause(v):
    assert fact_is__ANY__native__abstract_syntax_tree__TARGET          (v.target)
    assert fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v.iter)
    assert fact_is_some_native_list                                    (v.ifs)

    return create_Tree_Comprehension_Clause(
               convert_target                  (v.target),
               convert_expression              (v.iter),
               convert_some_list_of_expressions(v.ifs),
           )


#
#   convert_full_list_of_comprehensions(sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_Comprehension_Clause`
#       (i.e.: `list of _ast.Comprehension`) to a `Full_Native_List of Tree_Comprehension_Clause`.
#
convert_full_list_of_comprehensions = (
        produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_comprehension_clause)
    )
