#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('MultiProcessingExample.Core')
def gem():
    require_gem('Gem.Exception')
    require_gem('Gem.Traceback')
    require_gem('Gem.System')


    from Gem import execute, Exception, print_exception_chain, program_exit


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
