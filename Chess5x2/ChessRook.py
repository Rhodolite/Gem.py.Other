#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.ChessRook')
def module():
    @export
    class ChessRook(CardRoot):
        __slots__          = (())
        ally_abbreviation  = 'WR'
        enemy_abbreviation = 'BR'
        initial_attack     = 2
        initial_health     = 5


        def action(t, board):
            north = t.square.load_north(board)

            if (north.is_card) and (north.attacked(board, t)):
                return

            if (not north.is_card):
                board.a2.attacked_ignore_shield(board, t)


        def adjust(t, board, created):
            west = t.square.load_west(board)

            if west is created:
                west.shield(board, t, 1)
                return

            east = t.square.load_east(board)

            if east is created:
                east.shield(board, t, 1)


        def prepare(t, board):
            west = t.square.load_west(board)

            if west.is_card:
                west.shield(board, t, 1)

            east = t.square.load_east(board)

            if east.is_card:
                east.shield(board, t, 1)


        def reset(t, board):
            t.current_shield = 1


    @export
    def create_ally_chess_rook(square, special = false):
        health = ChessRook.initial_health + (1   if special else   0)

        return ChessRook(square, true, ChessRook.initial_attack, health, health)
