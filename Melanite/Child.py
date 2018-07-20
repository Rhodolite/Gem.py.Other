#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#


#
#   NOTE:
#       Due to the way the multiprocessing module works we can only pass in pickable functions.
#
#       This means the function has to be defined in a standand python module, so it can be pickled & found again.
#
def pickable_child_calculate(argument):
    import Melanite

    return Melanite.Shared.child_calculate(argument)
