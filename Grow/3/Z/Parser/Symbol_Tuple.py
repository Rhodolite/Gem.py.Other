#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Parser_Symbol_Tuple - Interface to a tuple of `Parser_Symbol`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  virtual


#
#   interface Parser_Symbol_Tuple
#       documentation
#           Interface to a tuple of `Parser_Symbol`.
#
#       debug
#           is_parser_symbol_tuple := true
#
#       attribute
#           tuple_estimate : integer { 1, 7 }
#               documentation
#                   A tuple estimate of 1 means 1         `Parser_Symbol`.
#                   A tuple estimate of 7 means 2 or more `Parser_Symbol`.
#
#       method
#           dump_symbol_tuple_tokens(f : Build_DumpToken)
#
class TRAIT_Parser_Symbol_Tuple(object):
    __slots__ = (())


    if __debug__:
        is_parser_symbol_tuple = True


#
#   USAGE:
#
#       v.dump_symbol_tuple_tokens(f)           #   Dump the tokens representing the symbol(s) to `f`.
#
#       v.tuple_estimate                        #   Estimate the number of symbol in this tuple.
#                                               #   (See documentation above for the estimate values).
#


#
#   USAGE (debug mode):
#
#       v.is_parser_symbol_tuple                #   Test if `v` is a parser symbol tuple.
#
#       assert fact_is_parser_symbol_tuple(v)   #   Assert that `v` is a parser symbol tuple.
#


#
#   fact_is_parser_symbol_tuple(v) - Assert that `v` is a parser symbol tuple.
#
if __debug__:
    def fact_is_parser_symbol_tuple(v):
        assert v.is_parser_symbol_tuple

        return True
