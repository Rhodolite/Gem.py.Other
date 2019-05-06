#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Alias_V5 - Convert Python Abstract Syntax Tree Alias to `Tree_{Module,Symbol}_Alias`, Version 5.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 4 & Version 5.
#
#       Version 4:
#
#           Creates either:
#
#               1)  `Tree_Module_Alias` (sometimes with a second argument of `parser_none`); or
#
#               2)  `Tree_Symbol_Alias` (sometimes with a second argument of `parser_none`).
#
#       Version 5:
#
#           Creates either:
#
#               1)  `Tree_Module_Alias` (when second argument has a value);
#
#               2)  `Tree_Symbol_Alias` (when second argument has a value):
#
#               3)  `Tree_Parser_Module_Name` (when `.asname` is `None`).
#
#               4)  `Tree_Parser_Symbol`      (when `.asname` is `None`).
#


from    Z.Tree.Alias_V5                     import  create_Tree_Module_Alias
from    Z.Tree.Alias_V5                     import  create_Tree_Symbol_Alias
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Alias_Clause
from    Z.Parser.Conjure_Module_Name        import  conjure_parser_module_name
from    Z.Parser.Symbol                     import  conjure_parser_symbol


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

    name = conjure_parser_module_name(self.name)

    if self.asname is None:
        return name

    return create_Tree_Module_Alias(
               name,
               conjure_parser_symbol(self.asname),
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

    name = conjure_parser_symbol(self.name)

    if self.asname is None:
        return name

    return create_Tree_Symbol_Alias(
               name,
               conjure_parser_symbol(self.asname),
           )


#
#   convert_full_list_of_module_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Module_Alias`.
#
def convert_full_list_of_module_aliases(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_module_alias(v)   for v in sequence]


#
#   convert_full_list_of_symbol_aliases(sequence)
#
#       Convert a `FullNativeList of Native_AbstractSyntaxTree_Alias_Clause` (i.e.: `list of _ast.alias`) to a
#       `FullNativeList of Tree_Symbol_Alias`.
#
def convert_full_list_of_symbol_aliases(sequence):
    assert fact_is_full_native_list(sequence)

    return [convert_symbol_alias(v)   for v in sequence]
