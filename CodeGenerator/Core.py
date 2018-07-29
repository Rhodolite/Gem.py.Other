#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CodeGenerator.Core')
def module():
    transport('Capital.Ascii',                      'lookup_ascii')
    transport('Capital.ContextManager',             'empty_context_manager')
    transport('Capital.Core',                       'execute')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.Path',                       'path_join')
    transport('Capital.SimpleStringIO',             'create_SimpleStringOutput')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'program_exit')
    transport('Capital.System',                     'slice_all')
    transport('Capital.Traceback',                  'print_exception_chain')
