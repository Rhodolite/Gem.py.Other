#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.TemporaryString_V3 - Temporaary String Implementation, Version 3.
#


#
#   Differences between Version 1, Version 2, and Version 3.
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
#           Exists (and transformed to a `Capital.Private.String_V3.FullString`).
#


from    Capital.Core                    import  creator
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.NativeString        import  fact_is_full_INTERNED_native_string


#
#   StringKey - String Key Implementation, Version 7.
#
class TemporaryString(
        #
        #   NOTE:
        #       Due to a bug in python class assignment, we can't declare that `TemporaryString` is derived
        #       from `TRAIT_TemporaryElement` like we want to.
        #
        #       If we do, we incorrectly get the error:
        #
        #           TypeError: __class__ assignment: 'TemporaryString` object layout differs from 'FullString'
        #
        #       Actually, their object layout would not differ, it would look like this:
        #
        #           object                              object
        #             |                                   |
        #             v                                   v
        #           TRAIT_TemporaryElement              TRAIT_Tempra:
        #             |
        #             v
        #           TemporaryString
        #
        #TRAIT_TemporaryElement,        -- BUG In Python class assignment, can't declare `TRAIT_TemporaryElement` here
        #
        #   NOTE:
        #       Does *NOT* implement the String interface.
        #
        #       This is *NOT* a string, but a temporary element (that *MIGHT* be transformed to a String).
        #
):
    #
    #   `__slots__` are equivalent to the [inherited] slots of `Capital.Private.String_V3.FullString` (which an
    #   instance of this class is transformed to).
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


@creator
def create_temporary_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return TemporaryString(interned_s)
