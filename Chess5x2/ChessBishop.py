#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Chess5x2.ChessBishop')
def gem():
    require_gem('Chess5x2.CardRoot')


    @export
    class ChessBishop(CardRoot):
        ally_abbreviation  = 'WB'
        enemy_abbreviation = 'BB'
        initial_attack     = 1
        initial_health     = 3


        __slots__ = (())


        def prepare(t, board):
            #
            #   Heal myself, if injured
            #
            if t.current_health < t.maximum_health:
                t.current_health += 1
                return

            #
            #   Otherwise, heal everyone else
            #
            square = t.square

            board.a1.heal_1(board, t)

            if square != square_b1:
                heal_1 = board.b1.heal_1

                if heal_1 != 0:
                    heal_1(board, t)

            if square != square_c1:
                heal_1 = board.c1.heal_1

                if heal_1 != 0:
                    heal_1(board, t)

            if square != square_d1:
                heal_1 = board.d1.heal_1

                if heal_1 != 0:
                    heal_1(board, t)

            if square != square_e1:
                heal_1 = board.e1.heal_1

                if heal_1 != 0:
                    heal_1(board, t)


        def action(t, board):
            north_east = t.square.load_north_east(board)
            north_west = t.square.load_north_west(board)

            if (north_east.is_card) and (north_east.attacked(board, t)):
                if north_west.is_card:
                    north_west.attacked(board, t)

                return

            if (north_west.is_card) and (north_west.attacked(board, t)):
                return

            if (not north_east.is_card) and (not north_west.is_card):
                board.a2.attacked_ignore_shield(board, t)


    @export
    def create_ally_chess_bishop(square, special = false):
        health = ChessBishop.initial_health + (1   if special else   0)

        return ChessBishop(square, true, ChessBishop.initial_attack, health, health)
