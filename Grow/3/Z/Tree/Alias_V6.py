#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V6 - Implementation of `Tree_{Module,Symbol}_Alias`, Version 6.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           1)  `Tree_Module_Alias_Leaf.as_name` is a `Parser_Symbol_0`.
#
#           2)  `Tree_Symbol_Alias_Leaf.as_name` is a `Parser_Symbol_0`.
#
#       Version 6:
#
#           1)  `Tree_Module_Alias_Leaf.as_name` is a `Parser_Symbol`.
#
#           2)  `Tree_Symbol_Alias_Leaf.as_name` is a `Parser_Symbol`.
#
#           3)  Instead of creating either a `Tree_Module_Alias_Leaf` with a `.as_name` of `parser_none`;
#               instead it simply uses the `Parser_Module_Name` as the `Tree_Alias`
#
#           4)  Instead of creating either a `Tree_Symbol_Alias_Leaf` with a `.as_name` of `parser_none`;
#               instead it simply uses the `Parser_Symbol` as the `Tree_Alias`
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                    import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Z.Parser.Module_Name        import  fact_is_parser_module_name
    from    Z.Parser.Symbol             import  fact_is_parser_symbol


#
#   Tree: Module Alias [Leaf] - An alias in an `import` statement.
#
class Tree_Module_Alias_Leaf(
        TRAIT_Tree_Module_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Module_Name
        'as_name',                      #   Parser_Symbol
    ))


    #
    #   Private
    #
    def __init__(self, name, as_name):
        self.name    = name
        self.as_name = as_name


    #
    #   Interface Tree_Module_Alias
    #
    def dump_module_alias_tokens(self, f):
        f.arrange('<module-alias ')
        self.name.dump_module_name_token(f)
        f.write(' as ')
        self.as_name.dump_symbol_token(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        if self.as_name is None:
            return arrange('<Tree_Module_Alias_Leaf {!r}>', self.name)

        return arrange('<Tree_Module_Alias_Leaf {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Module_Alias(name, as_name):
    assert fact_is_parser_module_name(name)
    assert fact_is_parser_symbol     (as_name)

    return Tree_Module_Alias_Leaf(name, as_name)


#
#   Tree: Symbol Alias [Leaf] - An alias in a `from` statement.
#
class Tree_Symbol_Alias_Leaf(
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Symbol
        'as_name',                      #   Parser_Symbol
    ))


    #
    #   Private
    #
    def __init__(self, name, as_name):
        self.name    = name
        self.as_name = as_name


    #
    #   Interface Tree_Symbol_Alias
    #
    def dump_symbol_alias_tokens(self, f):
        f.arrange('<symbol-alias ')
        self.name.dump_symbol_token(f)
        f.write(' as ')
        self.as_name.dump_symbol_token(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        if self.as_name is None:
            return arrange('<Tree_Symbol_Alias_Leaf {!r}>', self.name)

        return arrange('<Tree_Symbol_Alias_Leaf {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Symbol_Alias(name, as_name):
    assert fact_is_parser_symbol(name)
    assert fact_is_parser_symbol(as_name)

    return Tree_Symbol_Alias_Leaf(name, as_name)
