#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Chess5x2.FrozenChessCard')
def gem():
    require_gem('Chess5x2.ChessBishop')
    require_gem('Chess5x2.ChessKing')
    require_gem('Chess5x2.ChessKnight')
    require_gem('Chess5x2.ChessPawn')
    require_gem('Chess5x2.ChessRook')
    require_gem('Chess5x2.FrozenCardRoot')


    class FrozenAllyChessBishop(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZWB'
        ally           = true
        card_name      = 'Frozen-Ally-Chess-Bishop'
        enemy          = false
        initial_health = ChessBishop.initial_health


    class FrozenAllyChessKing(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZWK'
        ally           = true
        card_name      = 'Frozen-Ally-Chess-King'
        enemy          = false
        initial_health = ChessKing.initial_health


    class FrozenAllyChessKnight(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZWN'
        ally           = true
        card_name      = 'Frozen-Ally-Chess-Knight'
        enemy          = false
        initial_health = ChessKnight.initial_health


    class FrozenAllyChessPawn(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZWP'
        ally           = true
        card_name      = 'Frozen-Ally-Chess-Pawn'
        enemy          = false
        initial_health = ChessPawn.initial_health


    class FrozenAllyChessRook(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZWR'
        ally           = true
        card_name      = 'Frozen-Ally-Chess-Rook'
        enemy          = false
        initial_health = ChessRook.initial_health


    class FrozenEnemyChessBishop(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZBB'
        ally           = false
        card_name      = 'Frozen-Enemy-Chess-Bishop'
        enemy          = true
        initial_health = ChessBishop.initial_health


    class FrozenEnemyChessKing(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZBK'
        ally           = false
        card_name      = 'Frozen-Enemy-Chess-King'
        enemy          = true
        initial_health = ChessKing.initial_health



    class FrozenEnemyChessKnight(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZBN'
        ally           = false
        card_name      = 'Frozen-Enemy-Chess-Knight'
        enemy          = true
        initial_health = ChessKnight.initial_health


    class FrozenEnemyChessPawn(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZBP'
        ally           = false
        card_name      = 'Frozen-Enemy-Chess-Pawn'
        enemy          = true
        initial_health = ChessPawn.initial_health



    class FrozenEnemyChessRook(FrozenCardRoot):
        __slots__ = (())


        abbreviation   = 'ZBR'
        ally           = false
        card_name      = 'Frozen-Enemy-Chess-Rook'
        enemy          = true
        initial_health = ChessRook.initial_health



    FrozenAllyChessBishop.k1 = FrozenAllyChessBishop.current_attack
    FrozenAllyChessBishop.k2 = FrozenAllyChessBishop.current_health
   #FrozenAllyChessBishop.k3 = FrozenAllyChessBishop.maximum_health


    FrozenAllyChessKing.k1 = FrozenAllyChessKing.current_attack
    FrozenAllyChessKing.k2 = FrozenAllyChessKing.current_health
   #FrozenAllyChessKing.k3 = FrozenAllyChessKing.maximum_health


    FrozenAllyChessKnight.k1 = FrozenAllyChessKnight.current_attack
    FrozenAllyChessKnight.k2 = FrozenAllyChessKnight.current_health
   #FrozenAllyChessKnight.k3 = FrozenAllyChessKnight.maximum_health


    FrozenAllyChessPawn.k1 = FrozenAllyChessPawn.current_attack
    FrozenAllyChessPawn.k2 = FrozenAllyChessPawn.current_health
   #FrozenAllyChessPawn.k3 = FrozenAllyChessPawn.maximum_health


    FrozenAllyChessRook.k1 = FrozenAllyChessRook.current_attack
    FrozenAllyChessRook.k2 = FrozenAllyChessRook.current_health
   #FrozenAllyChessRook.k3 = FrozenAllyChessRook.maximum_health


    FrozenEnemyChessBishop.k1 = FrozenAllyChessBishop.current_attack
    FrozenEnemyChessBishop.k2 = FrozenAllyChessBishop.current_health
   #FrozenEnemyChessBishop.k3 = FrozenAllyChessBishop.maximum_health


    FrozenEnemyChessKing.k1 = FrozenAllyChessKing.current_attack
    FrozenEnemyChessKing.k2 = FrozenAllyChessKing.current_health
   #FrozenEnemyChessKing.k3 = FrozenAllyChessKing.maximum_health


    FrozenEnemyChessKnight.k1 = FrozenAllyChessKnight.current_attack
    FrozenEnemyChessKnight.k2 = FrozenAllyChessKnight.current_health
   #FrozenEnemyChessKnight.k3 = FrozenAllyChessKnight.maximum_health


    FrozenEnemyChessPawn.k1 = FrozenAllyChessPawn.current_attack
    FrozenEnemyChessPawn.k2 = FrozenAllyChessPawn.current_health
   #FrozenEnemyChessPawn.k3 = FrozenAllyChessPawn.maximum_health


    FrozenEnemyChessRook.k1 = FrozenAllyChessRook.current_attack
    FrozenEnemyChessRook.k2 = FrozenAllyChessRook.current_health
   #FrozenEnemyChessRook.k3 = FrozenAllyChessRook.maximum_health


    conjure_frozen_ally_chess_bishop  = produce_conjure_triple('frozen_ally_chess_bishop',  FrozenAllyChessBishop)
    conjure_frozen_ally_chess_king    = produce_conjure_triple('frozen_ally_chess_king',    FrozenAllyChessKing)
    conjure_frozen_ally_chess_knight  = produce_conjure_triple('frozen_ally_chess_knight',  FrozenAllyChessKnight)
    conjure_frozen_ally_chess_pawn    = produce_conjure_triple('frozen_ally_chess_pawn',    FrozenAllyChessPawn)
    conjure_frozen_ally_chess_rook    = produce_conjure_triple('frozen_ally_chess_rook',    FrozenAllyChessRook)

    conjure_frozen_enemy_chess_bishop = produce_conjure_triple('frozen_enemy_chess_bishop', FrozenEnemyChessBishop)
    conjure_frozen_enemy_chess_king   = produce_conjure_triple('frozen_enemy_chess_king',   FrozenEnemyChessKing)
    conjure_frozen_enemy_chess_knight = produce_conjure_triple('frozen_enemy_chess_knight', FrozenEnemyChessKnight)
    conjure_frozen_enemy_chess_pawn   = produce_conjure_triple('frozen_enemy_chess_pawn',   FrozenEnemyChessPawn)
    conjure_frozen_enemy_chess_rook   = produce_conjure_triple('frozen_enemy_chess_rook',   FrozenEnemyChessRook)


    share(
        'conjure_frozen_ally_chess_bishop',     conjure_frozen_ally_chess_bishop,
        'conjure_frozen_ally_chess_king',       conjure_frozen_ally_chess_king,
        'conjure_frozen_ally_chess_knight',     conjure_frozen_ally_chess_knight,
        'conjure_frozen_ally_chess_pawn',       conjure_frozen_ally_chess_pawn,
        'conjure_frozen_ally_chess_rook',       conjure_frozen_ally_chess_rook,

        'conjure_frozen_enemy_chess_bishop',    conjure_frozen_enemy_chess_bishop,
        'conjure_frozen_enemy_chess_king',      conjure_frozen_enemy_chess_king,
        'conjure_frozen_enemy_chess_knight',    conjure_frozen_enemy_chess_knight,
        'conjure_frozen_enemy_chess_pawn',      conjure_frozen_enemy_chess_pawn,
        'conjure_frozen_enemy_chess_rook',      conjure_frozen_enemy_chess_rook,
    )
