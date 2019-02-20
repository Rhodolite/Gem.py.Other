#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
import  sys


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
#
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
#   ERROR - output an error message to standard error
#
def ERROR(message, *arguments):
    message = arrange(message, *arguments)          #   Example: Use case #2 of `arrange` -- see comment above.

    sys.stderr.write(arrange("? {}\n", message))    #   Example: Use case #1 of `arrange` -- see comment above.


#
#   FATAL - output an error message to standard error, then EXIT THE PROGRAM.
#
#   NOTE:
#       Exiting the program is done using `sys.exit` -- which throw a `SystemExit` exception (which can be
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
#       The disabled function below `FATAL_AND_FORCE_EXIT` cannot be unit tested as easily -- thus it is
#       not preferred & is in fact disabled & not used.
#
def FATAL(message, *arguments):
    ERROR(message, *arguments)
    sys.exit(1)

#
#   FATAL_AND_FORCE_EXIT - output an error message to standard error, then FORCE a program exit.
#
#       Example code to force an exit using `sys._exit` -- which does not thrown an exception, cannot be
#       caught & cannot be ignored.
#
#       We don't actually use this yet, so for now this is disabled.
#
#       This code is only shown here to compare & contrast with `FATAL`.
#
if 0:                                                                   #   DISABLED code -- not used.
    def FATAL_AND_FORCE_EXIT(message, *arguments):
        ERROR(message, *arguments)
        sys._exit(1)


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
