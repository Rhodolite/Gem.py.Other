#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String - String Interface.  Strings are Unique (in normal case).
#
#       By "Unique" we mean is only one string for each unique value.
#
#       In addition to being unique, strings are currently classified into two groups:
#
#           empty       - The singleton `empty_string` has a value of `<''>`.
#           full        - A string with length greater than 0.
#
#       Testing for these groups is done with:
#
#           .is_empty_string
#           .is_full_string
#
#       Testing is *NOT* done with the python `type` builtin.
#


#
#   interface String - String Interface.
#
#       Since interfaces are not native to python, for now, we just show them in comments:
#
#           interface String
#               attribute
#                   is_empty_string : Boolean
#                   is_full_string  : Boolean
#
#               method
#                   python_code() : FullNativeString
#
#               debug
#                   is_some_string : Boolean
#
#   FUTURE:
#
#       The code generator will be able to accept interfaces, in a syntax similiar to the above, and verify them when
#       generating code.
#
class TRAIT_String(object):
    __slots__ = (())


    if __debug__:
        is_some_string = True


#
#   USAGE:
#
#       conjure_string(s)                   #   Conjure a string.
#       empty_string                        #   The empty string singleton.
#
#       s.is_empty_string                   #   Test if `s` is an empty string.
#       s.is_full_string                    #   Test if `s` is a  full  string.
#
#       s.python_code()                     #   Return a `NativeString` that is the python code that python will
#                                           #   compile to a `str` with the same characters as `s`.
#
#


#
#   USAGE (debug mode):
#
#       s.is_some_string                    #   Test if `s` is a string.
#
#       assert fact_is_empty_string(s)      #   Assert that `s` is an empty string.
#       assert fact_is_full_string(s)       #   Assert that `s` is a  full  string.
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
#           s = conjure_string('hi')
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


from    Capital.Private.ConjureString_V3    import  conjure_string_v3   as  conjure_string
from    Capital.Private.EmptyString_V3      import  empty_string_v3     as  empty_string


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
