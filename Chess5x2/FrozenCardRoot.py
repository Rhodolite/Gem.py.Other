#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Chess5x2.FrozenCardRoot')
def gem():
    @share
    class FrozenCardRoot(Object):
        __slots__ = ((
            'current_attack',           #   Integer
            'current_health',           #   Integer
            'maximum_health',           #   Integer
        ))


        is_blank_square = false
        is_card         = true


        def __init__(t, current_attack, current_health, maximum_health):
            t.current_attack = current_attack
            t.current_health = current_health
            t.maximum_health = maximum_health


        def __repr__(t):
            return arrange('<%s %s>', t.abbreviation, t.portray_numbers())


        def portray_abbreviation(t):
            return t.abbreviation


        def portray_numbers(t):
            if t.maximum_health == t.initial_health:
                return arrange('%d/%d', t.current_attack, t.current_health)

            return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)
