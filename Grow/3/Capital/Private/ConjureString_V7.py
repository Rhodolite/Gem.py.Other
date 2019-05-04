#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V7 - Private implementation of the public `String` Interface, Version 7.
#


from    Capital.Fact                    import  fact_is_some_native_string
from    Capital.Private.EmptyString_V7  import  empty_string
from    Capital.Private.FullString_V7   import  FullString
from    Capital.StringKey_V7            import  create_string_key


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


#
#   DETAILS OF CURRENT PRIVATE IMPLEMENTATION
#
#       There are three classes:
#
#           Capital.Private.FullString_V7.EmptyString   - An empty string.
#           Capital.Private.FullString_V7.FullString    - A string with length greater than 0.
#           Capital.String_V7.StringKey                 - A `FullString` in the process of being constructed.
#
#       All three of these are inherited from the python builtin `str`.
#
#
#   DIFFERENCES:
#
#       The main difference is the two different string types ("Empty" .vs. "Full").
#
#       Conceptually, they both implement the `String` interface.
#
#       In addition we have our own `.__repr__` method to portray strings with the consistent way we
#       want all `.__repr__` methods in Capital to be portrayed.
#
#
#   FUTURE:
#
#       In the future, the code generator, will add interfaces to classes (yes, even in python, which does not support
#       interfaces nativly).
#
#       For now, since this is not implemented, we just show interfaces in comments (see "Capital.String" for an
#       example of the String interface in comments).
#


#
#   EXPLANATION OF VERBS
#
#       The following functions:
#
#           conjure_string       - Lookup or "create & insert" a string.
#           lookup_string        - Lookup a string.
#           provide_string_key   - Provide a `StringKey` instance.
#
#       The verb "conjure" in Capital code means "lookup, and if not found, create & insert a new one".
#
#       The verb "lookup"  in Capital code means "attempt to find, and return `None` if not found".
#
#       The verb "provide" in Capital code means "lookup, and use if found; if not found -- insert".
#
#           Returns the value used (either the one found with lookup, or the one inserted).
#
#           In python code this is `dict.setdefault` ("provide" is a clearer name than "setdefault").
#


#
#   string_cache - A cache of strings
#
#       All strings are stored in this as key/value pairs, where the key & value are the same.
#
#       Starts initialized with the key/value pair:
#
#           empty_string : empty_string
#
#       Thus, initially, the following function calls:
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
#       Likewise, we can use the string key `"Hello"` to lookup a `FullString("hello")` key,
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
#       where `String` can be one of `EmptyString`, `FulllString`, or `StringKey`.
#
string_cache = { empty_string : empty_string }

lookup_string      = string_cache.get
provide_string_key = string_cache.setdefault                       #   Thread safe (see comment below).


#
#   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness.
#
#       `s` must be of type `SomeNativeString` (i.e.: `str`).
#
#   NOTE:
#       There exists the possibility that internal instances may "leak" from this code.
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
#       By creating a `StringKey` instance, we make the following guarentee:
#
#           Any leakage of `FullString` instance is unique.
#
#   NOTE:
#       A `StringKey` may leak -- it may not be unique.
#
#       A `StringKey` may at any moment be transformed (by another thread, or by multiple other threads) to a
#       `FullString`.
#
def conjure_string(s):
    assert fact_is_some_native_string(s)

    r = lookup_string(s)

    if r is not None:
        #
        #   MULTI-THREADING NOTE:
        #
        #       Due to multithreading `r` may actually be a `StringKey`.
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
        #           1.  `r` may have been a `hidden.EmptyString` -- It would be incorrect to transform `r` in such a
        #               case.
        #
        #       Also, as a secondary consideration:
        #
        #           2.  There is a very minor expense to transforming a string, so we don't want to attempt to
        #               transform a `FullString` to a `FullString` -- it's safe, but no need to try when we can avoid
        #               it with the `r.is_string` above.
        #
        r.__class__ = FullString             #   THREAD SAFE: Make `r` a string.

        assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

        return r

    #
    #   NOTE:
    #       Due to multi-threading `k` may *NOT* be unique.
    #
    #       There may be two or more seperate threads, all of which, simultanously, create a `StringKey` with the same
    #       internal characters.
    #
    k = create_string_key(s)

    #
    #   `provide_string_key` is thread safe, and all threads will return the same `hidden.Build_A_String`
    #   instance.
    #
    #   NOTE:
    #       `provide_string_key` is thread safe since it is the python builtin method `dict.setdefault` (which
    #       is thread safe).
    #
    #       If two (or more) threads, simultanoulsy, create a `StringKey` with the same internal characters, then
    #       `provide_string_key` will return the same instance in all threads.
    #
    r = provide_string_key(k, k)            #   THREAD SAFE: Guarentees Uniqueness (see comment above)

    if r.temporary_element_has_definitively_been_transformed:       #   Has `r` already definitively been transformed?
        return r

    #
    #   NOTE:
    #       Multiple threads may be simultanously transforming `r` from a `StringKey` to a `FullString`.
    #
    #       This is thread safe.
    #
    r.__class__ = FullString                                        #   THREAD SAFE: Make `r` a string.

    #
    #   At this point `r` is now a `FullString` (either we transformed it, or we & other threads all
    #   attempted to transformd it [and one thread actually did transform it]).
    #
    assert r.temporary_element_has_definitively_been_transformed    #   `r` has definitively been transformed now.

    return r
