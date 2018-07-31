#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Core')
def module():
    require_module('Capital.Cache')
    require_module('Capital.Exception')
    require_module('Capital.Sleep')
    require_module('Capital.System')
    require_module('Capital.Thread')
    require_module('Capital.Traceback')


    from Capital import allocate_lock, change_check_interval, fetch_check_interval
    from Capital import print_exception_chain, produce_conjure_dual, produce_conjure_triple, produce_conjure_triple__312
    from Capital import sleep, start_new_thread, thread_identifier


    share(
        'change_check_interval',            change_check_interval,
        'fetch_check_interval',             fetch_check_interval,
        'print_exception_chain',            print_exception_chain,
        'produce_conjure_dual',             produce_conjure_dual,
        'produce_conjure_triple',           produce_conjure_triple,
        'produce_conjure_triple__312',      produce_conjure_triple__312,
        'sleep',                            sleep,
        'allocate_lock',                    allocate_lock,
        'start_new_thread',                 start_new_thread,
        'thread_identifier',                thread_identifier,
    )
