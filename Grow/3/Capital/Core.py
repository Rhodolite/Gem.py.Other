#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
import  sys


from    Capital.System                  import  exit_thread
from    Capital.Types                   import  BoundMethod


#
#   trace mode.
#
tracing = True


#
#   arrange - A simple wrapper around `.format`.
#
#       This makes the code more readable, instead of:
#
#           'hello {} #{}'.format('world', 7)
#
#       We can use:
#
#           arrange('hello {} #{}', 'world', 7)
#
#       which is more readable as the format string is closer to its arguments.
#       (This is use case #1 of `arrange` -- the primary purpose for the `arrange` function).
#
#   NOTE:
#       The concept of `arrange` taking a `message` argument, followed by it's arguments ....is *COPIED* into all other
#       functions, that take a message with a arguments.
#
#       For example, `ERROR` and `FATAL` below both take a message with arguments, and are based on the parameters to
#       `arrange` (i.e.: take the same parameters with the same meaning).
#
#       To support this use case #1, instead of:
#
#           message.format(*arguments)
#
#       We can also use:
#
#           arrange(message, *arguments)
#
#       (This is use case #2 of `arrange` -- a secondary purpose of the `arrange` function).
#
def arrange(message, *arguments):
    return message.format(*arguments)


#
#   creator(f) - Doesn't do anything at all.
#
#       Used to document that a function is a "create" function and calls a constructor.
#
#   EXAMPLE USAGE:
#
#       See below, the `bind_method` creation function.
#
#       The `@creator` annotation is used on `bind_method` to indicate is the creation function.
#
#       In particular, `bind_method` is the creation function for instances of type "BoundMethod".
#
def creator(f):
    return f


#
#   bind_method(method, instance) - Binds an instance to a method (of that instance's class).
#
@creator
def bind_method(method, instance):
    return BoundMethod(method, instance)


#
#   enumeration(e) - Doesn't do anything at all.
#
#       Used to document that a class is *NOT* really a class, but is actually an enumeration.
#
#   NOTE:
#       The parameter is named `e` (to stand for "enumeration").
#
#       This is a little clearer than naming the parameter "enumeration" (which would be confusing as
#       the parameter would have the same name as the annotation function, also named "enumeration").
#
#   EXAMPLE USAGE:
#
#       In the following example we define an enumeration "Color" with three enumerators "blue", "green", and "red".
#
#       `@enumeration` is used to indicate that "Color" is *NOT* really a class, but is actually an enumeration:
#
#
#           @enumeration
#           class Color(str):
#               __slots__ = (())
#
#
#               def __repr__(self):
#                   return arrange('<Color {}>', self)
#
#
#           Color.blue  = Color('blue')
#           Color.red   = Color('red')
#           Color.green = Color('green')
#
#   SEE ALSO:
#
#       "Z/Tree_Context_2.py" for a real example usage of `@enumeration`.
#
def enumeration(e):
    return e


#
#   ERROR - output an error message to standard error
#
def ERROR(message, *arguments):
    message = arrange(message, *arguments)          #   Example: Use case #2 of `arrange` -- see comment above.

    sys.stderr.write(arrange("? {}\n", message))    #   Example: Use case #1 of `arrange` -- see comment above.


#
#   FATAL - output an error message to standard error, then EXIT THE PROGRAM.
#
#   NOTE:
#       Exiting the program is done using `exit_thread` -- which throw a `SystemExit` exception (which can be
#       caught & ignored).
#
#       In our code, we do not, yet, catch `SystemExit` and ignore it.
#
#   UNIT TESTING:
#
#       It would be quite appropriate for a unit test to catch `SystemExit`, mark the unit test as
#       pass, fail, or error  -- and *THEN* continue to the next unit test.
#
#       Thus `FATAL` is prefered, as it make unit testing better.
#
#       The disabled function below `FATAL_AND_EXIT_PROCESS` cannot be unit tested as easily -- thus it is
#       not preferred & is in fact disabled & not used.
#
def FATAL(message, *arguments):
    ERROR(message, *arguments)
    exit_thread(1)


#
#   FATAL_AND_EXIT_PROCESS - output an error message to standard error, then FORCE a program exit.
#
#       We don't actually use this yet, so for now this is disabled.
#
#       This code is only shown here to compare & contrast with `FATAL`.
#
if 0:                                                                   #   DISABLED code -- not used.
    import  os


    def FATAL_AND_EXIT_PROCESS(message, *arguments):
        ERROR(message, *arguments)
        os._exit(1)


#
#   iterate(v) - create an iterator for `v`
#
from    Capital.BuiltIn     import      iterate


#
#   trace - Output a line of text if `tracing` is set.
#
if tracing:
    #
    #   In trace mode, the line of text is prefixed with '% ' to identify it as a traced line of text.
    #
    def trace(message, *arguments):
        print('% ' + arrange(message, *arguments))
else:
    def trace(message, *arguments):
        '''Do nothing -- since `tracing` is not set.'''
