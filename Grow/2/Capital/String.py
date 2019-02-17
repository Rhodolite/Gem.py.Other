#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String - String Interface.  Strings are Unique (in normal cases).
#
#       By "Unique" we mean is only one instance for each unique value.
#
#       String are tested for by the folowing method:
#
#           .is_string.
#
#       Testing is *NOT* done with the python `type` built-in.


#
#   PUBLIC INTERFACES, PRIVATE IMPLEMENTATION
#
#       Interfaces are public, and show the user the interface to be used.
#
#       The implementation is private -- and can be implemented as one or more classes to implement a single interface.
#
#       This means that:
#
#           You do *NOT* Use the python `type` operator to test if something is "an interface" (since it may be
#           implemented by one or more classes).
#
#           Instead you always use `.is_name` (i.e.: for a String you use `.is_string`).
#

#
#   STRING EXAMPLE of "Public Interface, Private Implementation".
#
#       For the string example:
#
#           "Capital/String.py"                 - Public Interface to String's
#           "Capital/String_Implementation.py"  - Private Interface
#


from    Capital.String_Implementation   import  conjure_string      #   See `USAGE` below.
from    Capital.String_Implementation   import  empty_string        #   See `USAGE` below.


#
#   interface String - String Interface.  Strings are Unique (in normal case).
#
#       Since interfaces are not native to python, for now, we just show them in comments
#
#           interface String
#               is_string       : Boolean
#               python_code()   : Python_String
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
#       s.is_string                         #   Test if `s` is a string.
#
#       s.python_code()                     #   Return a `str` instance that is the python code that python will
#                                           #   compile to a `str` instance with the same characters.
#
#       assert fact_is_string(s)            #   Assert that `s` is a string.
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
