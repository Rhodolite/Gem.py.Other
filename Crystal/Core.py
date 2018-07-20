#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Crystal.Core')
def gem():
    require_gem('Gem.Cache')


    from Gem import produce_conjure_dual, produce_conjure_triple, produce_conjure_triple__312


    share(
        'produce_conjure_dual',             produce_conjure_dual,
        'produce_conjure_triple',           produce_conjure_triple,
        'produce_conjure_triple__312',      produce_conjure_triple__312,
    )
