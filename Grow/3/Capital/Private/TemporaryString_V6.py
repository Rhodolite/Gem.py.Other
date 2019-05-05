#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.TemporaryString_V6 - Temporaary String Implementation, Version 6.
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
#           String classes use `NativeString` as their base class.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.NativeString            import  NativeString
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   method__NativeString__representation - The python implemention of `repr` for `str` (i.e.: `str.__repr__`).
#
method__NativeString__representation = NativeString.__repr__


#
#   StringKey - String Key Implementation, Version 6.
#
class TemporaryString(
        NativeString,
        TRAIT_TemporaryElement,
        #
        #   NOTE:
        #       Does *NOT* implement the String interface.
        #
        #       This is *NOT* a string, but a temporary element (that *MIGHT* be transformed to a String).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.String_V6.FullString` (which an instance of this
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
        return arrange('<TemporaryString {!r}>', method__NativeString__representation(self))


@export
@creator
def create_temporary_string(s):
    assert fact_is_full_native_string(s)

    return TemporaryString(s)
