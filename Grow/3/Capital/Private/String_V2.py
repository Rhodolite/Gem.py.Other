#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V2 - Private implementation of the public `String` Interface, Version 2.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique
#       in later versions.
#


#
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           Implementation of creator function `create_full_string` and singleton `empty_string`.
#
#       Version 2:
#
#           Identical to version 1, imports `create_full_string` and `empty_string` from version 1.
#


from    Capital.Core                    import  export
from    Capital.Private.String_V1       import  create_full_string
from    Capital.Private.String_V1       import  empty_string


export(create_full_string)
export(empty_string)
