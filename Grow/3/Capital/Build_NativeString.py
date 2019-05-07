#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Build_NativeString - Build a `Some_Native_String`
#


from    Capital.Core                    import  creator
from    Capital.System                  import  is_python_2


if is_python_2:
    from    cStringIO                   import  StringIO
else:
    from    _io                         import  StringIO


#
#   NOTE:
#       In python `StringIO` does both string input and string output.
#
#       We name it `build_native_string` to indicate we are only using string output (considering this very different from
#       string input).
#
@creator
def build_native_string():
    return StringIO()
