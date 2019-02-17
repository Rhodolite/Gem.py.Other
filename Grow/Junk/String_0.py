#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.String_0 - String or Absent String Interface.
#
from    Capital.String_Implementation   import  string_is_absent    #   See `USAGE` below.
from    Capital.String_Implementation   import  conjure_string_0    #   See `USAGE` below.


#
#   interface String_0 - String or Absent String Interface.
#
#       Since interfaces are not native to python, for now, we just show them in comments
#
#           interface String_0 (
#                   implements Absent_Interface,
#                   implements String,
#           )
#               inherit from Absent_Interface
#                   is_absent  : Boolean
#                   is_present : Boolean
#
#               inherit from String
#                   is_empty_string : Boolean
#                   is_full_string  : Boolean
#                   is_string       : Boolean
#
#               is_string_0 : Boolean
#               is_string   : Boolean
#


#
#   USAGE OF String_0
#
#       conjure_string_0(v)                 #   Conjure a string or `string_is_absent`.
#       string_is_absent                    #   The "string is absent" singleton.
#
#       s.is_string_0                       #   Test if `s` is a string or `string_is_absent`.
#       s.is_string                         #   Test if `s` is a string.
#
#       assert fact_is_string_0(s)          #   Assert that `s` is a string or `string_is_absent`.
#       assert fact_is_string  (s)          #   Assert that `s` is a string.
#
#
#   Usage of Absent_Interface (copied from "Capital/Absent_Interface.py"):
#
#       v.is_absent                         #   Test if `v` is absent.
#
#       assert fact_is_absent(v)            #   Assert that `v` is absent.
#
#
#   USAGE of String (copied from "Capital/String.py"):
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


#
#   DIFFERENCE BETWEEN `empty_string` & `string_is_absent`
#
#       It's best to understand this in terms of databases.
#
#       The `string_is_absent` singleton is equivalent to a NULL entry in a row.  It's simply NOT THERE.
#
#       The `empty string` singleton is equivalent to a "" entry in a row.  It's there -- but has no length.
#
#       The following conceptual equivalence table can also help:
#
#           String              Conceptually Equivalent to
#           ------              --------------------------
#           empty_string        ""
#           full_string         'any string with a length greater than 0'
#           string_0            "any string" or None
#           string              "any string, including the empty_string, but *NOT* `None`."
#           string_is_absent    None
#
#   NOTE:
#
#       In a boolean context (i.e.: when `.__bool__` is called by python) both `empty_string` and
#       `string_is_absent` evaluate to `false`.
#
#       This follows the standard python pratice that both `None` and `""` evaluate to `false`.
#


#
#   WHY USE `String_0`?
#
#       `String_0` is incredibly powerful!
#
#       Instead of constantly testing for `none`, we instead use `String_0` and use `string_is_absent` to mean none.
#
#       Tons of code disappears this way, and the code becomes way more concise and clear.
#
#       In fact, in code dealing with databases, the use of `String_0` to represent a NULL row, can often
#       cause a code reduction of more than 50%.
#
#       More, importantly, the code is much easier to understand, modify, and test.
#
#       Changing code to match a database change of `NULL` to `NOT NULL` (or vice versa) often becomes
#       a single one line change, instead of hundreds of lines of code having to be modified.
#
#       It really is incredibly powerful!
#


#
#   WHY IT IS CALLED String_0?
#
#       It's very readable & concise.
#
#       Especially, in the future, when there are hundreds of interfaces named "*_0", it become
#       even more readalbe & concise.
#

#
#   NAMING CONVENTION
#
#       "empty_string"     - Uses the adjective "empty" to modify the noun "string".  Hence a string.
#
#       "full_string"      - Uses the adjective "full"  to modify the noun "string".  Hence a string.
#
#       "string_is_absent" - A phrase indicating a "string is absent".                Hence, *NOT* a string.
#
#   EXAMPLE:
#
#       s1 = string_is_absent
#       s2 = empty_string
#       s3 = conjure_string('I am a string.')
#
#       if s1.is_string:                                    #   NO  -- `s1` is *NOT* a string.
#           assert 0
#       else:
#           trace('{!r} is NOT a string, it is absent!', s)
#
#       if s2.is_string:                                    #   YES -- `s2` is a string.
#           trace('{!r} is a string, although empty.', s2)
#
#       if s3.is_string:                                    #   YES -- `s2` is a string.
#           trace('{!r} is also a string', s3)
#
#
#   WILL PRINT:
#
#       <string-is-absent> is NOT a string, it is absent!
#       <''> is a string, although empty.
#       <'I am a string.'> is also a string.
#
