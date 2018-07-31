#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Core')
def module():
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'iterate_range')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'Method')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'Object')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Sleep',                      'sleep')
    transport('Capital.System',                     'change_check_interval')
    transport('Capital.System',                     'fetch_check_interval')
    transport('Capital.Thread',                     'allocate_lock')
    transport('Capital.Thread',                     'start_new_thread')
    transport('Capital.Thread',                     'thread_identifier')
    transport('Capital.Traceback',                  'print_exception_chain')
