#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Development')
def module():
    class DevelopmentThread(BaseThread):
        __slots__ = ((
            'ephemeral',                #   FibonacciEphemeral
            'shared',                   #   Shared
        ))


        def __init__(t, thread_number, lock, ephemeral, shared):
            BaseThread.__init__(t, thread_number, lock)

            t.ephemeral = ephemeral
            t.shared    = shared


        def run(t):
            line('Now running: %s', t)

            ephemeral     = t.ephemeral
            shared        = t.shared
            thread_number = t.thread_number
            use_right     = (7   if thread_number & 1 else   0)

            while ephemeral.atom.second < 100:
                priority = t.shared.ATOMIC_INCREMENT__priority()
                my_chore = create_DiamondChore(priority, t, ephemeral)

                line('#%d: created %s', thread_number, my_chore)

                if use_right:
                    if shared.left is none:
                        previous = shared.COMPARE_AND_SWAP__chore(0, my_chore)

                        success = (7   if previous is 0 else   0)
                    else:
                        success = 0

                    if success is 0:
                        #assert shared.right_status == LIFE_CYCLE_ACTIVE
                        assert shared.right        is 0

                        #shared.right_status = LIFE_CYCLE_USING__1
                        shared.right        = my_chore
                else:
                    if shared.right is none:
                        previous = shared.COMPARE_AND_SWAP__chore(0, my_chore)

                        success = (7   if previous is 0 else   0)
                    else:
                        success = 0

                    if success is 0:
                        #assert shared.left_status == LIFE_CYCLE_ACTIVE
                        assert shared.left        is 0

                        #shared.left_status = LIFE_CYCLE_USING__1
                        shared.left        = my_chore

                sleep(0.00001)

                while (my_chore is not 0) and (my_chore.done is 0):
                    chore = shared.chore

                    if my_chore is not chore:
                        if chore is 0:
                            if use_right:
                                if shared.right != my_chore:
                                    line('#%d: my_chore is no longer in the "right" slot ... %s',
                                         thread_number, my_chore)

                                    assert my_chore.done is 7

                                    my_chore.release(thread_number)
                                    my_chore = 0
                                    break

                                left  = shared.fetch_left_0__AND__increment_count(thread_number)
                                right = my_chore
                            else:
                                if shared.left != my_chore:
                                    line('#%d: my_chore is no longer in the "left" slot ... %s',
                                         thread_number, my_chore)

                                    assert my_chore.done is 7

                                    my_chore.release(thread_number)
                                    my_chore = 0
                                    break

                                left  = my_chore
                                right = shared.fetch_right_0__AND__increment_count(thread_number)

                            if (right is 0) or ((left is not 0) and (left.priority < right.priority)):
                                previous = shared.COMPARE_AND_SWAP__chore(0, left)

                                if previous is 0:
                                    #
                                    #   The extra reference count taken above is now used by 'shared.chore'
                                    #
                                    line('#%d: swapped in "left" slot into chore ... %s', thread_number, left)
                                else:
                                    line('#%d: FAILED to swap in "left" slot into chore ... %s', thread_number, left)

                                    if left is not my_chore:
                                        line('#%d: releasing left (due to FAILED swap) ... %s', thread_number, left)
                                        left.release(thread_number)

                                if (right is not 0) and (right is not my_chore):
                                    line('#%d: releasing "right" (not my_chore & not relevant) ... %s', thread_number, right)
                                    right.release(thread_number)

                                previous = shared.COMPARE_AND_SWAP__left(left, 0)

                                if previous is left:
                                    line('#%d: cleared "left" ... %s', thread_number, left)
                                    left.release(thread_number)
                                else:
                                    line('#%d: FAILED TO clear "left" ... %s', thread_number, left)

                                chore = left
                            else:
                                previous = shared.COMPARE_AND_SWAP__chore(0, right)

                                if previous is 0:
                                    #
                                    #   The extra reference count taken above is now used by 'shared.chore'
                                    #
                                    line('#%d: swapped in "right" slot into chore ... %s', thread_number, right)
                                else:
                                    line('#%d: FAILED to swap in "right" slot into chore ... %s', thread_number, right)

                                    if right is not my_chore:
                                        line('#%d: releasing right (due to FAILED swap) ... %s', thread_number, right)
                                        right.release(thread_number)

                                if (left is not 0) and (left is not my_chore):
                                    line('#%d: releasing "left" (not my_chore & not relevant) ... %s', thread_number, left)
                                    left.release(thread_number)

                                previous = shared.COMPARE_AND_SWAP__right(right, 0)

                                if previous is right:
                                    line('#%d: cleared "right" ... %s', thread_number, right)
                                    right.release(thread_number)
                                else:
                                    line('#%d: FAILED TO clear "right" ... %s', thread_number, right)

                                chore = right

                            left  = 0
                            right = 0
                        else:
                            chore.ATOMIC_INCREMENT__lifecycle()

                            if chore is not shared.chore:                       #   Chore is now longer valid
                                line('#%d: OOPS -- grabbed an INVALID chore %s ...', thread_number, chore)
                                chore.release(thread_number)
                                continue

                    chore.chore()

                    assert chore.done is 7

                    previous = shared.COMPARE_AND_SWAP__chore(chore, 0)

                    if previous is chore:
                        line('#%d: removed active chore %s', thread_number, chore)

                        chore.removing = 7

                        if chore is my_chore:
                            my_chore.release__DOUBLE(thread_number)
                            my_chore  = 0
                        else:
                            chore.release(thread_number)
                    else:
                        line('#%d: FAILED to remove active chore %s', thread_number, chore)

                        if chore is my_chore:
                            my_chore.release(thread_number)
                            my_chore = 0


    @share
    def command_development():
        line('check_interval is %d', fetch_check_interval())

        ephemeral = create_Fibonacci()
        shared    = create_DiamondShared()

        line('shared: %s', shared)

        thread_many = []

        append_thread = thread_many.append

        for thread_number in iterate_range(2):
            thread = create_Thread(DevelopmentThread, thread_number, ephemeral, shared)

            append_thread(thread)

            thread.start()

        for v in thread_many:
            line("Waiting for %s to exit ...", v)
            v.wait()
            line("... done waiting for %s to exit", v)
