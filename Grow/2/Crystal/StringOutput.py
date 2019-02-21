#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    Python_c_StringIO = __import__('cStringIO'   if is_python_2 else   '_io')


    Python_StringIO = Python_c_StringIO.StringIO


    #
    #   NOTE:
    #       In python `Python_StringIO` (i.e.: `cStringIO.StringIO` or `io.StringIO`) does both string input and
    #       string output.
    #
    #       We name it `Python_StringOutput` to indicate we are only using string output (considering this very
    #       different from string input).
    #
    @creator
    def create_Python_StringOutput():
        return Python_StringIO()


    #
    #   StringOutput
    #
    #       `prefix`:          Prefix for a normal line of text
    #       `prefix_blanks`:   `prefix` (striped of trailing spaces) + '\n'
    #
    class StringOutput(Mutable_12):
        __slots__ = (())

        lifecycle = mutable_12_1        #   SimpleContextLifeCycle

        f             = mutable_12_2    #   None | Python_StringOutput
        cached_result = mutable_12_3    #   None | Python_String

        prefix        = mutable_12_4    #   None | ActualString
        prefix_blanks = mutable_12_5    #   ActualString

        position     = mutable_12_6     #   Integer
        total_blanks = mutable_12_7     #   Integer

        f__write                            = mutable_12_8     #   None | Python_Method
        cached__method__line                = mutable_12_9     #   None | Python_Method
        cached__method__query_position      = mutable_12_10    #   None | Python_Method
        cached__method__stash_prefix_blanks = mutable_12_11    #   None | Python_Method
        cached__method__stash_prefix        = mutable_12_12    #   None | Python_Method


        #
        #   Private
        #
        def _close(self):
            assert fact_is_reusable_context_lifecycle_changing(self.lifecycle)
            assert fact_is_not_none                           (self.f)
            assert fact_is_not_none                           (self.f__write)

            f = self.f

            self.f        = none
            self.f__write = none

            f.close()


        def _exit_with_exception(self, e_type, e, traceback):
            if self.f is not none:
                self.lifecycle = reusable_context_lifecycle_changing

                self._close()

            self.lifecycle = reusable_context_lifecycle_exited

            return false


        def _exit_normal(self):
            exit_lifecycle = self.lifecycle.exit_lifecycle

            assert fact_is_not_none(exit_lifecycle)
            assert fact_is_not_none(self.f)
            assert fact_is_not_none(self.f__write)
            assert fact_is_none    (self.cached_result)

            if exit_lifecycle is reusable_context_lifecycle_exited:
                self.lifecycle = reusable_context_lifecycle_changing

                self.cached_result = self.f.getvalue()

                self._close()

            self.lifecycle = exit_lifecycle

            return false


        def _method__line(self):
            r = self.cached__method__line

            if r is none:
                r = self.line

                self.cached__method__line = r

            return r


        def _method__query_position(self):
            r = self.cached__method__query_position

            if r is none:
                r = bind_method(query__StringOutput__position, self)

                self.cached__method__query_position = r

            return r


        def _method__stash_prefix(self):
            r = self.cached__method__stash_prefix

            if r is none:
                r = bind_method(stash__StringOutput__prefix, self)

                self.cached__method__stash_prefix = r

            return r


        def _method__stash_prefix_blanks(self):
            r = self.cached__method__stash_prefix_blanks

            if r is none:
                r = bind_method(stash__StringOutput__prefix_blanks, self)

                self.cached__method__stash_prefix_blanks = r

            return r


        def _open(self):
            assert fact_is_reusable_context_lifecycle_changing(self.lifecycle)
            assert fact_is_none                               (self.f)
            assert fact_is_none                               (self.f__write)

            f        = create_Python_StringOutput()
            f__write = f.write

            self.f        = f
            self.f__write = f__write


        #
        #   Public
        #
        def __dtor__(self):
            self.lifecycle = reusable_context_lifecycle_changing

            if self.f is not none:
                self._close()

            self.cached_result = none


        def __enter__(self):
            lifecycle = self.lifecycle

            assert lifecycle.is_created_or_reusable

            if lifecycle is reusable_context_lifecycle_created:
                self.lifecycle = reusable_context_lifecycle_changing

                self._open()

            self.lifecycle = reusable_context_lifecycle_entered

            return self


        def __exit__(self, e_type, e, e_traceback):
            if e is not none:
                return self._exit_with_exception(e_type, e, e_traceback)

            assert fact_is_none(e)
            assert fact_is_none(e_traceback)

            return self._exit_normal()


        def blank(self):
            assert self.position == 0

            if self.total_blanks == 0:
                self.total_blanks = 1


        def blank2(self):
            assert self.position is 0

            if 0 <= self.total_blanks < 2:
                self.total_blanks = 2


        def blank_suppress(self):
            assert self.position is 0

            self.total_blanks = -1


        def change_prefix(self, prefix):
            assert self.prefix is none

            prefix_without_trailing_spaces = prefix.rstrip()

            if prefix_without_trailing_spaces == '':
                old__prefix_blanks          = none
                new__prefix_blanks          = none
                method__stash_prefix_blanks = none
            else:
                old__prefix_blanks          = self.prefix_blanks
                new__prefix_blanks          = prefix_without_trailing_spaces + '\n'
                method__stash_prefix_blanks = self._method__stash_prefix_blanks()

            return create_ChangePrefix(
                        none,                           #   old__prefix
                        old__prefix_blanks,             #   old__prefix_blanks

                        none,                           #   method__line
                        none,                           #   method__query_position
                        self._method__stash_prefix(),   #   method__stash_prefix
                        method__stash_prefix_blanks,    #   method__stash_prefix_blanks

                        none,                           #   ending

                        prefix,                         #   new__prefix
                        new__prefix_blanks,             #   new__prefix_blanks
                   )


        def flush(self):
            if self.position:
                self.f__write('\n')
                self.position = 0

            total_blanks = self.total_blanks

            if total_blanks > 0:
                self.f__write(self.prefix_blanks * total_blanks)

            self.total_blanks = 0


        def indent(self, header = none, ending = none, prefix = 4):
            assert fact_is__none__or__actual_string(header)
            assert fact_is__none__or__actual_string(ending)
            assert fact_is_positive_integer        (prefix)

            if header is not none:
                self.line(header)

            if ending is none:
                method__line           = none
                method__query_position = none
            else:
                method__line           = self._method__line()
                method__query_position = self._method__query_position()

            old__prefix = self.prefix

            if old__prefix is none:
                new__prefix = prefix * ' '
            else:
                new__prefix = old__prefix + prefix * ' '

            return create_ChangePrefix(
                        old__prefix,                    #   old__prefix
                        none,                           #   old__prefix_blanks

                        method__line,                   #   method__line
                        method__query_position,         #   method__query_position
                        self._method__stash_prefix(),   #   method__stash_prefix
                        none,                           #   method__stash_prefix_blanks

                        ending,                         #   ending

                        new__prefix,                    #   new__prefix
                        none,                           #   new__prefix_blanks
                   )


        def indent_2(self, header = none, ending = none):
            return self.indent(header, ending, 2)


        def line(self, message, *arguments):
            assert fact_is_python_string(message)

            if arguments:
                message = message.format(*arguments)

            self.f__write(message + '\n')


        def line(self, message = none, *arguments):
            assert fact_is_reusable_context_lifecycle_entered(self.lifecycle)
            assert fact_is_not_none                          (self.f)
            assert fact_is_not_none                          (self.f__write)

            assert fact_is__none__or__actual_string(message)

            if self.position:
                #
                #   Finish current line (does not alter `total_blanks`)
                #
                self.position = 0

                if message is none:
                    assert length(arguments) is 0

                    self.f__write('\n')
                    return

                if arguments:
                    message = message.format(*arguments)

                self.f__write(message + '\n')
                return

            total_blanks = self.total_blanks

            if message is none:
                assert length(arguments) is 0

                #
                #   Always write this [explicit] blank line out (even if blanks are currently disabled; or *IF* blanks
                #   are disabled in the future).
                #
                self.f__write(self.prefix_blanks)

                if total_blanks > 0:
                    self.blanks = total_blanks - 1

                return

            prefix = self.prefix

            if arguments:
                message = message.format(*arguments)

            if prefix is none:
                if total_blanks > 0:
                    self.f__write(self.prefix_blanks * total_blanks + message + '\n')
                else:
                    self.f__write(message + '\n')
            else:
                if total_blanks > 0:
                    self.f__write(self.prefix_blanks * total_blanks + prefix + message + '\n')
                else:
                    self.f__write(prefix + message + '\n')

            #
            #   Always `.total_blanks = 0`; that way even if was previously `-1`, it is reset to `0`.
            #
            self.total_blanks = 0


        @property
        def result(self):
            lifecycle = self.lifecycle

            if lifecycle is reusable_context_lifecycle_exception:
                attribute_error = PREPARE_AttributeError(
                                      "`StringOutput.result`: context handler for `with` clause exited {}",
                                      "with an exception; no `.result` available",
                                  )

                raise attribute_error


            if lifecycle is not reusable_context_lifecycle_exited:
                attribute_error = PREPARE_AttributeError(
                                      "`StringOutput.result`: can only be queried after context handler {}",
                                      "for `with` clause has exited (without an exception)",
                                  )

                raise attribute_error

            assert fact_is_not_none(self.cached_result)

            return self.cached_result


    stash__StringOutput__prefix        = StringOutput.prefix       .__set__
    stash__StringOutput__prefix_blanks = StringOutput.prefix_blanks.__set__


    @share
    @creator
    def create_StringOutput():
        return create_mutable_12(
                   StringOutput,                                #   `self = python_new_vacant_object_instance(StringOutput)`

                   reusable_context_lifecycle_created,          #   `self.lifecycle = reusable_context_lifecycle_created`

                   none,                                        #   `self.f             = none`
                   none,                                        #   `self.cached_result = none`

                   none,                                        #   `self.prefix        = none`
                   '\n',                                        #   `self.prefix_blanks = "\n"`

                   0,                                           #   `self.position     = 0`
                   -1,                                          #   `self.total_blanks = -1`

                   none,                                        #   `self.f__write                            = none`
                   none,                                        #   `self.cached__method__alter_prefix_blanks = none`
                   none,                                        #   `self.cached__method__alter_prefix        = none`
                   none,                                        #   `self.cached__method__line                = none`
                   none,                                        #   `self.cached__method__query_position      = none`
               )
