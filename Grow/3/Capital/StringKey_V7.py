#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.StringKey_V7 - String Key Implementation, Version 1.
#


from    Capital.Core                    import  creator
from    Capital.Temporary_Key           import  TRAIT_Temporary_Key


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   native_string_representation_method - NativeString implementation of `__repr__`.
#
native_string_representation_method = str.__repr__


#
#   StringKey - String Key Implementation, Version 7.
#
class StringKey(
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
        return arrange('<StringKey {}>', native_string_representation_method(self))


@creator
def create_string_key(s):
    assert fact_is_full_native_string(s)

    return StringKey(s)
