#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Onyx.Development')
def gem():
    require_gem('Onyx.Core')


    def dump_result(name, r):
        line('Dump of %s', name)

        for [k, v] in r.iteritems():
            line('  %s : %s', k, v)


    @share
    def command_development():
        client = elastic___create_connection()
        #line('client: %s', client)

        #client.indices.create(index = 'onyx', ignore = 400)
        r = client.indices.delete(index = 'onyx')
        dump_result('delete index', r)

        #r = client.index(index = 'onyx', doc_type = 'test', id = 1, body = { 'test' : 7 } )
        #dump_result('index', r)

        #r = client.delete(index = 'onyx', doc_type = 'test', id = 1)
        #dump_result('delete', r)

        r = client.index(
            index    = 'onyx',
            doc_type = 'people',
            id      = 1,
            body = {
                'name' : 'Joy',
                'title' : 'Programmer',
            },
        )

        dump_result('people', r)

