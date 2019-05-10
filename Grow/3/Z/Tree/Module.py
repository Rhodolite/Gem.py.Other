#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Module - Tree class that represent a module.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator


if __debug__:
    from    Capital.Fact                import  fact_is_native_list


#
#   Tree_Module
#
class Tree_Module(object):
    __slots__ = ((
        'body',                         #   Native_List of Tree_Statement
    ))


    def __init__(self, body):
        self.body = body


    def __repr__(self):
        return arrange('<Tree.Module {!r}>', self.body)


    def dump_module_tokens(self, f):
        with f.indent_2('<module [', ']>'):
            for v in self.body:
                v.dump_statement_tokens(f)


@creator
def create_Tree_Module(body):
    assert fact_is_native_list(body)

    return Tree_Module(body)
