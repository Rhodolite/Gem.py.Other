#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Exception_V1 - Implementation of exceptions for "Capital" library, Version 1.
#


#
#   NOTE:
#
#       In Version 1 (this version):
#
#           1)  `PREPARE_AttributeError` is defined.
#
#           2)  `PREPARE_ValueError` is also defined, duplicating a lot of code from `PREPARE_AttributeError`.
#
#       In Version 2:
#
#           1)  `produce_PREPARE_Exception` is defined to produce functions (closures).
#
#           2)  Both `PREPARE_AttributeError` and `PREPARE_ValueError` are produced, eliminating duplicated code.


#
#   PRODUCE FUNCTIONS AND CLOSURES.
#
#       See very long explanation below for an explantion of "produce" functions and closures.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


#
#   NOTE on functions named "PREPARE_*Error`".
#
#       These are the create function for `*Error` types (such as `AttributeError` and `ValueError`).
#
#       They are *NOT* called `create_*Error` since they takes different arguments than the `*Error` constructor do.
#
#       Also, in the future, they will do "special" modifications to `*Error` in python 2.*, to emulate python 3.*
#       exception chaining.
#


#
#   produce_PREPARE_Exception(function_name, Exception_Class)
#
#       Produce a function to prepare an exception (using `Exception_Class` for the exception).
#
#       Signature of produced function:
#
#           produce_PREPARE_Exception(message, *arguments)
#
#               Prepare a `Exception_Class` instance initialized with an error message consisting of `message` formatted
#               using `arguments`.
#
#   CURRENT IMPLEMENTATION:
#
#       1)  Does not do exception chaining in python 2.*.
#
#       2)  Does not rename the function to `function_name` (for debugging purposes).
#
#   FUTURE:
#
#       1)  Will emulate exception chaining in python 2.*.
#
#       2)  Will rename the function to `function_name` (for debuggging purposes).
#
def produce_PREPARE_Exception(function_name, Exception_Class):
   #@rename(function_name)                      #   Will implement `rename` in the future.
    @creator
    def PREPARE_Exception(message, *arguments):
        if arguments:
            message = message.format(*arguments)

        error = Exception_Class(message)

       #trace('{} => {}', function_name, error)

        return error


    return PREPARE_Exception


PREPARE_AttributeError = produce_PREPARE_Exception('PREPARE_AttributeError', AttributeError)
PREPARE_ValueError     = produce_PREPARE_Exception('PREPARE_ValueError',     ValueError)


