#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V3 - Private implementation of the public `String` Interface, Version 3.
#


#
#   Difference between Version 2 & Version 3
#
#       Version 2:
#
#           1)  Strings are unique (in normal cases).
#
#           2)  Uses `create_full_string` to create a full string, before attempting to put it in `string_cache`
#               (as explained there, in abnormal cases, this `FullString` may leak).
#
#       Version 3:
#
#           1)  Strings are unique (always).
#
#           2)  Uses `create_temporary_string` to create a temporary string, before attempting to put it in
#               `string_cache`.
#
#               Only after the temporary string is guarentted unique (in the contect of `string_cache`), is it
#               then transformed to a unique `FullString`.
#
#               See all the comments below for more details.
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


from    Capital.Core                        import  trace
from    Capital.NativeString                import  intern_native_string
from    Capital.Private.String_V3           import  empty_string
from    Capital.Private.String_V3           import  FullString
from    Capital.Private.TemporaryString_V3  import  create_temporary_string


if __debug__:
    from    Capital.Fact                    import  fact_is_some_native_string


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
#   string_cache - A cache of strings
#
#       All strings are stored in this as key/value pairs:
#
#           1)  The key   is an interned `NativeString`; and
#           2)  The value is a `String_V1`.
#
#       The type of `string_cache` is `Map { interned NativeString } of EmptyString | FullString | TemporaryString`
#
#       The cache is initialized with `empty_string`, to make sure that `empty_string` is returned uniquely
#       when the `conjure_string("")` is called.
#
#
string_cache = { intern_native_string("") : empty_string }

lookup_string  = string_cache.get
provide_string = string_cache.setdefault            #   Thread safe (see comment below).


#
#   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (always).
#
#       `s` must be of type `SomeNativeString` (i.e.: `str` or a subclass derived from `str`).
#
#   NOTE:
#       There exists the possibility that internal instances of `TemporaryString* may "leak" from this code.
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
#       By creating a `TemporaryString` instance, we make the following guarentee:
#
#           Any leakage of `FullString` instance is unique.
#
#   NOTE:
#       A `TemporaryString` may leak -- it may not be unique.
#
#       A `TemporaryString` may at any moment be transformed (by another thread, or by multiple other threads) to a
#       `FullString`.
#
def conjure_string(s):
    assert fact_is_some_native_string(s)

    r = lookup_string(s)

    if r is not None:
        #
        #   MULTI-THREADING NOTE:
        #
        #       Due to multithreading `r` may actually be a `TemporaryString`.
        #
        #       In this case, transform it to a `FullString`
        #
        #       This is thread safe, as the fact it made it *INTO* `string_cache`, is a guarentee of it's
        #       uniqueness.
        #
        if r.temporary_element_has_definitively_been_transformed:   #   Has `r` already definitively been transformed?
            return r

        #
        #   NOTE:
        #       See note below on "multiple threads may be simultanously transforming `r`" being thread safe.
        #
        #   NOTE -- DO NOT OPTIMIZE:
        #
        #       Do *NOT* remove the `r.temporary_element_has_definitively_been_transformed` above.
        #
        #       The test `r.temporary_element_has_definitively_been_transformed` above is needed for the following
        #       reason:
        #
        #           1.  `r` may have been a `EmptyString` -- It would be incorrect to transform `r` in such a case.
        #
        #       Also, as a secondary consideration:
        #
        #           2.  There is a very minor expense to transforming a string, so we don't want to attempt to
        #               [identity] transform a `FullString` to a `FullString` -- it's safe, but no need to try when we
        #               can avoid it with the `r.temporary_element_has_definitively_been_transformed` above.
        #
        r.__class__ = FullString                                        #   THREAD SAFE: Make `r` a string.

        assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

        return r

    #
    #   NOTE:
    #       Due to multi-threading `temporary_string__possibly_non_unique` may *NOT* be unique.
    #
    #       There may be two or more seperate threads, all of which, simultanously, create a `TemporaryString` with the same
    #       internal characters.
    #
    interned_s = intern_native_string(s)

    temporary_string__possibly_non_unique = create_temporary_string(interned_s)

    #
    #   `provide_string` is thread safe, and all threads will return the same instance (which may be a `TemporaryString`
    #   or a `FullString`).
    #
    #   NOTE:
    #       `provide_string` is thread safe since it is the python builtin method `dict.setdefault` (which is thread
    #       safe).
    #
    #       If two (or more) threads, simultanoulsy, create a `TemporaryString` with the same internal characters, then
    #       `provide_string_key` will return the same instance in all threads.
    #
    r = provide_string(interned_s, temporary_string__possibly_non_unique)

    if r.temporary_element_has_definitively_been_transformed:       #   Has `r` already definitively been transformed?
        return r

    #
    #   NOTE:
    #       Multiple threads may be simultanously transforming `r` from a `TemporaryString` to a `FullString`.
    #
    #       This is thread safe.
    #
    trace('TemporaryString.mro: {}', type(r).mro())
    trace('TemporaryString.__slots__: {}', type(r).__slots__)
    trace('TemporaryString.__slots__: {}', type(r).mro()[1].__slots__)

    trace('FullString.mro: {}',             FullString.mro())
    trace('FullString.__slots__: {}',  FullString.mro()[0].__slots__)
    trace('BaseString.__slots__: {}',  FullString.mro()[1].__slots__)
    trace('TRAIT_String.__slots__: {}',  FullString.mro()[2].__slots__)
    trace('TRAIT_TemporaryELement.__slots__: {}',  FullString.mro()[3].__slots__)

    r.__class__ = FullString

    #
    #   At this point `r` is now a `FullString` (either we transformed it, or we & other threads all attempted to
    #   transformd it [and one thread actually did transform it]).
    #
    assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

    return r
