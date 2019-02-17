#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Argument_V1 - Implementation of `Tree_Argument`, Version 1.
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Z.Tree.Expression           import  fact_is_tree_expression


#
#   Tree_Keyword_Argument_V1 - A keyword argment in a function call.
#
class Tree_Keyword_Argument_V1(object):
    __slots__ = ((
        'name',                         #   FullNativeString
        'value',                        #   Tree_Expression
    ))


    def __init__(self, name, value):
        self.name  = name
        self.value = value


    def __repr__(self):
        return arrange('<Tree_Keyword_Argument_V1 {!r} = {!r}>', self.name, self.value)


    def dump_argument_tokens(self, f):
        f.arrange('<keyword_argument {} = ', self.name)
        self.value.dump_evaluate_tokens(f)
        f.greater_than_sign()


def create_Tree_Keyword_Argument_V1(name, value):
    assert fact_is_full_native_string(name)
    assert fact_is_tree_expression   (value)

    return Tree_Keyword_Argument_V1(name, value)
