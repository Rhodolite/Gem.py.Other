#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Native_String - Native String & methods.
#


from    Capital.System                  import  is_python_2


#
#   Empty_Native_String - An empty native string (i.e.: `str` that has a length of 0).
#
Empty_Native_String = str


#
#   Full_Native_String - A full native string (i.e.: `str` that has a length greater than 0).
#
Full_Native_String = str


#
#   Native_String - A native string (i.e.: `str`).  Either empty or full.
#
Native_String = str


#
#   intern_native_string - intern a `Native_String` (i.e.: `str`).
#
if is_python_2:
    from    __builtin__                 import  intern as intern_native_string
else:
    from    sys                         import  intern as intern_native_string


#
#   strip_trailing_whitespace - strip trailing whitespace
#
strip_trailing_whitespace = Native_String.rstrip


#
#   native_string__lookup_index__OR__MINUS_1(s, sub) - Look for `sub` in `s`.  Return `-1` on failure.
#
native_string__lookup_index__OR__MINUS_1 = Native_String.find


#
#   fact_is_empty_native_string(s)
#
#       Assert that `s` is a *DIRECT* `str` instance, and is "empty" (i.e.: has a length of 0).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_empty_native_string(s):
        assert type(s) is str
        assert len(s) == 0

        return True


#
#   fact_is_empty_INTERNED_native_string(s)
#
#       Assert that `s` is a *DIRECT* `str` instance that has been interned, and is empty (i.e.: is the string `""`).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
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
#       Assert that `s` is a *DIRECT* `str` instance that has been interned, and is "full" (i.e.: has a length greater
#       than 0).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_full_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)
        assert len(s)  > 0

        return True


#
#   fact_is_full_native_string(s)
#
#       Assert that `s` is a *DIRECT* `str` instance, and is "full" (i.e.: has a length greater than 0).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is_full_native_string(s):
        assert type(s) is str
        assert len(s) > 0

        return True


#
#   fact_is_native_string(s)
#
#       Assert that `s` is a *DIRECT* `Native_String` (i.e.: `str`) instance.
#
#       `s` may *NOT* be an instance of a subclass of `Native_String` (i.e.: `str`).
#
if __debug__:
    def fact_is_native_string(s):
        assert type(s) is str

        return True


#
#   fact_is__native_none__OR__full_native_string(s)
#
#       Assert that `s` is either:
#
#           1)  `NONE`; OR
#
#           2)  a *DIRECT* `str` instance, and is "full" (i.e.: has a length greater than 0).
#
#               `s` may *NOT* be an instance of a subclass of `str`.
#
if __debug__:
    def fact_is__native_none__OR__full_native_string(s):
        if s is None:
            return True

        assert type(s) is str
        assert len(s) > 0

        return True


#
#   fact_is_some_INTERNED_native_string(s) - Assert that `s` is a `str` instance that has been interned.
#
if __debug__:
    def fact_is_some_INTERNED_native_string(s):
        assert type(s) is str
        assert s       is intern_native_string(s)

        return True
