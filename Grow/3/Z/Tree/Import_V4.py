#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Import_V2 - Implementation of `from` and `import` statements, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1, Version 2, Version 3, and Version 4.
#
#       Version 1:
#
#           Tree Statements implement `Tree_Statement`.
#
#       Version 2 & 3:
#
#           Does not exist.
#
#       Version 4:
#
#           Tree Statements implement `Tree_Statement`; and ...
#
#           ... in addition also implement `Tree_Suite`, and `Tree_Suite_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_list
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Tree: `from ... import ...` statement
#
class Tree_From_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'module',                       #   Full_Native_String
        'names',                        #   FullNativeList of Tree_Symbol_Alias
        'level',                        #   Substantial_Integer
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, module, names, level):
        self.line_number = line_number
        self.column      = column

        self.module = module
        self.names  = names
        self.level  = level


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        f.arrange('<from @{}:{} {} import ', self.line_number, self.column, self.module)

        #
        #<names>
        #
        f.write('[')

        first = True

        for v in self.names:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_symbol_alias_tokens(f)

        f.write(']')
        #</>

        if self.level:
            f.arrange('; level<{}>', self.level)

        f.line('>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_From_Import_Statement @{}:{} {!r} {!r} {!r}>',
                       self.line_number, self.column,
                       self.module, self.names, self.level)


@creator
def create_Tree_From_Import_Statement(line_number, column, module, names, level):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_string (module)
    assert fact_is_full_native_list   (names)
    assert fact_is_substantial_integer(level)

    return Tree_From_Import_Statement(line_number, column, module, names, level)


#
#   Tree: `import` statement
#
class Tree_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'module_aliases',               #   NativeList of Tree_Module_Alias
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
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_full_native_list(module_aliases)

    return Tree_Import_Statement(line_number, column, module_aliases)
