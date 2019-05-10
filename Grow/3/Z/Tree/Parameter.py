#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Parameter - Interface to tree classes that represent parameters.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   TREE_PARAMETER
#
#       Version 1:
#
#           `Tree_Parameter`            - Base interface of parameters.
#
#           `Tree_Keyword_Parameter`    - A keyword parameter.
#
#           `Tree_Name`                 - A name (with a context of `Tree_Context_Parameter`).
#
#           `Tree_Parameters_All`       - All the parameters.
#
#       Version 6:
#
#           `Tree_Normal_Parameter`     - A normal parameter.
#
#           `Tree_Map_Parameter`        - A map parameter (representing variable keywords);
#
#           `Tree_Tuple_Parameter`      - A tuple parameter (representing a variable argument list).
#
#           `Tree_Parameter_Tuple`      - More than one parameter.
#
#       Example:
#
#           The following statement:
#
#               def f(a, b, c, d = 7, e = "eight", *g, **h): pass
#
#           Verify 1:
#
#               Has the following parameters:
#
#                   `a`             - A `Tree_Name` with a context of `Tree_Context_Parameter`.
#
#                   `b`             - A `Tree_Name` with a context of `Tree_Context_Parameter`.
#
#                   `c`             - A `Tree_Name` with a context of `Tree_Context_Parameter`.
#
#                   `d = 7`         - A `Tree_Name` with a context of `Tree_Context_Parameter, representing `d`
#                                     (NOTE: The value `7` is stored separately in the `.defaults` member of
#                                     `Tree_Parameters_All`).
#
#                   `e = "eight"`   - A `Tree_Name` with a context of `Tree_Context_Parameter, representing `e`
#                                     (NOTE: The value `"eight"` is stored separately in the `.defaults` member of
#                                     `Tree_Parameters_All`).
#
#                   `a, b, c, d = 7, e = "eight", *g, **h`
#
#                                   - A `Tree_Parameters_All`, representing all the parameters.
#
#                                     It has the following four members:
#
#                                       `.normal_parameters`    - Stores `a, b, c, d, e` as a `NativeList of Tree_Name`
#                                                                 (each `Tree_Name` has a context of
#                                                                 `Tree_Context_Parameter`).
#
#                                       `.tuple_parameter`      - Stores `*g` as a `Full_Native_String`.
#
#                                       `.map_parameter`        - Stored `**h` as a `Full_Native_String`.
#
#                                       `.defaults'             - Stores `7, "eight"` as a
#                                                                 `NativeList of Tree_Value_Expression`.
#
#               In the current version, the following are *NOT* `Tree_Parameter`:
#
#                   `*g`            - Instead is a `Native_String` (stored in the `.tuple_parameters` member of
#                                     `Tree_All_Parameters`).
#
#                   `**h`           - Instead is a `Native_String` (stored in the `.map_parameters` members of
#                                     `Tree_All_Parameters`).
#
#               Why are `*g`, and `**h` *NOT* currently a `Tree_Parameter`:
#
#                   Because this version is a 1-1 emulation of `_ast`, and is exactly copying how the classes are
#                   defined there.
#
#                   The future version will not be a 1-1 emulation of `_ast`, and instead simplify all parameters to be
#                   a `Tree_Parameter`.
#
#           Future:
#
#               Will have the following parameters:
#
#                   `a`             - Will be a `Tree_Normal_Parameter`.
#
#                   `b`             - Will be a `Tree_Normal_Parameter`.
#
#                   `c`             - Will be a `Tree_Normal_Parameter`.
#
#                   `d = 7`         - Will be a `Tree_Keyword_Paramter`.
#
#                   `e = "eight"`   - Will be a `Tree_Keyword_Paramter`.
#
#                   `*g`            - Will be a `Tree_Tuple_Parameter`, representing `d` (which takes a variable
#                                     argument list
#
#                   `**h`           - Will be a `Tree_Map_Parameter`, representing `e` (which takes a variable
#                                     argument list
#
#                   `a, b, c, d = 7, e = "eight", *g, **h`
#
#                                   - A `Tree_Parameters_Many`, representing a list of all the parameters.
#
#                                     Instead of grouping them into four seperate groups like `Tree_All_Parameters`:
#
#                                       i)  the future `Tree_Parameters_Many` will simply represent them as a
#                                           list of Tree_Parameter (which each `Tree_Parameter` internally
#                                           tracking what king of parameter it is);
#
#                                       ii) Also, instead of storing `d` and `7` separately (The `d` in the
#                                           `.normal_parameters` member, and the `7` in the `.defaults` member),
#                                           they will be combined into a `Tree_Keyword_Parameter` that stores


