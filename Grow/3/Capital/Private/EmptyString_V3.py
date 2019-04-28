#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.EmptyString_V3 - Private implementation of the public `String` Interface, Version 3.
#


from    Capital.Core                    import  creator
from    Capital.String                  import  TRAIT_String
from    Capital.Temporary_Key           import  TRAIT_Temporary_Key


#
#   EmptyString_V3 - An empty string.
#
#       This is a singleton, there is only one empty string named `empty_string_v3`.
#
#   NOTE:
#
#       In a boolean context evaluates to `False` (see `.__nonzero__` below).
#
class EmptyString_V3(
        str,
        TRAIT_String,
        TRAIT_Temporary_Key,
):
    __slots__ = (())


    #
    #   Interface String
    #
    is_empty_string = True
    is_full_string  = False


    #
    #   Public
    #
    #__init__    - inherited from `str.__init__`        #   Does nothing.
    #__new__     - inherited from `str.__new__`         #   Creates the new empty string.
    #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `False`.


    @staticmethod
    def __repr__():
        return "<''>"                                   #   `''` surrounded with angle brackets.


    @staticmethod
    def python_code():
        return "''"                                     #   Same as `str.__repr__("")`


@creator
def create_empty_string_v3():
    return EmptyString_V3('')


empty_string_v3 = create_empty_string_v3()
