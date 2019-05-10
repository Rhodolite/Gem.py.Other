#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V1 - Implementation of Tree Name, Version 1
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  replace
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression
from    Z.Tree.Parameter                import  TRAIT_Tree_Parameter
from    Z.Tree.Target                   import  TRAIT_Tree_Delete_Target


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Capital.Native_Integer              import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
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
        'column',                       #   Keen_Native_Integer

        'id',                           #   Full_Native_String
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, id, context):
        self.line_number = line_number
        self.column      = column

        self.id      = id
        self.context = context


    def _dump_tree_name_token(self, f):
        f.arrange('<name @{}:{} {} ', self.line_number, self.column, self.id)
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
        return arrange('<Tree_Name @{}:{} {!r} {}>', self.line_number, self.column, self.id, self.context)


@creator
def create_Tree_Name(line_number, column, id, context):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_full_native_string(id)
    assert fact_is_tree_context      (context)

    return Tree_Name(line_number, column, id, context)
