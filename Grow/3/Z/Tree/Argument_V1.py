#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Argument_V1 - Implementation of class that implement `Tree_Argument`, Version 1.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Argument                 import  TRAIT_Tree_Argument


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Keyword Argument - A keyword argment in a function call.
#
class Tree_Keyword_Argument(
        TRAIT_Tree_Argument,
):
    __slots__ = ((
        'name',                         #   Full_Native_String
        'value',                        #   Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, name, value):
        self.name  = name
        self.value = value


    #
    #   Interface Tree_Argument
    #
    def dump_argument_tokens(self, f):
        f.arrange('<keyword_argument {} = ', self.name)
        self.value.dump_value_expression_tokens(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Keyword_Argument {!r} = {!r}>', self.name, self.value)


@creator
def create_Tree_Keyword_Argument(name, value):
    assert fact_is_full_native_string   (name)
    assert fact_is_tree_value_expression(value)

    return Tree_Keyword_Argument(name, value)