#
#   PRODUCE FUNCTIONS AND CLOSURES (very long explanation).
#
#       A produce function, is a function that produces other functions (using closures).
#
#       Produce function are named "produce_*".
#
#       In the code above `produce_PREPARE_Exception` is a produce funtion.
#
#       Each time it is called, it produces another function (using a closure), in this case a closure around
#       `PREPARE_Exception`.
#
#       `produce_PREPARE_Exception` is called twice in the code above:
#
#           PREPARE_AttributeError = produce_PREPARE_Exception('PREPARE_AttributeError', AttributeError)
#           PREPARE_ValueError     = produce_PREPARE_Exception('PREPARE_ValueError',     ValueError)
#
#       It thus produces two functions:
#
#           1)  `PREPARE_AttributeError` which is a closure around `PREPARE_Exception` with two "cell variables":
#
#                   1a) `function_name` is `"PREPARE_AttributeError"`;
#
#                   2a) `Exception_Class` is `AttributeError`.
#
#           2)  `PREPARE_ValueError` which is a closure around `PREPARE_Exception` with two "cell variables":
#
#                   1a) `function_name` is `"PREPARE_ValueError"`;
#
#                   2a) `Exception_Class` is `ValueError`.
#
#       Thus, behavior wise, the two functions produced here `PREPARE_AttributeError` and `PREPARE_ValueError` have the
#       same behavior as the same two functions "Capital.Private.Exeception_V1.py" (where they are defined separately).
#
#
#   CLOSURE
#
#       In python terminology, a closure is produced around a nested inner function (in our case `PREPARE_Exception`)
#       when that line of code is executed by the enclosing function.
#
#
#   FREE VARIABLE
#
#       A "Free Variable", is a variable defined in a nested inner function (in our case `PREPARE_Exception`) that is
#       "free" (does not have an assigned value) when the function is defined.
#
#       For `PREPARE_Exception` there are two "free variables":
#
#           1)  `Exception_Class`
#
#           2)  `function_name`
#
#       When a closure is created, the "cell variables" of the executing outer function are "bound" to the free
#       variables to create a closure.
#
#       Thus for each closure produced the "free variables" are bound to a different set of "cell variables".
#
#   CELL VARIABLE
#
#       A "cell variable", is a variable defined in a outer function that can be "bound" to a free variable
#       when creating a closure.
#
#       For `produced_PREPARE_Exception` there are two "cell variables":
#
#           1)  `Exception_Class`
#
#           2)  `function_name`
#
#
#   DETAILS OF `produce_PREPARE_Exception`
#
#       Lets look at `produce_PREPARE_Exception`
#
if 0:
    code = produce_PREPARE_Exception.func_code

    trace('==== Code for {} ===', code.co_name)

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
#
#       If you change the `if 0:` above to `if 7:` you get the following:
#
#           % ==== Code for produce_PREPARE_Exception ===
#           % Constant #0: None
#           % Constant #1: <code object PREPARE_Exception at 0x..., file ".../Exception_V2.py", line 74>
#           % Local Variable & Function Parameter #0: 'function_name'
#           % Local Variable & Function Parameter #1: 'Exception_Class'
#           % Local Variable #2: 'PREPARE_Exception'
#           % Cell Variable #0: 'Exception_Class'
#           % Cell Variable #1: 'function_name'
#
#       Which means the following:
#
#           1)  `produce_PREPARE_Exception` has two constants:
#
#                   1a)  Constant #0: None
#
#                   1b)  Constant #1: <code object PREPARE_Exception at 0x..., file ".../Exception_V2.py", line 74>
#
#                        This is the template for creating closures.
#
#           2)  `produce_PREPARE_Exception` has three local variables:
#
#                   2a) `function_name`   (a parameter when calling `produce_PREPARE_Exception`);
#
#                   2b) `Exception_Class` (a parameter when calling `produce_PREPARE_Exception`);
#
#                   2c) `PREPARE_Exception` -- This is the local variable the closure around is stored in.
#
#           3)  `produce_PREPARE_Exception` also has two cell variables:
#
#                   3a) `Exception_Class`
#
#                   3b) `function_name`
#
#       As can be seen, as mentioned above, `Exception_Class` and `function_name` are cell variables.
#
#       These values are "bound" to the free variables of `PREPARE_Exception` when a closure is procuced.
#
#
#   DETAILS OF `PREPARE_Exception`
#
#       Lets look at `PREPARE_Exception` (or actually at `PREPARE_AttributeError` which is a closure around
#       `PREPARE_Exception`)
#
if 0:
    function = PREPARE_AttributeError
    code     = function.func_code

    trace('==== Function PREPARE_AttributeError ===')

    for [i, v] in enumerate(function.func_closure):
        trace('Cell #{}: {!r}', i, v.cell_contents)

    trace('==== Code for {} ===', code.co_name)

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
#
#       If you change the `if 0:` above to `if 7:` you get the following:
#
#           % ==== Function PREPARE_AttributeError ===
#           % Cell #0: <type 'exceptions.AttributeError'>
#           % Cell #1: 'PREPARE_AttributeError'
#           % ==== Code for PREPARE_Exception ===
#           % Constant #0: None
#           % Constant #1: '{} => {}'
#           % Local Variable & Function Parameter #0: 'message'
#           % Local Variable #1: 'arguments'
#           % Local Variable #2: 'error'
#           % Free Variable #0: 'Exception_Class'
#           % Free Variable #1: 'function_name'
#
#       Which means the following:
#
#           1)  `PREPARE_AttributeError` has two "cell variables" that are bound to the "free variables":
#
#                   1a) Cell #0: <type 'exceptions.AttributeError'>
#
#                           This is `AttributeError`.
#
#                   1b) Cell #1: 'PREPARE_AttributeError'
#
#                           This is the string `"PREPARE_AttributeError"`.
#
#           2)  `PREPARE_AttributeError` (or the closure around `PREPARE_Exception`) has two constants:
#
#                   1a)  Constant #0: None
#
#                   1b)  Constant #1: '{} => {}'
#
#           2)  `PREPARE_AttributeError` (or the closure around `PREPARE_Exception`) has three local variables:
#
#                   2a) `message`   (a parameter when calling `PREPARE_AttributeError`);
#
#                   2b) `arguments`
#
#                   2c) `error`
#
#           3)  `produce_PREPARE_Exception` also has two free variables:
#
#                   3a) `Exception_Class`
#
#                   3b) `function_name`
#
#       Thus we can see the two free variables are "bound" to the two cell variables:
#
#           Cell #0: `AttributeError`            is "bound" to free variable #0 `Exception_Class`.
#
#           Cell #1: `"PREPARE_AttributeError"`` is "bound" to free variable #1 `function_name`.
#
#   DISASSEMBLING `produce_PREPARE_Exception`
#
#       Lets look at the virtual code for `produce_PREPARE_Exception`:
#
if 0:
    import dis

    dis.dis(produce_PREPARE_Exception)
#
#       If you change the `if 0:` above to `if 7:` you get the following:
#
#            74   0 LOAD_GLOBAL      0 (creator)
#                 3 LOAD_CLOSURE     0 (Exception_Class)
#                 6 LOAD_CLOSURE     1 (function_name)
#                 9 BUILD_TUPLE      2
#                12 LOAD_CONST       1 (<code object PREPARE_Exception at 0x..., file ".../Exception_V2.py", line 74>)
#                15 MAKE_CLOSURE     0
#                18 CALL_FUNCTION    1
#                21 STORE_FAST       2 (PREPARE_Exception)
#
#            86  24 LOAD_FAST        2 (PREPARE_Exception)
#                27 RETURN_VALUE
#
#       which means:
#
#           line 74     push global          `creator`
#                       push cell variable   `Exception_Class`
#                       push cell variable   `function_name`
#                       create a tuple       ((`Exception_Class`, `function_name`)
#                       push code object for `PREPARE_Exception`
#                       create a closure for `PREPARE_Exception` with the tuple ((`Exception_Class`, `function_name`)
#                       call                 @creator (with 1 argument, the closure)
#                       store result in      `PREPARE_Exception`
#
#           line 86     return              `PREPARE_Exception`
#
#       Here for comparasion is the code for `produce_PREPARE_Exception`:
#
#           def produce_PREPARE_Exception(function_name, Exception_Class):
#               @creator                                                        #   line 74
#               def PREPARE_Exception(message, *arguments):
#                   if arguments:
#                       message = message.format(*arguments)
#
#                   error = Exception_Class(message)
#
#                   trace('{} => {}', function_name, error)
#
#                   return error
#
#
#               return PREPARE_Exception                                        #   line 86
#
#       (All the lines beginning with lines 75..84 that `def PREPARE_Exception(...): ...` are in the code object.
#
