#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    class ChangePrefix(Mutable_10):
        __slots__ = (())

        lifecycle                   = mutable_10_1      #   LifeCycle

        old__prefix                 = mutable_10_2      #   None | String
        old__prefix_blanks          = mutable_10_3      #   None | String

        method__line                = mutable_10_4      #   None | Python_Method
        method__query_position      = mutable_10_5      #   None | Python_Method
        method__stash_prefix        = mutable_10_6      #   Python_Method
        method__stash_prefix_blanks = mutable_10_7      #   None | Python_Method

        ending                      = mutable_10_8      #   None | String

        new__prefix                 = mutable_10_9      #   String
        new__prefix_blanks          = mutable_10_10     #   None | String


        #
        #   Private
        #
        def _pop_prefix(self):
            self.method__stash_prefix(self.old__prefix)

            method__stash_prefix_blanks = self.method__stash_prefix_blanks

            if method__stash_prefix_blanks is none:
                assert self.old__prefix_blanks is none
            else:
                method__stash_prefix_blanks(self.old__prefix_blanks)


        def _push_prefix(self):
            self.method__stash_prefix(self.new__prefix)

            method__stash_prefix_blanks = self.method__stash_prefix_blanks

            if method__stash_prefix_blanks is none:
                assert self.new__prefix_blanks is none
            else:
                method__stash_prefix_blanks(self.new__prefix_blanks)


        def _exit_with_exception(self, e_type, e, traceback):
            self.lifecycle = simple_context_lifecycle_changing

            self._pop_prefix()

            self.lifecycle = simple_context_lifecycle_exception

            return false


        def _exit_normal(self):
            exit_lifecycle = self.lifecycle.exit_lifecycle

            assert fact_is_not_none(exit_lifecycle)

            self.lifecycle = simple_context_lifecycle_changing

            self._pop_prefix()

            ending = self.ending

            if ending is not none:
                method__line = self.method__line

                if self.method__query_position():
                    method__line()

                method__line(ending)

            self.lifecycle = exit_lifecycle

            return false


        #
        #   Public
        #
        def __enter__(self):
            assert self.lifecycle.is_created_or_reusable

            self.lifecycle = reusable_context_lifecycle_changing

            self._push_prefix()

            self.lifecycle = reusable_context_lifecycle_entered

            return self


        def __exit__(self, e_type, e, e_traceback):
            if e is not none:
                assert fact_is_not_none(e_type)
                assert fact_is_not_none(e_traceback)

                return self._exit_with_exception(e_type, e, e_traceback)

            assert fact_is_none(e_type)
            assert fact_is_none(e_traceback)

            return self._exit_normal()


        def reuse(self):
            assert fact_is_reusable_context_lifecycle_entered(self.lifecycle)

            self.lifecycle = reusable_context_lifecycle_reusing

            return self


    @share
    @creator
    def create_ChangePrefix(
            old__prefix, old__prefix_blanks,
            method__line, method__query_position, method__stash_prefix, method__stash_prefix_blanks,
            ending, new__prefix, new__prefix_blanks,
    ):
        if method__query_position is none:
            assert ending is none
        else:
            assert ending is not none

        if method__stash_prefix_blanks is none:
            assert old__prefix_blanks is new__prefix_blanks is none
        else:
            assert old__prefix_blanks is not none
            assert new__prefix_blanks is not none

        if method__line is none:
            assert ending is none
        else:
            assert ending is not none

        return create_mutable_10(
                   ChangePrefix,                        #   `self = python_new_vacant_object_instance(ChangePrefix)`

                   reusable_context_lifecycle_created,  #   `self.lifecycle = reusable_context_lifecycle_created`

                   old__prefix,                         #   `self.old__prefix        = old__prefix`
                   old__prefix_blanks,                  #   `self.old__prefix_blanks = old__prefix_blanks`

                   method__line,                        #   `self.method__line                = method__line`
                   method__query_position,              #   `self.method__query_position      = method__query_position`
                   method__stash_prefix,                #   `self.method__stash_prefix        = method__stash_prefix`
                   method__stash_prefix_blanks,         #   `self.method__stash_prefix_blanks = ...`

                   ending,                              #   `self.ending = ending`

                   new__prefix,                         #   `self.new__prefix        = new__prefix`
                   new__prefix_blanks,                  #   `self.new__prefix_blanks = new__prefix_blanks`
               )
