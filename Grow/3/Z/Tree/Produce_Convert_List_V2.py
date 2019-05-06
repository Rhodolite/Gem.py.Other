#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Produce_Convert_List_V2 - Produce a `convert full_list of Native_AbstractSyntaxTree_*` function, Version 2.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All convert functions take a `z` parameter of type `Convert_Zone.
#


if __debug__:
    from    Capital.Fact                    import  fact_is_full_native_list
    from    Capital.Fact                    import  fact_is_some_native_list
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert)
#
#       Produce a `convert full_list of Native_AbstractSyntaxTree_*` function.
#
#       Produces: `convert__full_list_of__Native_AbstractSyntaxTree_STAR(sequence)`
#
#           Converts a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.*`) to a
#           `FullNativeList of Tree_*`.
#
def produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert):
    #
    #   convert__full_list_of__Native_AbstractSyntaxTree_STAR(z, sequence)
    #
    #       Convert a `FullNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.*`) to a
    #       `FullNativeList of Tree_*`.
    #
    def convert__full_list_of__Native_AbstractSyntaxTree_STAR(z, sequence):
        assert fact_is_convert_zone    (z)
        assert fact_is_full_native_list(sequence)

        return [convert(z, v)   for v in sequence]


    return convert__full_list_of__Native_AbstractSyntaxTree_STAR


#
#   produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert)
#
#       Produce a `convert some_list of Native_AbstractSyntaxTree_*` function.
#
#       Produces: `convert__some_list_of__Native_AbstractSyntaxTree_STAR(z, sequence)`
#
#           Converts a `SomeNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.*`) to a
#           `SomeNativeList of Tree_*`.
#
def produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert):
    #
    #
    #   convert__some_list_of__Native_AbstractSyntaxTree_STAR(sequence)
    #
    #       Convert a `SomeNativeList of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.*`) to a
    #       `SomeNativeList of Tree_*`.
    #
    def convert__some_list_of__Native_AbstractSyntaxTree_STAR(z, sequence):
        assert fact_is_convert_zone    (z)
        assert fact_is_some_native_list(sequence)

        return [convert(z, v)   for v in sequence]


    return convert__some_list_of__Native_AbstractSyntaxTree_STAR
