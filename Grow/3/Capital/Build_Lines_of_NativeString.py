#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Build_Lines_of_NativeString - A "file" like context, that creates lines of text.
#
#       A "file" like context, that creates lines of text (saved as `Native_String`s; i.e.: `str`).
#
#       After the context has exited, it can be iterated, to return the lines of text (as `Native_String`).
#


from    Capital.BuildContextLifecycle   import  build_context_lifecycle_changing
from    Capital.BuildContextLifecycle   import  build_context_lifecycle_created
from    Capital.BuildContextLifecycle   import  build_context_lifecycle_entered
from    Capital.BuildContextLifecycle   import  build_context_lifecycle_exception
from    Capital.BuildContextLifecycle   import  build_context_lifecycle_exited
from    Capital.BuildContextLifecycle   import  build_context_lifecycle_iterating
from    Capital.Build_NativeString      import  build_native_string
from    Capital.ChangePrefix            import  change_prefix
from    Capital.Exception               import  PREPARE_AttributeError
from    Capital.Core                    import  bind_method
from    Capital.Core                    import  creator
from    Capital.Core                    import  iterate
from    Capital.Native_String           import  strip_trailing_whitespace


if __debug__:
    from    Capital.Fact                    import  fact_is_native_none
    from    Capital.Fact                    import  fact_is_not_native_none
    from    Capital.Fact                    import  fact_is_positive_integer
    from    Capital.Native_String           import  fact_is_empty_native_string
    from    Capital.Native_String           import  fact_is__native_none__OR__full_native_string
    from    Capital.Native_String           import  fact_is_some_native_string
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_created
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_entered


#
#   Build_Lines_of_NativeString
#
#   Important Members (excludes members named "_*", or "cached_method__*"):
#
#       .lifecycle         - Current BuildContextLifecycle.
#
#       .lines             - Lines of text.
#
#       .prefix            - Prefix for a normal line of text.
#       .prefix_blank      - Prefix (striped of trailing spaces).
#
#       .position          - Position on a line.
#       .f                 - NativeStringOutput.
#
#       .total_blanks      - Total blank lines queued; OR `-1` to supress blank lines.
#
#
#   Changing the prefix:
#
#       The initial prefix is blank.
#
#       The prefix can be changed with `ChangePrefix` to push a temporary prefix ... by using the python `with` statement.
#
#       When the python `with` statement is exited, the prefix will revert to the previous prefix.
#
def PREPARE__Build_Lines_of_NativeString__iteration__EXCEPTION(message):
    return PREPARE_AttributeError("`Build_Lines_of_NativeString.operator iterate (__iter__)`: {}", message)


