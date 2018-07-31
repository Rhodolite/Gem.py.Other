#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.ChessKing')
def module():
    @export
    class ChessKing(CardRoot):
        __slots__          = (())
        ally_abbreviation  = 'WK'
        enemy_abbreviation = 'BK'
        initial_attack     = 1
        initial_health     = 20


        def action(t, board):
            t.square.load_north(board).attacked(board, t)


        def attacked(t, board, attacked_by):
            damage = t.current_attack - t.current_shield

            if damage <= 0:
                return false

            before_1 = attacked_by.portray()
            before_2 = t          .portray()

            health = t.current_health - damage

            if health < 0:
                health = 0

            t.current_health = health

            line('%s: %s attacked %s; result %s', board.player.name, before_1, before_2, t.portray())

            return true


        def attacked_ignore_shield(t, board, attacked_by):
            before_1 = attacked_by.portray()
            before_2 = t          .portray()

            health = t.current_health - attacked_by.current_attack

            if health < 0:
                health = 0

            t.current_health = health

            line('%s: %s attacked (ignore shield) %s; result %s', board.player.name, before_1, before_2, t.portray())


    @export
    def create_ally_chess_king():
        return ChessKing(square_a1, true, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)


    @export
    def create_enemy_chess_king():
        return ChessKing(
                square_b1,
                false,
                ChessKing.initial_attack,
                ChessKing.initial_health,
                ChessKing.initial_health,
            )
