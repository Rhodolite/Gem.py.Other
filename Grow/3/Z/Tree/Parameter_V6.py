#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_V6 - Implementation of tree parameters, Version 6.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 5 & Version 6.
#
#       Version 5.
#
#           Parameters do not implement `Tree_Parameter_Tuple_0`.
#
#       Version 4:
#
#           Parameters implement `Tree_Parameter_Tuple_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Name_V4                  import  Tree_Name_Branch
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter_0
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple_0


if __debug__:
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Expression           import  fact_is_tree_value_expression
    from    Z.Tree.Parameter            import  fact_is_tree_parameter_0


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
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
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


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        f.line('<parameter-tuple map-parameter **{}>', self.symbol)


@creator
def create_Tree_Map_Parameter(symbol):
    assert fact_is_parser_symbol(symbol)

    return Tree_Map_Parameter(symbol)


#
#   Tree: Keyword Parameter
#
class Tree_Keyword_Parameter(
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbol',                       #   Parser_Symbol
        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Protected
    #
    def __init__(self, line_number, column, symbol, value):
        self.line_number = line_number
        self.column      = column

        self.symbol = symbol
        self.value  = value


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_keyword_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<keyword-parameter @{}:{} ', self.line_number, self.column)
        self.symbol.dump_symbol_token(f)
        f.write(' = ')
        self.value.dump_value_expression_tokens(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        f.arrange('<parameter-tuple keyword-parameter @{}:{} ', self.line_number, self.column)
        self.symbol.dump_symbol_token(f)
        f.write(' = ')
        self.value.dump_value_expression_tokens(f)
        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {} {}>',
                      self.__class__.__name__, self.line_number, self.column, self.symbol, self.value)


@creator
def create_Tree_Keyword_Parameter(line_number, column, symbol, value):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol        (symbol)
    assert fact_is_tree_value_expression(value)

    return Tree_Keyword_Parameter(line_number, column, symbol, value)


#
#   Tree: Normal Parameter
#
class Tree_Normal_Parameter(
        Tree_Name_Branch,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = (())


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_normal_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<normal-parameter @{}:{} ', self.line_number, self.column)
        self.symbol.dump_symbol_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        f.arrange('<parameter-tuple normal-parameter @{}:{} ', self.line_number, self.column)
        self.symbol.dump_symbol_token(f)
        f.line('>')


@creator
def create_Tree_Normal_Parameter(line_number, column, symbol):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Normal_Parameter(line_number, column, symbol)


#
#   Tree: Tuple Parameter
#
class Tree_Star_Parameter(
        Tree_Special_Parameter,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
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


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        f.line('<parameter-tuple star-parameter **{}>', self.symbol)


@creator
def create_Tree_Star_Parameter(symbol):
    assert fact_is_parser_symbol(symbol)

    return Tree_Star_Parameter(symbol)
