#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V5 - Implementation of `Tree_{Module,Symbol}_Alias`, Version 5.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Differences between Version 4 & Version 5.
#
#       Version 4:
#
#           1)  `Tree_Module_Alias_Leaf.as_name` is a `None | Full_Native_String`.
#
#           2)  `Tree_Symbol_Alias_Leaf.name`    is a        `Full_Native_String`.
#
#           3)  `Tree_Symbol_Alias_Leaf.as_name` is a `None | Full_Native_String`.
#
#       Version 5:
#
#           1)  `Tree_Module_Alias_Leaf.as_name` is a `Parser_Symbol_0`.
#
#           2)  `Tree_Symbol_Alias_Leaf.name`    is a `Parser_Symbol`.
#
#           3)  `Tree_Symbol_Alias_Leaf.as_name` is a `Parser_Symbol_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                    import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Z.Parser.Module_Name        import  fact_is_parser_module_name
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Parser.Symbol             import  fact_is_parser_symbol_0


#
#   Tree: Module Alias [Leaf] - An alias in an `import` statement.
#
class Tree_Module_Alias_Leaf(
        TRAIT_Tree_Module_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Module_Name
        'as_name',                      #   Parser_Symbol_0
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

        if self.as_name.has_parser_symbol:
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
    assert fact_is_parser_symbol_0   (as_name)

    return Tree_Module_Alias_Leaf(name, as_name)


#
#   Tree: Symbol Alias [Leaf] - An alias in a `from` statement.
#
class Tree_Symbol_Alias_Leaf(
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Symbol
        'as_name',                      #   Parser_Symbol_0
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

        if self.as_name.has_parser_symbol:
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
    assert fact_is_parser_symbol  (name)
    assert fact_is_parser_symbol_0(as_name)

    return Tree_Symbol_Alias_Leaf(name, as_name)
