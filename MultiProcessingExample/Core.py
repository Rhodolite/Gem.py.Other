#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('MultiProcessingExample.Core')
def module():
    transport('Capital.Exception',                  'Exception')
    transport('Capital.System',                     'program_exit')
    transport('Capital.Traceback',                  'print_exception_chain')
