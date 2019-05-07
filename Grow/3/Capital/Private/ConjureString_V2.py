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
#   Difference between Version 1 & Version 2
#
#       Version 1:
#
#           Implementation of creator function `conjure_string`.
#
#       Version 2:
#
#           Producer function `produce_conjure_string` to produce `conjure_string` functions.
#
#           The initially created `conjure_string` is identical to `Capital.Private.ConjureString_V1.conjure_string`
#           (the only internal difference is using a closure for variables instead of global variables).
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Fact                    import  fact_is_some_native_string
from    Capital.Core                    import  trace
from    Capital.Native_String           import  intern_native_string
from    Capital.Private.String_V2       import  create_full_string
from    Capital.Private.String_V2       import  empty_string


#
#   EXPLANATION OF VERBS
#
#       The following functions have a "verb" in their name:
#
#           conjure_string       - Lookup or "create & insert" a string.
#           lookup_string        - Lookup a string.
#           provide_string       - Provide a `String_V1`.
#
#       The verb "conjure" in Capital code means "lookup, and if not found, create & insert a new one".
#
#       The verb "lookup"  in Capital code means "attempt to find, and return `None` if not found".
#
#       The verb "provide" in Capital code means "lookup, and use if found; if not found -- insert".
#
#           Returns the value used (either the one found with lookup, or the one inserted).
#
#           In python code this is `dict.setdefault` ("provide" is a used as it is a clearer name than "setdefault").
#


#
#   produce_conjure_string(empty_string, create_string) - Produce a `conjure_string(s)` function.
#
#       Produces: `conjure_string(s)` - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
#
#           `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
#
#           Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
#           version.
#
@export
def produce_conjure_string(empty_string, create_full_string):
    #
    #   string_cache - A cache of strings
    #
    #       All strings are stored in this as key/value pairs:
    #
    #           1)  The key is an interned `Some_Native_String`; and
    #
    #           2)  The value is a `String`.
    #
    #       The type of `string_cache` is `Map { interned Some_Native_String } of String`
    #
    #       The cache is initialized with `empty_string`, to make sure that `empty_string` is returned uniquely
    #       when the `conjure_string("")` is called.
    #
    string_cache = { intern_native_string("") : empty_string }

    lookup_string  = string_cache.get
    provide_string = string_cache.setdefault


    #
    #   conjure_string(s) - Conjure a string, based on `s`.  Guarentees Uniqueness (in normal cases).
    #
    #       `s` must be of type `Some_Native_String` (i.e.: `str` or a subclass derived from `str`).
    #
    #       Please see comment at the top about non-uniqueness in abnormal cases, and how this will be fixed in future
    #       version.s
    #
    @creator
    def conjure_string(s):
        assert fact_is_some_native_string(s)

        r = lookup_string(s)

        if r is not None:
            return r

        interned_s = intern_native_string(s)

        string__possibly_non_unique = create_full_string(interned_s)

        #
        #   The result of `provide_string` will be unique (in the contect of `string_cache`; i.e.: the unique version of
        #   `String_V1` that is stored in `string_cache).
        #
        return provide_string(interned_s, string__possibly_non_unique)


   #trace('produce_conjure_string({!r}, <function {}>)', empty_string, create_full_string.__name__)

    return conjure_string


conjure_string = produce_conjure_string(empty_string, create_full_string)


export(conjure_string)


