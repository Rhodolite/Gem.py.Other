#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Reusable Context Lifecycles:
    #
    #       reusable_context_lifecycle_changing   - The context is changing states.
    #
    #       reusable_context_lifecycle_created    - The context has been created.
    #       reusable_context_lifecycle_entered    - The context has been entered.
    #       reusable_context_lifecycle_exited     - The context has been exited (without an exception)
    #       reusable_context_lifecycle_exception  - The context has been exited with an exception
    #
    #       reusable_context_lifecycle_reusing    - The context will be reused after it has exited.
    #       reusable_context_lifecycle_reusable   - The context has exited (without an exception) and can be reused.
    #
    class ReusableContextLifecycle(Fixed_3):
        __slots__ = (())

        name                   = fixed_3_1      #   ActualString
        is_created_or_reusable = fixed_3_2      #   Boolean
        exit_lifecycle         = fixed_3_3      #   None | ReusableContextLifecycle


        def __repr__(self):
            return arrange('<ReusableContextLifecycle {}>', self.name)


    #
    #   create_ReusableContextLifecycle
    #
    @creator
    def create_ReusableContextLifecycle(
            name,

            changing = false,

            created   = false,
            entered   = false,
            exited    = false,
            exception = false,

            reusing  = false,
            reusable = false,

            exit_lifecycle = none,
    ):
        assert fact_is_actual_string(name)
        assert changing + created + entered + exited + exception + reusing + reusable == 1

        if (entered) or (reusing):
            assert fact_is_not_none(exit_lifecycle)
        else:
            assert fact_is_none(exit_lifecycle)

        interned_name = intern_python_string(name)

        return create_fixed_3(
                   ReusableContextLifecycle,        #   `self = python_new_vacant_object_instance(ReusableContextLifecycle)`

                   interned_name,                   #   `self.name                   = interned_name`
                   (created) or (reusable),         #   `self.is_created_or_reusable = (created) or (reusable)`
                   exit_lifecycle,                  #   `self.exit_lifecycle         = exit_lifecycle`
               )


    reusable_context_lifecycle_changing = create_ReusableContextLifecycle('changing', changing = true)

    reusable_context_lifecycle_created   = create_ReusableContextLifecycle('created',   created   = true)
   #reusable_context_lifecycle_entered   = defined below
    reusable_context_lifecycle_exited    = create_ReusableContextLifecycle('exited',    exited    = true)
    reusable_context_lifecycle_exception = create_ReusableContextLifecycle('exception', exception = true)

   #reusable_context_lifecycle_reusing  = defined below
    reusable_context_lifecycle_reusable = create_ReusableContextLifecycle('reusable', reusable = true)


    #
    #   Defined last as `exit_lifecycle` has to refer to previously defined values
    #
    reusable_context_lifecycle_entered = create_ReusableContextLifecycle(
            'entered', entered = true, exit_lifecycle = reusable_context_lifecycle_exited,
        )

    reusable_context_lifecycle_reusing = create_ReusableContextLifecycle(
            'reusing', reusing = true, exit_lifecycle = reusable_context_lifecycle_reusable,
        )


    if python_debug_mode:
        @share
        def fact_is_reusable_context_lifecycle_changing(v):
            assert v is reusable_context_lifecycle_changing

            return true


        @share
        def fact_is_reusable_context_lifecycle_entered(v):
            assert v is reusable_context_lifecycle_entered

            return true


    share(
            #
            #   Values
            #
            reusable_context_lifecycle_changing = reusable_context_lifecycle_changing,

            reusable_context_lifecycle_created   = reusable_context_lifecycle_created,
            reusable_context_lifecycle_entered   = reusable_context_lifecycle_entered,
            reusable_context_lifecycle_exited    = reusable_context_lifecycle_exited,
            reusable_context_lifecycle_exception = reusable_context_lifecycle_exception,

            reusable_context_lifecycle_reusing  = reusable_context_lifecycle_reusing,
            reusable_context_lifecycle_reusable = reusable_context_lifecycle_reusable,
        )
