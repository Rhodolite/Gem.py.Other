#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Types - Types used, or exported, by the Capital module.
#


import  types                           #   python `types` module.


#
#   NoneType - The type of python `None`.
#
NoneType = types.NoneType               #   The type of python `None`.

assert type(None) is NoneType


#
#   BoundMethod - An instance bound to a method
#
BoundMethod = types.MethodType

assert BoundMethod.__name__ == 'instancemethod'


#
#   Native_Built_In_Function
#
Native_Built_In_Method = types.BuiltinMethodType


#
#   Native_Function - A native function (i.e.: `types.FunctionType`).
#
Native_Function = types.FunctionType


#
#   Python_Type - The base type (metaclass) of all classes and types.
#
#       See comments in "Capital/Python_Type.py" that explains how we use `type` .vs. `Python_Type`.
#
#   NOTE:
#       The assertion below is COPIED from "Capital/Python_Type.py".
#
#       It is included here, not for code purposes, but as an educational assertion, that clearly and concisely shows
#       that `Python_Type` is "The base type (metaclass) of all classes and types".
#
from    Capital.Python_Type             import  Python_Type

assert type(bool) is type(int) is type(object) is type(str) is type(Python_Type) is Python_Type


#
#   Delete `Capital.Python_Type` and `sys.modules["Python_Type"]` as we don't need either of them again.
#
#       Other modules should import `Python_Type` as follows:
#
#           from    Capital.Types           import  Python_Type
#
import  Capital
import  sys


del Capital.Python_Type, sys.modules['Capital.Python_Type']
del Capital, sys
