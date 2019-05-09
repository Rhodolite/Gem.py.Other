#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V5
#
#       Private implementation of `conjure_some_string` for `String` Interface, Version 5.
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
#   Difference between Version 4 & Version 5.
#
#       Version 4:
#
#           Uses the same producer function from Version 2.
#
#           The arguments to `produce_conjure_string_functions` are:
#
#               1)  `Capital.Privage.String_V4.empty_string`; and
#
#               2)  `Capital.Privage.String_V4.create_full_string`.
#
#           (i.e.: "*_V4.*").
#
#       Version 5:
#
#           Uses the same producer function from Version 2.
#
#           The arguments to `produce_conjure_string_functions` are:
#
#               1)  `Capital.Privage.String_V5.empty_string`; and
#
#               2)  `Capital.Privage.String_V5.create_full_string`.
#
#           (i.e.: "*_V5.*").
#


from    Capital.Core                        import  export
from    Capital.Private.ConjureString_V3    import  produce_conjure_string_functions
from    Capital.Private.String_V5           import  create_full_string
from    Capital.Private.String_V5           import  empty_string


[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, create_full_string)


#
#   conjure_full_string(s) - Conjure a full `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
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
#   conjure_some_string(s) - Conjure a `String`, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
export(conjure_some_string)
