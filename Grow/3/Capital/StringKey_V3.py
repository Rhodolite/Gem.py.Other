#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.StringKey_V3 - String Key Implementation, Version 1.
#


from    Capital.Temporary_Key           import  TRAIT_Temporary_Key


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   StringKey_V3 - String Key Implementation, Version 1.
#
native_string_representation_method = str.__repr__


class StringKey_V3(
        str,
        TRAIT_Temporary_Key,
        #
        #   NOTE:
        #       Does *NOT* implement the String interface.
        #
        #       This is *NOT* a string, but a string key (that *MIGHT* be transformed to a String).
        #
):
    __slots__ = (())


    #
    #   Interface Temporary_Key
    #
   #@replace
    temporary_key_has_definitively_been_transformed = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<StringKey_V3 {}>', native_string_representation_method(self))


def create_string_key_v3(s):
    assert fact_is_full_native_string(s)

    return StringKey_V3(s)
