#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_String - Native String & methods.
#


from    Capital.System                  import  is_python_2


#
#   Empty_Native_String - An empty native string (i.e.: `str` that has 0 characaters).
#
Empty_Native_String = str


#
#   Full_Native_String - A full native string (i.e.: `str` that has at least 1 characater).
#
Full_Native_String = str


#
#   NativeString - A native string (i.e.: `str`)
#
NativeString = str


#
#   Some_Native_String - A native string (i.e.: `str`).
#
Some_Native_String = str


#
#   intern_native_string - intern a `Some_Native_String` (i.e.: `str`).
#
if is_python_2:
    from    __builtin__                 import  intern as intern_native_string
else:
    from    sys                         import  intern as intern_native_string


#
#   strip_trailing_whitespace - strip trailing whitespace
#
strip_trailing_whitespace = Some_Native_String.rstrip


#
#   native_string__lookup_index__OR__MINUS_1(s, sub) - Look for `sub` in `s`.  Return `-1` on failure.
#
native_string__lookup_index__OR__MINUS_1 = Some_Native_String.find


#
#   fact_is_empty_INTERNED_native_string(s)
#
#       Assert that `s` is a `str` instance that has been interned, and is empty (i.e.: is the string `""`).
#
if __debug__:
    def fact_is_empty_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)
        assert len(s)  == 0

        return True


#
#   fact_is_full_INTERNED_native_string(s)
#
#       Assert that `s` is a `str` instance that has been interned, and is "full" (i.e.: has a length greater than 0).
#
if __debug__:
    def fact_is_full_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)
        assert len(s)  > 0

        return True


#
#   fact_is_some_INTERNED_native_string(s) - Assert that `s` is a `str` instance that has been interned.
#
if __debug__:
    def fact_is_some_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)

        return True
