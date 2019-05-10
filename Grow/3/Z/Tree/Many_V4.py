#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Many_V4 - Implementation of tree target classes (tuple & list), Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       See "Tree.Target" for an explanation of "target".
#


#
#   Difference between Version 2, Version 3 & Version 4.
#
#       Version 2:
#
#           `Tree_List_Expression` and `Tree_Tuple_Expression` had a `.context` member which two possible values:
#
#               tree_load_context
#               tree_store_context
#
#       Version 3:
#
#           Does *NOT* exist.
#
#       Version 4:
#
#           Instead of `Tree_List_Expression` with a `.context` member, two classes exist instead:
#
#               Tree_Evaluate_List
#               Tree_Store_List
#
#           Instead of `Tree_Store_Expression` with a `.context` member, two classes exist instead:
#
#               Tree_Evaluate_Tuple
#               Tree_Store_Tuple
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Target                   import  TRAIT_Tree_Store_Target


if __debug__:
    from    Capital.Fact                import  fact_is_positive_native_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_native_integer


#
#   Tree_Many_Expresion.dump_value_expression_tokens(self, f)
#
#       Method `.dump_value_expression_tokens` used by `Tree_Evaluate_List` and `Tree_Evaluate_Tuple`.
#
def Tree_Many_Expresion__dump_evaluate_tokens(self, f):
    first = True

    f.arrange('<{} @{}:{}', self.keyword, self.line_number, self.column)

    for v in self.elements:
        if first:
            first = False

            f.write(';')
        else:
            f.write(',')

        f.space()
        v.dump_value_expression_tokens(f)

    f.greater_than_sign()


#
#   Tree_Many_Expresion.dump_store_target_tokens(self, f)
#
#       Method `.dump_store_target_tokens` used by `Tree_Store_List` and `Tree_Store_Tuple`.
#
#   NOTE:
#       The method `.dump_store_target_tokens` below has one lines different from method
#       `.dump_value_expression_tokens` above:
#
#           v.dump_store_target_tokens(f)
#
def Tree_Many_Expresion__dump_store_target_tokens(self, f):
    first = True

    f.arrange('<{} @{}:{}', self.keyword, self.line_number, self.column)

    for v in self.elements:
        if first:
            first = False

            f.write(';')
        else:
            f.write(',')

        f.space()
        v.dump_store_target_tokens(f)

    f.greater_than_sign()


#
#   Tree: Evaluate Many - Base class of `Tree_{Evaluate_List,Evaluate_Tuple,Store_List,Store_Tuple}`.
#
class Tree_Many_Expression(object):
    __slots__ = ((
        'line_number',                  #   Native_Positive_Integer
        'column',                       #   Native_Substantial_Integer

        'elements',                     #   Some_Native_List of (Tree_Store_Target | Tree_Value_Expression)
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, elements):
        self.line_number = line_number
        self.column      = column

        self.elements = elements


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r}>', self.__class__.__name__, self.line_number, self.column, self.elements)


@creator
def create_Tree_Many_Expression(Meta, line_number, column, elements):
    assert fact_is_positive_native_integer   (line_number)
    assert fact_is_substantial_native_integer(column)

    assert fact_is_some_native_list(elements)

    return Meta(line_number, column, elements)


#
#   Tree: Evaluate List
#
class Tree_Evaluate_List(
        Tree_Many_Expression,
        TRAIT_Tree_Value_Expression,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Some_Native_List of Tree_Value_Expression
    ))


    #
    #   Interface Tree_Value_Expression
    #
    dump_value_expression_tokens = Tree_Many_Expresion__dump_evaluate_tokens


    #
    #   Public
    #
    keyword = 'evaluate-list'


@creator
def create_Tree_Evaluate_List(line_number, column, elements):
    return create_Tree_Many_Expression(Tree_Evaluate_List, line_number, column, elements)


#
#   Tree: Evaluate Tuple
#
class Tree_Evaluate_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Value_Expression,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Some_Native_List of Tree_Value_Expression
    ))




    #
    #   Interface Tree_Value_Expression
    #
    dump_value_expression_tokens = Tree_Many_Expresion__dump_evaluate_tokens


    #
    #   Public
    #
    keyword = 'evaluate-tuple'


@creator
def create_Tree_Evaluate_Tuple(line_number, column, elements):
    return create_Tree_Many_Expression(Tree_Evaluate_Tuple, line_number, column, elements)


#
#   Tree: Store List
#
class Tree_Store_List(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Some_Native_List of Tree_Store_Target
    ))


    #
    #   Interface Tree_Store_Target
    #
    dump_store_target_tokens = Tree_Many_Expresion__dump_store_target_tokens


    #
    #   Public
    #
    keyword = 'store-list'


@creator
def create_Tree_Store_List(line_number, column, elements):
    return create_Tree_Many_Expression(Tree_Store_List, line_number, column, elements)


#
#   Tree: Store Tuple
#
class Tree_Store_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Some_Native_List of Tree_Store_Target
    ))


    #
    #   Interface Tree_Store_Target
    #
    dump_store_target_tokens = Tree_Many_Expresion__dump_store_target_tokens


    #
    #   Public
    #
    keyword = 'store-tuple'


@creator
def create_Tree_Store_Tuple(line_number, column, elements):
    return create_Tree_Many_Expression(Tree_Store_Tuple, line_number, column, elements)
