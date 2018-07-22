#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('LockFree.Status')
def gem():
    require_gem('LockFree.Core')


    STATUS_ACTIVE   = 1
    STATUS_DONE     = 2
    STATUS_REMOVING = 3


    status_map = {
        STATUS_ACTIVE   : "active",
        STATUS_DONE     : "done",
        STATUS_REMOVING : "removing",
    }


    share(
        'STATUS_ACTIVE',    STATUS_ACTIVE,
        'STATUS_DONE',      STATUS_DONE,
        'STATUS_REMOVING',  STATUS_REMOVING,

        'status_map',       status_map,
    )
