#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Some_String - Some String Interface.  Strings are Unique (in normal case).
#
#       By "Unique" we mean is only one string for each unique value.
#
#       In addition to being unique, strings are currently classified into three groups:
#
#           empty       - The singleton `empty_string` has a value of `<''>`.
#           full        - A string with length greater than 0.
#           some        - Either "empty" or "full".
#
#       Testing for two of these groups is done with:
#
#           .is_empty_string
#           .is_full_string
#
#       In debug mode, testing can also be done for a `Some_String` with:
#
#           .is_some_string
#
#       Testing is *NOT* done with the python `type` builtin.
#


from    Capital.Core                    import  export
from    Capital.Core                    import  FATAL


#
#   interface Some_String - Some String Interface.
#
#       Since interfaces are not native to python, for now, we just show them in comments:
#
#           interface String
#               method
#                   python_code()   : Full_Native_String
#                   native_string() : Some_Native_String
#
#               attribute
#                   is_empty_string : Boolean
#                   is_full_string  : Boolean
#
#               debug
#                   is_some_string  : Boolean
#
#   FUTURE:
#
#       The code generator will be able to accept interfaces, in a syntax similiar to the above, and verify them when
#       generating code.
#
class TRAIT_Some_String(object):
    __slots__ = (())


    if __debug__:
        is_some_string = True


#
#   USAGE:
#
#       s.is_empty_string                   #   Test if `s` is an empty string.
#
#       s.is_full_string                    #   Test if `s` is a  full  string.
#
#       conjure_some_string(s)              #   Conjure a string.
#
#       empty_string                        #   The empty string singleton.
#
#       s.native_string                     #   The `Some_Native_String` that `s` represents (may be a subclass of
#                                           #   `Some_Native_String).
#
#       s.python_code()                     #   Return a `Full_Native_String` that is the python code that python will
#                                           #   compile to a `str` with the same characters as `s`.
#


#
#   USAGE (debug mode):
#
#       s.is_some_string                    #   Test if `s` is a string.
#
#       assert fact_is_empty_string(s)      #   Assert that `s` is an empty string.
#
#       assert fact_is_full_string(s)       #   Assert that `s` is a  full  string.
#
#       assert fact_is_some_string(s)       #   Assert that `s` is a        string.
#


#
#   EVALUATION IN BOOLEAN CONTEXT
#
#       Following standard python conventions of evaluating an object in a boolean context:
#
#           `empty_string`      - In a boolean context, evaluates to `False`.
#           All full strings    - In a boolean context, evaluates to `True`.
#
#       This matches what python does:
#
#           ""                  - In a boolean context, evaluates to `False`.
#           "any other string"  - In a boolean context, evaluates to `True`.
#


#
#   CONCEPTUALLY
#
#       Conceptually there is a `String` interface -- however, there is nothing that can be
#       accessed as `String` in any python code.
#
#       Does *NOT* work:
#
#           type(s) is String           #   NameError: name 'String' is not defined
#
#       Do this instead:
#
#           s = conjure_some_string('hi')
#
#           if s.is_full_string:        #   How to test if something is a string.
#               trace('Yes, s is a String!')
#
#   NOTE:
#
#       To use `s.is_some_string`, `s` must be a Capital type, so that it supports the `.is_some_string` attribute.
#
#       Does *NOT* work:
#
#           s = "a python string, not a capital string"
#
#           s.is_full_string            #   AttributeError: 'str' object has no attribute 'is_full_string'
#


#
#   fact_is_empty_string(s) - Assert that `s` is an empty string.
#
if __debug__:
    def fact_is_empty_string(v):
        assert s.is_empty_string

        return True


#
#   fact_is_full_string(s) - Assert that `s` is an full string.
#
if __debug__:
    def fact_is_full_string(v):
        assert s.is_full_string

        return True


#
#   fact_is_some_string(s) - Assert that `s` is a string.
#
if __debug__:
    def fact_is_some_string(v):
        assert s.is_some_string

        return True


#
#   Import the version of tree names we want to use.
#
#       (imports must be after the "fact_*" functions, in case the imported file needs the "fact_*" functions).
#
from    Capital.Global                  import  capital_globals


string_version = capital_globals.string_version


if string_version == 0:
    pass
elif string_version == 1:
    from    Capital.Private.ConjureString_V1    import  conjure_full_string
    from    Capital.Private.ConjureString_V1    import  conjure_some_string
    from    Capital.Private.String_V1           import  empty_string
elif string_version == 2:
    from    Capital.Private.ConjureString_V2    import  conjure_full_string
    from    Capital.Private.ConjureString_V2    import  conjure_some_string
    from    Capital.Private.String_V2           import  empty_string
elif string_version == 3:
    from    Capital.Private.ConjureString_V3    import  conjure_full_string
    from    Capital.Private.ConjureString_V3    import  conjure_some_string
    from    Capital.Private.String_V3           import  empty_string
elif string_version == 4:
    from    Capital.Private.ConjureString_V4    import  conjure_full_string
    from    Capital.Private.ConjureString_V4    import  conjure_some_string
    from    Capital.Private.String_V4           import  empty_string
elif string_version == 5:
    from    Capital.Private.ConjureString_V5    import  conjure_full_string
    from    Capital.Private.ConjureString_V5    import  conjure_some_string
    from    Capital.Private.String_V5           import  empty_string
elif string_version == 6:
    from    Capital.Private.ConjureString_V6    import  conjure_full_string
    from    Capital.Private.ConjureString_V6    import  conjure_some_string
    from    Capital.Private.String_V6           import  empty_string
else:
    from    Capital.Core                import  FATAL

    FATAL('Capital/String.py: unknown string version: {!r}', string_version)


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


#
#   empty_string - The empty string singleton.
#
export(empty_string)
