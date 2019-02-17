#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    sys                             import  stderr  as  standard_error
from    sys                             import  exit    as  PROGRAM_EXIT


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
def arrange(message, *arguments):
    return message.format(*arguments)


#
#   ERROR - output an error message to standard error
#
def ERROR(format, *arguments):
    message = arrange(format, *arguments)

    standard_error.write(arrange("? {}\n", message))


#
#   FATAL - output an error message to standard error, then EXIT THE PROGRAM.
#
def FATAL(format, *arguments):
    ERROR(format, *arguments)
    PROGRAM_EXIT(1)


#
#   trace - Output a line of text if `tracing` is set.
#
if tracing:
    #
    #   In trace mode, the line of text is prefixed with '% Z.py: ' to identify it as a traced line of text.
    #
    def trace(message, *arguments):
        print('% Z.py: ' + arrange(message, *arguments))
else:
    def trace(message, *arguments):
        '''Do nothing -- since `tracing` is not set.'''
