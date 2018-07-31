#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LockFree.LifeCycle')
def module():
    COUNT_MASK      = 0x0f
    LIFE_CYCLE_MASK = 0x70


    LIFE_CYCLE_ACTIVE   = 0x10
    LIFE_CYCLE_USING    = 0x20
    LIFE_CYCLE_REMOVING = 0x30
    LIFE_CYCLE_ZAPPING  = 0x40


    LIFE_CYCLE_ACTIVE__1   = LIFE_CYCLE_ACTIVE | 1
    LIFE_CYCLE_ACTIVE__2   = LIFE_CYCLE_ACTIVE | 2
    LIFE_CYCLE_REMOVING__1 = LIFE_CYCLE_REMOVING | 1
    LIFE_CYCLE_USING__1    = LIFE_CYCLE_USING | 1


    life_cycle_map = {
        LIFE_CYCLE_ACTIVE   : "active",
        LIFE_CYCLE_USING    : "using",
        LIFE_CYCLE_REMOVING : "removing",
        LIFE_CYCLE_ZAPPING  : "zapping"
    }


    share(
        'COUNT_MASK',               COUNT_MASK,
        'LIFE_CYCLE_MASK',          LIFE_CYCLE_MASK,

        'LIFE_CYCLE_ACTIVE',        LIFE_CYCLE_ACTIVE,
        'LIFE_CYCLE_REMOVING',      LIFE_CYCLE_REMOVING,
        'LIFE_CYCLE_USING',         LIFE_CYCLE_USING,
        'LIFE_CYCLE_ZAPPING',       LIFE_CYCLE_ZAPPING,

        'LIFE_CYCLE_ACTIVE__1',     LIFE_CYCLE_ACTIVE__1,
        'LIFE_CYCLE_ACTIVE__2',     LIFE_CYCLE_ACTIVE__2,
        'LIFE_CYCLE_REMOVING__1',   LIFE_CYCLE_REMOVING__1,
        'LIFE_CYCLE_USING__1',      LIFE_CYCLE_USING__1,

        'life_cycle_map',           life_cycle_map,
    )
