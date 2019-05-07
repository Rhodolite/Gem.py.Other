#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameters_All_V1 - Implementation of `Tree_Parameters_All`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       `Tree_Parameters_All` is a 1-1 implementation of `Native_AbstractSyntaxTree_Parameters_All`
#       (i.e.: `_ast.Parameters`).
#


from    Capital.Core                    import  creator


if __debug__:
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string



#
#   Tree_Parameters_All - All the parameters of a function definition
#
class Tree_Parameters_All(object):
    #
    #   Implements Tree_Parameter
    #
    __slots__ = ((
        'normal_parameters',            #   SomeNativeList of Tree_NormalParameter
        'tuple_parameter',              #   None | Full_Native_String
        'map_parameter',                #   None | Full_Native_String
        'defaults',                     #   SomeNativeList of Tree_Expression
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
        is_tree_keyword_parameter = False
        is_tree_normal_parameter  = False
        is_tree_parameter         = True
        is_tree_parameters_all    = True


    def dump_parameter_tokens(self, f):
        normal_parameters = self.normal_parameters
        tuple_parameter   = self.tuple_parameter
        map_parameter     = self.map_parameter
        defaults          = self.defaults

        if (len(normal_parameters) == 0) and (tuple_parameter is map_parameter is None):
            assert len(defaults) == 0

            f.line('<parameters-all>')
        else:
            with f.indent_2('<parameters-all', '>'):
                if normal_parameters:
                    for v in normal_parameters:
                        v.dump_parameter_tokens(f)
                        f.line(',')

                if tuple_parameter:
                    f.line('*{},', tuple_parameter)

                if map_parameter:
                    f.line('**{},', map_parameter)

                if defaults:
                    for v in defaults:
                        f.write('= ')
                        v.dump_evaluate_tokens(f)
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
    assert fact_is__native_none__OR__full_native_string(map_parameter)
    assert fact_is_some_native_list                    (defaults)

    return Tree_Parameters_All(normal_parameters, tuple_parameter, map_parameter, defaults)
