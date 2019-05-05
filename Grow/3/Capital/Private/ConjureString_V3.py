#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V2 - Private implementation of `conjure_string` for `String` Interface, Version 2.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#
#           2.  Tracebacks due to MemoryError (out of memory);
#
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique.
#
#


#
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           1)  Uses `Capital.Private.String_V1.empty_string`           #   NOTE: "*_V1.*"
#
#           2)  Uses `Capital.Private.String_V1.create_full_string`     #   NOTE: "*_V1.*"
#
#       Version 2:
#
#           1)  Uses `Capital.Private.String_V2.empty_string`           #   NOTE: "*_V2.*"
#
#           2)  Uses `Capital.Private.String_V2.create_full_string`     #   NOTE: "*_V2.*"
#
#       Internally, this code has no other differences from "Capital.Private.CreateString_V1" -- most of the actual
#       difference are between the two files:
#
#           Capital.Private.String_V1.py            #   Uses class `String_V1`.
#
#                    .vs.
#
#           Capital.Private.String_V2.py            #   Uses classes `EmptyString` and `FullString`.
#


from    Capital.Core                        import  export
from    Capital.Private.ConjureString_V2    import  produce_conjure_string
from    Capital.Private.String_V3           import  create_full_string
from    Capital.Private.String_V3           import  empty_string


conjure_string = produce_conjure_string(empty_string, create_full_string)


export(conjure_string)
