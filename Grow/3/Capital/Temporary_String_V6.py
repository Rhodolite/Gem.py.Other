#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_String_V6 - Temporary String Implementation, Version 6.
#


#
#   Differences between Versions 1..6
#
#       Version 1..2:
#
#           Do not exist (not used to transform to `Capital.Private.String_V{1,2}.String_Leaf`).
#
#       Version 3..5:
#
#           Do not exist (not used to transform to `Capital.Private.String_V{3,4,5}.Full_String`)
#
#       Version 6:
#
#           Exists (and transformed to a `Capital.Private.String_V6.Full_String`).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Temporary_Element


if __debug__:
    from    Capital.Native_String       import  fact_is_full_INTERNED_native_string


#
#   StringKey - String Key Implementation, Version 5.
#
class Temporary_String(
        TRAIT_Temporary_Element,
        #
        #   NOTE:
        #       Does *NOT* implement the String interface.
        #
        #       This is *NOT* a string, but a temporary element (that *MIGHT* be transformed to a String).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.String_V6.Full_String` (which an instance of this
    #   class is transformed to).
    #
    __slots__ = ((
        'interned_s',                   #   Full_Native_String
    ))


    #
    #   Private
    #
    def __init__(self, interned_s):
        self.interned_s = interned_s


    #
    #   Interface Maybe_Temporary
    #
   #@replace
    temporary_element_has_definitively_been_transformed = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Temporary_String {!r}>', repr(self.interned_s))


@export
@creator
def create_temporary_string(interned_s):
    assert fact_is_full_INTERNED_native_string(interned_s)

    return Temporary_String(interned_s)
