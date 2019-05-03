#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.FullString_V7 - Private implementation of the public `String` Interface, Version 7.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  FATAL
from    Capital.String                  import  TRAIT_String
from    Capital.Temporary_Key           import  TRAIT_Temporary_Key


#
#   FullString - A full string.
#
#       These are unique, there is only one `FullString` for each unique value.
#
#       Uniqueness is guarenteed with `conjure_string` (in "Capital.Private.ConjureString_V7").
#
#   NOTE:
#       A `FullString` is never created or constructed.
#
#       Instead a `Capital.Private.StringKey_V7.StringKey` is created, and [sometimes] transformed to a `FullString`.
#
#   NOTE:
#
#       In a boolean context evaluates to `True` (see `.__nonzero__` below).
#
class FullString(
        str,
        TRAIT_String,
        TRAIT_Temporary_Key,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL('{}: A FullString may not be created',
                  "Capital.Private.FullString_V7.FullString.operator new (`__new__`)")


    if __debug__:
        def __init__(self, s):
            FATAL('{}: A FullString may not be construted',
                  "Capital.Private.FullString_V7.FullString.constructor (`__init__`)")


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True


    #
    #   Public
    #
    #__init__    - inherited from `str.__init__`        #   Not Used.
    #__new__     - inherited from `str.__new__`         #   Not Used.
    #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


    #
    #   .__repr__ - Portraying a `FullString`
    #
    #   CURRENT
    #
    #       Surround the python code representation (i.e.: `str.__repr__`) with angle brackets.
    #
    #       Example:
    #
    #           assert __repr__(conjure_string('hello')) == "<'hello'>"
    #
    #   FUTURE
    #
    #       See `.python_code` for an explanation of how `.python_code` will behave differently in the future.
    #
    #
    def __repr__(self):
        return arrange('<{}>', self.python_code())


    #
    #   .python_code
    #
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the
    #       same characters.
    #
    #   CURRENT
    #
    #       For now, we just use the python built in `str.__repr__`.
    #
    #   FUTURE:
    #
    #       We will use the funtion `portray_python_string` which does a really good job of a python
    #       represenation (much more readable than `str.__repr__` when presented with a "raw" string).
    #
    #       However, that code is quite large, so we are not including it for now.
    #
    #       Also, really, we want to code generate the `portray_python_string` ... so will wait until the
    #       code generator can generate that function, before using it.
    #
    python_code = str.__repr__                #   `str.__repr__` implements the python representation.
