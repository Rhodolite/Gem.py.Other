#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_V5 - Implementation of tree parameters, Version 5.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 4 & Version 5.
#
#       Version 4.
#
#           Does not have a `Tree_{Map,Star}_Parameter`.
#
#       Version 4:
#
#           Has a `Tree_{Map,Star}_Parameter`
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Name_V4                  import  Tree_Name_Branch
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter_0


if __debug__:
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol


#
#   Tree: Special Parameter - Base class of Tree_{Map,Tuple}_Parameter
#
class Tree_Special_Parameter(object):
    __slots__ = ((
        'symbol',                       #   Parser_Symbol
    ))


    #
    #   Private
    #
    def __init__(self, symbol):
        self.symbol = symbol


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} {}>', self.__class__.__name__, self.symbol)


#
#   Tree: Map Parameter
#
class Tree_Map_Parameter(
        Tree_Special_Parameter,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_map_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<map-parameter **{}>', self.symbol)


@creator
def create_Tree_Map_Parameter(symbol):
    assert fact_is_parser_symbol(symbol)

    return Tree_Map_Parameter(symbol)


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


#
#   Tree: Star Parameter
#
class Tree_Star_Parameter(
        Tree_Special_Parameter,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_star_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<star-parameter *{}>', self.symbol)


@creator
def create_Tree_Star_Parameter(symbol):
    assert fact_is_parser_symbol(symbol)

    return Tree_Star_Parameter(symbol)