class Build_Lines_of_NativeString(object):
    __slots__ = ((
        'lifecycle',                #   BuildContextLifeCycle

        'lines',                    #   Some_Native_List of Some_Native_String
        '_append_line',             #   NativeMethod

        'prefix',                   #   None | Full_Native_String
        'prefix_blank',             #   Some_Native_String

        'position',                 #   SignificantInteger
        'f',                        #   None | BuildNativeString
        '_f__write',                #   None | NativeMethod

        'total_blanks',             #   Integer

        'cached__method__line',                 #   None | NativeMethod
        'cached__method__query_position',       #   None | NativeMethod
        'cached__method__stash_prefix_blank',   #   None | NativeMethod
        'cached__method__stash_prefix',         #   None | NativeMethod
    ))


    #
    #   Constructor
    #
    def __init__(self):
        self.lifecycle = build_context_lifecycle_changing

        self.lines        = lines        = []
        self._append_line = lines.append

        self.prefix       = None
        self.prefix_blank = ''

        self.position  = 0
        self.f         = None
        self._f__write = None

        self.total_blanks = -1

        self.cached__method__line               = None
        self.cached__method__query_position     = None
        self.cached__method__stash_prefix_blank = None
        self.cached__method__stash_prefix       = None

        self.lifecycle = build_context_lifecycle_created


    #
    #   Private
    #
    def _close(self):
        assert fact_is_not_native_none(self.f)
        assert fact_is_not_native_none(self._f__write)

        f = self.f

        self.f         = None
        self._f__write = None

        f.close()


    def _exit_with_exception(self, e_type, e, traceback):
        if self.f is not None:
            self.lifecycle = build_context_lifecycle_changing

            self._close()

        self.lifecycle = build_context_lifecycle_exception

        return False


    def _exit_normal(self):
        assert fact_is_lifecycle_entered(self.lifecycle)

        if self.f is not None:
            self.lifecycle = build_context_lifecycle_changing

            self._close()

        self.lifecycle = build_context_lifecycle_exited

        return False


    def _flush_total_blanks(self):
        total_blanks = self.total_blanks

        assert total_blanks

        if total_blanks > 0:
            _append_line = self._append_line
            prefix_blank = self.prefix_blank

            while True:
                _append_line(prefix_blank)

                if total_blanks == 1:
                    break

                total_blanks -= 1

        self.total_blanks = 0


    def _method__line(self):
        r = self.cached__method__line

        if r is None:
            r = self.cached__method__line = self.line

        return r


    def _method__query_position(self):
        r = self.cached__method__query_position

        if r is None:
            r = self.cached__method__query_position = bind_method(query__Build_Lines_of_NativeString__position, self)

        return r


    def _method__stash_prefix(self):
        r = self.cached__method__stash_prefix

        if r is None:
            r = self.cached__method__stash_prefix = bind_method(stash__Build_Lines_of_NativeString__prefix, self)

        return r


    def _method__stash_prefix_blank(self):
        r = self.cached__method__stash_prefix_blank

        if r is None:
            r = self.cached__method__stash_prefix_blank = (
                    bind_method(stash__Build_Lines_of_NativeString__prefix_blank, self)
                )


        return r


    #
    #   Public
    #
    def __enter__(self):
        assert fact_is_lifecycle_created(self.lifecycle)

       #self.lifecycle = build_context_lifecycle_changing
        self.lifecycle = build_context_lifecycle_entered

        return self


    def __exit__(self, e_type, e, e_traceback):
        if e is not None:
            return self._exit_with_exception(e_type, e, e_traceback)

        assert fact_is_native_none(e)
        assert fact_is_native_none(e_traceback)

        return self._exit_normal()


    def __iter__(self):
        lifecycle = self.lifecycle

        if lifecycle.exception:
            attribute_error = PREPARE__Build_Lines_of_NativeString__iteration__EXCEPTION(
                    "context handler for `with` clause exited with an exception; iteration not available",
                )

            raise attribute_error

        if lifecycle.iterating:
            attribute_error = PREPARE__Build_Lines_of_NativeString__iteration__EXCEPTION(
                    "has already been iterated once; cannot iterate another time",
                )

            raise attribute_error

        if not lifecycle.exited:
            attribute_error = PREPARE__Build_Lines_of_NativeString__iteration__EXCEPTION(
                    "context handler for `with` clause has not yet exited; cannot iterate yet",
                )

            raise attribute_error


        self.lifecycle = build_context_lifecycle_iterating

        return iterate(self.lines)


    def arrange(self, message, *arguments):
        self.write(message.format(*arguments))


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
        assert fact_is_native_none        (self.prefix)
        assert fact_is_empty_native_string(self.prefix_blank)
        assert fact_is_some_native_string (prefix)

        new__prefix_blank = strip_trailing_whitespace(prefix)

        if len(new__prefix_blank) == 0:
            old__prefix_blank          = None
            new__prefix_blank          = None
            method__stash_prefix_blank = None
        else:
            old__prefix_blank          = self.prefix_blank
            method__stash_prefix_blank = self._method__stash_prefix_blank()

        return change_prefix(
                    None,                           #   old__prefix
                    old__prefix_blank,              #   old__prefix_blank

                    None,                           #   method__line
                    None,                           #   method__query_position
                    self._method__stash_prefix(),   #   method__stash_prefix
                    method__stash_prefix_blank,     #   method__stash_prefix_blank

                    None,                           #   ending

                    prefix,                         #   new__prefix
                    new__prefix_blank,              #   new__prefix_blank
               )


    def indent(self, header = None, ending = None, prefix = 4):
        assert fact_is__native_none__OR__full_native_string(header)
        assert fact_is__native_none__OR__full_native_string(ending)
        assert fact_is_positive_integer                    (prefix)

        if header is not None:
            self.line(header)

        if ending is None:
            method__line           = None
            method__query_position = None
        else:
            method__line           = self._method__line()
            method__query_position = self._method__query_position()

        old__prefix = self.prefix

        if old__prefix is None:
            new__prefix = prefix * ' '
        else:
            new__prefix = old__prefix + prefix * ' '

        return change_prefix(
                    old__prefix,                    #   old__prefix
                    None,                           #   old__prefix_blank

                    method__line,                   #   method__line
                    method__query_position,         #   method__query_position
                    self._method__stash_prefix(),   #   method__stash_prefix
                    None,                           #   method__stash_prefix_blank

                    ending,                         #   ending

                    new__prefix,                    #   new__prefix
                    None,                           #   new__prefix_blank
               )


    def indent_2(self, header = None, ending = None):
        return self.indent(header, ending, 2)


    def line(self, message = None, *arguments):
        assert fact_is_lifecycle_entered                   (self.lifecycle)
        assert fact_is__native_none__OR__full_native_string(message)

        if self.position:
            f = self.f

            assert fact_is_not_native_none(f)
            assert fact_is_not_native_none(self._f__write)


            #
            #   Finish current line (does not alter `total_blanks`)
            #
            self.position = 0

            if message is None:
                assert len(arguments) is 0
            elif arguments:
                self._f__write(message.format(*arguments))
            else:
                self._f__write(message)

            self._append_line(f.getvalue())
            self._close()
            return

        assert fact_is_native_none(self.f)
        assert fact_is_native_none(self._f__write)

        if message is None:
            assert len(arguments) is 0

            #
            #   Always write this [explicit] blank line out (even if blanks are currently disabled; or *IF* blanks
            #   are disabled in the future).
            #
            self._append_line(self.prefix_blank)

            total_blanks = self.total_blanks

            if total_blanks > 0:
                self.blanks = total_blanks - 1

            return

        if self.total_blanks:
            self._flush_total_blanks()

        prefix = self.prefix

        if prefix is None:
            if arguments:
                self._append_line(message.format(*arguments))
                return

            self._append_line(message)
            return

        if arguments:
            self._append_line(prefix + message.format(*arguments))
            return

        self._append_line(prefix + message)


    def write(self, s):
        assert fact_is_lifecycle_entered(self.lifecycle)
        assert '\n' not in s

        position = self.position

        self.position = position + len(s)

        if position:
            assert fact_is_not_native_none(self.f)
            assert fact_is_not_native_none(self._f__write)

            #
            #   Continue current line (does not alter `total_blanks`)
            #
            self._f__write(s)
            return

        if self.total_blanks:
            self._flush_total_blanks()

        assert fact_is_native_none(self.f)
        assert fact_is_native_none(self._f__write)

        self.f         = f         = build_native_string()
        self._f__write = _f__write = f.write

        prefix = self.prefix

        if prefix is not None:
            _f__write(prefix)

        _f__write(s)


query__Build_Lines_of_NativeString__position     = Build_Lines_of_NativeString.position    .__get__
stash__Build_Lines_of_NativeString__prefix       = Build_Lines_of_NativeString.prefix      .__set__
stash__Build_Lines_of_NativeString__prefix_blank = Build_Lines_of_NativeString.prefix_blank.__set__


@creator
def build_lines_of_native_string():
    return Build_Lines_of_NativeString()
