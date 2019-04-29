#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V2 - Implementation of `Tree_Alias`, Version 2.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
#


#
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           `Tree_Alias_Clause` is used for both module aliases & symbol aliases  (so as to do a 1-1 emulation of
#           `_ast`).
#
#       Version 2:
#
#           1)  `Tree_Alias_Clause` removed.
#
#           2)  `Tree_Module_Alias` used for module aliases.
#
#           3)  `Tree_Symbol_Alias` used for symbol aliases.
#
#           NOTE:
#
#               In version 2, `Tree_Module_Alias` and `Tree_Symbol_Alias` are identical (other than minor differences
#               in output for internal representation).
#
#               However, this will soon change, in Version 3.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Alias                    import  TRAIT_Tree_Alias


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression
    from    Z.Tree.Expression           import  fact_is_tree_expression


#
#   Tree: Module Alias - An alias in an `import` statement.
#
class Tree_Module_Alias(
        TRAIT_Tree_Alias,
):
    __slots__ = ((
        'name',                         #   NativeString
        'as_name',                      #   None | NativeString
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
            return arrange('<Tree_Module_Alias {!r}>', self.name)

        return arrange('<Tree_Module_Alias {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Module_Alias(name, as_name):
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Module_Alias(name, as_name)


#
#   Tree: Symbol Alias - An alias in a `from` statement.
#
class Tree_Symbol_Alias(
        TRAIT_Tree_Alias,
):
    __slots__ = ((
        'name',                         #   NativeString
        'as_name',                      #   None | NativeString
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
            return arrange('<Tree_Symbol_Alias {!r}>', self.name)

        return arrange('<Tree_Symbol_Alias {!r} as {!r}>', self.name, self.as_name)


@creator
def create_Tree_Symbol_Alias(name, as_name):
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Symbol_Alias(name, as_name)
