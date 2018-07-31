#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CodeGenerator.Core')
def gem():
    require_gem('Gem.Ascii')
    require_gem('Gem.ContextManager')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Path')
    require_gem('Gem.SimpleStringIO')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')


    from Gem import create_DelayedFileOutput, create_SimpleStringOutput, empty_context_manager, execute
    from Gem import lookup_ascii, module_path, path_join, print_exception_chain, program_exit, slice_all


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
