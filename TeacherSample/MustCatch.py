#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


class TestingError(RuntimeError):
    __slots__ = ((
    ))


#
#   NOTE:
#       I had serious problems using `pytest.raise`, since Ubuntu came with pytest version 2.9.7,
#       which does not support the `message=` argument (only supported in pytest version 3.0 or higher).
#
#       Hence, I implemented my own version of `MustCatchException`.
#
#       Also, I find the syntax of using:
#
#           1.  must_catch_ValueError("Oops")               #   to be less clutter than
#           2.  pytest.raise(ValueError, message="Oops")
#
#       Thus I would still prefer the wrapper `must_catch_ValueError` around `pytest.raise` even if
#       using pytest version 3.0 or higher.
#
class MustCatchException(object):
    __slots__ = ((
        'exception_type',           #   Type
        'caught',                   #   Zero | Exception+
    ))


    def __init__(self, exception_type):
        self.exception_type = exception_type
        self.caught         = 0


    def __repr__(self):
        if self.caught is 0:
            return '<MustCatchException {}>'.format(self.exception_type.__name__)

        return '<MustCatchException {}; caught: {!r}>'.format(self.exception_type.__name__, self.caught)


    def __enter__(self):
        return self


    def __exit__(self, e_type, e, traceback):
        if e_type is self.exception_type:
            arguments = e.args

            if (type(arguments) is tuple) and (len(arguments) is 1):
                return True

        if e_type is not None:
            raise TestingError('Failed to raise {} (actually raised {!r})'.format(self.exception_type.__name__, e))

        raise TestingError('Failed to raise {}'.format(self.exception_type.__name__))



class MustCatchExceptionWithMessage(MustCatchException):
    __slots__ = ((
    #   'exception_type',           #   Inherited from MustCatchException
    #   'caught',                   #   Inherited from MustCatchException
        'message',                  #   String
    ))


    def __init__(self, exception_type, message):
        super(MustCatchExceptionWithMessage, self).__init__(exception_type)

        self.message = message


    def __repr__(self):
        if self.caught is 0:
            return '<MustCatchException {} {!r}>'.format(self.exception_type.__name__, self.message)

        return '<MustCatchException {} {!r}; caught: {!r}>'.format(
                self.exception_type.__name__,
                self.message,
                self.caught,
            )

    #.enter                         #   Inherited from MustCatchException


    def __exit__(self, e_type, e, traceback):
        if e_type is self.exception_type:
            arguments = e.args

            if (type(arguments) is tuple) and (len(arguments) is 1):
                if arguments[0] == self.message:
                    self.caught = e

                    return True

                #
                #   NOTE:
                #       Usage of `\n` here makes it easier to see the mistake by quickly glancing at the output of pytest.
                #
                #   Example error:
                #
                #       E     TestingError: Failed to raise <type 'exceptions.ValueError'> with correct message
                #       E           Actual: Attempt to ... (duplicate of: <CourseIdentifier 'math' #1>)
                #       E         Expected: Attempt to ... (duplicate of: <CourseIdentifier 'swimming' #1>)
                #
                #   It is much easier to see by glance that the problem is 'math' .vs. 'swimming'.
                #
                raise TestingError(
                            (
                                 'Failed to raise {} with correct message'
                               + '\n      Actual: {}'
                               + '\n    Expected: {}'
                            ).format(
                                self.exception_type.__name__,
                                arguments[0],
                                self.message,
                            ),
                        )


        if e_type is not None:
            raise TestingError(
                        'Failed to raise {} with message {!r} (actually raised {!r})'.format(
                            self.exception_type.__name__,
                            self.message,
                            e,
                        )
                    )

        raise TestingError('Failed to raise {} with message {!r}'.format(self.exception_type.__name__, self.message))


#
#   must_catch_AssertionError()
#
def must_catch_AssertionError():
    return MustCatchException(AssertionError)


#
#   must_catch_TestingError(message)
#   must_catch_ValueError(message)
#       message     - A non-empty string.
#
def must_catch_TestingError(message):
    assert (type(message) is str) and (len(message) > 0)

    return MustCatchExceptionWithMessage(TestingError, message)


def must_catch_ValueError(message):
    assert (type(message) is str) and (len(message) > 0)

    return MustCatchExceptionWithMessage(ValueError, message)


#
#   Exports
#
__all__ = ((
    'must_catch_AssertionError',
    'must_catch_TestingError',
    'must_catch_ValueError',
))
