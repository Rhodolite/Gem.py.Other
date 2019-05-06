#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V1 - Implementation of `Tree_{Module,Symbol}_Alias`, Version 1.
#
#       See "Z.Tree.Alias" for an explanation of "tree aliases".
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
#   Tree: Alias Clause - An alias in an `import` or `from` statement.
#
#       Again, see "Z.Tree.Alias" for an explanation of "tree aliases".
#
class Tree_Alias_Clause(
        TRAIT_Tree_Module_Alias,
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'symbol',                       #   FullNativeString
        'as_name',                      #   None | FullNativeString
    ))


    #
    #   Private
    #
    def __init__(self, symbol, as_name):
        self.symbol  = symbol
        self.as_name = as_name


    #
    #   Interface Tree_Module_Alias
    #
    def dump_module_alias_tokens(self, f):
        f.arrange('<module-alias {}', self.symbol)

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

        f.greater_than_sign()


    #
    #   Interface Tree_Symbol_Alias
    #
    def dump_symbol_alias_tokens(self, f):
        f.arrange('<symbol-alias {}', self.symbol)

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        if self.as_name is None:
            return arrange('<Tree_Alias_Clause {!r}>', self.symbol)

        return arrange('<Tree_Alias_Clause {!r} as {!r}>', self.symbol, self.as_name)


@creator
def create_Tree_Alias_Clause(symbol, as_name):
    assert fact_is_full_native_string                  (symbol)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Alias_Clause(symbol, as_name)
