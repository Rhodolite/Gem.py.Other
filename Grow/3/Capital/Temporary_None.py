#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_None - Temporary None (for use as second argument to "lookup" functions).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


#
#   StringKey - String Key Implementation, Version 5.
#
class Temporary_None(
        TRAIT_Maybe_Temporary_0,
):
    __slots__ = (())


    #
    #   Interface Maybe_Temporary
    #
   #@replace
    definitively_not_temporary = False


    #
    #   Technically, the `.__nonzero__` method should be as follows:
    #
    #       @staticmethod
    #       def __nonzero__():
    #           return False
    #
    #   However, since `temporary_none` is only a sentinel used in "lookup" functions, we never use it in a boolean
    #   context, and hence we don't need a `.__nonzero__` method.
    #


    #
    #   Public
    #
    @staticmethod
    def __repr__(self):
        return '<Temporary_None>'


@creator
def create_temporary_none():
    return Temporary_None()


temporary_none = create_temporary_none()


#
#   temporary_none - sentinel to use as second argument to "lookup" functions.
#
export(temporary_none)
