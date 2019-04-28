#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.FullString_3 - Private implementation of the public `String` Interface, Version 3.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  FATAL


#
#   FullString_V3 - A full string.
#
#       These are unique, there is only one `FullString_V3` for each unique value.
#
#       Uniqueness is guarenteed with `conjure_string_v3`.
#
#   NOTE:
#       A `FullString_V3` is never created or constructed.
#
#       Instead a `StringKey_V3` is created, and [sometimes] transformed to a `FullString_V3`.
#
#   NOTE:
#
#       In a boolean context evaluates to `True` (see `.__nonzero__` below).
#
class FullString_V3(str):
    #
    #   implements Temporary_Key,
    #              String
    #
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL("FullString_V3.operator new (`__new__`): A FullString_V3 may not be created");


    if __debug__:
        def __init__(self, s):
            FATAL("FullString_V3.constructor (`__init__`): A FullString_V3 may not be contructed");


    #
    #   Interface Temporary_Key
    #
    temporary_key_has_definitively_been_transformed = True


    #
    #   Interface String
    #
    is_empty_string = False
    is_full_string  = True

    if __debug__:
        is_some_string = True


    #__init__    - inherited from `str.__init__`        #   Not Used.
    #__new__     - inherited from `str.__new__`         #   Not Used.
    #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


    #
    #   .__repr__ - Portraying a `FullString_V3`
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
