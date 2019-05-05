#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V3 - Private implementation of `conjure_string` for `String` Interface, Version 3.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique.
#


#
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           1)  Producer function `produce_conjure_string` to produce `conjure_string` functions.
#
#           2)  Give the producer function `produce_conjure_string` the following two arguments:
#
#                   2A)     `Capital.Private.String_V2.empty_string`, and
#
#                   2B)     `Capital.Private.String_V2.create_full_string`.
#
#       Version 3:
#
#           1)  Use the same producer function as in version 2
#               (i.e.: `Capital.Private.ConjureString_V2.produce_conjure_string`).
#
#           2)  Give the producer function `produce_conjure_string` the following two arguments:
#
#                   2A)     `Capital.Private.String_V3.empty_string`, and
#
#                   2B)     `Capital.Private.String_V3.create_full_string`.
#
#               (i.e.: The "_V3*" versions of `empty_string` and `create_full_string`).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Fact                    import  fact_is_some_native_string
from    Capital.Core                    import  trace
from    Capital.NativeString            import  intern_native_string
from    Capital.Private.String_V1       import  create_full_string
from    Capital.Private.String_V1       import  empty_string


#
#   EXPLANATION OF VERBS
#
#       The following functions have a "verb" in their name:
#
#           conjure_string       - Lookup or "create & insert" a string.
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
#   produce_conjure_string(empty_string, create_string) - Produce a `conjure_string(s)` function.
#
#       Produced `conjure_string(s)` - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#           `s` must be of type `SomeNativeString` (i.e.: `str` or a subclass derived from `str`).
#
#           Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
#           version.s
#
def produce_conjure_string(empty_String, create_full_string):
    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key   is an interned `NativeString`; and
    #           2)  The value is a `String`.
    #
    #       The type of `string_cache` is `Map { interned NativeString } of String`
    #
    #       The cache is initialized with `empty_string`, to make sure that `empty_string` is returned uniquely
    #       when the `conjure_string("")` is called.
    #
    string_cache = { intern_native_string("") : empty_string }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
    #
    #       `s` must be of type `SomeNativeString` (i.e.: `str` or a subclass derived from `str`).
    #
    #       Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
    #       version.s
    #
    @creator
    def conjure_string(s):
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            return r

        interned_s = intern_native_string(s)

        string__possibly_non_unique = create_full_string(interned_s)

        #
        #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
        #   `String_V1` that is stored in `string_cache).
        #
        return provide_string(interned_s, string__possibly_non_unique)


   #trace('produce_conjure_string({!r}, <function {}>)', empty_string, create_full_string.__name__)

    return conjure_string


conjure_string = produce_conjure_string(empty_string, create_full_string)


export(conjure_string)
