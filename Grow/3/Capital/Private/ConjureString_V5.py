#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V5 - Private implementation of the public `String` Interface, Version 5.
#


#
#   Difference between Version 4 & Version 5.
#
#       Version 4:
#
#           Uses the same producer function from Version 2.
#
#           1)  Strings are unique (in normal cases).
#
#           2)  Uses `create_full_string` to create a full string, before attempting to put it in `string_cache`
#               (as explained there, in abnormal cases, this `Full_String` may leak).
#
#           3)  The second argument to `produce_conjure_string_functions` is `create_full_string` (to create a
#               full string)
#
#       Version 5:
#
#           1)  Strings are unique (always).
#
#           2)  Uses `create_temporary_string` to create a temporary string, before attempting to put it in
#               `string_cache`.
#
#               Only after the temporary string is guaranteed unique (in the contect of `string_cache`), is it
#               then transformed to a unique `Full_String`.
#
#               See all the comments below for more details.
#
#           3)  The second argument to `produce_conjure_string_functions` is a `Full_String` (the type to
#               tranform `Temporary_String` to).
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
from    Capital.Private.String_V5       import  empty_string
from    Capital.Private.String_V5       import  Full_String
from    Capital.Temporary_String_V5     import  create_temporary_string


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_native_none
    from    Capital.Fact                import  fact_is_native_type
    from    Capital.Fact                import  fact_is_not_native_none
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
#   produce_conjure_string_functions(
#           empty_string,
#           Full_String,
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
#           2)  `Full_String` - Type type to transform a `Temporary_String` to when creating a new string.
#
#           3)  `make_conjure_full_string` - Must be `True`; will always produce a `conjure_full_string` function.
#
#           4)  `make_conjure_some_string` - Set to `True` if a `conjure_some_string` should be produced.
#
#
#       Produced function:
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
        Full_String,

        make_conjure_full_string = True,
        make_conjure_some_string = True,
):
    if make_conjure_full_string:
        assert fact_is_not_native_none(empty_string)
    else:
        assert fact_is_native_none    (empty_string)

    assert fact_is_native_type        (Full_String)
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
            #
            #   MULTI-THREADING NOTE:
            #
            #       Due to multithreading `r` may actually be a `Temporary_String`.
            #
            #       In this case, transform it to a `Full_String`
            #
            #       This is thread safe, as the fact it made it *INTO* `string_cache`, is a guarentee of it's
            #       uniqueness.
            #


            #
            #   Has `r` already definitively been transformed?
            #
            if r.temporary_element_has_definitively_been_transformed:
                return r

            #
            #   NOTE:
            #       See note below on "multiple threads may be simultaneously transforming `r`" being thread safe.
            #
            #   NOTE -- DO NOT OPTIMIZE:
            #
            #       Do *NOT* remove the `r.temporary_element_has_definitively_been_transformed` above.
            #
            #       The test `r.temporary_element_has_definitively_been_transformed` above is needed for the following
            #       reason:
            #
            #           1.  `r` may have been a `Empty_String` -- It would be incorrect to transform `r` in such a
            #               case.
            #
            #       Also, as a secondary consideration:
            #
            #           2.  There is a very minor expense to transforming a string, so we don't want to attempt to
            #               [identity] transform a `Full_String` to a `Full_String` -- it's safe, but no need to try
            #               when we can avoid it with the `r.temporary_element_has_definitively_been_transformed`
            #               above.
            #
            r.__class__ = Full_String                                              #   THREAD SAFE: Make `r` a string.

            assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

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


        #
        #   NOTE:
        #       Due to multi-threading `temporary_string__maybe_duplicate` may be a duplicate (not unique).
        #
        #       There may be two or more seperate threads, all of which, simultaneously, create a `Temporary_String`
        #       with the same internal characters.
        #
        interned_s = intern_native_string(s)

        temporary_string__maybe_duplicate = create_temporary_string(interned_s)

        #
        #   `provide_string` is thread safe, and all threads will return the same instance (which may be a
        #   `Temporary_String` or a `Full_String`).
        #
        #   NOTE:
        #       `provide_string` is thread safe since it is the python builtin method `dict.setdefault` (which is thread
        #       safe).
        #
        #       If two (or more) threads, simultaneously, create a `Temporary_String` with the same internal
        #       characters, then `provide_string_key` will return the same instance in all threads.
        #
        r = provide_string(interned_s, temporary_string__maybe_duplicate)

        if r.temporary_element_has_definitively_been_transformed:   #   Has `r` already definitively been transformed?
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
        assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

        return r


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
    def conjure_some_string(s):
        #
        #   NOTE: See comments in `conjure_full_string`
        #
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            if r.temporary_element_has_definitively_been_transformed:
                return r

            r.__class__ = Full_String

            assert r.temporary_element_has_definitively_been_transformed

            return r

        #
        #   NOTE:
        #
        #       The next two lines are the only code difference between `conjure_full_string` and `conjure_some_string`.
        #
        if len(s) == 0:
            return empty_string

        interned_s = intern_native_string(s)

        temporary_string__maybe_duplicate = create_temporary_string(interned_s)

        r = provide_string(interned_s, temporary_string__maybe_duplicate)

        if r.temporary_element_has_definitively_been_transformed:
            return r

        r.__class__ = Full_String

        assert r.temporary_element_has_definitively_been_transformed 

        return r


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



[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, Full_String)


export(conjure_full_string)
export(conjure_some_string)
