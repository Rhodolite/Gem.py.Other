#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V4 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           1)  The second argument to `create_Tree_Module_Alias` is of type `None | FullNativeString`.
#
#           2)  The first argument to `create_Tree_Symbol_Alias` is of type `FullNativeString`.
#
#           3)  The second argument to `create_Tree_Symbol_Alias` is of type `None | FullNativeString`.
#
#       Version 4:
#
#           1)  The second argument to `create_Tree_Module_Alias` is of type `Parser_Symbol_0`.
#
#           2)  The first argument to `create_Tree_Symbol_Alias` is of type `Parser_Symbol`.
#
#           3)  The second argument to `create_Tree_Symbol_Alias` is of type `Parser_Symbol_0`.
#
#


from    Z.Parser.Conjure_Module_Name        import  conjure_parser_module_name
from    Z.Parser.Symbol                     import  conjure_parser_symbol
from    Z.Parser.Symbol                     import  conjure_parser_symbol_0
from    Z.Tree.Alias_V4                     import  create_Tree_Module_Alias
from    Z.Tree.Alias_V4                     import  create_Tree_Symbol_Alias
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause
from    Z.Tree.Produce_Convert_List         import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list
    from    Capital.Fact                    import  fact_is_full_native_string
    from    Capital.Fact                    import  fact_is__native_none__OR__full_native_string


#
#   convert_module_alias(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Module_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_module_alias(self):
    assert fact_is_full_native_string                  (self.name)
    assert fact_is__native_none__OR__full_native_string(self.asname)

    return create_Tree_Module_Alias(
               conjure_parser_module_name(self.name),
               conjure_parser_symbol_0   (self.asname),
           )


#
#   convert_symbol_alias(self)
#
#       Convert a `Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `_ast.alias`) to a `Tree_Symbol_Alias`.
#
assert Native_AbstractSyntaxTree_Alias_Clause._attributes == (())
assert Native_AbstractSyntaxTree_Alias_Clause._fields     == (('name', 'asname'))


def convert_symbol_alias(self):
    assert fact_is_full_native_string                  (self.name)
    assert fact_is__native_none__OR__full_native_string(self.asname)

    return create_Tree_Symbol_Alias(
               conjure_parser_symbol  (self.name),
               conjure_parser_symbol_0(self.asname),
           )


#
#   convert_full_list_of_module_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Module_Alias`.
#
convert_full_list_of_module_aliases = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_module_alias)


#
#   convert_full_list_of_symbol_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Symbol_Alias`.
#
convert_full_list_of_symbol_aliases = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_symbol_alias)