#
#   EXPLANATION OF THE PYTHON TERMINOLOGY: "closure", "cell variable", and "free variable".
#
#   SUMMARY of "closure" (more details below)
#
#       Above, `produce_conjure_string` is a function.
#
#       Inside of `produce_conjure_string` is the nested function `conjure_string`
#
#       There are local variables of `produce_conjure_string` that are used in `conjure_string`, in particular:
#
#           1)  `lookup_string`;
#
#           2)  `create_full_string`; and
#
#           3)  `provide_string`
#
#       These are "cell variables" in `produce_conjure_string`.
#
#       These are "free variables" in `conjure_string`.
#
#       When a "closure" is created around `conjure_string`, then each of the "free variables" in `conjure_string`
#       is bound to the "cell variable" in `produce_conjure_string` (with the same name).
#
#       By "bound" we mean the "free variable" is set as a pointer to the "cell variable".
#
#   "CELL VARIABLE"
#
#       A "cell variable" is a variable in a function (in our case in function `produce_conjure_string`) that can
#       be used by a nested function (in our case the function `conjure_string) when a closure is produced around
#       the nested function.
#
#       The following are the variables in `produce_conjure_string`:
#
#           0)  `empty_string` is local variable at index 0 (and it is also a parameter);
#
#           1)  `create_full_string` is local variable at index 0 (and it is also a parameter); it is also a
#               "cell variable" at index 0;
#
#           2)  `string_cache` is a local variable at index 2; and
#
#           3)  `conjure_string` is a local variable at index 3; (the value of `conjure_string` will be the closure
#               around the nested function `conjure_string`).
#
#       And also:
#
#           0)  As already mentioned, `create_full_string` is a cell variable at index 0; and it is also
#               a local variable at index 0 (and it is also a parameter);
#
#           1)  `lookup_string` is a cell variable at index 1; and
#
#           2)  `provide_string` is a cell variable at index 2.
#
#   "FREE VARIABLE"
#
#       A "free variable" is a variable inside a nested function (in our case the nested function `conjure_string`)
#       that is found to a "cell variable" in the enclosing function when a closure is produced around the nested
#       function.
#
#       The following are the variables in the function `conjure_string` (not to be confused with the local variable
#       `conjure_string`; which is used to store a closure around the function `conjure_string`):
#
#           0)  `s` is a local variable at index 0 (and it is also a parameter);
#
#           1)  `r` is a local variable at index 1;
#
#           2)  `interned_s` is a local variable at index 2; and
#
#           3)  `string__possibly_non_unique` is a local variabl at index 3.
#
#       And also:
#
#           0)  `create_full_string` is a free variable at index 0;
#
#           1)  `lookup_string` is a free variable at index 1; and
#
#           2)  `provide_string` is a free variable at index 2.
#
#   "CLOSURE"
#
#       A "closure" is created around a nested function, when the it's code is executed during execution of the
#       outer function.
#
#       In out case a closure is created around nested function `conjure_string` when the code to define `conjure_string`
#       is executed during the execution of `produce_conjure_string`.
#
#       To create this closure, each of it's free variable's is bound to a cell variable in the currently executing
#       enclosing function (i.e.: in the current execution of `produce_conjure_string`).
#
#       As stated above, by "bound" we mean the "free variable" is set as a pointer to the "cell variable".
#
#       This closure is then assigned to a variable with the same name as the nested function (i.e.: in our case
#       this closure is assigned to local variable `conjure_string` in the enclosing function `produce_conjure_string`).
#
#   DISABLED CODE BELOW.
#
#       The disable code below prints the following when enabled:
#
#           % ==== Code for produce_conjure_string ===
#           % Constant #0: None
#           % Constant #1: ''
#           % Constant #2: <code object conjure_string at 0x..., file ".../Grow/3/Capital/Private/ConjureString_V2.py", line 145>
#           % Local Variable & Function Parameter #0: 'empty_string'
#           % Local Variable & Function Parameter #1: 'create_full_string'
#           % Local Variable #2: 'string_cache'
#           % Local Variable #3: 'conjure_string'
#           % Cell Variable #0: 'create_full_string'
#           % Cell Variable #1: 'lookup_string'
#           % Cell Variable #2: 'provide_string'
#
#           % ==== Code for conjure_string ===
#           % Constant #0: None
#           % Local Variable & Function Parameter #0: 's'
#           % Local Variable #1: 'r'
#           % Local Variable #2: 'interned_s'
#           % Local Variable #3: 'string__possibly_non_unique'
#           % Free Variable #0: 'create_full_string'
#           % Free Variable #1: 'lookup_string'
#           % Free Variable #2: 'provide_string'
#           % Cell #0: <function create_full_string at 0x...>
#           % Cell #1: <built-in method get of dict object at 0x...>
#           % Cell #2: <built-in method setdefault of dict object at 0x...>
#
#       As can be seen, this matched what has been explaied above.
#
#       One comment on "Constant #2".  It's value is:
#
#           <code object conjure_string at 0x..., file "...//Grow/3/Capital/Private/ConjureString_V2.py", line 145>
#
#       This is the original code object for `conjure_string`, all the closures for `conjure_string` use the same
#       code object (NOTE: This is a code object, not a function object.  When creating a closure, a function object
#       is created to refer to this common code object ... see below for more details).
#
#       When a closure is created, it is created from this original code object, and the new code object for the
#       closure, is as explained above:
#
#           "each of it's free variable's is bound to a cell variable in the currently executing enclosing function
#           (i.e.: in the current execution of `produce_conjure_string`)."
#
#           The value for the cells is stored in the function object for each closure.
#
#           This is seen below where it reads:
#
#               % Cell #0: <function create_full_string at 0x...>
#               % Cell #1: <built-in method get of dict object at 0x...>
#               % Cell #2: <built-in method setdefault of dict object at 0x...>
#
#           This is showing the value of the three cells is:
#
#               1)  `create_full_string`;
#
#               2)  `lookup_string`; (i.e.: `string_cache.get`).
#
#               2)  `provide_string`; (i.e.: `string_cache.setdefault`).
#
#       The code below which dumps the variables (and cells) for `conjure_string`, is dumping the variables for a
#       closure of `conjure_string`.
#
if 0:
    def dump_code(code):
        trace('==== Code for {} ===', code.co_name)
       #trace('dir: {}', dir(code))

        for [i, v] in enumerate(code.co_consts):
            trace('Constant #{}: {!r}', i, v)

        for [i, v] in enumerate(code.co_varnames):
            if i < code.co_argcount:
                trace('Local Variable & Function Parameter #{}: {!r}', i, v)
            else:
                trace('Local Variable #{}: {!r}', i, v)

        for [i, v] in enumerate(code.co_cellvars):
            trace('Cell Variable #{}: {!r}', i, v)

        for [i, v] in enumerate(code.co_freevars):
            trace('Free Variable #{}: {!r}', i, v)

    def dump_functions():
        dump_code(produce_conjure_string.func_code)
        dump_code(conjure_string.func_code)

        for [i, v] in enumerate(conjure_string.func_closure):
            trace('Cell #{}: {!r}', i, v.cell_contents)

    dump_functions()
