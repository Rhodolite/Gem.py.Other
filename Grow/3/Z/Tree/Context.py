#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Context - Interface to tree classes that represent tree context.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       Explanation:
#
#           A "tree context" is used to indicate the context of another tree node:
#
#               A `Tree_Name` is used to access a symbol (i.e: a variable), it has a context that is either:
#
#                   `delete`            (to delete the symbol),
#                   `load`              (to get the value of the symbol),
#                   `parameter`         (to define a function parameter), or
#                   `store`             (to save a new value to the symbol).
#
#               A `Tree_Attribute` is used to access an attribute (i.e.: what appears after the `.`, as in `a.b`, which
#               accesses attribute `.b`), it has a context that is either:
#
#                   `delete`            (to delete the attribute),
#                   `load`              (to get the value of the attribute), or
#                   `store`             (to save a new value to the attribute).
#
#       Example:
#
#           In the following statements:
#    
#               def f(a): pass
#               b = c.d
#               del e, g.h
#    
#           There are seven contexts:
#    
#               `a`     - On the `Tree_Name` of `a`, the context is `Parameter` to indicate `a` is a parameter to
#                         function `f`.
#    
#               `b`     - On the `Tree_Name` of `b`, the context is `Store`, to indicate we are storing (saving) a new
#                         value to symbol `b`.
#    
#               `c`     - On the `Tree_Name` of `c`, the context is `load`, to indicate we are loading the value of
#                         symbol `c` (so as to next load the value of attribute `c.d`)
#    
#               `c.d`   - On the `Tree_Attribute` of `c.d` the context is `load` to indicate we are loading the value
#                         of attribute `c.d`.
#    
#               `e`     - On the `Tree_Name` of `e`, the context is `delete`, to indicate we are deleting `e`.
#    
#               `g`     - On the `Tree_Name` of `g`, the context is `load`, to indicate we are loading the value of `g`
#                         (so as to next delete `g.h`)
#    
#               `g.h`   - On the `Tree_Attribute` of `g.h` the context is `delete` to indicate we are deleting the
#                         attribute `g.h`
#
#           NOTE:
#
#               In the function definition above, there is no context for `f`.  In fact, in the function definition
#               above, `f` is not a `Tree_Name` but instead just a NativeString.
#


#
#   interface Tree_Context - Interface to tree classes that represent context.
#
#       interface Tree_Context
#           attributes
#               is_tree_load_context      : boolean
#               is_tree_parameter_context : boolean
#               is_tree_store_context     : boolean
#
#           method
#               dump_context_token(f : Build_DumpToken)
#
#           debug
#               is_tree_context := true
#


#
#   USAGE:
#
#       v.is_tree_load_context              #   Test if `v` is a tree "load" context.
#
#       v.is_tree_parameter_context         #   Test if `v` is a tree "parameter" context.
#
#       v.is_tree_store_context             #   Test if `v` is a tree "store" context.
#
#       v.dump_context_token(f)             #   Dump the token representing the tree context to `f`.
#


#
#   USAGE (debug mode):
#
#       v.is_tree_context                           #   Test if `v` is a `Tree_Context`
#
#       assert fact_is_tree_context(v)              #   Assert that `v` is a tree context.
#
#       assert fact_is_tree_delete_context(v)       #   Assert that `v` is a tree "delete" context.
#
#       assert fact_is_tree_load_context(v)         #   Assert that `v` is a tree "load" context.
#
#       assert fact_is_tree_parameter_context(v)    #   Assert that `v` is a tree "parameter" context.
#
#       assert fact_is_tree_store_context(v)        #   Assert that `v` is a tree "store" context.
#


from    Capital.Core                    import  trace


#
#   Import the version of tree aliases we want to use
#
from    Z.Tree.Global                   import  tree_globals


version = tree_globals.context_version


if version == '1':
    from    Z.Tree.Context_V1               import  tree_context_delete_v1      as  tree_delete_context
    from    Z.Tree.Context_V1               import  tree_context_load_v1        as  tree_load_context
    from    Z.Tree.Context_V1               import  tree_context_parameter_v1   as  tree_parameter_context
    from    Z.Tree.Context_V1               import  tree_context_store_v1       as  tree_store_context
elif version == '2':
    from    Z.Tree.Context_V2               import  Tree_Context_2


    tree_delete_context    = Tree_Context_2.delete
    tree_load_context      = Tree_Context_2.load
    tree_parameter_context = Tree_Context_2.parameter
    tree_store_context     = Tree_Context_2.store
else:
    from    Capital.Core                    import  FATAL

    FATAL('Z/Tree/Context.py: not relevant for context version: {}', version)


#
#   fact_is_tree_context(v) - Assert that `v` is a `Tree_Context`.
#
if __debug__:
    def fact_is_tree_context(v):
        assert v.is_tree_context

        return True


#
#   fact_is_tree_delete_context(v) -  Assert that `v` is a tree "delete" context.
#
if __debug__:
    def fact_is_tree_delete_context(v):
        assert v.is_tree_delete_context

        return True


#
#   fact_is_tree_load_context(v) -  Assert that `v` is a tree "load" context.
#
if __debug__:
    def fact_is_tree_load_context(v):
        assert v.is_tree_load_context

        return True


#
#   fact_is_tree_parameter_context(v) -  Assert that `v` is a tree "parameter" context.
#
if __debug__:
    def fact_is_tree_parameter_context(v):
        assert v.is_tree_parameter_context

        return True


#
#   fact_is_tree_store_context(v) -  Assert that `v` is a tree "store" context.
#
if __debug__:
    def fact_is_tree_store_context(v):
        assert v.is_tree_store_context

        return True
