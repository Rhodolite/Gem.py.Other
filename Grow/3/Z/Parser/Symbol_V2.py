#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V2 - Implementation of an identifier used in the Z parser, Version 2
#


#
#   Differences between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not exist.
#
#       Version 2:
#
#           Exists.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.Native_String               import  Native_String
from    Capital.Maybe_Temporary             import  TRAIT_Maybe_Temporary_0
from    Z.Parser.Produce_ConjureFullName    import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol


if __debug__:
    from    Capital.Cannot                  import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot                  import  raise__CANNOT__create__ERROR


#
#   Parser: Symbol [Leaf]
#
class Parser_Symbol_Leaf(
        Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Parser_Symbol,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Parser_Symbol
    #
    def dump_symbol_token(self, f):
        f.arrange('<$ {}>', self)



    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Parser_Symbol_Leaf {}>', self)


conjure_parser_symbol = produce_conjure_full_name__with_unused_Z_parameter(Parser_Symbol_Leaf)


#
#   conjure_parser_symbol(z, name)
#
#       Conjure a `Parser_Symbol`, based on `name`.  Guarantees Uniqueness.
#
#       PARAMETERS:
#
#            `z` must be a `Convert_Zone`, but is otherwise ignored.
#
#            `name` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#            `name` may *NOT* be an instance of a subclass of `str`.
#
#       EXCEPTION
#
#           If `name` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
export(conjure_parser_symbol)
