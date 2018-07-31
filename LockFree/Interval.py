#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('LockFree.Interval')
def gem():
    require_gem('LockFree.Core')


    check_interval = fetch_check_interval()


    NORMAL_CHECK_INTERVAL = Method(change_check_interval, check_interval)
    LARGE_CHECK_INTERVAL  = Method(change_check_interval, check_interval + 7777777)


    share(
        'NORMAL_CHECK_INTERVAL',    NORMAL_CHECK_INTERVAL,
        'LARGE_CHECK_INTERVAL',     LARGE_CHECK_INTERVAL,
    )
