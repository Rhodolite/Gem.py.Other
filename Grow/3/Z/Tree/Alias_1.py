#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Alias_V1 - Implementation of `Tree_Alias`, Version 1.
#
#       See "Z/Tree/Alias.py" for an explanation of "tree aliases".
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is__native_none__OR__full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_expression
    from    Z.Tree.Expression           import  fact_is_tree_expression


#
#   Tree_Alias_V1 - An alias in an `import` or `from` statement.
#
#       Again, see "Z/Tree/Alias.py" for an explanation of "tree aliases".
#
class Tree_Alias_V1(object):
    __slots__ = ((
        'name',                         #   NativeString
        'as_name',                      #   None | NativeString
    ))


    def __init__(self, name, as_name):
        self.name    = name
        self.as_name = as_name


    def __repr__(self):
        if self.as_name is None:
            return arrange('<Tree.Alias#1 {!r}>', self.name)

        return arrange('<Tree.Alias#1 {!r} as {!r}>', self.name, self.as_name)


    def dump_alias_tokens(self, f):
        f.arrange('<alias {}', self.name)

        if self.as_name is not None:
            f.write(' as ')
            f.write(self.as_name)

        f.greater_than_sign()


def create_Tree_Alias_V1(name, as_name):
    assert fact_is_full_native_string                  (name)
    assert fact_is__native_none__OR__full_native_string(as_name)

    return Tree_Alias_V1(name, as_name)
