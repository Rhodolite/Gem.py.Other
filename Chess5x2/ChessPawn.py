#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.ChessPawn')
def module():
    require_module('Chess5x2.CardRoot')


    @export
    class ChessPawn(CardRoot):
        __slots__          = (())
        ally_abbreviation  = 'WP'
        enemy_abbreviation = 'BP'
        initial_attack     = 1
        initial_health     = 1


        def action(t, board):
            north_east = t.square.load_north_east(board)

            if (north_east.is_card) and (north_east.attacked(board, t)):
                return

            north_west = t.square.load_north_west(board)

            if (north_west.is_card) and (north_west.attacked(board, t)):
                return

            if (not north_east.is_card) and (not north_west.is_card):
                board.a2.attacked_ignore_shield(board, t)


    @export
    def create_ally_chess_pawn(square, special = false):
        health = ChessPawn.initial_health + (1   if special else   0)

        return ChessPawn(square, true, ChessPawn.initial_attack, health, health)
