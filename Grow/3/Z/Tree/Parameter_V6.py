#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_V6 - Implementation of tree parameters, Version 6.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 5 & Version 6.
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
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Capital.Native_String               import  fact_is__native_none__OR__full_native_string
    from    Z.Parser.Symbol                     import  fact_is_parser_symbol
    from    Z.Tree.Expression                   import  fact_is_tree_value_expression
    from    Z.Tree.Parameter                    import  fact_is_tree_parameter_0


#
#   Tree: Special Parameter - Base class of Tree_{Map,Tuple}_Parameter
#
class Tree_Special_Parameter(object):
    __slots__ = ((
        'symbol',                       #   Symbol
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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'symbol',                       #   Symbol
        'value',                        #   Tree_Expression
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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_parser_symbol(symbol)

    return Tree_Normal_Parameter(line_number, column, symbol)


#
#   Tree_Parameters_All - All the parameters of a function definition
#
#       `Tree_Parameters_All` is a 1-1 implementation of `Native_AbstractSyntaxTree_Parameters_All`
#       (i.e.: `_ast.Parameters`).
#
class Tree_Parameters_All(
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = ((
        'normal_parameters',            #   SomeNativeList of Tree_NormalParameter
        'tuple_parameter',              #   Tree_Parameter_0
        'map_parameter',                #   Tree_Parameter_0
        'defaults',                     #   SomeNativeList of Tree_Value_Expression
    ))


    def __init__(self, normal_parameters, tuple_parameter, map_parameter, defaults):
        self.normal_parameters = normal_parameters
        self.tuple_parameter   = tuple_parameter
        self.map_parameter     = map_parameter
        self.defaults          = defaults


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        if (
                len(self.normal_parameters) == 0
            and not self.tuple_parameter.has_tree_parameter
            and not self.map_parameter  .has_tree_parameter
        ):
            assert len(self.defaults) == 0

            f.line('<parameters-all>')
        else:
            with f.indent_2('<parameters-all', '>'):
                if self.normal_parameters:
                    for v in self.normal_parameters:
                        v.dump_parameter_tokens(f)
                        f.line(',')

                if self.tuple_parameter.has_tree_parameter:
                    self.tuple_parameter.dump_parameter_tokens(f)
                    f.line(',')

                if self.map_parameter.has_tree_parameter:
                    self.map_parameter.dump_parameter_tokens(f)
                    f.line(',')

                if self.defaults:
                    for v in self.defaults:
                        f.write('= ')
                        v.dump_value_expression_tokens(f)
                        f.line(',')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Parameters_All {} {} {} {}>',
                       self.normal_parameters, self.tuple_parameter, self.map_parameter, self.defaults)


@creator
def create_Tree_Parameters_All(normal_parameters, tuple_parameter, map_parameter, defaults):
    assert fact_is_some_native_list(normal_parameters)
    assert fact_is_tree_parameter_0(tuple_parameter)
    assert fact_is_tree_parameter_0(map_parameter)
    assert fact_is_some_native_list(defaults)

    return Tree_Parameters_All(normal_parameters, tuple_parameter, map_parameter, defaults)


#
#   Tree: Tuple Parameter
#
class Tree_Tuple_Parameter(
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
        is_tree_tuple_parameter = True


    def dump_parameter_tokens(self, f):
        f.arrange('<tuple-parameter *{}>', self.symbol)


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        f.line('<parameter-tuple tuple-parameter **{}>', self.symbol)


@creator
def create_Tree_Tuple_Parameter(symbol):
    assert fact_is_parser_symbol(symbol)

    return Tree_Tuple_Parameter(symbol)
