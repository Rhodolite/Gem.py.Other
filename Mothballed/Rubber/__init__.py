#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Rubber')
def module():
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'privileged')


    require_module('Rubber.ElasticSearch')                              #   Must appear after transport of `privileged`
    require_module('Rubber.Development')
