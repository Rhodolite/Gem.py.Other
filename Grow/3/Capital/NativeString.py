#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.NativeString - Native String & methods.
#


from    Capital.System                  import  is_python_2


#
#   NativeString - A native String (i.e.: `str`)
#
NativeString = str


#
#   intern_native_string - intern a NativeString
#
if is_python_2:
    from    __builtin__                 import  intern as intern_native_string
else:
    from    sys                         import  intern as intern_native_string


#
#   strip_trailing_whitespace - strip trailing whitespace
#
strip_trailing_whitespace = NativeString.rstrip



#
#   fact_is_some_INTERNED_native_string(s) - Assert that `s` is a `str` instance that has been interned.
#
if __debug__:
    def fact_is_some_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)

        return True
