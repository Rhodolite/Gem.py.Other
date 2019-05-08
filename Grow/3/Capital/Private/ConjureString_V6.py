#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V6 - Private implementation of `conjure_string` for `String` Interface, Version 6.
#


#
#   Difference between Version 5 & Version 6.
#
#       Version 5:
#
#           The key/value pairs in `string_cache` are:
#
#               1)  Key is an interned `Some_Native_String`;
#
#               2)  Value is one of `Empty_String | Meta | Temporary_String`.
#
#       Version 6:
#
#           The key/value pairs in `string_cache` are:
#
#               1)  Key is the same as value;
#
#               2)  Value is one of `Empty_String | Meta | Temporary_String`.
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


from    Capital.Core                    import  export
from    Capital.Core                    import  trace
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V6       import  empty_string
from    Capital.Private.String_V6       import  Full_String
from    Capital.Temporary_String_V6     import  create_temporary_string


if __debug__:
    from    Capital.Fact                    import  fact_is_some_native_string


#
#   EXPLANATION OF VERBS
#
#       The following functions have a "verb" in their name:
#
#           conjure_string       - Lookup or "create & insert" a string.
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
#       The keys in `string_cache` are the same as the values (i.e.: one of `Empty_String`, `Meta`, or
#       `Temporary_String`).
#
#       However, you can still do a lookup using a native string, and it will still work.
#
#       For example, the following function calls
#
#           conjure_string('')
#
#       will return:
#
#           empty_string
#
#       This is because we have *NOT* overridden the following methods:
#
#           str.__eq__
#           str.__hash__
#
#       Since these methods, treat all strings (direct instance of `str`, or instances of any subclass of `str`)
#       as equal if their characters match.
#
#       Likewise, we can use the string key `"Hello"` to lookup a `Meta("hello")` key,
#       as they will these two different instances as equal (and having the same hash)..
#
#       Or in other words:
#
#           assert "hello"       == conjure_string("hello")             #   Uses `str.__eq__`
#           assert hash("hello") == hash(conjure_string("Hello"))       #   Uses `str.__hash__` [twice].
#
#       The "type" of `string_cache` is:
#
#           Map { String } of String
#
#       where `String` can be one of `Empty_String`, `FulllString`, or `StringKey`.
#


#
#   produce_conjure_string(empty_string, create_temporary_string, Meta) - Produce a `conjure_string(s)` function.
#
#       Produces: `conjure_string(s)` - Conjure a string, based on `s`.  Guarentees Uniqueness (always).
#
#           `s` must be of type some `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
@export
def produce_conjure_string(empty_string, create_temporary_string, Meta):
    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key  is the same as the value;
    #
    #           2)  The value is a `String`.
    #
    #       The type of `string_cache` is
    #       `Map { Empty_String | Meta | Temporary_String } of Empty_String | Meta | Temporary_String`.
    #
    #       The cache is initialized with `empty_string`, to make sure that `empty_string` is returned uniquely
    #       when the `conjure_string("")` is called.
    #
    string_cache = { empty_string : empty_string }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault            #   Thread safe (see comment below).


    #
    #   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (always).
    #
    #       `s` must be of type some `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
    #
    #   NOTE:
    #       There exists the possibility that internal instances of `Temporary_String* may "leak" from this code.
    #
    #       Three common ways of "leakage" are:
    #
    #           1.  An `MemoryException` is thrown -- the instance will leak through tracebacks.
    #
    #           2.  A different thread examines the stack frames of this thread.
    #
    #           3.  A different thread uses the python `gc` module (garbage collection) to look at the internal
    #               instances of `conjure_string`.
    #
    #       By creating a `Temporary_String` instance, we make the following guarentee:
    #
    #           Any leakage of `Meta` instance is unique.
    #
    #   NOTE:
    #       A `Temporary_String` may leak -- it may not be unique.
    #
    #       A `Temporary_String` may at any moment be transformed (by another thread, or by multiple other threads) to
    #       a `Meta`.
    #
    def conjure_string(s):
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            #
            #   MULTI-THREADING NOTE:
            #
            #       Due to multithreading `r` may actually be a `Temporary_String`.
            #
            #       In this case, transform it to a `Meta`
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
            #               [identity] transform a `Meta` to a `Meta` -- it's safe, but no need to try when
            #               we can avoid it with the `r.temporary_element_has_definitively_been_transformed` above.
            #
            r.__class__ = Meta                                              #   THREAD SAFE: Make `r` a string.

            assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

            return r

        #
        #   NOTE:
        #       Due to multi-threading `temporary_string__maybe_duplicate` may be a duplicate (not unique).
        #
        #       There may be two or more seperate threads, all of which, simultaneously, create a `Temporary_String`
        #       with the same internal characters.
        #
        temporary_string__maybe_duplicate = create_temporary_string(s)

        #
        #   `provide_string` is thread safe, and all threads will return the same instance (which may be a
        #   `Temporary_String` or a `Meta`).
        #
        #   NOTE:
        #       `provide_string` is thread safe since it is the python builtin method `dict.setdefault` (which is thread
        #       safe).
        #
        #       If two (or more) threads, simultaneously, create a `Temporary_String` with the same internal
        #       characters, then `provide_string_key` will return the same instance in all threads.
        #
        r = provide_string(temporary_string__maybe_duplicate, temporary_string__maybe_duplicate)

        if r.temporary_element_has_definitively_been_transformed:   #   Has `r` already definitively been transformed?
            return r

        #
        #   NOTE:
        #       Multiple threads may be simultaneously transforming `r` from a `Temporary_String` to a `Meta`.
        #
        #       This is thread safe.
        #
        r.__class__ = Meta

        #
        #   At this point `r` is now a `Meta` (either we transformed it, or we & other threads all attempted to
        #   transformd it [and one thread actually did transform it]).
        #
        assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

        return r


    return conjure_string


conjure_string = produce_conjure_string(empty_string, create_temporary_string, Full_String)


export(conjure_string)
