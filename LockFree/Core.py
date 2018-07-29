#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Core')
def module():
    require_module('Capital.Sleep')
    require_module('Capital.System')
    require_module('Capital.Thread')
    require_module('Capital.Traceback')


    transport('Capital.Traceback',                  'print_exception_chain')


    from Capital import allocate_lock, change_check_interval, fetch_check_interval
    from Capital import sleep, start_new_thread, thread_identifier


    share(
        'change_check_interval',            change_check_interval,
        'fetch_check_interval',             fetch_check_interval,
        'sleep',                            sleep,
        'allocate_lock',                    allocate_lock,
        'start_new_thread',                 start_new_thread,
        'thread_identifier',                thread_identifier,
    )
