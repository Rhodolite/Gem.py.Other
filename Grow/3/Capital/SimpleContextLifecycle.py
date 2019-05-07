#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.SimpleContextLifecyle - Lifecycle for a simple context (`with` statement handler)
#


from    Capital.Core                    import  creator
from    Capital.Native_String           import  intern_native_string


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   Simple Context Lifecycles:
#
#       simple_context_changing   - The context is changing states.
#       simple_context_created    - The context has been created.
#       simple_context_entered    - The context has been entered.
#       simple_context_exited     - The context has exited.
#
#
#   NOTE #1:
#       `simple_context_changing` is reused to mean different state changes (see picture of state
#       machine below).
#
#       It is possible to make different states for all these state changes, however, it seems unneccessary.
#
#
#   NOTE #2:
#       This state machine does not represent exceptions.
#
#       Any exception leaves the state machine in it's last state, until the underlying structure is
#       garbaged collected & reclaimed.
#
#       Thus, the state machine, can *end* in any state, before being destroyed.
#
#
#   NOTE #3:
#       There is no state to indicate the underlying structure is being garbage collected & destroyed.
#       (if there was such a state it would be called `simple_context_destroying`; or
#       `simple_context_changing` could be reused).
#
#
#   State Machine Picture:
#
#                                               simple_context_changing   - The context is being created.
#                                                             |
#                     +---------------------------------------+
#                     |
#                     v
#       simple_context_created                                            - The context has been created.
#                     |
#                     +---------------------------------------+
#                                                             |
#                                                             v
#                                               simple_context_changing   - The context is being entered.
#                                                             |
#                     +---------------------------------------+
#                     |
#                     v
#       simple_context_entered                                            - The context has been entered.
#                     |
#                     +---------------------------------------+
#                                                             |
#                                                             v
#                                               simple_context_changing   - The context is exiting.
#                                                             |
#                     +---------------------------------------+
#                     |
#                     v
#       simple_context_exited                                             - The context has exited.
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
class SimpleContextLifecycle(object):
    __slots__ = ((
        'name',           #   ActualString
        'changing',       #   Boolean
        'created',        #   Boolean
        'entered',        #   Boolean
        'exited',         #   Boolean
    ))


    exception = False
    iterating = False


    def __init__(self, name, changing, created, entered, exited):
        self.name     = name
        self.changing = changing
        self.created  = created
        self.entered  = entered
        self.exited   = exited


    def __repr__(self):
        return arrange('<SimpleContextLifecycle {}>', self.name)


@creator
def create_SimpleContextLifecycle(
        name,

        changing = False,
        created  = False,
        entered  = False,
        exited   = False,
):
    assert fact_is_full_native_string(name)
    assert (changing + created + entered + exited == 1)

    interned_name = intern_native_string(name)

    return SimpleContextLifecycle(interned_name, changing, created, entered, exited)


simple_context_lifecycle_changing = create_SimpleContextLifecycle('changing', changing = True)
simple_context_lifecycle_created  = create_SimpleContextLifecycle('created',  created  = True)
simple_context_lifecycle_entered  = create_SimpleContextLifecycle('entered',  entered  = True)
simple_context_lifecycle_exited   = create_SimpleContextLifecycle('exited',   exited   = True)


if __debug__:
    #
    #   Aliases, for better debug code.
    #
    #       So the debug code can say `.lifecycle_created` instead of `.created`
    #       (`.created` might accidently access another class that has a `.created` member).
    #
    SimpleContextLifecycle.lifecycle_changing = SimpleContextLifecycle.changing
    SimpleContextLifecycle.lifecycle_created  = SimpleContextLifecycle.created
    SimpleContextLifecycle.lifecycle_entered  = SimpleContextLifecycle.entered
    SimpleContextLifecycle.lifecycle_exited   = SimpleContextLifecycle.exited


    def fact_is_lifecycle_changing(v):
        assert v.lifecycle_changing

        return True


    def fact_is_lifecycle_created(v):
        assert v.lifecycle_created

        return True


    def fact_is_lifecycle_entered(v):
        assert v.lifecycle_entered

        return True


    def fact_is_lifecycle_exited(v):
        assert v.lifecycle_exited

        return True
