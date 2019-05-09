#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V7 - Private implementation of the public `String` Interface, Version 7.
#


#
#   Difference between Version 6 & Version 7.
#
#       Version 6:
#
#           The key/value pairs in `string_cache` are:
#
#               1)  Key is an interned `Some_Native_String`;
#
#               2)  Value is one of `Full_String | Temporary_String`.
#
#       Version 7:
#
#           The key/value pairs in `string_cache` are:
#
#               1)  Key is the same as value;
#
#               2)  Value is one of `Full_String | Temporary_String` (same as Version 5).
#


#
#   +===========================================================================================================+
#   |                                                                                                           |
#   |   MULTI THREADING WARNING                                                                                 |
#   |                                                                                                           |
#   |       This code (like all good multi-threading code that properly handles errors) is quite convoluted.    |
#   |                                                                                                           |
#   |       You can *IGNORE* reading and understanding the rest of this file, since it is the *PRIVATE*         |
#   |       implementation of the public `String` Interface.                                                    |
#   |                                                                                                           |
#   |       Initially, you really only need to read and understand the public `String` interface.               |
#   |                                                                                                           |
#   +===========================================================================================================+
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Exception               import  PREPARE_ValueError
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V7       import  empty_string
from    Capital.Private.String_V7       import  Full_String
from    Capital.Temporary_None          import  temporary_none
from    Capital.Temporary_String_V7     import  create_temporary_string


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_built_in_method
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_native_type
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
#           provide_string       - Provide a `Temporary_String`.
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
#   COMMENT ON KEYS in `string_cache`.
#
#       The keys in `string_cache` are the same as the values (i.e.: one of `Full_String` or `Temporary_String`).
#
#       However, you can still do a lookup using a native string, and it will still work.
#
#       For example, the following function calls
#
#           conjure_some_string('hello')
#
#       will return:
#
#           The `Full_String` with a value of `"Hello"`.
#
#       This is because we have *NOT* overridden the following methods:
#
#           str.__eq__
#           str.__hash__
#
#       Since these methods, treat all strings (direct instance of `str`, or instances of any subclass of `str`)
#       as equal if their characters match.
#
#       Or in other words:
#
#           assert "hello"       == conjure_some_string("hello")        #   Uses `str.__eq__`
#           assert hash("hello") == hash(conjure_some_string("Hello"))  #   Uses `str.__hash__` [twice].
#
#       The "type" of `string_cache` is:
#
#           Map { Full_String | Temporary_String : Full_String | Temporary_String }
#


