#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_V4 - Implementation of tree parameters, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 1..4.
#
#       Version 1.
#
#           `Tree_Normal_Parameter` does not exist.
#
#           Instead, for a normal parameter `Capital.Tree.Name_V1.Tree_Name` was used in previous versions with a
#           `.context` member with a value of `tree_parameter_context`
#
#           (i.e.: a "normal parameter" was implemented in as part of "tree names" in earlier versions)
#
#       Versions 2..3:
#
#           Do not exist.
#
#       Version 4:
#
#           `Tree_Normal_Parameter` is implemented in this file.
#
#           This is instead of using `Tree_Name` a `.context` member with a value of `tree_parameter_context` as was
#           done in previous versions.
#
#           (i.e.: a "normal parameter" is now implemented in this file instead of as part of "tree names").
#
#   SEE ALSO
#
#       See "Z.Tree.Name_V4.py" for more details on how `Tree_Name` was split into four classes.
#


from    Capital.Core                    import  creator
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple_0
from    Z.Tree.Name_V4                  import  Tree_Name_Branch


if __debug__:
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string
    from    Z.Parser.Symbol             import  fact_is_parser_symbol


#
#   Tree: Normal Parameter
#
class Tree_Normal_Parameter(
        Tree_Name_Branch,
        TRAIT_Tree_Parameter,
):
    __slots__ = (())


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_normal_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<normal-parameter @{}:{} {}>', self.line_number, self.column, self.symbol)


@creator
def create_Tree_Normal_Parameter(line_number, column, symbol):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Normal_Parameter(line_number, column, symbol)
