#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.BuiltIn - A wrapper around python `builtins` module (known as `__builtin__` in Python 2.*)
#


#
#   Python_BuiltIn - The python `builtins` module (known as `__builtin__` in Python 2.*)
#
if 0:
    #
    #   DISABLED
    #       This code is temporarily disabled, as we, currently, do not actually need to use `Python_BuiltIn`.
    #
    #       The code is left here for educational reasons:
    #
    #           1.  Show how to import `Python_BuiltIn`; and
    #
    #           2.  We will probably need `Python_BuiltIn` in the future -- so keeping this code around for then.
    #
    from    Z.System                        import  is_python_2


    if is_python_2:
        import  __builtin__ as  Python_BuiltIn  #   The python "built-in" module is named `__builtin__` in Python 2.*
    else:
        import  builtins    as  Python_BuiltIn  #   The python "built-in" module is named `builtins` in Python 3.*


#
#   NOTE:
#       `Python_Type` should be imported from "Capital.Types", which, internally, imports it from this file.
#
#       For everyone else, `Python_Type` should *NOT* be imported from this file.
#
#       The only reason it in in this file, is because, logically, `type` comes from `Python_BUiltIn`.
#

#
#   Python_Type - The base type (metaclass) of all classes and types.
#
#       ===  About `type` .vs. `Python_Type`  ===
#
#           In python, the builtin `type` is a type (the base metaclass of all classes and types).
#
#           When called with three arguments, as a normal constructor, it constructs a new type.
#
#           However, when `type` is called with one argument, it instead behaves as if it was a function, returning the
#           type of it's first argument.
#
#           To distinguish between these two cases, in Capital code, the following is always used:
#
#               `type`          - A function that returns the python type of something.
#               `Python_Type`   - The base type (metaclass) of all classes and types.
#
#           Obviously, `Python_Type` is mapped to the python builtin `type` (done below).
#
#       REASON:
#
#           It is already confusing enough that `Python_Type` is "The base type (metaclass) of all classes and types"
#           (Including, of course, itself; i.e.:
#
#               1.  The metaclass of `Python_Type` is `Python_Type;
#
#               2.  that is: `Python_Type` is it's own metaclass).
#
#           We are working to avoid, some of that confusion, by making a clear distinction between `type` (used as
#           a function) and `Python_Type` (used as a type).
#
#           Thus instead of the very confusing statement:
#
#               assert type(type) is type                       #   Very confusing -- Don't do this!
#
#           We can say the slightly less confusing statement:
#
#               assert type(Python_Type) is Python_Type         #   Slightly less confusing.
#
#       EXAMPLE:
#
#           Example (see the fuller assertion below):
#
#               assert type(Python_Type) is Python_Type
#
#           Here we are taking the type of `Python_Type` and verifying it is a `Python_Type` instance (in other
#           words verifying that `Python_Type` is a class -- like all classes it's base metaclass will be
#           `Python_Type`).
#
#           Thus we are using the two different meanings (`type` .vs. `Python_Type`) of the underlying
#           python builtin `type` in a single asserttion.
#
#   NOTE:
#       The assertion below are included, not for code purposes, but as educational assertions, that clearly and
#       concisely shows that `Python_Type` is "The base type (metaclass) of all classes and types".
#
Python_Type = type                      #   The base type (metaclass) of all classes and types.


#
#   Simple assertions ...
#
assert type(0)           is int         #   The type of `0` is an integer.
assert type(int)         is Python_Type #   The type of integer is `Python_Type`.
assert type(Python_Type) is Python_Type #   The type of `Python_type` is `Python_Type`.


#
#   Slightly more complicated assertion ...
#
#       The type of any type (`bool`, `int`, `object`, `str`, etc) is `Python_Type`, (including of course, the type of
#       `Python_Type` is `Python_Type`).
#
assert type(bool) is type(int) is type(object) is type(str) is type(Python_Type) is Python_Type