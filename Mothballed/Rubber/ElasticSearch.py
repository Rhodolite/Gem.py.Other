#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Rubber.ElasticSearch')
def gem():
    share = Shared.share


    @privileged
    def run_privileged_import():
        import sys


        sys.path.append('/usr/local/lib/python2.7/dist-packages')


        import  elasticsearch
        import  elasticsearch_dsl                                       #   "dsl" means "Domain Specific Language"


        del sys.path[-1]


        share(
            #
            #   Types
            #
            #       NOTE:
            #           `ElasticSearch` would be exported with a capital 'S'
            #
            #           Howebver don't use this, intead use `elastic___create_connection`.
            #
            #'ElasticSearch',                   elasticsearch.Elasticsearch,
            #
            'Search',                           elasticsearch_dsl.Search,

            #
            #   Functions
            #
            'elastic___create_connection',     elasticsearch_dsl.connections.create_connection
        )



    run_privileged_import()
