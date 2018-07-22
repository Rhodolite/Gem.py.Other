#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('MultiProcessingExample.Multiprocessing')
def gem():
    require_gem('MultiProcessingExample.Core')


    @privileged
    def import_multiprocessing():
        import          multiprocessing                     #   Must be @privileged to import multiprocessing


        #
        #   NOTE:
        #       Despite the *FALSE* documentation at https://docs.python.org/2/library/multiprocessing.html
        #       `multiprocess.Pool` is *NOT* a class -- it is a factory function.
        #
        #       (The real class that the factory creates is `multiprocessing.pool.Pool`)
        #
        #   Hence we properly name this 'create_MultiprocessingPoolPool' as it is really a factory that creates
        #   a `multiprocessing.pool.Pool` instance).
        #
        create_MultiprocessingPoolPool = multiprocessing.Pool


        return ((create_MultiprocessingPoolPool,))


    [create_MultiprocessingPoolPool] = import_multiprocessing()


    #
    #   Our wrapper around `multiprocessing.pool.Pool`
    #
    class MultiprocessingPool(Object):
        __slots__ = ((
            'client',                           #   MultiProcessing.Pool.Pool
        ))


        def __init__(t, client):
            t.client = client


        @privileged
        def map(t, f, iterable):
            return t.client.map(f, iterable)


        def __repr__(t):
            return '<MultiprocessingPool>'


    @share
    def create_MultiprocessingPool():
        client = create_MultiprocessingPoolPool()

        return MultiprocessingPool(client)
