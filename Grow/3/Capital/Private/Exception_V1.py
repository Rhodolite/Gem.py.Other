#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Exception_V1 - Implementation of exceptions for "Capital" library, Version 1.
#


#
#   Version 1.
#
#       Implements both `PREPARE_AttributeError` and `PREPARE_ValueError`, which share a lot of duplicate code.
#
#       Version 2 will eliminate this & share the code between them.
#
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


#
#   NOTE on functions named "PREPARE_*Error`".
#
#       These are the create function for `*Error` types (such as `AttributeError` and `ValueError`).
#
#       They are *NOT* called `create_*Error` since they takes different arguments than the `*Error` constructor do.
#
#       Also, in the future, they will do "special" modifications to `*Error` in python 2.*, to emulate python 3.*
#       exception chaining.
#


#
#   PREPARE_AttributeError(message, *arguments)
#
#       Prepare an `AttributeError` instance initialized with an error message consisting of `message` formatted
#       using `arguments`.
#
#   CURRENT IMPLEMENTATION:
#
#       Does not do exception chaining in python 2.*.
#
#   FUTURE:
#
#       Will emulate exception chaining in python 2.*.
#
def PREPARE_AttributeError(message, *arguments):
    if arguments:
        message = message.format(*arguments)

    error = AttributeError(message)

    trace('{} => {}', "PREPARE_AttributeError", error)

    return error


#
#   PREPARE_ValueError(message, *arguments)
#
#       Prepare an `ValueError` instance initialized with an error message consisting of `message` formatted
#       using `arguments`.
#
#   CURRENT IMPLEMENTATION:
#
#       Does not do exception chaining in python 2.*.
#
#   FUTURE:
#
#       Will emulate exception chaining in python 2.*.
#
def PREPARE_ValueError(message, *arguments):
    if arguments:
        message = message.format(*arguments)

    error = ValueError(message)

    trace('{} => {}', "PREPARE_ValueError", error)

    return error
