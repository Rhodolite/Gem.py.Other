#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Thread')
def module():
    require_module('LockFree.Core')


    @export
    class BaseThread(Object):
        __slots__ = ((
            'thread_number',            #   Integer
            'thread_identifier',        #   Integer | None
            'thread_lock',              #   thread.LockType
        ))


        def __init__(t, thread_number, thread_lock):
            t.thread_number     = thread_number
            t.thread_identifier = none
            t.thread_lock       = thread_lock


        def __repr__(t):
            #if t.thread_identifier is not none:
            #    return arrange("<Thread #%d; identifier %s>", t.thread_number, t.thread_identifier)

            return arrange("<Thread #%d>", t.thread_number)


        def start(t):
            start_new_thread(BaseThread.wrapper, ((t,)))


        def wait(t):
            t.thread_lock.acquire()


        def wrapper(t):
            try:
                t.thread_identifier = thread_identifier()

                t.run()
            except:
                with except_any_clause() as e:
                    print_exception_chain(e)

            t.thread_lock.release()


    @export
    def create_Thread(Meta, thread_number, *other):
        lock = allocate_lock()

        lock.acquire()

        r = Meta(thread_number, lock, *other)

        return r
