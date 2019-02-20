#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.BuiltIn - A wrapper around python `__builtin__` module (known as `builtins` in Python 3.*)
#
from    Z.System                        import  is_python_2


if is_python_2:
    import  __builtin__ as  Python_BuiltIn      #   The python "built-in" module is named `__builtin__` in Python 2.*
else:
    import  builtins    as  Python_BuiltIn      #   The python "built-in" module is named `builtins` in Python 3.*


#
#   Python Types
#
#       All python types are renamed to `Python_*` to make it clear these are
#       python types we are using.
#
#       This is important, since we will, eventually, need to create our own
#       types, that are fully compatiable with all the languages we will translate
#       to.
#
#       Thus any use of `Python_*` in code that is translated to multiple language (most of
#       the future code) will eventually need to go through a wrapper that in Python translated
#       to `Python_*`, but in other languages translates to something else.
#
Python_Integer  = Python_BuiltIn.int
Python_List     = Python_BuiltIn.list
Python_Object   = Python_BuiltIn.object
Python_String   = Python_BuiltIn.str
Python_Tuple    = Python_BuiltIn.tuple
#Python_Type    = Python_BuiltIn.type                #   See the comment below on `python_type` .vs. `Python_Type`


#
#   Python Functions
#
#       All python functions are renamed to `python_*` to make it clear these are
#       python functions we are using.
#
python_compile = Python_BuiltIn.compile
python_length  = Python_BuiltIn.len
#python_type   = Python_BuiltIn.type                #   See the comment below on `python_type` .vs. `Python_Type`


#
#   Python Values
#
#       All python values are renamed to `python_*` to make it clear these are
#       python values we are using.
#
python_debug_mode = Python_BuiltIn.__debug__
python_true       = True                            #   Python 3.* keyword
python_false      = False                           #   Python 3.* keyword
python_none       = None                            #   Python 3.* keyword


#
#   ===  About `python_type` .vs. `Python_Type`  ===
#
#       In python, the builtin `type` is a type (the base metaclass of all
#       classes and types).
#
#       When called with three arguments, as a normal constructor, it
#       constructs a new type.
#
#       However, when `type` is called with one argument, it instead behaves as
#       a function, returning the type of it's first argument.
#
#       To distinguish between these two cases, in Z code, the following is
#       used:
#
#           `python_type` - A function that returns the python type of something.
#           `Python_Type` - A type (the base metaclass of all classes and types).
#
#       Both `python_type` and `Python_Type` are mapped to the python builtin
#       `type`.
#
#   Example:
#
#       assert python_is_instance(python_type(classification), Python_Type)
#
#   Here we are taking the python type of `classification` and verifying it is
#   an instance of `Python_Type` (in other words verifying that
#   `classification` is a class -- like all classes it's base metaclass will
#   be `Python_Type`).
#
#   Thus we are using the two different meanings (`python_type` .vs.
#   `Python_Type`) of the underlying python `type` in a single asserttion.
#
python_type = Python_BuiltIn.type           #   Really a type, but used as if a function
Python_Type = Python_BuiltIn.type           #   The base type (metaclass) of all classes and types.


#
#   Python_NoneType - The type of `python_none` (i.e.: `none`).
#
Python_NoneType = python_type(python_none)
