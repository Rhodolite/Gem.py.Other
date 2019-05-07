#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol - Interface to an identifier used in the Z parser.
#


#
#   interface Parser_Symbol
#       documentation
#           Interface to an identifier used in the Z parser.
#
#       extends
#           Parser_Module_Name
#
#       debug
#           is_parser_symbol := true
#
#       method
#           dump_symbol_token(f : Build_DumpToken)
#
class TRAIT_Parser_Symbol(object):
    __slots__ = (())


    if __debug__:
        is_parser_symbol = True


#
#   interface Parser_Symbol_0
#       documentation
#           Interface to an identifier used in the Z parser; OR the `parser_none`.
#
#       attribute
#           has_parser_symbol : Boolean
#
#       if has_parser_symbol
#           implements Parser_Symbol
#
#       debug
#           is_parser_symbol_0 := true
#
#   NOTE:
#       `Parser_Symbol_0` is only used in `symbol_version >= 4` (see "Z.Tree.Convert_Zone.py" for `symbol_version`).
#
class TRAIT_Parser_Symbol_0(object):
    __slots__ = (())


    if __debug__:
        is_parser_symbol_0 = True


   #@virtual
    has_parser_symbol = True


#
#   USAGE:
#
#       v.has_parser_symbol                 #   Test if `v` has a parser symbol and is *NOT* `parser_none`.
#


#
#   USAGE (debug mode):
#
#       v.is_parser_symbol                  #   Test if `v` is a parser symbol.
#
#       v.is_parser_symbol_0                #   Test if `v` is a `Parser_Symbol_0`.
#
#       assert fact_is_parser_symbol(v)     #   Assert that `v` is a parser symbol.
#
#       assert fact_is_parser_symbol_0(v)   #   Assert that `v` is a `Parser_Symbol_0`.
#


if __debug__:
    #
    #   fact_is_parser_symbol(v) - Assert the fact that `v` is a parser symbol.
    #
    def fact_is_parser_symbol(v):
        assert v.is_parser_symbol

        return True


if __debug__:
    #
    #   fact_is_parser_symbol_0(v) - Assert the fact that `v` is a `Parser_Symbol_0`.
    #
    def fact_is_parser_symbol_0(v):
        assert v.is_parser_symbol_0

        return True
