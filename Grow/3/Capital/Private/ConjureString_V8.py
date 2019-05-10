#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.ConjureString_V8 - Private implementation of the public `String` Interface, Version 8.
#


#
#   Difference between Version 7 & Version 8.
#
#       Version 7:
#
#           Defines the producer function `produce_conjure_string_functions`.
#
#           The arguments to `produce_conjure_string_functions` are:
#
#               1)  `Capital.Privage.String_V7.empty_string`; and
#
#               2)  `Capital.Privage.String_V7.create_full_string`.
#
#           (i.e.: "*_V7.*").
#
#       Version 8:
#
#           Uses the same producer function from Version 7.
#
#           The arguments to `produce_conjure_string_functions` are:
#
#               1)  `Capital.Privage.String_V8.empty_string`; and
#
#               2)  `Capital.Privage.String_V8.create_full_string`.
#
#           (i.e.: "*_V8.*").
#


from    Capital.Core                        import  export
from    Capital.Private.ConjureString_V7    import  produce_conjure_string_functions
from    Capital.Private.String_V8           import  Full_String_Leaf
from    Capital.Private.String_V8           import  empty_string


[conjure_full_string, conjure_string] = produce_conjure_string_functions(empty_string, Full_String_Leaf)


#
#   conjure_full_string(s) - Conjure a `Full_String`, based on `s`.  Guarantees Uniqueness (in all cases).
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
#   conjure_string(s) - Conjure a `String`, based on `s`.  Guarantees Uniqueness (in all cases).
#
#       `s` must be a *DIRECT* `Native_String` instance.
#
#       `s` may *NOT* be an instance of a subclass of `str`.
#
export(conjure_string)
