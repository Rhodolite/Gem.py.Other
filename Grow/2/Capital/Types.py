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
#   Python_Type - The base type (metaclass) of all classes and types.
#
#       See comments in "Capital/BuiltIn.py" that explains how we use `type` .vs. `Python_Type`.
#
#   NOTE:
#       The assertion below is COPIED from "Capital/BuiltIn.py".
#
#       It is included here, not for code purposes, but as an educational assertion, that clearly and concisely shows
#       that `Python_Type` is "The base type (metaclass) of all classes and types".
#
from    Capital.BuiltIn                 import  Python_Type

assert type(bool) is type(int) is type(object) is type(str) is type(Python_Type) is Python_Type
