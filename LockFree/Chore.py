#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('LockFree.Chore')
def gem():
    require_gem('LockFree.Core')
    require_gem('LockFree.LifeCycle')


    class DiamondChore(Object):
        __slots__ = ((
            'lifecycle',                #   Integer
            'done',                     #   Integer {0 | 7}
            'removing',                 #   Integer {0 | 7}
            'priority',                 #   Integer
            'thread',                   #   BaseThread+
            'ephemeral',                #   FibonacciEphemeral
            'atom',                     #   FibonacciAtom
        ))


        def __init__(t, priority, thread, ephemeral):
            t.lifecycle = LIFE_CYCLE_ACTIVE__2
            t.done      = 0
            t.removing  = 0
            t.priority  = priority
            t.thread    = thread
            t.ephemeral = ephemeral
            t.atom      = none


        def ATOMIC_DECREMENT__lifecycle(t):
            LARGE_CHECK_INTERVAL()

            lifecycle = t.lifecycle = t.lifecycle - 1

            NORMAL_CHECK_INTERVAL()

            return lifecycle


        def ATOMIC_DECREMENT__lifecycle__DOUBLE(t):
            LARGE_CHECK_INTERVAL()

            lifecycle = t.lifecycle = t.lifecycle - 2

            NORMAL_CHECK_INTERVAL()

            return lifecycle


        def ATOMIC_INCREMENT__lifecycle(t):
            LARGE_CHECK_INTERVAL()

            lifecycle = t.lifecycle = t.lifecycle + 1

            NORMAL_CHECK_INTERVAL()

            return lifecycle


        def ATOMIC_INCREMENT__lifecycle__DOUBLE(t):
            LARGE_CHECK_INTERVAL()

            lifecycle = t.lifecycle = t.lifecycle + 2

            NORMAL_CHECK_INTERVAL()

            return lifecycle


        def release(t, thread_number):
            lifecycle = t.ATOMIC_DECREMENT__lifecycle()

            if lifecycle == LIFE_CYCLE_ACTIVE:
                previous = t.COMPARE_AND_SWAP__lifecycle(LIFE_CYCLE_ACTIVE, LIFE_CYCLE_REMOVING__1)

                if lifecycle != previous:
                    line('#%d: attempted to remove %s; BUT failed; so someone else\'s problem now ...',
                         thread_number, t)
                else:
                    line('#%d: removing %s ...', thread_number, t)


        def release__DOUBLE(t, thread_number):
            lifecycle = t.ATOMIC_DECREMENT__lifecycle__DOUBLE()

            if lifecycle == LIFE_CYCLE_ACTIVE:
                previous = t.COMPARE_AND_SWAP__lifecycle(LIFE_CYCLE_ACTIVE, LIFE_CYCLE_REMOVING__1)

                if lifecycle != previous:
                    line('#%d: attempted to remove %s; BUT failed; so someone else\'s problem now ...',
                         thread_number, t)
                else:
                    line('#%d: removing %s ...', thread_number, t)


        #
        #   Step 1: t.atom        = ephemeral.atom      [CAS]
        #   Step 2: epemeral.atom = t.atom.next_atom()  [CAS]
        #   Step 3: t.done        = 7                   [OVERWRITE]
        #
        def chore(t):
            thread_number = t.thread.thread_number
            ephemeral     = t.ephemeral
            atom          = t.atom

            if atom is none:
                atom = ephemeral.atom

                previous = t.COMPARE_AND_SWAP__atom(none, atom)                 #   ATTEMPT: Step #1 [CAS]

                if previous is none:                                            #   SUCCESS: Step #1 [CAS]
                    line('#%d: step #1 done ... %s ...', thread_number, t)

                    after = atom.next_atom()

                    previous = ephemeral.COMPARE_AND_SWAP__atom(atom, after)    #   ATTEMPT: Step #2 [CAS]

                    t.done = 7                                                  #   STEP #3 [OVERWRITE]

                    if previous is atom:                                        #   SUCCESS: Step #2 [CAS]
                        line('#%d: step #2 done ... %s', thread_number, t)
                    else:                                                       #   FAILED: Step #2 [CAS]
                        line('#%d: attempted to do step #2 ... BUT already done ... %s', thread_number, t)

                    #
                    #   PRIMARY PATH:
                    #       We did Step #1
                    #       Attempted to do Step #2 (Either we did it or someone else did it)
                    #       We did Step #3
                    #
                    return

                #
                #   We TRIED to do step #1; but someone else did it instead ...
                #
                if t.done is 7:
                    line('#%d: attempted to do step #1 ... BUT steps #1, #2 & #3 already done ... %s',
                         thread_number, t)

                    return

                line('#%d: attempted to do step #1 ... BUT step #1 already done (step #3 NOT done) ... %s ...',
                     thread_number, t)

                t.atom = previous
            else:                                                               #   Step #1 already done
                if t.done is 7:                                                 #   Step #1, #2 & #3 already done
                    line('#%d: steps #1, #2, & #3 already done ... %s', thread_number, t)
                    return

                line('#%d: step #1 already done ... %s ...', thread_number, t)

            #
            #   SECONDARY path:
            #       1.  Someone else did step #1:
            #               o   We may have attempted to do step #1 & failed; OR
            #               o   Step #1 was already done before we started.
            #       2.  We did not check if they did Step #2
            #       3.  They did NOT do step #3.
            #
            #       So we need to check if Step #2 needs to be done
            #
            if atom is not ephemeral.atom:                                      #   Step #2 already done
                t.done = 7
                line('#%d: step #2 already done ... %s', thread_number, t)
                return

            after = atom.next_atom()

            previous = ephemeral.COMPARE_AND_SWAP__atom(atom, after)            #   Step #2 [CAS]

            t.done = 7                                                          #   Step #3 [OVERWRITE]

            if previous is atom:                                                #   SUCCESS: Step #2 [CAS]
                line('#%d: step #2 done ... %s', thread_number, t)
            else:                                                               #   FAILED: Step #2 [CAS]
                line('#%d: attempted to do step #2 ... BUT already done ... %s', thread_number, t)


        def COMPARE_AND_SWAP__atom(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.atom

            if r is before:
                t.atom = after

            NORMAL_CHECK_INTERVAL()

            return r


        def COMPARE_AND_SWAP__lifecycle(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.lifecycle

            if r is before:
                t.lifecycle = after

            NORMAL_CHECK_INTERVAL()

            return r


        def __repr__(t):
            LARGE_CHECK_INTERVAL()

            lifecycle = t.lifecycle
            done      = t.done
            removing  = t.removing
            priority  = t.priority
            thread    = t.thread
            ephemeral = t.ephemeral
            atom      = t.atom

            NORMAL_CHECK_INTERVAL()

            status_name = life_cycle_map[lifecycle & LIFE_CYCLE_MASK]
            count       = lifecycle & COUNT_MASK

            return arrange('<DiamondChore %s %s %d %s; %d #%d; %s>',
                           status_name, ('done'   if done else   '-'), count, ('removing'   if removing else   '-'),
                           priority, thread.thread_number,
                           ('none'   if atom is none else   atom))


    @share
    def create_DiamondChore(priority, thread, ephemeral):
        return DiamondChore(priority, thread, ephemeral)
