#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V4 - Implementation of `Tree_Alias`, Version 4.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           1)  `Tree_Module_Alias.as_name` is a `None | FullNativeString`.
#
#           2)  `Tree_Symbol_Alias.name` is a `FullNativeString`.
#
#           3)  `Tree_Symbol_Alias.as_name` is a `None | FullNativeString`.
#
#       Version 4:
#
#           1)  `Tree_Module_Alias.as_name` is a `Parser_Symbol_0`.
#
#           2)  `Tree_Symbol_Alias.name` is a `Parser_Symbol`.
#
#           3)  `Tree_Symbol_Alias.as_name` is a `Parser_Symbol_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Alias


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Parser.Module_Name        import  fact_is_parser_module_name
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Parser.Symbol             import  fact_is_parser_symbol_0


#
#   Tree: Module Alias - An alias in an `import` statement.
#
class Tree_Module_Alias(
        TRAIT_Tree_Alias,
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
    #   Interface Tree_Alias
    #
    def dump_alias_tokens(self, f):
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
            return arrange('<Tree_Module_Alias {!r}>', self.name)

        return arrange('<Tree_Module_Alias {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Module_Alias(name, as_name):
    assert fact_is_parser_module_name(name)
    assert fact_is_parser_symbol_0   (as_name)

    return Tree_Module_Alias(name, as_name)


#
#   Tree: Symbol Alias - An alias in a `from` statement.
#
class Tree_Symbol_Alias(
        TRAIT_Tree_Alias,
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
    #   Interface Tree_Alias
    #
    def dump_alias_tokens(self, f):
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
            return arrange('<Tree_Symbol_Alias {!r}>', self.name)

        return arrange('<Tree_Symbol_Alias {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Symbol_Alias(name, as_name):
    assert fact_is_parser_symbol  (name)
    assert fact_is_parser_symbol_0(as_name)

    return Tree_Symbol_Alias(name, as_name)
