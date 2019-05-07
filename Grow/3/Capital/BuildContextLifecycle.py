#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.BuildContextLifecyle - Lifecycle for a build context (`with` statement handler)
#


from    Capital.Core                    import  creator
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_changing
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_created
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_entered
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_exited


#
#   Build Context Lifecycles:
#
#       Same as Simple Context LifeCycle:
#
#           build_context_lifecycle_changing    - The context is changing states.
#           build_context_lifecycle_created     - The context has been created.
#           build_context_lifecycle_entered     - The context has been entered.
#           build_context_lifecycle_exited      - The context has exited.
#
#       With two additional states:
#
#           build_context_lifecycle_exception   - The context exited with an exception.
#
#           build_context_lifecycle_iterating   - The context has exited, and is iterating
#                                                 (or has finished iterating).
#
#
#   NOTE #1:
#       Similiar to `SimpleContextLifeCycle', this state machine does not [fully] represent exceptions.
#
#       Any exception leaves the state machine in it's last state, until the underlying structure is
#       garbaged collected & reclaimed.
#
#       Thus, the state machine, can *end* in any state, before being destroyed.
#
#
#   NOTE #2:
#       An exception caught in the `.__exit__` is handled, and represented by `build_context_lifecycle_exception`.
#
#
#   NOTE #3:
#       Similiar to `SimpleContextLifeCycle', there is no state to indicate the underlying structure is being
#       garbage collected & destroyed.
#
#
#   NOTE #4:
#       Due to the way iteration is handled, there is no state to indicate that the iteration has completed.
#
#       Instead `build_context_lifecycle_iterating` is used both to indicate iterating, and that iteration
#       has finished.
#
#       Basically `build_context_lifecycle_iterating` is used to detect (in debug mode) that iteration is only
#       *STARTED* once.
#
#       It is not used to detect (in debug mode) that iteration has finished.
#
#
#   State Machine Picture:
#
#
#                                               build_context_lifecycle_changing    - The context is being created.
#                                                             |
#                     +---------------------------------------+
#                     |
#                     v
#       build_context_lifecycle_created                                             - The context has been created.
#                     |
#                     +---------------------------------------+
#                                                             |
#                                                             v
#                                               build_context_lifecycle_changing    - The context is being entered.
#                                                             |
#                     +---------------------------------------+
#                     |
#                     v
#       build_context_lifecycle_entered                                             - The context has been entered.
#                     |
#                     +---------------------------------------+
#                                                             |
#                                                             v
#                                               build_context_lifecycle_changing    - The context is exiting.
#                                                             |
#                     +---------------------------------------+--------+
#                     |                                                |
#                     |                                                v
#                     |                         build_context_lifecycle_exception   - The context has exited
#                     |                                                               with an exception.
#                     v
#       build_context_lifecycle_exited                                              - The context has exited.
#                     |
#                     +---------------------------------------+
#                                                             |
#                                                             v
#                                               build_context_lifecycle_changing    - The context has exited, and is
#                                                             |                       starting to iterate.
#                     +---------------------------------------+
#                     |
#                     v
#       build_context_lifecycle_exited                                              - The context has exited,
#                                                                                     and is iterating
#                                                                                     (or has finished iterating).
#
#
#   NOTE:
#       These `lifecycles` are only used for debugging (by using assertions) in context handlers ...
#
#       Context handlers are quite complex to write properly (especially handling exceptions in the exception
#       function of a context hander).
#
#       Hence the importance of debugging lifecycle management for context handlers.
#
class BuildContextLifecycle(object):
    __slots__ = ((
        'name',                     #   Full_Native_String
        'exception',                #   Boolean
        'iterating',                #   Boolean
    ))


    changing  = False
    created   = False
    entered   = False
    exited    = False


    def __init__(self, name, exception, iterating):
        self.name      = name
        self.exception = exception
        self.iterating = iterating


    def __repr__(self):
        return arrange('<BuildContextLifecycle {}>', self.name)


@creator
def create_BuildContextLifecycle(
        name,

        changing  = False,
        created   = False,
        entered   = False,
        exception = False,
        exited    = False,
        iterating = False,
):
    assert changing  is False
    assert created   is False
    assert entered   is False
    assert exited    is False
    assert (exception + iterating == 1)

    return BuildContextLifecycle(name, exception, iterating)


build_context_lifecycle_changing = simple_context_lifecycle_changing
build_context_lifecycle_created  = simple_context_lifecycle_created
build_context_lifecycle_entered  = simple_context_lifecycle_entered
build_context_lifecycle_exited   = simple_context_lifecycle_exited

build_context_lifecycle_exception = create_BuildContextLifecycle('exception', exception = True)
build_context_lifecycle_iterating = create_BuildContextLifecycle('iterating', iterating = True)
