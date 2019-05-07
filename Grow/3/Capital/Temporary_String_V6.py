#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_String_V6 - Temporary String Implementation, Version 6.
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           String classes use `object` as their base class.
#
#       Version 6:
#
#           String classes use `Some_Native_String` (i.e.: `str`) as their base class.
#
#           (although some string classes use `Full_Native_String` (also: `str`) as their base class,
#           to indicate they only handle "full" strings).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_String           import  Full_Native_String
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   method__Full_Native_String__representation - The python implemention of `repr` for `str` (i.e.: `str.__repr__`).
#
method__Full_Native_String__representation = Full_Native_String.__repr__


#
#   Temporary_String - Temporary String Implementation, Version 6.
#
class Temporary_String(
        Full_Native_String,
        TRAIT_TemporaryElement,
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
    __slots__ = (())


    #
    #   Interface TemporaryElement
    #
   #@replace
    temporary_element_has_definitively_been_transformed = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Temporary_String {!r}>', method__Full_Native_String__representation(self))


@export
@creator
def create_temporary_string(s):
    assert fact_is_full_native_string(s)

    return Temporary_String(s)
