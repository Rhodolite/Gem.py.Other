#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Call_Expression_V1 - Implementation of `Tree_Call_Expression`, Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Expression               import  TRAIT_Tree_Value_Expression


if __debug__:
    from    Capital.Fact                import  fact_is_native_list
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Z.Tree.Expression           import  fact_is__native_none__OR__tree_value_expression
    from    Z.Tree.Expression           import  fact_is_tree_value_expression


#
#   Tree: Call Expression
#
class Tree_Call_Expression(
        TRAIT_Tree_Value_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'function',                     #   Tree_Value_Expression
        'arguments',                    #   Native_List of Tree_Value_Expression
        'keywords',                     #   Native_List of Tree_Value_Expression
        'star_arguments',               #   None | Tree_Value_Expression
        'keyword_arguments',            #   None | Tree_Value_Expression
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, function, arguments, keywords, star_arguments, keyword_arguments):
        self.line_number = line_number
        self.column      = column

        self.function          = function
        self.arguments         = arguments
        self.keywords          = keywords
        self.star_arguments    = star_arguments
        self.keyword_arguments = keyword_arguments


    #
    #   Interface Tree_Value_Expression
    #
    def dump_value_expression_tokens(self, f):
        first = True

        star_arguments    = self.star_arguments
        keyword_arguments = self.keyword_arguments

        f.arrange('<call @{}:{} ', self.line_number, self.column)
        self.function.dump_value_expression_tokens(f)

        f.write(' (')

        for v in self.arguments:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_value_expression_tokens(f)

        for v in self.keywords:
            if first:
                first = False
            else:
                f.write(', ')

            v.dump_argument_tokens(f)

        if star_arguments is not None:
            if first:
                first = False
            else:
                f.write(', ')

            f.write('*')
            star_arguments.dump_value_expression_tokens(f)

        if keyword_arguments is not None:
            if first:
                first = False
            else:
                f.write(', ')

            f.write('**')
            keyword_arguments.dump_value_expression_tokens(f)

        f.write(')>')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Call_Expression @{}:{} {!r} {} {} {} {}>',
                       self.line_number, self.column,
                       self.function, self.arguments, self.keywords, self.star_arguments, self.keyword_arguments)


@creator
def create_Tree_Call_Expression(
        line_number, column, function, arguments, keywords, star_arguments, keyword_arguments,
):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_tree_value_expression                  (function)
    assert fact_is_native_list                            (arguments)
    assert fact_is_native_list                            (keywords)
    assert fact_is__native_none__OR__tree_value_expression(star_arguments)
    assert fact_is__native_none__OR__tree_value_expression(keyword_arguments)

    return Tree_Call_Expression(
               line_number, column, function, arguments, keywords, star_arguments, keyword_arguments,
           )
