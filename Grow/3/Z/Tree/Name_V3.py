#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V3 - Implementation of Tree Name, Version 3
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2 & Version 3.
#
#       Version 2:
#
#           `Tree_Name` had a `.id` member of type `Full_Native_String`.
#
#       Version 3:
#
#           `Tree_Name` removes the `.id` member, and replaces it with a `.symbol` of type `Parser_Symbol`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  replace
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target


if __debug__:
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_parameter_context
    from    Z.Tree.Context              import  fact_is_tree_store_context



#
#   Tree: Name - A name (in a specific context)
#
#       See "Z.Tree.Context" for explanation of contexts.
#
#       Because a `Tree_Name` can appear both as an expression, as a parameter, and as a target, it implements the
#       `Tree_Parameter`, `Tree_Target`, and `Tree_Value_Expression` interfaces.
#
class Tree_Name(
        TRAIT_Tree_Delete_Target,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Value_Expression,
):
    #
    #   Implements Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbol',                       #   Parser_Symbol
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, symbol, context):
        self.line_number = line_number
        self.column      = column

        self.symbol  = symbol
        self.context = context


    def _dump_tree_name_token(self, f):
        f.arrange('<name @{}:{} {} ', self.line_number, self.column, self.symbol)
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        @replace
        @property
        def is_tree_delete_target(self):
            return self.context.is_tree_delete_context


    if __debug__:
        def dump_delete_target_tokens(self, f):
            assert fact_is_tree_delete_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_delete_target_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
        @replace
        @property
        def is_tree_parameter(self):
            return self.context.is_tree_parameter_context


       #@replace
        is_tree_normal_parameter = is_tree_parameter


    if __debug__:
        def dump_parameter_tokens(self, f):
            assert fact_is_tree_parameter_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_parameter_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context


    if __debug__:
        def dump_store_target_tokens(self, f):
            assert fact_is_tree_store_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_store_target_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Value_Expression
    #
    if __debug__:
        @replace
        @property
        def is_tree_value_expression(self):
            return self.context.is_tree_load_context


    if __debug__:
        def dump_value_expression_tokens(self, f):
            assert fact_is_tree_load_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_value_expression_tokens = _dump_tree_name_token


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Name @{}:{} {!r} {}>', self.line_number, self.column, self.symbol, self.context)


@creator
def create_Tree_Name(line_number, column, symbol, context):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(symbol)
    assert fact_is_tree_context (context)

    return Tree_Name(line_number, column, symbol, context)
