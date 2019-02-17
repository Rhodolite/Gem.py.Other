#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.StringImplementation - V2 Implementation of String Interface.  Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       V3 (Version 3) of the string implementation fixes this issue, and strings are always unique in V3.
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


#
#   NOTE:
#       We don't really need to define `conjure_string` and `empty_string` to `0`.
#
#       Whether we define them here or not, python will define them when `hidden()` is called below.
#
#       We define them here for clarity, to make it clear we are exporting only these two values.
#
conjure_string = 0                      #   Properly defined in `hidden` below.
empty_string   = 0                      #   Properly defined in `hidden` below.


#
#   DETAILS OF CURRENT PRIVATE IMPLEMENTATION
#
#       There is one class:
#
#           hidden.UniqueString         - The string implementation (a simple implementation)
#
#       This is inherited from the python builtin `str`.
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
    #   hidden.UniqueString     - An empty or full string.
    #
    #       These are unique, there is only one `UniqueString` for each unique value.
    #
    #       Uniqueness is guarenteed, below, with `conjure_string` (for normal cases).
    #
    #   NOTE:
    #
    #       In a boolean context the empty string evaults to `False` and all full strings evaluate to `True`
    #       (see `.__nonzero__` below).
    #
    class UniqueString(str):
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
        #   .__repr__ - Portraying a `UniqueString`
        #
        #       CURRENT
        #
        #           Surround the python code representation (i.e.: `str.__repr__`) with angle brackets.
        #
        #       Example:
        #
        #           __repr__(conjure_string('hello')) == "<'hello'>"
        #
        #   FUTURE
        #
        #       See `.python_code` for an explanation of how `.python_code` will behave differently in the future.
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
    #   empty_string - The empty string singleton.
    #
    empty_string = UniqueString()

    exported(empty_string)              #   Does nothing.  Documentation only.  Exported with `global` above.


    #
    #   string_cache   - A cache of strings.  Guarentees Uniqueness (in normal cases).
    #
    #   conjure_string - Lookup or "create & insert" a string.
    #   lookup_string  - Lookup a string.
    #   provide_string - Provide a `hidden.UniqueString` instance.
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
    #       Likewise, we can use the native string key `"Hello"` to lookup a `FullUniqueString("hello")` key,
    #       as they will these two different instances as equal (and having the same hash)..
    #
    #       Or in other words:
    #
    #           assert "hello"       == conjure_string("hello")       #   Uses `str.__eq__`
    #           assert hash("hello") == hash(conjure_string("Hello")) #   Uses `str.__hash__` [twice].
    #
    #       The "type" of `string_cache` is:
    #
    #               Map { UniqueString } of UniqueString
    #
    string_cache = {
                       empty_string : empty_string,
                   }

    lookup_string        = string_cache.get
    provide_build_string = string_cache.setdefault       #   Thread safe (see comment below).


    #
    #   conjure_string(s) - Conjure a string, based on `s`.  Guarantees uniqueness (in normal cases).
    #
    #       `s` must be one of the following types:
    #
    #       1.  `str`; OR
    #       2   implements the UniqueString Interface (i.e.: `hidden.UniqueString`).
    #
    @exported                           #   `@exported` does nothing.  Exported with `global` above.
    def conjure_string(s):
        r = lookup_string(s)

        if r is not None:
            return r

        #
        #   The code above here has handled the following types:
        #
        #       `str`                   - when empty, i.e.: (`""`).
        #       `hidden.UniqueString`   - will be found in the cache & returned.
        #
        #   The only types left to handle are:
        #
        #       `str`                   - when full, that is, has a length greater than 0.
        #
        #   We thus assert the "fact" that `s` is a full python string.
        #
        assert fact_is_full_python_string(s)

        #
        #   NOTE:
        #       Due to multi-threading `build` may *NOT* be unique.
        #
        #       As noted above, this may "leak".  Fixed in the V3 implementation to not leak.
        #
        build = UniqueString(s)

        #
        #   `provide_build_string` is thread safe, and all threads will return the same `hidden.UniqueString`
        #   instance.
        #
        #   NOTE:
        #       `provide_build_string` is thread safe since it is the python builtin method `dict.setdefault` (which
        #       is thread safe).
        #
        #       If two (or more) threads, simultanoulsy, create a `hidden.UniqueString` with the same internal
        #       characters, then `provide_build_string` will return the same instance in all threads.
        #
        r = provide_build_string(build, build)      #   THREAD SAFE: Guarantees uniqueness (see comment above)

        #
        #   Return the unique string stored in `r`.
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
