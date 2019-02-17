#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String_Implementation - Private implementation of the public `String` Interface.
#


from    Capital.Core                    import  arrange
from    Capital.Fact                    import  fact_is_full_python_string


#
#   HIDDEN
#
#       All details of classes, functions, values (etc.) that implement the `String` interface are hidden from the
#       user.
#
#       These details will change over time.
#
#       The user should instead be using the `String` interface -- which will not change much over time.
#


#
#   EXPORT
#
#       We only export two symbols from this file:
#
#           `conjure_string`
#           `empty_string`
#
#       However, the user should not be using this file.
#
#       Instead, the user should be importing `conjure_string` and `empty_string` from "Capital/String.py".
#
#   NOTE:
#       We don't really need to define `conjure_string` and `empty_string` to `0`.
#
#       Whether we define them here or not, python will define them when `hidden()` is called below.
#
#       We define them here for clarity, to make it clear we are exporting only these two values.
#
conjure_string = 0                          #   Properly defined in `hidden` below.
empty_string   = 0                          #   Properly defined in `hidden` below.


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
#           hidden.Build_A_String   - A `hidden.FullUniqueString` instance in the process of being constructed.
#           hidden.EmptyString      - An empty string.
#           hidden.FullUniqueString - A string with length greater than 0.
#
#       All three of these are inherited from the python builtin `str`.
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
#   FUTURE:
#
#       In the future, the code generator, will add interfaces to classes
#       (yes, even in python, which does not support interfaces nativly).
#
#       For now, since this is not implemented, we just show this in comments.
#
def hidden():
    global conjure_string               #   Export this so the "Capital/String.py" can import this.
    global empty_string                 #   Export this so the "Capital/String.py" can import this.


    #
    #   exported - Does nothing.  Used for documentation only
    #
    def exported(f):
        return f


    #
    #   hidden.EmptyString - An empty string.
    #
    #       This is a singleton, there is only one empty string named `empty_string`.
    #
    #   NOTE:
    #
    #       In a boolean context evaluates to `False` (see `.__nonzero__` below).
    #
    class EmptyString(str):
        #
        #   implements String
        #
        __slots__ = (())


        #
        #   Interface String
        #
        is_empty_string = True
        is_full_string  = False
        is_string       = True


        #__init__    - inherited from `str.__init__`        #   Does nothing.
        #__new__     - inherited from `str.__new__`         #   Creates the new empty string.
        #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `False`.


        @staticmethod
        def __repr__():
            return "<''>"                                   #   `''` surrounded with angle brackets.


        @staticmethod
        def python_code():
            return "''"                                     #   Same as `str.__repr__("")`


    #
    #   hidden.FullUniqueString - A full string.
    #
    #       These are unique, there is only one `FullUniqueString` for each unique value.
    #
    #       Uniqueness is guarenteed, below, with `conjure_string`.
    #
    #   NOTE:
    #
    #       In a boolean context evaluates to `True` (see `.__nonzero__` below).
    #
    class FullUniqueString(str):
        #
        #   implements String
        #
        __slots__ = (())

        
        #
        #   Interface String
        #
        is_empty_string = False
        is_full_string  = True
        is_string       = True


        #__init__    - inherited from `str.__init__`        #   Not Used.
        #__new__     - inherited from `str.__new__`         #   Not Used.
        #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


        #
        #   .__repr__ - Portraying a `FullUniqueString`
        #
        #   CURRENT
        #
        #       Surround the python code representation (i.e.: `str.__repr__`) with angle brackets.
        #
        #       Example:
        #
        #           __repr__(conjure_string('hello')) == "<'hello'>"
        #
        #   FUTURE
        #
        #       See `.python_code` for an explanation of how `.python_code` will behave differently in the future.
        #
        #
        def __repr__(self):
            return arrange('<{}>', self.python_code(self))


        #
        #   .python_code
        #
        #       Return a `str` instance that is the python code that python will compile to a `str` instance with the
        #       same characters.
        #
        #   CURRENT
        #
        #       For now, we just use the python built in `str.__repr__`.
        #
        #   FUTURE:
        # 
        #       We will use the funtion `portray_python_string` which does a really good job of a python
        #       represenation (much more readable than `str.__repr__` when presented with a "raw" string).
        #
        #       However, that code is quite large, so we are not including it for now.
        #
        #       Also, really, we want to code generate the `portray_python_string` ... so will wait until the
        #       code generator can generate that function, before using it.
        #
        python_code = str.__repr__                #   `str.__repr__` implements the python representation.


    #
    #   hidden.Build_A_String - A `hidden.FullUniqueString` instance in the process of being constructed.
    #
    #       Due to multi-threading, may *NOT* be unique.
    #
    #       Once it is guarenteed to be unique, it is "transformed" to a `hidden.FullUniqueString`.
    #
    class Build_A_String(str):
        #
        #   Does *NOT* implement the String interface.
        #
        #   This is *NOT* a string, but a string in the process of being constructed.
        #
        __slots__ = (())


        is_string = False                                   #   This is *NOT* a string (it will become a string, later).


        #__init__    - inherited from `str.__init__`        #   Does nothing.
        #__new__     - inherited from `str.__new__`         #   Creates the new `Build_A_String` instance.
        #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


        def __repr__(self):
            return arrange('<Build_A_String {}>', str.__repr__(self))


    #
    #   empty_string - The empty string singleton.
    #
    empty_string = EmptyString()

    exported(empty_string)              #   Does nothing.  Documentation only.  Exported with `global` above.


    #
    #   string_cache         - A cache of strings.  Guarentees Uniqueness.
    #
    #   conjure_string       - Lookup or "create & insert" a string.
    #   lookup_string        - Lookup a string.
    #   provide_build_string - Provide a `hidden.Build_A_String` instance.
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
    #       Thus, initially, the following two function calls:
    #
    #           conjure_string('')
    #           conjure_string(empty_string)
    #
    #       will both return:
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
    #       Likewise, we can use the string key `"Hello"` to lookup a `FullUniqueString("hello")` key,
    #       as they will these two different instances as equal (and having the same hash)..
    #
    #       Or in other words:
    #
    #           assert "hello"       == conjure_string("hello")       #   Uses `str.__eq__`
    #           assert hash("hello") == hash(conjure_string("Hello")) #   Uses `str.__hash__` [twice].
    #
    #       The "type" of `string_cache` is:
    #
    #               Map { *String } of *String
    #
    #               Where `*String` means `Build_A_String | EmptyString | FullUniqueString`.
    #
    string_cache = {
                       empty_string : empty_string,
                   }

    lookup_string        = string_cache.get
    provide_build_string = string_cache.setdefault                       #   Thread safe (see comment below).


    #
    #   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness.
    #
    #       `s` must be one of the following types:
    #
    #       1.  `str`; OR
    #       2   implements the String Interface (i.e.: `hidden.EmptyString`, or `hidden.FullUniqueString`).
    #
    #   NOTE:
    #       There exists the possibility that internal instances may "leak" from this code.
    #
    #       Three common ways of "leakage" are:
    #
    #           1.  An `MemoryException` is thrown -- the instance will leak through tracebacks.
    #
    #           2.  A differnt thread examines the stack frames of this thread.
    #
    #           3.  A diferent thread uses the python `gc` module (garbage collection) to look at the internal
    #               instances of `conjure_string`.
    #
    #       By creating a `hidden.Build_A_String` instance, we make the following guarentee:
    #
    #           Any leakage of `hidden.FullUniqueString` instance is unique.
    #
    #   NOTE:
    #       A `hidden.Build_A_String` may leak -- it may not be unique.
    #
    #       A `hidden.Build_A_String` instance may at any moment be transformed (by another thread, or by multiple
    #       other threads) to a `hidden.FullUniqueString` instance.
    #
    @exported                           #   `@exported` does nothing.  Exported with `global` above.
    def conjure_string(s):
        r = lookup_string(s)

        if r is not None:
            #
            #   MULTI-THREADING NOTE:
            #
            #       Due to multithreading `r` may actually be a `hidden.Build_A_String`.
            #
            #       In this case, transform it to a `hidden.FullUniqueString`
            #
            #       This is thread safe, as the fact it made it *INTO* `string_cache`, is a guarentee of it's
            #       uniqueness.
            #
            if r.is_string:                         #   Is `r` a string?
                return r

            #
            #   The test just above, `r.is_string`, tested if `r` *WAS* a string.
            #
            #   `r` wasn't.
            #
            #   `r` *MAY* be a string by now (another thread may have transformed `r` to a `hidden.FullUniqueString` instance
            #   since we did the `r.is_string` test above).
            #
            #   The following code is *INCORRECT*:
            #
            #       assert type(r) is Build_A_String
            #
            #   All we know is that `r` *WAS* a `hidden.Build_A_String`, we know that *NOW* `r` is *EITHER*
            #   a `hidden.Build_A_String` OR a `hidden.FullUniqueString`.
            #
            if 0:
                #
                #   DISABLED.
                #
                #       The following assertion is correct (unlike the assertion in the above comment which is
                #       incorrect).
                #
                #       It's a waste of time to assert this, so the code is disabled.
                #
                #       The disabled code is left here for educational purposes only.
                #
                assert (type(r) is Build_A_String) or (type(r) is FullUniqueString)


            #
            #   NOTE:
            #       See note below on "multiple threads may be simultanously transforming `r`" being thread safe.
            #
            #   NOTE -- DO NOT OPTIMIZE:
            #
            #       Do *NOT* remove the `r.is_string` above.  The test `r.is_string` above is needed for the following reason:
            #
            #           1.  `r` may have been a `hidden.EmptyString` -- It would be incorrect to transform `r` in such a case.
            #
            #       Also, as a secondary consideration:
            #
            #           2.  There is a very minor expense to transforming a string, so we don't want to attempt to
            #               transform a `hidden.FullUniqueString` to a `hidden.FullUniqueString` -- it's safe, but no
            #               need to try when we can avoid it with the `r.is_string` above.
            #
            r.__class__ = FullUniqueString          #   THREAD SAFE: Make `r` a string.

            assert r.is_string                      #   `r` had *BETTER* be a string now!

            return r

        #
        #   The code above here has handled the following types:
        #
        #       `str`                       - when empty, i.e.: (`""`).
        #       `hidden.EmptyString`        - will be found in the cache & returned.
        #       `hidden.FullUniqueString`   - will be found in the cache & returned.
        #
        #   The only types left to handle are:
        #
        #       `str`                       - when full, that is, has a length greater than 0.
        #
        #   We thus assert the "fact" that `s` is a full python string.
        #
        assert fact_is_full_python_string(s)

        #
        #   NOTE:
        #       Due to multi-threading `build` may *NOT* be unique.
        #
        #       There may be two or more seperate threads, all of which, simultanously, create a
        #       `hidden.Build_A_String` with the same internal characters.
        #
        build = Build_A_String(s)

        #
        #   `provide_build_string` is thread safe, and all threads will return the same `hidden.Build_A_String`
        #   instance.
        #
        #   NOTE:
        #       `provide_build_string` is thread safe since it is the python builtin method `dict.setdefault` (which
        #       is thread safe).
        #
        #       If two (or more) threads, simultanoulsy, create a `hidden.Build_A_String` with the same internal
        #       characters, then `provide_build_string` will return the same instance in all threads.
        #
        r = provide_build_string(build, build)      #   THREAD SAFE: Guarentees Uniqueness (see comment above)

        #
        #   NOTE:
        #       Multiple threads may be simultanously transforming `r` from a `hidden.Build_A_String` instance
        #       to a `hidden.FullUniqueString` instance.
        #
        #       This is thread safe.
        #
        r.__class__ = FullUniqueString              #   THREAD SAFE: Make `r` a string.

        #
        #   At this point `r` is now a `hidden.FullUniqueString` (either we transformed it, or we & other threads
        #   all transformed it).
        #
        return r


#
#   Call `hidden` & then delete it
#
hidden()
del hidden


#
#   VERIFY EXPORT
#
#       Assert that `conjure_string` and `empty_string` both got replaced by `hidden()`.
#
assert conjure_string is not 0
assert empty_string   is not 0
