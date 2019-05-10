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
#           Does not have a `Tree_Map_Parameter`.
#
#       Version 4:
#
#           Has a `Tree_Map_Parameter`
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Name_V4                  import  Tree_Name_Branch
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter_0


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Parameter            import  fact_is_tree_parameter_0


#
#   Tree: Map Parameter
#
class Tree_Map_Parameter(
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
):
    __slots__ = ((
        'symbol',                       #   Symbol
    ))


    #
    #   Private
    #
    def __init__(self, symbol):
        self.symbol = symbol


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_map_parameter = True


    #
    #   Public
    #
    def dump_parameter_tokens(self, f):
        f.arrange('<map-parameter **{}>', self.symbol)


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} {}>', self.__class__.__name__, self.symbol)


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
        TRAIT_Tree_Parameter,
):
    __slots__ = ((
        'normal_parameters',            #   SomeNativeList of Tree_NormalParameter
        'tuple_parameter',              #   None | Full_Native_String
        'map_parameter',                #   None | Full_Native_String
        'defaults',                     #   SomeNativeList of Tree_Value_Expression
    ))


    def __init__(self, normal_parameters, tuple_parameter, map_parameter, defaults):
        self.normal_parameters = normal_parameters
        self.tuple_parameter   = tuple_parameter
        self.map_parameter     = map_parameter
        self.defaults          = defaults


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
       #@replace
        is_tree_parameters_all = True


    def dump_parameter_tokens(self, f):
        if (len(self.normal_parameters) == 0) and (self.tuple_parameter is self.map_parameter is None):
            assert len(self.defaults) == 0

            f.line('<parameters-all>')
        else:
            with f.indent_2('<parameters-all', '>'):
                if self.normal_parameters:
                    for v in self.normal_parameters:
                        v.dump_parameter_tokens(f)
                        f.line(',')

                if self.tuple_parameter:
                    f.line('*{},', self.tuple_parameter)

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
    assert fact_is_some_native_list                    (normal_parameters)
    assert fact_is__native_none__OR__full_native_string(tuple_parameter)
    assert fact_is_tree_parameter_0                    (map_parameter)
    assert fact_is_some_native_list                    (defaults)

    return Tree_Parameters_All(normal_parameters, tuple_parameter, map_parameter, defaults)
