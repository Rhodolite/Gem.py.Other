#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V4 - Private implementation of `conjure_string` for `String` Interface, Version 4.
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
#   Difference between Version 3 & Version 4.
#
#       Version 3:
#
#           Uses the same producer function from Version 2.
#
#           The arguments to `produce_conjure_string` are:
#
#               1)  `Capital.Privage.String_V3.empty_string`; and
#
#               2)  `Capital.Privage.String_V3.create_full_string`.
#
#           (i.e.: "*_V3.*").
#
#       Version 4:
#
#           Uses the same producer function from Version 2.
#
#           The arguments to `produce_conjure_string` are:
#
#               1)  `Capital.Privage.String_V4.empty_string`; and
#
#               2)  `Capital.Privage.String_V4.create_full_string`.
#
#           (i.e.: "*_V4.*").
#


from    Capital.Core                        import  export
from    Capital.Private.ConjureString_V2    import  produce_conjure_string
from    Capital.Private.String_V4           import  create_full_string
from    Capital.Private.String_V4           import  empty_string


conjure_string = produce_conjure_string(empty_string, create_full_string)


export(conjure_string)
