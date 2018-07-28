#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CodeGenerator.Core')
def module():
    require_module('Capital.Ascii')
    require_module('Capital.ContextManager')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.Exception')
    require_module('Capital.Path')
    require_module('Capital.SimpleStringIO')
    require_module('Capital.System')
    require_module('Capital.Traceback')


    from Capital import create_DelayedFileOutput, create_SimpleStringOutput, empty_context_manager, execute
    from Capital import lookup_ascii, module_path, path_join, print_exception_chain, program_exit, slice_all


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_SimpleStringOutput',    create_SimpleStringOutput,
        'empty_context_manager',        empty_context_manager,
        'execute',                      execute,
        'lookup_ascii',                 lookup_ascii,
        'path_join',                    path_join,
        'print_exception_chain',        print_exception_chain,
        'program_exit',                 program_exit,


        #
        #   Imported values
        #
        'module_path',                  module_path,
        'slice_all',                    slice_all,
    )
