#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.Player')
def module():
    class Player(Object):
        __slots__ = ((
            'name',                     #   String+
        ))


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<Player %s>', t.name)


    alice = Player('Alice')
    bob   = Player('Bob')


    share(
        'alice',        alice,
        'bob',          bob,
    )
