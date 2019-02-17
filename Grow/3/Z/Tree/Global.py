#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


default_tree_version = '2'


#
#   Z.Tree.Global - Globals to affect the creation of `Tree_*` classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   Tree_Globals - Globals to affect the creation of `Tree_*` classes.
#
class Tree_Globals(object):
    __slots__ = ((
        'tree_version',                 #   NativeString
    ))


    def __init__(self, tree_version):
        self.tree_version = tree_version


    def __repr__(self):
        return arrange('<Tree_Globals {}>', self.tree_version)


def create_tree_globals(tree_version):
    assert fact_is_full_native_string(tree_version)

    r = Tree_Globals(tree_version)

    trace('Tree Globlals: {}', r)

    return r


tree_globals = create_tree_globals(default_tree_version)
