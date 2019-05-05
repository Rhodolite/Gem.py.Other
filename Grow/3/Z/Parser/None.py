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
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


#
#   Parser: None
#
class Parser_None(
        TRAIT_Parser_Symbol_0,
        TRAIT_Tree_Suite_0,
):
    __slots__ = (())


    #
    #   Interface Parser_Symbol_0
    #
   #@replace
    has_parser_symbol = False


    #
    #   Interface Tree_Suite_0
    #
   #@replace
    suite_estimate = 0


    #
    #   Public
    #
    @staticmethod
    def __repr__():
        return '<parser-none>'


@creator
def create_Parser_None():
    return Parser_None()


parser_none = create_Parser_None()


export(parser_none)
