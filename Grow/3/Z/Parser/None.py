#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.None - Implementation of the singleton `parser_none`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       `parser_none` is used to represent `None` in the Z parser.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Z.Parser.Symbol                 import  TRAIT_Parser_Symbol_0
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter_0
from    Z.Tree.Parameter_Tuple          import  TRAIT_Tree_Parameter_Tuple_0
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


#
#   Parser: None
#
class Parser_None(
        TRAIT_Parser_Symbol_0,
        TRAIT_Tree_Parameter_0,
        TRAIT_Tree_Parameter_Tuple_0,
        TRAIT_Tree_Suite_0,
):
    __slots__ = (())


    #
    #   Interface Parser_Symbol_0
    #
   #@replace
    has_parser_symbol = False


    #
    #   Interface Tree_Parameter_0
    #
   #@replace
    has_tree_parameter = False


    #
    #   Interface Tree_Parameter_Tuple_0
    #
   #@replace
    suite_estimate = 0


    def dump_parameter_tuple_tokens(self, f):
        f.line('<parameters-tuple-0>')


    #
    #   Interface Tree_Suite_0
    #
   #@replace
   #suite_estimate = 0      #   Done above in interface Tree_Parameter_Tuple_0


    #
    #   Public
    #


    #
    #   Technically, the `.__nonzero__` method should be as follows:
    #
    #       @staticmethod
    #       def __nonzero__():
    #           return False
    #
    #   However, since `parser_none` is never used in a boolean context, and hence we don't need a `.__nonzero__` method.
    #


    @staticmethod
    def __repr__():
        return '<parser-none>'


@creator
def create_Parser_None():
    return Parser_None()


parser_none = create_Parser_None()


export(parser_none)
