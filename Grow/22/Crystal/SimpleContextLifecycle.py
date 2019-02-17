#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Simple Context Lifecycles:
    #
    #       simple_context_lifecycle_changing   - The context is changing states.
    #       simple_context_lifecycle_created    - The context has been created.
    #       simple_context_lifecycle_entered    - The context has been entered.
    #       simple_context_lifecycle_exited     - The context has been exited.
    #
    #   NOTE:
    #       These `lifecycles` are only used for debugging (by using assertions) in context handlers ...
    #
    #       Context handlers are quite complex to write properly (especially handling exceptions in the exception
    #       function of a context hander).
    #
    #       Hence the importance of debugging lifecycle management for context handlers.
    #
    class SimpleContextLifecycle(Fixed_5):
        __slots__ = (())


        name     = fixed_5_1            #   ActualString
        changing = fixed_5_2            #   Boolean
        created  = fixed_5_3            #   Boolean
        entered  = fixed_5_4            #   Boolean
        exited   = fixed_5_5            #   Boolean


        def __repr__(self):
            return arrange('<SimpleContextLifecycle {}>', self.name)


    #
    #   create_SimpleContextLifecycle
    #
    @creator
    def create_SimpleContextLifecycle(
            name,

            changing = false,
            created  = false,
            entered  = false,
            exited   = false,
    ):
        assert fact_is_actual_string(name)

        interned_name = intern_python_string(name)

        return create_fixed_5(SimpleContextLifecycle, interned_name, changing, created, entered, exited)


    simple_context_lifecycle_changing = create_SimpleContextLifecycle('changing', changing = true)
    simple_context_lifecycle_created  = create_SimpleContextLifecycle('created',  created = true)
    simple_context_lifecycle_entered  = create_SimpleContextLifecycle('entered',  entered = true)
    simple_context_lifecycle_exited   = create_SimpleContextLifecycle('exited',   exited  = true)


    if python_debug_mode:
        @share
        def fact_is_simple_context_lifecycle_created(v):
            assert v is simple_context_lifecycle_created

            return true


        @share
        def fact_is_simple_context_lifecycle_entered(v):
            assert v is simple_context_lifecycle_entered

            return true


        @share
        def fact_is_simple_context_lifecycle_exited(v):
            assert v is simple_context_lifecycle_exited

            return true


    share(
            #
            #   Values
            #
            simple_context_lifecycle_changing = simple_context_lifecycle_changing,
            simple_context_lifecycle_created  = simple_context_lifecycle_created,
            simple_context_lifecycle_entered  = simple_context_lifecycle_entered,
            simple_context_lifecycle_exited   = simple_context_lifecycle_exited,
        )
