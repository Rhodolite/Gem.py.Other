#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Rubber.Development')
def module():
    def dump_result(name, r):
        line('Dump of %s', name)

        for [k, v] in r.iteritems():
            line('  %s : %s', k, v)


    @share
    def command_development():
        client = elastic___create_connection()
        line('client: %s', client)

        client.indices.create(index = 'rubber', ignore = 400)
        r = client.indices.delete(index = 'rubber')
        dump_result('delete index', r)

        #r = client.index(index = 'rubber', doc_type = 'test', id = 1, body = { 'test' : 7 } )
        #dump_result('index', r)

        #r = client.delete(index = 'rubber', doc_type = 'test', id = 1)
        #dump_result('delete', r)

        r = client.index(
            index    = 'rubber',
            doc_type = 'people',
            id      = 1,
            body = {
                'name' : 'Joy',
                'title' : 'Programmer',
            },
        )

        dump_result('people', r)

