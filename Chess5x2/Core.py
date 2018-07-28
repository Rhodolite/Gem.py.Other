#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.Core')
def module():
    require_module('Capital.Cache')


    from Capital import produce_conjure_dual, produce_conjure_triple, produce_conjure_triple__312


    share(
        'produce_conjure_dual',             produce_conjure_dual,
        'produce_conjure_triple',           produce_conjure_triple,
        'produce_conjure_triple__312',      produce_conjure_triple__312,
    )