#
#   produce_conjure_X_functions(
#           function_name,
#
#           lookup_string,
#           provide_string,
#           Full_String,
#
#           allow_empty_string = False,
#           empty_string       = None,
#   )
#
#       Produce a `conjure_some_string` or `conjure_full_string` function.
#
#       PARAMETERS:
#
#           1)  function_name           - Function name produced:
#
#                   1a) For Value_Error message;
#
#                   1b) In the future, will also rename the internal conjure_X_routine to this name
#                       (for debugging purposes).
#
#           2)  lookup_string           - Lookup a string in string_cache.
#
#           3)  provide_string          - Provide a string in string_cache.
#
#           4)  Full_String             - Type type to transform a Temporary_String to when creating a new string.
#
#           5)  allow_empty_string      - True if s may be "", in which case return empty_string.
#
#           6)  empty_string            - The singleton to return when the conjuring an empty string.
#
#                                         Must be `None` if `allow_empty_string` is not set.
#
#       PRODUCED FUNCTION:
#
#           `conjure_X_string(s)` - Conjure a `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#                   `s` must be a *DIRECT* `str` instance, and "full" (i.e.: has a length greater than 0).
#
#                   `s` may *NOT* be an instance of a subclass of `str`.
#
#               EXCEPTION
#
#                   If `allow_empty_string` is `False`, then the produced function has this behavior:
#
#                       If `s` is empty (i.e.: has 0 characters), throws a `ValueError`.
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
        Full_String,

        allow_empty_string = False,
        empty_string       = None,
):
    assert fact_is_full_native_string    (function_name)
    assert fact_is_native_built_in_method(lookup_string)
    assert fact_is_native_built_in_method(provide_string)
    assert fact_is_native_type           (Full_String)
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
    #                       Conjure a full `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
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
    #                       Conjure a `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
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

        r = lookup_string(s, temporary_none)

        #
        #   Is `r` definitively not temporary (i.e.: a real string)?
        #
        #   POSSIBILITIES
        #
        #       1)  Found a transformed temporary key (i.e.: a real value).
        #           The `if` statement will succeed.
        #
        #           This is the *MOST* common case.
        #
        #       2)  Not found, returns, `temporary_none`.
        #           The `if` statement will fail
        #           (since `temporary_none.definitively_not_temporary` is False)
        #
        #           This is the second most common case.
        #
        #       3)  Found a temporary key.  
        #           The `if` statement will fail.
        #
        #           This is a very rare case (only happens in multi threading race conditions).
        #
        #   SPEED ISSUES
        #
        #       The code below is designed to handle the most common case first (*before* testing for
        #       `temporary_none`).
        #
        #       Thus the most common case is:
        #
        #           r = lookup_string(s, temporary_none)
        #
        #           if r.definitively_not_temporary:
        #               return r
        #
        #       Later versions of crystal, will be able to "inline" this code into callers of `conjure_full_string`.
        #
        if r.definitively_not_temporary:
            return r

        if r is temporary_none:
            #
            #   Handle an empty string here (even in release mode).
            #
            #       Hence the assert above is "*_some_*" on purpose, so this code can catch the empty strings instead of the
            #       assert.
            #
            if len(s) == 0:
                if allow_empty_string:
                    return empty_string

                value_error = PREPARE_ValueError(
                        "parameter `s` is empty; `{}` requires a non-empty string; (i.e.: has a length greater than 0)",
                        function_name,
                    )

                raise value_error

            #
            #   NOTE:
            #       Due to multi-threading `temporary_string__maybe_duplicate` may be a duplicate (not unique).
            #
            #       There may be two or more seperate threads, all of which, simultaneously, create a
            #       `Temporary_String` with the same internal characters.
            #
            temporary_string__maybe_duplicate = create_temporary_string(s)

            #
            #   `provide_string` is thread safe, and all threads will return the same instance (which may be a
            #   `Temporary_String` or a `Full_String`).
            #
            #   NOTE:
            #       `provide_string` is thread safe since it is the python builtin method `dict.setdefault` (which is
            #       thread safe).
            #
            #       If two (or more) threads, simultaneously, create a `Temporary_String` with the same internal
            #       characters, then `provide_string_key` will return the same instance in all threads.
            #
            r = provide_string(temporary_string__maybe_duplicate, temporary_string__maybe_duplicate)

            #
            #   Is `r` definitively not temporary (i.e.: a real string)?
            #
            if r.definitively_not_temporary:
                return r

        #
        #   NOTE:
        #       Multiple threads may be simultaneously transforming `r` from a `Temporary_String` to a `Full_String`.
        #
        #       This is thread safe.
        #
        r.__class__ = Full_String

        #
        #   At this point `r` is now a `Full_String` (either we transformed it, or we & other threads all attempted to
        #   transformed it [and one thread actually did transform it]).
        #
        assert r.definitively_not_temporary    #   `r` has definitively been transformed now.

        return r


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
def produce_conjure_string_functions(empty_string, Full_String):
    assert fact_is_not_native_none(empty_string)
    assert fact_is_native_type    (Full_String)

    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is an interned `Some_Native_String`; and
    #
    #           2)  The value is a `String`.
    #
    #       The type of `string_cache` is `Map { interned Some_Native_String } of (Full_String | String_Leaf)`
    #
    string_cache = {}

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   Produce both functions, sharing `string_cache` (via `{lookup,provide}_cache`).
    #
    conjure_full_string = produce_conjure_X_string(
            'conjure_full_string', lookup_string, provide_string, Full_String,
        )

    conjure_some_string = produce_conjure_X_string(
            'conjure_some_string', lookup_string, provide_string, Full_String,

            allow_empty_string = True,
            empty_string       = empty_string,
        )

    #
    #   Return both produced functions.
    #
    return ((conjure_full_string, conjure_some_string))



[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, Full_String)


#
#   conjure_full_string(s) - Conjure a full `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
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
#   conjure_some_string(s) - Conjure a `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
export(conjure_some_string)
