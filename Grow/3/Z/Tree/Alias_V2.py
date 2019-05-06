#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V2 - Implementation of `Tree_{Module,Symbol}_Alias`, Version 2.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           `Tree_Alias_Clause` is used for both module aliases & symbol aliases (so as to do a 1-1 emulation of
#           `_ast`).
#
#       Version 2:
#
#           1)  `Tree_Alias_Clause` removed.
#
#           2)  `Tree_Module_Alias_Implementation` used for module aliases.
#
#           3)  `Tree_Symbol_Alias_Implementation` used for symbol aliases.
#
#           NOTE:
#
#               In version 2, `Tree_Module_Alias_Implementation` and `Tree_Symbol_Alias_Implementation` are identical
#               (other than minor differences in result of `__repr__`).
#
#               However, this will soon change, in Version 3.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Module_Alias
from    Z.Tree.Alias                    import  TRAIT_Tree_Symbol_Alias


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Tree: Module Alias Implementation - An alias in an `import` statement.
#
class Tree_Module_Alias_Implementation(
        TRAIT_Tree_Module_Alias,
):
    __slots__ = ((
        'name',                         #   FullNativeString
        'as_name',                      #   None | FullNativeString
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
        f.arrange('<module-alias {}', self.name)

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        if self.as_name is None:
            return arrange('<Tree_Module_Alias_Implementation {!r}>', self.name)

        return arrange('<Tree_Module_Alias_Implementation {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Module_Alias(name, as_name):
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Module_Alias_Implementation(name, as_name)


#
#   Tree: Symbol Alias Implementation - An alias in a `from` statement.
#
class Tree_Symbol_Alias_Implementation(
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'name',                         #   FullNativeString
        'as_name',                      #   None | FullNativeString
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
            return arrange('<Tree_Symbol_Alias_Implementation {!r}>', self.name)

        return arrange('<Tree_Symbol_Alias_Implementation {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Symbol_Alias(name, as_name):
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Symbol_Alias_Implementation(name, as_name)
