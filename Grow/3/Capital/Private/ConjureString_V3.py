#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V2
#
#       Private implementation of `conjure_some_string` for `String` Interface, Version 2.
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
#   Difference between Version 2 & Version 3.
#
#       Version 2:
#
#           Producer function `produce_conjure_string_functions` to produce `conjure_{full,some}_string` functions.
#
#           The arguments to `produce_conjure_string` are:
#
#               1)  `Capital.Privage.String_V2.empty_string`; and
#
#               2)  `Capital.Privage.String_V2.create_full_string`.
#
#           (i.e.: "*_V2.*").
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


from    Capital.Core                        import  export
from    Capital.Private.ConjureString_V2    import  produce_conjure_string_functions
from    Capital.Private.String_V3           import  create_full_string
from    Capital.Private.String_V3           import  empty_string


[conjure_full_string, conjure_some_string] = produce_conjure_string_functions(empty_string, create_full_string)


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
