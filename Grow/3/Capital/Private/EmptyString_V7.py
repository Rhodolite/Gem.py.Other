#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.EmptyString_V7 - Private implementation of the public `String` Interface, Version 3.
#


from    Capital.Core                    import  creator
from    Capital.String                  import  TRAIT_String
from    Capital.TemporaryElement        import  TRAIT_TemporaryElement


#
#   EmptyString - An empty string.
#
#       This is a singleton, there is only one empty string named `empty_string`.
#
#   NOTE:
#
#       In a boolean context evaluates to `False` (see `.__nonzero__` below).
#
class EmptyString(
        str,
        TRAIT_String,
        TRAIT_TemporaryElement,
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
def create_empty_string():
    return EmptyString('')


empty_string = create_empty_string()
