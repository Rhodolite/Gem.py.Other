#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Python_Exceptions_Module    -   This is named `Python_Exceptions_Module` instead of `Python_Exceptions` to
    #                                   avoid confusion with `Python_Exception` (an exception)
    #
    Python_Exceptions_Module = (__import__('exceptions')   if is_python_2 else  Python_BuiltIn)


    #
    #   Python Types
    #
    Python_AttributeError = Python_Exceptions_Module.AttributeError
    Python_Exception      = Python_Exceptions_Module.Exception
    Python_RuntimeError   = Python_Exceptions_Module.RuntimeError
    Python_ValueError     = Python_Exceptions_Module.ValueError


    #
    #   PREPARE_*Error
    #
    #   NOTE:
    #       These are the create function for `Python_*Error`.
    #
    #       They are *NOT* called `create_*Error` since they takes different arguments than the `*Error` constructor
    #       do.
    #
    #       Also, in the future, they will do "special" modifications to `*Error` in python 2.*, to emulate
    #       python 3.* exception chaining.
    #


    #
    #   produce_PREPARE_Exception
    #
    #   NOTE:
    #       Defined in "Crystal/Share.py"
    #


    #
    #   PREPARE_AttributeError
    #
    PREPARE_AttributeError = produce_PREPARE_Exception('PREPARE_AttributeError', Python_AttributeError)


    #
    #   PREPARE_NameError
    #
    #   NOTE:
    #       Defined in "Crystal/Share.py"
    #


    #
    #   PREPARE_RuntimeError
    #   PREPARE_ValueError
    #
    PREPARE_RuntimeError = produce_PREPARE_Exception('PREPARE_RuntimeError', Python_RuntimeError)
    PREPARE_ValueError   = produce_PREPARE_Exception('PREPARE_ValueError',   Python_ValueError)


    #
    #   share
    #
    share(
            #
            #   Python Types
            #
            Python_AttributeError = Python_AttributeError,
            Python_Exception      = Python_Exception,

            #
            #   Our functions
            #
            #   NOTE:
            #       Have to use keywords, since in release mode, the functions will all be [internally] named
            #       `PREPARE_Exception`
            #
            #
            PREPARE_AttributeError = PREPARE_AttributeError,
            PREPARE_RuntimeError   = PREPARE_RuntimeError,
            PREPARE_ValueError     = PREPARE_ValueError,
        )
