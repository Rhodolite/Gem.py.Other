#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter_Tuple - Interface to a tuple of `Parser_Tuple`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  virtual


#
#   interface Tree_Parameter_Tuple
#       documentation
#           Interface to a tuple of `Tree_Parameter`.
#
#       debug
#           is_tree_parameter_tuple := true
#
#       attribute
#           tuple_estimate : integer { 1, 7 }
#               documentation
#                   A tuple estimate of 1 means 1         `Tree_Parameter`.
#                   A tuple estimate of 7 means 2 or more `Tree_Parameter`.
#
#       method
#           dump_parameter_tuple_tokens(f : Build_DumpToken)
#
class TRAIT_Tree_Parameter_Tuple(object):
    __slots__ = (())


    if __debug__:
        is_tree_parameter_tuple = True


   #@replace
    tuple_estimate = 1


#
#   interface Tree_Parameter_Tuple_0
#       documentation
#           Interface to `parser_none` or `Tree_Parameter_Tuple`
#
#       debug
#           is_tree_parameter_tuple_0 := true
#
#       attribute
#           tuple_estimate : integer { 0, 1, 7 }
#               documentation
#                   A tuple estimate of 0 means 0         `Tree_Parameter`.
#                   A tuple estimate of 1 means 1         `Tree_Parameter`.
#                   A tuple estimate of 7 means 2 or more `Tree_Parameter`.
#
#       if tuple_estimate
#           implement Tree_Parameter_Tuple
#
class TRAIT_Tree_Parameter_Tuple_0(object):
    __slots__ = (())


    if __debug__:
        is_tree_parameter_tuple_0 = True


#
#   USAGE:
#
#       v.dump_symbol_tuple_tokens(f)           #   Dump the tokens representing the symbol(s) to `f`.
#
#       v.tuple_estimate                        #   Estimate the number of symbol in this tuple.
#                                               #   (See documentation above for the estimate values).
#


#
#   USAGE (debug mode):
#
#       v.is_tree_parameter_tuple                   #   Test if `v` is a `Tree_Parameter_Tuple`.
#
#       v.is_tree_parameter_tuple_0                 #   Test if `v` is a `Tree_Parameter_Tuple_0`.
#
#       assert fact_is_tree_parameter_tuple(v)      #   Assert that `v` is a `Tree_Parameter_Tuple`.
#
#       assert fact_is_tree_parameter_tuple_0(v)    #   Assert that `v` is a `Tree_Parameter_Tuple_0`.
#


#
#   fact_is_tree_parameter_tuple(v) - Assert that `v` is a `Tree_Parameter_Tuple`.
#
if __debug__:
    def fact_is_tree_parameter_tuple(v):
        assert v.is_tree_parameter_tuple

        return True


#
#   fact_is_tree_parameter_tuple_0(v) - Assert that `v` is a `Tree_Parameter_Tuple_0`.
#
if __debug__:
    def fact_is_tree_parameter_tuple_0(v):
        assert v.is_tree_parameter_tuple_0

        return True