#
#   interface Tree_Parameter
#       documentation
#           Interface to tree classes that represent parameters.
#
#       method
#           dump_parameter_tokens(f : Build_DumpToken) => void
#
#       debug
#           is_tree_keyword_parameter : boolean
#           is_tree_map_parameter     : boolean
#           is_tree_normal_parameter  : boolean
#           is_tree_parameter         := true
#           is_tree_tuple_parameter   : boolean
#
class TRAIT_Tree_Parameter(object):
    __slots__ = (())


    if __debug__:
       #@virtual
        is_tree_keyword_parameter = False

       #@virtual
        is_tree_normal_parameter = False
    
        is_tree_parameter = True



#
#   interface Tree_Parameter_0
#       documentation
#           Interface to `parser_none` or tree classes that represent parameters.
#
#       attribute
#           has_tree_parameter : boolean
#
#       if has_tree_parameter:
#           implement Tree_Parameter
#
class TRAIT_Tree_Parameter_0(object):
    __slots__ = (())

   #@virtual
    has_tree_parameter = True


    if __debug__:
        is_tree_parameter_0 = True


#
#   USAGE:
#
#       v.dump_parameter_tokens(f)                  #   Dump the tokens representing the tree parameters to `f`.
#


#
#   USAGE (debug mode):
#
#       v.is_tree_keyword_parameter                 #   Test if `v` is a [tree] keyword parameter.
#
#       v.is_tree_map_parameter                     #   Test if `v` is a [tree] map parameter.
#
#       v.is_tree_normal_parameter                  #   Test if `v` is a [tree] normal parameter.
#
#       v.is_tree_parameter                         #   Test if `v` is a `Tree_Parameter`.
#
#       v.is_tree_parameter_0                       #   Test if `v` is a `Tree_Parameter_0`.
#
#       v.is_tree_tuple_parameter                   #   Test if `v` is a [tree] tuple parameter.
#
#       assert fact_is_tree_keyword_parameter(v)    #   Assert that `v` is a [tree] keyword parameter.
#
#       assert fact_is_tree_map_parameter(v)        #   Assert that `v` is a [tree] map parameter.
#
#       assert fact_is_tree_normal_parameter(v)     #   Assert that `v` is a [tree] normal parameter.
#
#       assert fact_is_tree_parameter(v)            #   Assert that `v` is a `Tree_Parameter`.
#
#       assert fact_is_tree_parameter_0(v)          #   Assert that `v` is a `Tree_Parameter_0`.
#
#       assert fact_is_tree_tuple_parameter(v)      #   Assert that `v` is a [tree] tuple parameter.
#


#
#   fact_is_tree_normal_parameter(v) - Assert that `v` is a [tree] normal parameter
#
if __debug__:
    def fact_is_tree_normal_parameter(v):
        assert v.is_tree_normal_parameter

        return True


#
#   fact_is_tree_parameter(v) - Assert that `v` is a tree parameter.
#
if __debug__:
    def fact_is_tree_parameter(v):
        assert v.is_tree_parameter

        return True


#
#   fact_is_tree_parameter_0(v) - Assert that `v` is a `Tree_Parameter_0`
#
if __debug__:
    def fact_is_tree_parameter_0(v):
        assert v.is_tree_parameter_0

        return True
