#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Symbol - A python symbol (i.e.: an identifier).
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_empty_native_list
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_parameter_context
    from    Z.Tree.Context              import  fact_is_tree_store_context


class Tree_Name(str):
    __slots__ = (())
