#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V4 - Implementation of an identifier used in the Z parser, Version 4.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           1)  `Parser_Symbol_Leaf` does not implement `Parser_Symbol_0`
#
#           2)  Does not define `conjure_parser_symbol_0`.
#
#       Version 4:
#
#           1)  `Parser_Symbol_Leaf` implements `Parser_Symbol_0`.
#
#           2)  Defines `conjure_parser_symbol_0`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  creator
from    Capital.Core                        import  export
from    Capital.Native_String               import  Full_Native_String
from    Capital.Maybe_Temporary             import  TRAIT_Maybe_Temporary_0
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol_0


if __debug__:
    from    Capital.Cannot                  import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot                  import  raise__CANNOT__create__ERROR
    from    Capital.Native_String           import  fact_is__native_none__OR__full_native_string
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   Parser: Symbol [Leaf]
#
class Parser_Symbol_Leaf(
        Full_Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Parser_Module_Name,
        TRAIT_Parser_Symbol,
        TRAIT_Parser_Symbol_0,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Parser_Module_Name
    #
    def dump_module_name_token(self, f):
        f.arrange('<module-name $ {}>', self)


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


#
#   conjure_parser_symbol_0(z, name)
#
#       Either return `parser_none`, or conjure a `Parser_Symbol`, based on `name`.  Guarantees Uniqueness.
#
#       PARAMETERS:
#
#            `z` must be a `Convert_Zone`, but is otherwise ignored.
#
#            `name` may be `None`, in which case `parser_none` is returned.
#
#            `name` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#            `name` may *NOT* be an instance of a subclass of `str`.
#
#       EXCEPTION
#
#           If `name` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
@export
@creator
def conjure_parser_symbol_0(z, name):
    assert fact_is_convert_zone                        (z)
    assert fact_is__native_none__OR__full_native_string(name)

    if name is None:
        return parser_none

    return z.conjure_parser_symbol(z, name)
