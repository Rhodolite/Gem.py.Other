#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Target - Convert Python Abstract Syntax Tree Targets to Tree classes.
#
#   See "Z/Tree/Target.py" for an explantion of what a "target" is.
#


from    Capital.Core                        import  FATAL
from    Z.Tree.Convert_Index                import  convert_index_clause
from    Z.Tree.Convert_Name                 import  convert_name_expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_List_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Map_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Name
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Subscript_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Tuple_Expression
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Unary_Expression


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list


#
#   Import the version of tree targets we want to use.
#
from    Z.Tree.Global                   import  tree_globals


target_version = tree_globals.target_version


if target_version == 1:
    from    Z.Tree.Convert_Attribute_V1     import  convert_attribute_expression
    from    Z.Tree.Convert_Many_V1          import  convert_list_expression
    from    Z.Tree.Convert_Many_V1          import  convert_tuple_expression
    from    Z.Tree.Convert_Subscript_V1     import  convert_subscript_expression
elif target_version == 2:
    from    Z.Tree.Convert_Attribute_V2     import  convert_attribute_expression
    from    Z.Tree.Convert_Many_V1          import  convert_list_expression             #   "_V1" on purpose
    from    Z.Tree.Convert_Many_V1          import  convert_tuple_expression            #   "_V1" on purpose
    from    Z.Tree.Convert_Subscript_V1     import  convert_subscript_expression        #   "_V1" on purpose
elif target_version == 3:
    from    Z.Tree.Convert_Attribute_V3     import  convert_attribute_expression
    from    Z.Tree.Convert_Many_V3          import  convert_list_expression
    from    Z.Tree.Convert_Many_V3          import  convert_tuple_expression
    from    Z.Tree.Convert_Subscript_V3     import  convert_subscript_expression
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Convert_Target.py: unknown tree target version: {!r}', target_version)



#
#   convert_none_OR_target(v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Target`.
#
def convert_none_OR_target(v):
    if v is None:
        return None

    return convert_target(v)


#
#<convert_target>
#
#   map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method
#           : Map { Native_AbstractSyntaxTree_* : Function }
#
#       This maps a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a "convert_target" psuedo method
#       (actually to a function).
#
map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method = {
        Native_AbstractSyntaxTree_Attribute_Expression : convert_attribute_expression,
        Native_AbstractSyntaxTree_List_Expression      : convert_list_expression,
        Native_AbstractSyntaxTree_Name                 : convert_name_expression,
        Native_AbstractSyntaxTree_Subscript_Expression : convert_subscript_expression,
        Native_AbstractSyntaxTree_Tuple_Expression     : convert_tuple_expression,
    }


#
#   convert_target(v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Expression`.
#
#       The expression must be a "target" expression.
#
def convert_target(v):
    convert_target__pseudo_method = (
            map__Native_AbstractSyntaxTree_TARGET__to__convert_target__pseudo_method[type(v)]
        )

    return convert_target__pseudo_method(v)
#</convert_target>


#
#   convert_full_list_of_targets(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `FullNativeList of Tree_Expression`.
#
#       Each of the expressions must be a target expresion.
#
def convert_full_list_of_targets(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_target(v)   for v in sequence]
