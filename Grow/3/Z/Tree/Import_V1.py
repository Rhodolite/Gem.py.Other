#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Import_V1 - Implementation of `import` statements, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_substantial_native_integer


#
#   Tree: `import` statement
#
class Tree_Import_Statement(
        TRAIT_Tree_Statement,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Substantial_Native_Integer

        'module_aliases',               #   Full_Native_List of Tree_Module_Alias
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, module_aliases):
        self.line_number = line_number
        self.column      = column

        self.module_aliases = module_aliases


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<import @{}:{} ', self.line_number, self.column)

        #
        #<module_aliases>
        #
        f.write('[')

        first = True

        for v in self.module_aliases:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_module_alias_tokens(f)

        f.write(']')
        #</>

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Import_Statement @{}:{} {!r}>', self.line_number, self.column, self.module_aliases)


@creator
def create_Tree_Import_Statement(line_number, column, module_aliases):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_full_native_list(module_aliases)

    return Tree_Import_Statement(line_number, column, module_aliases)
