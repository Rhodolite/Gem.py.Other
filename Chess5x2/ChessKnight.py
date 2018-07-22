#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Chess5x2.ChessKnight')
def gem():
    require_gem('Chess5x2.CardRoot')


    @export
    class ChessKnight(CardRoot):
        ally_abbreviation  = 'WN'
        enemy_abbreviation = 'BN'
        initial_attack     = 3
        initial_health     = 4


        __slots__ = (())


        def action(t, board):
            north_ww = t.square.load_north_ww(board)

            if (north_ww.is_card) and (north_ww.attacked(board, t)):
                return

            north_ee = t.square.load_north_ee(board)

            if (north_ee.is_card) and (north_ee.attacked(board, t)):
                return

            if (not north_ww.is_card) and (not north_ee.is_card):
                board.a2.attacked_ignore_shield(board, t)


    @export
    def create_ally_chess_knight(square, special = false):
        health = ChessKnight.initial_health + (1   if special else   0)

        return ChessKnight(square, true, ChessKnight.initial_attack, health, health)
