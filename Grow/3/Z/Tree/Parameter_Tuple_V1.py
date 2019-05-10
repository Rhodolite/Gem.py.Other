#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_Tuple_V1 - Implementation of tree parameters, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  creator
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple_0


if __debug__:
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string



#
#   Tree_All_Parameters - All the parameters of a function definition
#
#       `Tree_All_Parameters` is a 1-1 implementation of `Native_AbstractSyntaxTree_All_Parameters`
#       (i.e.: `_ast.Parameters`).
#
class Tree_All_Parameters(
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = ((
        'normal_parameters',            #   Some_Native_List of Tree_NormalParameter
        'star_parameter',               #   None | Full_Native_String
        'map_parameter',                #   None | Full_Native_String
        'defaults',                     #   Some_Native_List of Tree_Value_Expression
    ))


    def __init__(self, normal_parameters, star_parameter, map_parameter, defaults):
        self.normal_parameters = normal_parameters
        self.star_parameter    = star_parameter
        self.map_parameter     = map_parameter
        self.defaults          = defaults


    #
    #   Interface Tree_Parameter_Tuple
    #
    def dump_parameter_tuple_tokens(self, f):
        if (len(self.normal_parameters) == 0) and (self.star_parameter is self.map_parameter is None):
            assert len(self.defaults) == 0

            f.line('<parameters-all>')
        else:
            with f.indent_2('<parameters-all', '>'):
                if self.normal_parameters:
                    for v in self.normal_parameters:
                        v.dump_parameter_tokens(f)
                        f.line(',')

                if self.star_parameter:
                    f.line('*{},', self.star_parameter)

                if self.map_parameter:
                    f.line('**{},', self.map_parameter)

                if self.defaults:
                    for v in self.defaults:
                        f.write('= ')
                        v.dump_value_expression_tokens(f)
                        f.line(',')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_All_Parameters {} {} {} {}>',
                       self.normal_parameters, self.star_parameter, self.map_parameter, self.defaults)


@creator
def create_Tree_All_Parameters(normal_parameters, star_parameter, map_parameter, defaults):
    assert fact_is_some_native_list                    (normal_parameters)
    assert fact_is__native_none__OR__full_native_string(star_parameter)
    assert fact_is__native_none__OR__full_native_string(map_parameter)
    assert fact_is_some_native_list                    (defaults)

    return Tree_All_Parameters(normal_parameters, star_parameter, map_parameter, defaults)
