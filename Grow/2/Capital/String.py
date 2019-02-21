#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String - String Interface.
#
from    Capital.String_Implementation   import  conjure_string      #   See `USAGE` below.
from    Capital.String_Implementation   import  empty_string        #   See `USAGE` below.


#
#   interface String - String Interface.
#
#       Since interfaces are not native to python, for now, we just show them in comments
#
#           interface String
#               is_empty_string : Boolean
#               is_full_string  : Boolean
#               is_string       : Boolean
#
#   FUTURE:
#
#       The code generator will be able to accept interfaces, in a syntax similiar to the above, and verify them when
#       generating code.
#


#
#   USAGE:
#
#       empty_string                        #   The empty string singleton.
#       conjure_string(s)                   #   Conjure a string.
#
#       s.is_empty_string                   #   Test if `s` is an empty string.
#       s.is_full_string                    #   Test if `s` is a  full  string.
#       s.is_string                         #   Test if `s` is a        string.
#
#       assert fact_is_empty_string(s)      #   Assert that `s` is an empty string.
#       assert fact_is_full_string(s)       #   Assert that `s` is a  full  string.
#       assert fact_is_string(s)            #   Assert that `s` is a        string.
#
if __debug__:
    def fact_is_empty_string(s):
        assert s.is_empty_string

        return True


    def fact_is_full_string(s):
        assert s.is_full_string

        return True


    def fact_is_string(s):
        assert s.is_string

        return True


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
#           if s.is_string:             #   How to test if something is a string.
#               trace('Yes, s is a String!')
#
#   NOTE:
#
#       To use `s.is_string`, `s` must be a Capital type, so that it supports the `.is_string` attribute.
#
#       Does *NOT* work:
#
#           s = "a python string, not a capital string"
#
#           s.is_string                 #   AttributeError: 'str' object has no attribute 'is_string'
#
