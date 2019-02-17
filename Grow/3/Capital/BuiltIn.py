#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.BuiltIn - A wrapper around python `builtins` module (known as `__builtin__` in Python 2.*)
#


#
#   Python_BuiltIn - The python `builtins` module (known as `__builtin__` in Python 2.*)
#


from    Capital.System                  import  is_python_2


if is_python_2:
    import  __builtin__ as  Python_BuiltIn  #   The python "built-in" module is named `__builtin__` in Python 2.*
else:
    import  builtins    as  Python_BuiltIn  #   The python "built-in" module is named `builtins` in Python 3.*


#
#   iterate(v) - create an iterator for `v`
#
iterate = Python_BuiltIn.iter
