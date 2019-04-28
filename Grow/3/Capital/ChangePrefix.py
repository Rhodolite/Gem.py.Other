#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.ChangePrefix - Change (and restore) prefix of a "file" like output object
#
#       `ChangePrefix` is currently used by `Build_Lines_of_NativeString` to change (and restore) it's prefix.
#


from    Capital.Core                    import  creator
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_changing
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_created
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_entered
from    Capital.SimpleContextLifecycle  import  simple_context_lifecycle_exited


if __debug__:
    from    Capital.Fact                    import  fact_is_native_none
    from    Capital.Fact                    import  fact_is_not_native_none
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_changing
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_created
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_entered


#
#   ChangePrefix - Change (and restore) prefix of a "file" like output object
#
class ChangePrefix(object):
    __slots__ = ((
        'lifecycle',                    #   SimpleContextLifeCycle

        'old__prefix',                  #   None | NativeString
        'old__prefix_blank',            #   None | NativeString

        'method__line',                 #   None | BoundMethod
        'method__query_position',       #   None | BoundMethod
        'method__stash_prefix',         #   BoundMethod
        'method__stash_prefix_blank',   #   None | BoundMethod

        'ending',                       #   None | NativeString

        'new__prefix',                  #   NativeString
        'new__prefix_blank',            #   None | NativeString
    ))


    def __init__(
            self,
            old_prefix, old__prefix_blank,
            method__line, method__query_position, method__stash_prefix, method__stash_prefix_blank,
            ending,
            new__prefix, new__prefix_blank,
    ):
        self.lifecycle = simple_context_lifecycle_changing

        self.old__prefix       = old_prefix
        self.old__prefix_blank = old__prefix_blank

        self.method__line               = method__line
        self.method__query_position     = method__query_position
        self.method__stash_prefix       = method__stash_prefix
        self.method__stash_prefix_blank = method__stash_prefix_blank

        self.ending = ending

        self.new__prefix       = new__prefix
        self.new__prefix_blank = new__prefix_blank

        self.lifecycle = simple_context_lifecycle_created


    #
    #   Private
    #
    def _pop_prefix(self):
        assert fact_is_lifecycle_changing(self.lifecycle)

        self.method__stash_prefix(self.old__prefix)

        method__stash_prefix_blank = self.method__stash_prefix_blank

        if method__stash_prefix_blank is None:
            assert fact_is_native_none(self.old__prefix_blank)
            return

        method__stash_prefix_blank(self.old__prefix_blank)


    def _push_prefix(self):
        assert fact_is_lifecycle_changing(self.lifecycle)

        self.method__stash_prefix(self.new__prefix)

        method__stash_prefix_blank = self.method__stash_prefix_blank

        if method__stash_prefix_blank is None:
            assert fact_is_native_none(self.new__prefix_blank)
            return

        method__stash_prefix_blank(self.new__prefix_blank)


    def _exit_with_exception(self, e_type, e, traceback):
        self.lifecycle = simple_context_lifecycle_changing

        self._pop_prefix()

        return False


    def _exit_normal(self):
        assert fact_is_lifecycle_entered(self.lifecycle)

        self.lifecycle = simple_context_lifecycle_changing

        self._pop_prefix()

        ending = self.ending

        if ending is not None:
            method__line = self.method__line

            if self.method__query_position():
                method__line()

            method__line(ending)

        self.lifecycle = simple_context_lifecycle_exited

        return False


    #
    #   Public
    #
    def __enter__(self):
        assert fact_is_lifecycle_created(self.lifecycle)

        self.lifecycle = simple_context_lifecycle_changing

        self._push_prefix()

        self.lifecycle = simple_context_lifecycle_entered

        return self


    def __exit__(self, e_type, e, e_traceback):
        if e is not None:
            assert fact_is_not_native_none(e_type)
            assert fact_is_not_native_none(e_traceback)

            return self._exit_with_exception(e_type, e, e_traceback)

        assert fact_is_native_none(e_type)
        assert fact_is_native_none(e_traceback)

        return self._exit_normal()


@creator
def change_prefix(
        old__prefix, old__prefix_blank,
        method__line, method__query_position, method__stash_prefix, method__stash_prefix_blank,
        ending, new__prefix, new__prefix_blank,
):
    if old__prefix_blank is None:
        assert fact_is_native_none(method__stash_prefix_blank)
        assert fact_is_native_none(new__prefix_blank)
    else:
        assert fact_is_not_native_none(method__stash_prefix_blank)
        assert fact_is_not_native_none(new__prefix_blank)

    if ending is None:
        assert fact_is_native_none(method__line)
        assert fact_is_native_none(method__query_position)
    else:
        assert fact_is_not_native_none(method__line)
        assert fact_is_not_native_none(method__query_position)

    assert fact_is_not_native_none(method__stash_prefix)

    return ChangePrefix(
               old__prefix, old__prefix_blank,
               method__line, method__query_position, method__stash_prefix, method__stash_prefix_blank,
               ending,
               new__prefix, new__prefix_blank,
           )
