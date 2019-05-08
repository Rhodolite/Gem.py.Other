#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V4 - Implementation of `Tree_{Module,Symbol}_Alias`, Version 4.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           `Tree_Module_Alias_Leaf.name` is a `Full_Native_String`.
#
#       Version 4:
#
#           `Tree_Module_Alias_Leaf.name` is a `Parser_Module_Name`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                    import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string
    from    Z.Parser.Module_Name        import  fact_is_parser_module_name


#
#   Tree: Module Alias Implementation - An alias in an `import` statement.
#
class Tree_Module_Alias_Leaf(
        TRAIT_Tree_Module_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Module_Name
        'as_name',                      #   None | Full_Native_String
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

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

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
    assert fact_is_parser_module_name                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Module_Alias_Leaf(name, as_name)


#
#   Tree: Symbol Alias [Leaf] - An alias in a `from` statement.
#
class Tree_Symbol_Alias_Leaf(
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'name',                         #   Full_Native_String
        'as_name',                      #   None | Full_Native_String
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
        f.arrange('<symbol-alias {}', self.name)

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

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
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Symbol_Alias_Leaf(name, as_name)
