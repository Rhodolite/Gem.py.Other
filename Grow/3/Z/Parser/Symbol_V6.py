#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol_V6 - Implementation of an identifier used in the Z parser, Version 6
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           `Parser_Symbol_Leaf` does not implement `Parser_Symbol_Tuple`.
#
#       Version 5:
#
#           `Parser_Symbol_Leaf` implements `Parser_Symbol_Tuple`.
#


from    Capital.Core                        import  arrange
from    Capital.Core                        import  export
from    Capital.Native_String               import  Native_String
from    Capital.Maybe_Temporary             import  TRAIT_Maybe_Temporary_0
from    Z.Parser.Module_Name                import  TRAIT_Parser_Module_Name
from    Z.Parser.None                       import  parser_none
from    Z.Parser.Produce_ConjureFullString  import  produce_conjure_full_name__with_unused_Z_parameter
from    Z.Parser.Symbol                     import  TRAIT_Parser_Symbol
from    Z.Parser.Symbol_Tuple               import  TRAIT_Parser_Symbol_Tuple
from    Z.Tree.Alias                        import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                        import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Capital.Cannot                  import  raise__CANNOT__create__ERROR
    from    Capital.Cannot                  import  raise__CANNOT__construct__ERROR


#
#   Parser: Symbol [Leaf]
#
class Parser_Symbol_Leaf(
        Native_String,
        TRAIT_Maybe_Temporary_0,
        TRAIT_Parser_Module_Name,
        TRAIT_Parser_Symbol,
        TRAIT_Parser_Symbol_Tuple,
        TRAIT_Tree_Module_Alias,
        TRAIT_Tree_Symbol_Alias,
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
    #   Interface Parser_Symbol_Tuple
    #
    tuple_estimate = 1


    def dump_symbol_tuple_tokens(self, f):
        f.arrange('<symbol-tuple $ {}>', self)


    #
    #   Interface Tree_Module_Alias
    #
    def dump_module_alias_tokens(self, f):
        f.arrange('<module-alias $ {}>', self)


    #
    #   Interface Tree_Symbol_Alias
    #
    def dump_symbol_alias_tokens(self, f):
        f.arrange('<symbol-alias $ {}>', self)


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
