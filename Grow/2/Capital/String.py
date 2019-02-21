#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String - String Interface
#
#       EmptyString - An empty string.
#       FullString  - A string with length greater than 0
#
#   Both of these are inherited from the python builtin `str`.
#
#   DIFFERENCES:
#
#       The main difference is the two different string types.
#
#       Conceptually, they both implement the `String` interface (shown below).
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


#
#   Usage:
#
#       empty_string            #   The EmptyString singleton.
#       conjure_string(s)       #   Conjure a String (either an EmptyString or a FullString).
#
#       assert fact_is_empty_string(s)
#       assert fact_is_full_string(s)
#       assert fact_is_string(s)
#
#       s.is_empty_string       #   Test if `s` is an empty string.
#       s.is_full_string        #   Test if `s` is a full string.
#       s.is_string             #   Test if `s` is a string.
#
#   DO NOT:
#
#       EmptyString(s)          #   DO NOT CONSTRUCT an Emptystring.  Use `empty_string` instead.
#       FullString(s)           #   DO NOT CONSTRUCT a  FullString.   Use `conjure_string` instead.
#
#   FUTURE:
#
#       We will throw assertions if you attempt to construct an EmptyString, or FullString intead
#       of using `empty_string` or `conjure_string`.
#
#       We will *HIDE* `EmptyString` and `FullString` so you can NEVER access these directly!
#
#   interface String
#
#       Since interfaces are not native to python, for now, we just show them in comments
#
#       interface String
#           is_empty_string : boolean
#           is_full_string  : boolean
#           is_string       := true
#
    


#
#   EmptyString - An empty string.
#
#       This is a singleton, there is only one empty string named `empty_string`.
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


    #__init__ - inherited from `str.__init__`
    #__new__  - inherited from `str.__new__`


    @staticmethod
    def __repr__():
        return "<''>"


class FullString(str):
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


    #__init__ - inherited from `str.__init__`
    #__new__  - inherited from `str.__new__`


    def __repr__(self):
        return arrange('<{}>', str.__repr__(self))


#
#   empty_string - The empty string singleton.
#   
empty_string = EmptyString()



#
#   string_cache       - A cache of strings
#   conjure_string     - Lookup or Create & Insert a string.
#   insert_full_string - Insert a FullString.
#   lookup_string      - Lookup a string.
#   stash_string       - Stash a FullString
#
#       The verb "conjure" in Capital code means "lookup, and if not found, create & insert a new one".
#
#       The verb "insert"  in Capital code means "insert a new key; throw an exception if the key already exist".
#
#       The verb "lookup"  in Capital code means "attempt to find, and return `None` if not found".
#
#       The verb "stash"   in Capital code means "set" (set, including possibly overwriting, a value).
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
#           conjure_string("")
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
#       Likewise, we can use the string key `"Hello"` to lookup a `FullString("hello")` key,
#       as they will these two different instances as equal (and having the same hash)..
#
#       Or in other words:
#
#           assert "hello"       == FullString("hello")             #   Uses `str.__eq__`
#           assert hash("hello") == hash(FullString("Hello"))       #   Uses `str.__hash__` [twice].
#
string_cache = {                #   Map { EmptyString | FullString } of ( EmptyString | FullString )
                   empty_string : empty_string,
               }

lookup_full_string = string_cache.get
stash_string       = string_cache.__setitem__


def insert_full_string(k):
    assert k not in string_cache

    stash_string(k, k)


#
#   conjure_string(s)   - Conjure a string, based on `s`.
#
#       `s` must be one of the following types:
#
#           `str`, `EmptyString`, or `FullString`.
#
def conjure_string(s):
    r = lookup_string(s)

    if r is not None:
        return r

    #
    #   The code above here has handled the following types:
    #
    #       `str`         - when empty, i.e.: (`""`).
    #       `EmptyString` - will be found in the cache & returned.
    #       `FullString`  - will be found in the cache & returned.
    #
    #   The only types left to handle are:
    #
    #       `str`         - when full, that is, has a length greater than 0.
    #
    #   We thus assert the "fact" that `s` is a full python string.
    #
    assert fact_is_full_python_string(s)

    r = FullString(s)

    insert_full_string(r)

    return r
