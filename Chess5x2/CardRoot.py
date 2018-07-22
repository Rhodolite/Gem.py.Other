#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Chess5x2.CardRoot')
def gem():
    @export
    class CardRoot(Object):
        adjust          = 0
        prepare         = 0
        is_blank_square = false
        is_card         = true


        __slots__ = ((
            'square',                   #   Square
            'ally',                     #   Boolean
            'current_attack',           #   Integer
            'current_health',           #   Integer
            'current_shield',           #   Integer
            'maximum_health',           #   Integer
        ))


        def __init__(t, square, ally, current_attack, current_health, maximum_health):
            t.square         = square
            t.ally           = ally
            t.current_attack = current_attack
            t.current_health = current_health
            t.current_shield = 0
            t.maximum_health = maximum_health


        @property
        def enemy(t):
            return not t.ally


        def attacked(t, board, by_attacker):
            damage = t.current_attack - t.current_shield

            if damage <= 0:
                return false

            before_1 = by_attacker.portray()
            before_2 = t          .portray()

            health = t.current_health - damage

            if health <= 0:
                square = t.square
                blank  = square.blank

                square.store_center(board, blank)

                line('%s: %s attacked %s; result %s', board.player.name, before_1, before_2, blank.portray())
                return

            t.current_health = health

            line('%s: %s attacked %s; result %s', board.player.name, before_1, before_2, t.portray())

            return true


        def attacked_ignore_shield(t, board, by_attacker):
            before_1 = by_attacker.portray()
            before_2 = t          .portray()

            health = t.current_health - t.current_attack

            if health <= 0:
                square = t.square
                blank  = square.blank

                square.store_center(board, blank)

                line('%s: %s attacked (ignore shield) %s; result %s',
                     board.player.name,
                     before_1,
                     before_2,
                     blank.portray())

                return

            t.current_health = health

            line('%s: %s attacked (ignore shield) %s; result %s', board.player.name, before_1, before_2, t.portray())


        def heal_1(t, board, healed_by):
            if t.current_health < t.maximum_health:
                before_1 = healed_by.portray()
                before_2 = t        .portray()

                t.current_health += 1

                line('%s: %s healed %s; result %s', board.player.name, before_1, before_2, t.portray())
                return


        def mirror(t, square):
            t.square = square
            t.ally   = not t.ally

            return t


        def move(t, board, square):
            before = t.portray()
            t.square = square

            line("%s: moved %s to %s", board.player.name, before, t.portray())

            return t


        def portray(t):
            return arrange("<%s %s>", t.portray_abbreviation(), t.portray_numbers())


        def portray_abbreviation(t):
            return arrange('%s: %s', t.square.name, (t.ally_abbreviation   if t.ally else   t.enemy_abbreviation))


        def portray_numbers(t):
            if t.maximum_health == t.initial_health:
                if t.current_shield == 0:
                    return arrange('%d/%d', t.current_attack, t.current_health)

                return arrange('%d/%d/%d', t.current_attack, t.current_health, t.current_shield)

            if t.current_shield == 0:
                return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)

            return arrange('%d/%d(%d)/%d', t.current_attack, t.current_health, t.maximum_health, t.current_shield)


        def reset(t, board):
            t.current_shield = 0


        def shield(t, board, increased_by, add):
            before_1 = increased_by.portray()
            before_2 = t.portray()

            t.current_shield += add

            line('%s: %s increased shield of %s to %s', board.player.name, before_1, before_2, t.portray())
