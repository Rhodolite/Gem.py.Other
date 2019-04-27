#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Target_V1 - Implementation of `Tree_Target`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_store_context
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Index                import  fact_is_tree_index_clause


#
#   Tree: Many Expression, Version 1 - Base class of `Tree_List_Expression_V1` and `Tree_Tuple_Expression_V1`
#
class Tree_Many_Expression_V1(object):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'elements',                     #   SomeNativeList of Tree_Expression
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, elements, context):
        self.line_number = line_number
        self.column      = column

        self.elements = elements
        self.context  = context


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        assert fact_is_tree_load_context(self.context)

        first = True

        f.arrange('<{} @{}:{}', self.keyword, self.line_number, self.column)

        for v in self.elements:
            if first:
                first = False

                f.write(';')
            else:
                f.write(',')

            f.space()
            v.dump_evaluate_tokens(f)

        f.write('; ')
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Store_Target
    #
    #   NOTE:
    #       The method `.dump_store_target_tokens` below has TWO lines different from method `.dump_evaluate_tokens`
    #       above:
    #
    #           1)  assert fact_is_tree_store_context(self.context)
    #           2)  v.dump_store_target_tokens(f)
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context


    def dump_store_target_tokens(self, f):
        assert fact_is_tree_store_context(self.context)

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

        f.write('; ')
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.elements, self.context)


def create_Tree_Many_Expression_V1(Meta, line_number, column, elements, context):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_list(elements)
    assert fact_is_tree_context    (context)

    return Meta(line_number, column, elements, context)


#
#   Tree_Attribute_V1 - An attribute access in an expresssion.
#
#   Example:
#
#       In the following statement:
#
#           a.b = c.d
#
#       The left hand side `a.b` will an attribute access, and the context will be `store`.
#
#       The right hand side `c.d` will be an attribute access, and the context will be `load`.
#
class Tree_Attribute_V1(object):
    #
    #   implements Tree_Delete_Target,
    #              Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'value',                        #   Tree_Expression
        'attribute',                    #   NativeString
        'context',                      #   Tree_Context
    ))


    def _dump_tree_attribute_token(self, f):
        f.arrange('<attribute @{}:{} ', self.line_number, self.column)
        self.value.dump_evaluate_tokens(f)
        f.space()
        f.write(self.attribute)
        f.space()
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Private
    #
    def __init__(self, line_number, column, value, attribute, context):
        self.line_number = line_number
        self.column      = column

        self.value     = value
        self.attribute = attribute
        self.context   = context


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        @property
        def is_tree_delete_target(self):
            return self.context.is_tree_delete_context


    if __debug__:
        def dump_delete_target_tokens(self, f):
            assert fact_is_tree_delete_context(self.context)

            self._dump_tree_attribute_token(f)
    else:
        dump_delete_target_tokens = _dump_tree_attribute_token

        
    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    if __debug__:
        def dump_evaluate_tokens(self, f):
            assert fact_is_tree_load_context(self.context)

            self._dump_tree_attribute_token(f)
    else:
        dump_evaluate_tokens = _dump_tree_attribute_token


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

            self._dump_tree_attribute_token(f)
    else:
        dump_store_target_tokens = _dump_tree_attribute_token


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Attribute_V1 @{}:{} {!r}.{} {}>',
                       self.line_number, self.column, self.value, self.attribute, self.context)


def create_Tree_Attribute_V1(line_number, column, value, attribute, context):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_tree_expression   (value)
    assert fact_is_full_native_string(attribute)
    assert fact_is_tree_context      (context)

    return Tree_Attribute_V1(line_number, column, value, attribute, context)


#
#   Tree: List Expression, V1
#
class Tree_List_Expression_V1(Tree_Many_Expression_V1):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = (())


    keyword = 'list-expression'


def create_Tree_List_Expression_V1(line_number, column, elements, context):
    return create_Tree_Many_Expression_V1(Tree_List_Expression_V1, line_number, column, elements, context)


#
#   Tree: Tuple Expression, V1
#
class Tree_Tuple_Expression_V1(Tree_Many_Expression_V1):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = (())


    keyword = 'tuple-expression'


def create_Tree_Tuple_Expression_V1(line_number, column, elements, context):
    return create_Tree_Many_Expression_V1(Tree_Tuple_Expression_V1, line_number, column, elements, context)
