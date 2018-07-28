#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('MultiProcessingExample.Core')
def module():
    require_module('Capital.Exception')
    require_module('Capital.Traceback')
    require_module('Capital.System')


    from Capital import execute, Exception, print_exception_chain, program_exit


    share(
        #
        #   Types
        #
        'Exception',                Exception,

        #
        #   Functions
        #
        'execute',                  execute,
        'print_exception_chain',    print_exception_chain,
        'program_exit',             program_exit,
    )
