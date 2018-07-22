#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('MultiProcessingExample.Development')
def gem():
    require_gem('MultiProcessingExample.Core')
    require_gem('MultiProcessingExample.Multiprocessing')


    #
    #   NOTE #1:
    #       See Note in 'MultiProcessingExample.Child' on pickling 'pickable_child_calculate'
    #
    #   NOTE #2:
    #       In order to import 'MultiProcessingExample.Child' we have to get around the Gem system, hence create a
    #       privileged function and do a normal python import :(
    #
    @privileged
    def import_pickable_child_calculate():
        from MultiProcessingExample.Child import pickable_child_calculate


        return pickable_child_calculate


    pickable_child_calculate = import_pickable_child_calculate()


    def calculate(value):
        return value * value;


    class CatchException(Object):
        __slots__ = ((
            'caught',                       #   None | Exception+
        ))


        def __init__(t):
            t.caught = none


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, e_traceback):
            if e_type == Exception:
                t.caught = e
                return true


    def create_CatchException():
        return CatchException()


    @share
    def child_calculate(argument):
        with create_CatchException() as catcher:
            [child_name, value] = argument

            if value == 6:
                error_message = arrange('child %r: YUCK -- I dislike the number %d', child_name, value);

                raise Exception(error_message)

            r = calculate(value)

            line('child %r: %d => %d', child_name, value, r)

            return r

        return catcher.caught


    @share
    def command_development():
        pool = create_MultiprocessingPool()

        line('Pool: %s', pool)

        work_assignment = ((
                (('alice',   1)),
                (('bob',     2)),
                (('charles', 3)),
                (('daphne',  4)),
                (('edward',  5)),
                (('faith',   6)),
                (('greg',    7)),
                (('hope',    8)),
                (('irvin',   9)),
            ))

        result = pool.map( pickable_child_calculate, work_assignment)

        line('Initial result: %s', result)

        for [i, v] in enumerate(result):
            if type(v) == Exception:
                result[i] = calculate(work_assignment[i][1])

        line('Fixed  result: %s', result)
