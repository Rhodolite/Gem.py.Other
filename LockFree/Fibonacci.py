#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.Counter')
def module():
    class FibonacciAtom(Object):
        __slots__ = ((
            'first',                    #   Integer
            'second',                   #   Integer
        ))


        def __init__(t, first, second):
            t.first  = first
            t.second = second


        def __repr__(t):
            return arrange("<Fibonacci %d %d>", t.first, t.second)


        def next_atom(t):
            first  = t.first
            second = t.second

            return create_FibonacciAtom(second, first + second)


    class FibonacciEphemeral(Object):
        __slots__ = ((
            'atom',                     #   FibonacciAtom
        ))


        def __init__(t, atom):
            t.atom = atom


        def COMPARE_AND_SWAP__atom(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.atom

            if r is before:
                t.atom = after

            NORMAL_CHECK_INTERVAL()

            return r


        def __repr__(t):
            atom = t.atom

            return arrange("<Fibonacci %d %d>", atom.first, atom.second)


    def create_FibonacciAtom(first, second):
        return FibonacciAtom(first, second)


    @share
    def create_Fibonacci():
        return FibonacciEphemeral(create_FibonacciAtom(1, 1))
