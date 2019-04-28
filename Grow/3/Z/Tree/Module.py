#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Module - Interface to tree class that represent a module.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                        import  arrange


if __debug__:
    from    Capital.Fact                        import  fact_is_some_native_list


#
#   Tree_Module
#
class Tree_Module(object):
    __slots__ = ((
        'body',                         #   NativeList of Tree_Statement
    ))


    def __init__(self, body):
        self.body = body


    def __repr__(self):
        return arrange('<Tree.Module {!r}>', self.body)


    def dump_module_tokens(self, f):
        with f.indent_2('<module [', ']>'):
            for v in self.body:
                v.dump_suite_tokens(f)


def create_Tree_Module(body):
    assert fact_is_some_native_list(body)

    return Tree_Module(body)
