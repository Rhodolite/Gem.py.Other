#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Diamond.Shared')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Interval')
    require_gem('Diamond.LifeCycle')


    class DiamondShared(Object):
        __slots__ = ((
            'status',                   #   Integer
            'chore',                    #   DiamondChore | Zero
            'priority',                 #   Integer

            'left_status',              #   Integer
            'left',                     #   DiamondChore | Zero

            'right_status',             #   Integer
            'right',                    #   DiamondChore | Zero
        ))


        def __init__(t):
            t.status       = LIFE_CYCLE_ACTIVE__1
            t.chore        = 0
            t.priority     = 0

            t.left_status = LIFE_CYCLE_ACTIVE
            t.left        = 0

            t.right_status = LIFE_CYCLE_ACTIVE
            t.right        = 0


        def ATOMIC_INCREMENT__priority(t):
            LARGE_CHECK_INTERVAL()

            priority = t.priority = t.priority +1

            NORMAL_CHECK_INTERVAL()

            return priority


        def COMPARE_AND_SWAP__chore(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.chore

            if r is before:
                t.chore = after

            NORMAL_CHECK_INTERVAL()

            return r


        def COMPARE_AND_SWAP__left(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.left

            if r is before:
                t.left = after

            NORMAL_CHECK_INTERVAL()

            return r


        def COMPARE_AND_SWAP__right(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.right

            if r is before:
                t.right = after

            NORMAL_CHECK_INTERVAL()

            return r


        def fetch_left_0(t, thread_number):
            left = t.left

            if left is 0:
                return 0

            left.ATOMIC_INCREMENT__lifecycle()

            if left is t.left:
                return left

            #
            #   left is no longer valid
            #
            line('#%d: OOPS -- grabbed an INVALID left %s ...', thread_number, left)
            left.release()
            return 0


        def fetch_left_0__AND__increment_count(t, thread_number):
            left = t.left

            if left is 0:
                return 0

            left.ATOMIC_INCREMENT__lifecycle__DOUBLE()

            if left is t.left:
                return left

            #
            #   left is no longer valid
            #
            line('#%d: OOPS -- grabbed an INVALID left %s ...', thread_number, left)
            left.release__DOUBLE()
            return 0


        def fetch_right_0(t, thread_number):
            right = t.right

            if right is 0:
                return 0

            right.ATOMIC_INCREMENT__lifecycle()

            if right is t.right:
                return right

            #
            #   right is no longer valid
            #
            line('#%d: OOPS -- grabbed an INVALID right %s ...', thread_number, right)
            right.release()
            return 0


        def fetch_right_0__AND__increment_count(t, thread_number):
            right = t.right

            if right is 0:
                return 0

            right.ATOMIC_INCREMENT__lifecycle__DOUBLE()

            if right is t.right:
                return right

            #
            #   right is no longer valid
            #
            line('#%d: OOPS -- grabbed an INVALID right %s ...', thread_number, right)
            right.release__DOUBLE()
            return 0


        def __repr__(t):
            LARGE_CHECK_INTERVAL()

            status       = t.status
            chore        = t.chore
            priority     = t.priority

            left_status  = t.left_status
            left         = t.left

            right_status = t.right_status
            right        = t.right

            NORMAL_CHECK_INTERVAL()

            status_name = life_cycle_map[status & LIFE_CYCLE_MASK]
            count       = status & COUNT_MASK

            left_status_name = life_cycle_map[left_status & LIFE_CYCLE_MASK]
            left_count       = left_status & COUNT_MASK

            right_status_name = life_cycle_map[right_status & LIFE_CYCLE_MASK]
            right_count       = right_status & COUNT_MASK

            return arrange('<DiamondShared %s %d %s; %d; %s %d %s; %s %d %s>',
                           status_name,       count,       chore,
                           priority,
                           left_status_name,  left_count,  left,
                           right_status_name, right_count, right)


    @share
    def create_DiamondShared():
        return DiamondShared()
