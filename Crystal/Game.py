#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.BlankSquare')
    require_gem('Crystal.Board')
    require_gem('Crystal.ChessBishop')
    require_gem('Crystal.ChessKing')
    require_gem('Crystal.ChessKnight')
    require_gem('Crystal.ChessPawn')
    require_gem('Crystal.ChessRook')
    require_gem('Crystal.Core')
    require_gem('Crystal.FrozenChessCard')
    require_gem('Crystal.Player')
    require_gem('Crystal.Square')
    require_gem('Crystal.VoidSquare')


    def action_and_dump(board, create_1, create_2):
        board.actions(create_1, create_2)
        line('---')
        board.dump_abbreviation()


    def bishop_pawn(board):
        action_and_dump(board, create_ally_chess_bishop, create_ally_chess_pawn)


    def knight_pawn(board):
        action_and_dump(board, create_ally_chess_knight, create_ally_chess_pawn)


    def pawn_pawn(board):
        action_and_dump(board, create_ally_chess_pawn, create_ally_chess_pawn)


    def rook_pawn(board):
        action_and_dump(board, create_ally_chess_rook, create_ally_chess_pawn)


    def command_test():
        line('Z: %s', conjure_frozen_ally_chess_bishop(ChessBishop.initial_attack, ChessBishop.initial_health, ChessBishop.initial_health))


    def command_dump():
        pass
        #line('store_v0:  %s', store_v0)


    @share
    def command_game():
        command_test()
        command_dump()

        return

        board = GameBoard(1, alice, create_enemy_chess_king(), create_ally_chess_king())

        board.dump_abbreviation()

        pawn_pawn(board)            #   Turn 1, Alice:  Pawn, Pawn
        bishop_pawn(board)          #   Turn 1, Bob:    Bishop, Pawn

        bishop_pawn(board)          #   Turn 2, Alice:  Bishop, Pawn
        knight_pawn(board)          #   Turn 2, Bob:    Knight, Pawn

        knight_pawn(board)          #   Turn 3, Alice:  Knight, Pawn
        bishop_pawn(board)          #   Turn 3, Bob:    Bishop, Pawn

        pawn_pawn(board)            #   Turn 4, Alice:  Pawn, Pawn
        rook_pawn(board)            #   Turn 4, Bob:    Rook, Pawn

        rook_pawn(board)            #   Turn 5, Alice:  Rook, Pawn
        pawn_pawn(board)            #   Turn 5, Bob:    Pawn, Pawn

        pawn_pawn(board)            #   Turn 6, Alice:  Pawn, Pawn
        pawn_pawn(board)            #   Turn 6, Bob:    Pawn, Pawn

        pawn_pawn(board)            #   Turn 7, Alice:  Pawn, Pawn
        pawn_pawn(board)            #   Turn 7, Bob:    Pawn, Pawn

        pawn_pawn(board)            #   Turn 8, Alice:  Pawn, Pawn
        pawn_pawn(board)            #   Turn 8, Bob:    Pawn, Pawn
