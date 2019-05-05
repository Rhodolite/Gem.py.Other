#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.TemporaryString_V5 - Temporaary String Implementation, Version 5.
#


#
#   Differences between Version 1, Version 2, Version 3, Version 4, and Version 5.
#
#       Version 1:
#
#           Does not exist (not used to transform to `Capital.Private.String_V1.String_V1`).
#
#       Version 2:
#
#           Does not exist (not used to transform to `Capital.Private.String_V2.FullString`)
#
#       Version 3:
#
#           Does not exist (not used to transform to `Capital.Private.String_V3.FullString`)
#
#       Version 4:
#
#           Does not exist (not used to transform to `Capital.Private.String_V5.FullString`)
#
#       Version 5:
#
#           Exists (and transformed to a `Capital.Private.String_V5.FullString`).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.NativeString        import  fact_is_full_INTERNED_native_string


#
#   StringKey - String Key Implementation, Version 5.
#
class TemporaryString(
        TRAIT_TemporaryElement,
        #
        #   NOTE:
        #       Does *NOT* implement the String interface.
        #
        #       This is *NOT* a string, but a temporary element (that *MIGHT* be transformed to a String).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.String_V5.FullString` (which an instance of this
    #   class is transformed to).
    #
    __slots__ = ((
        'interned_s',                   #   FullNativeString
    ))


    #
    #   Private
    #
    def __init__(self, interned_s):
        self.interned_s = interned_s


    #
    #   Interface TemporaryElement
    #
   #@replace
    temporary_element_has_definitively_been_transformed = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<TemporaryString {!r}>', repr(self.interned_s))


@export
@creator
def create_temporary_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return TemporaryString(interned_s)
