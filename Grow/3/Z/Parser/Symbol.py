#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol - Interface to an identifier used in the Z parser.
#


from    Z.Parser.Global                 import  parser_globals


symbol_version = parser_globals.symbol_version


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


if symbol_version >= 3:
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


#
#   Import the version of symbol we want to use (must be after the "facts" above)
#
if symbol_version == 1:
    from    Z.Parser.Symbol_V1          import  conjure_parser_symbol
elif symbol_version == 2:
    from    Z.Parser.Symbol_V2          import  conjure_parser_symbol
elif symbol_version == 3:
    from    Z.Parser.Symbol_V3          import  conjure_parser_symbol
    from    Z.Parser.Symbol_V3          import  conjure_parser_symbol_0
elif symbol_version == 4:
    from    Z.Parser.Symbol_V4          import  conjure_parser_symbol
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Parser/Symbol.py: unknown symbol version: {!r}', symbol_version)
