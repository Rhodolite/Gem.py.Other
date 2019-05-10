#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V3 - Private implementation of the public `String` Interface, Version 3.
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
from    Capital.Private.String_V1       import  create_full_string      #   "_V2" on purpose"
from    Capital.Private.String_V1       import  empty_string            #   "_V2" on purpose"


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_built_in_method
    from    Capital.Fact                import  fact_is_native_function
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_not_native_none
    from    Capital.Native_String       import  fact_is_full_native_string
    from    Capital.Native_String       import  fact_is_some_native_string


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
#   produce_conjure_X_functions(
#           function_name,
#
#           lookup_string,
#           provide_string,
#           create_full_string,
#
#           allow_empty_string = False,
#           empty_string       = None,
#   )
#
#       Produce a `conjure_some_string` or `conjure_full_string` function.
#
#       PARAMETERS:
#
#           1)  `function_name` - Function name produced:
#
#                   1a) For `Value_Error` message;
#
#                   1b) In the future, will also rename the internal `conjure_X_routine` to this name
#                       (for debugging purposes).
#
#           2)  `lookup_string` - Lookup a string in `string_cache`.
#
#           3)  `provide_string` - Provide a string in `string_cache`.
#
#           4)  `create_full_string` - The function to create a full string.
#
#           5)  `allow_empty_string` - `True` if s may be `""`, in which case return `empty_string`.
#
#           6)  `empty_string` - The singleton to return when the conjuring an empty string.
#
#                                Must be `None` if `allow_empty_string` is not set.
#
#       PRODUCED FUNCTION:
#
#           `conjure_X_string(s)` - Conjure a `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
#
#               `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#               `s` may *NOT* be an instance of a subclass of `str`.
#
#           EXCEPTION
#
#               If `allow_empty_string` is `False`, then the produced function has this behavior:
#
#                   If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
#
#   SEE ALSO
#
#       See "Capital.Private.Execption_V2.py" for an explanation of "closure", "cell variable", "free variable", and
#       "produce" functions.
#
@export
def produce_conjure_X_string(
        function_name,

        lookup_string,
        provide_string,
        create_full_string,

        allow_empty_string = False,
        empty_string       = None,
):
    assert fact_is_full_native_string    (function_name)
    assert fact_is_native_built_in_method(lookup_string)
    assert fact_is_native_built_in_method(provide_string)
    assert fact_is_native_function       (create_full_string)
    assert fact_is_native_boolean        (allow_empty_string)

    if allow_empty_string:
        assert fact_is_not_native_none   (empty_string)
    else:
        assert fact_is_native_none       (empty_string)


    #
    #   conjure_X_string(s)
    #
    #       One of the following two functions:
    #
    #           1)  IF `allow_empty_string` is `FALSE`, THEN
    #
    #                   conjure_full_string(s)
    #
    #                       Conjure a `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
    #
    #                       `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
    #
    #                       `s` may *NOT* be an instance of a subclass of `str`.
    #
    #                   EXCEPTION
    #
    #                       If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
    #
    #           2)  ELSE
    #
    #                   conjure_some_string(s)
    #
    #                       Conjure a `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
    #
    #                       `s` must be of a `Some_Native_String` (i.e.: `str`).
    #
    #                       `s` may *NOT* be an instance of a subclass of `str`.
    #
    @creator
    def conjure_X_string(s):
        #
        #   The following test is "*_some_*" on purpose (even when `allow_empty_string` is `False`).
        #
        #   This is to allow the case of `s` is `""` to throw a `ValueError` below.
        #
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            return r

        #
        #   Handle an empty string here (even in release mode).
        #
        #       Hence the assert above is "*_some_*" on purpose (even when `allow_empty_string` is `False`), so this code
        #       can throw a `ValueError` when an `s` is `""` (instead of the assert above catching it in debug mode).
        #
        if len(s) == 0:
            if allow_empty_string:
                return empty_string

            value_error = PREPARE_ValueError(
                    "parameter `s` is empty; `{}` requires a non-empty string; (i.e.: has a length greater than 0)",
                    function_name,
                )

            raise value_error

        interned_s = intern_native_string(s)

        string__possibly_non_unique = create_full_string(interned_s)

        #
        #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
        #   `String_Leaf` that is stored in `string_cache).
        #
        return provide_string(interned_s, string__possibly_non_unique)


    return conjure_X_string


#
#   produce_conjure_string_functions(empty_string, create_full_string)
#
#       Produce `conjure_some_string` and `conjure_full_string` functions.
#
#   NOTE:
#
#       `string_cache` is shared between `conjure_some_string` and `conjure_full_string`.
#
@export
def produce_conjure_string_functions(empty_string, create_full_string):
    assert fact_is_not_native_none(empty_string)
    assert fact_is_native_function(create_full_string)

    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is an interned `Full_Native_String`; and
    #
    #           2)  The value is a `String` (`Full_String_Leaf` or `String_Leaf`).
    #
    string_cache = {}                   #   Map { interned Full_Native_String : Full_String_Leaf | String_Leaf }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   Produce both functions, sharing `string_cache` (via `{lookup,provide}_cache`).
    #
    conjure_full_string = produce_conjure_X_string(
            'conjure_full_string', lookup_string, provide_string, create_full_string,
        )

    conjure_some_string = produce_conjure_X_string(
            'conjure_some_string', lookup_string, provide_string, create_full_string,

            allow_empty_string = True,
            empty_string       = empty_string,
        )

    #
    #   Return both produced functions.
    #
    return ((conjure_full_string, conjure_some_string))



[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, create_full_string)


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
export(conjure_full_string)


#
#   conjure_some_string(s) - Conjure a `String`, based on `s`.  Guarantees Uniqueness (in normal cases).
#
#       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
export(conjure_some_string)
