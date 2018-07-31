#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('MultiProcessingExample.__init__')
def module():
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'enumerate')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'Object')
    transport('Capital.Core',                       'privileged')
    transport('Capital.Core',                       'true')
    transport('Capital.Core',                       'type')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Exception',                  'Exception')
    transport('Capital.Exception',                  'raise_runtime_error')
    transport('Capital.System',                     'program_exit')
    transport('Capital.Traceback',                  'print_exception_chain')

    require_module('MultiProcessingExample.Multiprocessing')
    require_module('MultiProcessingExample.Development')
