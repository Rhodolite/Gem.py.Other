#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V1 - Private implementation of the public `String` Interface, Version 1.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#
#           2.  Tracebacks due to MemoryError (out of memory);
#
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Duplicate code in `conjure_full_string` and `conjure_some_string`.
#
#       Version 2:
#
#           Helper routine `conjure_X_string` to remove duplicate code between `conjure_{full,some}_string`.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Exception               import  PREPARE_ValueError
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V1       import  create_full_string
from    Capital.Private.String_V1       import  empty_string

if __debug__:
    from    Capital.Native_String       import  fact_is_some_native_string


#
#   EXPLANATION OF VERBS
#
#       The following functions have a "verb" in their name:
#
#           conjure_some_string  - Lookup or "create & insert" a string.
#           lookup_string        - Lookup a string.
#           provide_string       - Provide a `String_V1`.
#
#       The verb "conjure" in Capital code means "lookup, and if not found, create & insert a new one".
#
#       The verb "lookup"  in Capital code means "attempt to find, and return `None` if not found".
#
#       The verb "provide" in Capital code means "lookup, and use if found; if not found -- insert".
#
#           Returns the value used (either the one found with lookup, or the one inserted).
#
#           In python code this is `dict.setdefault` ("provide" is a used as it is a clearer name than "setdefault").
#


#
#   string_cache - A cache of strings
#
#       All strings are stored in this as key/value pairs:
#
#           1)  The key   is an interned `Full_Native_String`; and
#
#           2)  The value is a `String_Leaf`.
#
string_cache = {}                       #   Map { interned Full_Native_String : String_Leaf }

lookup_string  = string_cache.get
provide_string = string_cache.setdefault


#
#   conjure_full_string(s) - Conjure a full `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
#
#       `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
#   EXCEPTIONS
#
#       If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
#   SEE ALSO
#
#       Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
#       versions.
#
@export
@creator
def conjure_full_string(s):
    #
    #   The following test is "*_some_*" on purpose.
    #
    #   This is to allow the case of an empty string to be handled belows a `ValueError` (instead of in the assert).
    #
    assert fact_is_some_native_string(s)

    r = lookup_string(s)

    if r is not None:
        return r

    #
    #   Handle an empty string here (even in release mode).
    #
    #       Hence the assert above is "*_some_*" on purpose, so this code can catch the empty strings instead of the
    #       assert.
    #
    if len(s) == 0:
        value_error = PREPARE_ValueError(
                "parameter `s` is empty; `{}` requires a non-empty string; (i.e.: has a length greater than 0)",
                'conjure_full_string',
            )

        raise value_error

    interned_s = intern_native_string(s)

    string__possibly_non_unique = create_full_string(interned_s)

    #
    #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
    #   `String_Leaf` that is stored in `string_cache).
    #
    return provide_string(interned_s, string__possibly_non_unique)


#
#   conjure_some_string(s) - Conjure a `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
#
#       `s` must be of a `Some_Native_String` (i.e.: `str`).
#
#       `s` may *NOT* be an instance of a subclass of `Some_Native_String` (i.e.: `str`).
#
@export
@creator
def conjure_some_string(s):
    assert fact_is_some_native_string(s)

    r = lookup_string(s)

    if r is not None:
        return r

    #
    #   NOTE:
    #
    #       The next two lines are the only code difference between `conjure_full_string` and `conjure_some_string`.
    #
    if len(s) == 0:
        return empty_string

    interned_s = intern_native_string(s)

    string__possibly_non_unique = create_full_string(interned_s)

    #
    #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
    #   `String_Leaf` that is stored in `string_cache).
    #
    return provide_string(interned_s, string__possibly_non_unique)
