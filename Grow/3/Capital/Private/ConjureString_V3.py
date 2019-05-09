#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V3
#
#       Private implementation of `conjure_some_string` for `String` Interface, Version 3.
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
#   Difference between Version 2 & Version 3
#
#       Version 2:
#
#           Implementation of creator function `conjure_some_string`.
#
#       Version 3:
#
#           Producer function `produce_conjure_string` to produce `conjure_some_string` functions.
#
#           The initially created `conjure_some_string` is identical to
#           `Capital.Private.ConjureString_V1.conjure_some_string` (the only internal difference is using a closure for
#           variables instead of global variables).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Core                    import  trace
from    Capital.Exception               import  PREPARE_ValueError
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V3       import  create_full_string
from    Capital.Private.String_V3       import  empty_string


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_native_function
    from    Capital.Fact                import  fact_is_not_native_none
    from    Capital.Native_String       import  fact_is_some_native_string
    from    Capital.Native_String       import  fact_is__native_none__OR__full_native_string


#
#   EXPLANATION OF VERBS
#
#       The following functions have a "verb" in their name:
#
#           conjure_some_string  - Lookup or "create & insert" a string.
#           lookup_string        - Lookup a string.
#           provide_string       - Provide a `String_Leaf`.
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
#   produce_conjure_string_functions(
#           empty_string,
#           create_full_string,
#
#           make_conjure_full_string = True,
#           make_conjure_some_string = True,
#   )
#
#       Produce 1 or 2 conjure string functions (see below for details).
#
#       Parameters:
#
#           1)  `empty_string` - The singleton to return when the user attemps to conjure an empty string.
#
#               (if `make_conjure_some_string is `False`, then `empty_string` must be `None`).
#
#           2)  `create_full_string` - The function to create a full string.
#
#           3)  `make_conjure_full_string` - Must be `True`; will always produce a `conjure_full_string` function.
#
#           4)  `make_conjure_some_string` - Set to `True` if a `conjure_some_string` should be produced.
#
#
#       Produced function(s):
#
#           1)  `conjure_full_string(s)` - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#                   `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#                   `s` may *NOT* be an instance of a subclass of `str`.
#
#               EXCEPTIONS
#
#                   If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
#               SEE ALSO
#
#                   Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in
#                   future versions.
#
#
#           2)  `conjure_some_string(s)` - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#                   `s` must be of a `Some_Native_String` (i.e.: `str`).
#
#                   `s` may *NOT* be an instance of a subclass of `Some_Native_String` (i.e.: `str`).
#
#
#       Returns a tuple:
#
#           1)  If `not make_conjure_some_string`:
#
#                   Returns a tuple of 1 element:
#
#                       ((conjure_string_full,))
#
#           2)  If `make_conjure_some_string`:
#
#                   Returns a tuple of 2 elements:
#
#                       ((conjure_string_full, conjure_some_string))
#
#   NOTE:
#       This is a single function to produce two function, so they can share the following "cell" variables:
#
#           A)  `lookup_string`;
#
#           B)  `provide_string`.
#
#       This means both produced functions share the same cache (i.e.: `string_cache`).
#
#       See "Capital.Private.Execption_V2.py" for an explanation of "closure", "cell variable", "free variable", and
#       "produce" functions.
#
@export
def produce_conjure_string_functions(
        empty_string,
        create_full_string,

        make_conjure_full_string = True,
        make_conjure_some_string = True,
):
    if make_conjure_full_string:
        assert fact_is_not_native_none(empty_string)
    else:
        assert fact_is_native_none    (empty_string)

    assert fact_is_native_function    (create_full_string)
    assert fact_is_native_boolean     (make_conjure_full_string)
    assert fact_is_native_boolean     (make_conjure_some_string)

    assert make_conjure_full_string is True

    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is an interned `Some_Native_String`; and
    #
    #           2)  The value is a `String`.
    #
    #       The type of `string_cache` is `Map { interned Some_Native_String } of String`
    #
    #       The cache is initialized with `empty_string`, to make sure that `empty_string` is returned uniquely
    #       when the `conjure_some_string("")` is called.
    #
    #   As mentioned above, the string cache is *SHARED* between `conjure_full_string` and `conjure_some_string`.
    #
    string_cache = {}

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   conjure_full_string(s) - Conjure a full `Some_String`, based on `s`.  Guarentees Uniqueness (in normal cases).
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
    #   NOTE:
    #
    #       See above for explanation of case 3A.
    #
    #   ==========
    #
    #   3A) If `not make_conjure_some_string`:
    #
    #           Returns a tuple of 1 element:
    #
    #               ((conjure_string_full,))
    #
    if not make_conjure_some_string:
        return ((conjure_full_string,))


    #
    #   conjure_some_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
    #
    #       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
    #
    #       Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
    #       version.
    #
    @creator
    def conjure_some_string(s):
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            return r

        if len(s) == 0:
            return empty_string

        interned_s = intern_native_string(s)

        string__possibly_non_unique = create_full_string(interned_s)

        #
        #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
        #   `String_Leaf` that is stored in `string_cache).
        #
        return provide_string(interned_s, string__possibly_non_unique)


    #
    #   NOTE:
    #
    #       See above for explanation of case 3B.
    #
    #   ==========
    #
    #   3B) If `make_conjure_some_string':
    #
    #               Returns a tuple of 2 elements:
    #
    #                   ((conjure_string_full, conjure_some_string))
    #
    return ((conjure_full_string, conjure_some_string))



[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, create_full_string)


#
#   conjure_full_string(s) - Conjure a full `Some_String`, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#       `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
#   EXCEPTIONS
#
#       If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
export(conjure_full_string)


#
#   conjure_some_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
export(conjure_some_string)
