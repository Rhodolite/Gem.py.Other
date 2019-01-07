#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
#       This code is mostly to test that `must_catch_*` produce *GOOD* & correct `TestingError` when the expected
#       exceptions are not thrown.
#
from    MustCatch           import  must_catch_AssertionError
from    MustCatch           import  must_catch_TestingError
from    MustCatch           import  must_catch_ValueError
from    TestingFramework    import  cleanup_after_test


#
#   test_must_catch_AssertionError__negative
#
#       1.  Test that calling `must_catch_AssertionError` and then *NOT* raising an AssertionError *WILL* raise a
#           `TestingError` as a complaint.
#
#       2.  Test that calling `must_catch_AssertionError` and then raising a different excetpion *WILL* raise a
#           `TestingError` as a complaint.
#
#       This code is a little confusing since it uses `must_catch_TestingError` both as part of the testing framework,
#       while at the *same* time also using `must_catch_AssertionError` to test it's proper failure conditions ...
#
@cleanup_after_test
def test_must_catch_AssertionError__negative():
    def fail_to_raise_an_assertion():
        with must_catch_AssertionError():
            #
            #   This assert will *NOT* fail -- HENCE: `must_catch_AssertionError` needs to complain it *DOESN'T* catch an
            #   `AssertionError`
            #
            assert 1


    wrong_exception = ValueError('OOPS -- this should be an AssertionError instead')


    def raise_wrong_exception():
        with must_catch_AssertionError():
            raise wrong_exception


    #
    #   Test 1
    #
    with must_catch_TestingError('Failed to raise AssertionError'):
        fail_to_raise_an_assertion()


    #
    #   Test 2
    #
    with must_catch_TestingError("Failed to raise AssertionError (actually raised {!r})".format(wrong_exception)):
        raise_wrong_exception()


#
#   test_must_catch_AssertionError__positive
#       Test that `must_catch_AssertionError` properly catches an `AssertionError`
#
@cleanup_after_test
def test_must_catch_AssertionError__positive():
    with must_catch_AssertionError():
        assert 0


#
#   test_must_catch_ValueError__negative
#
#       1.  Test that calling `must_catch_ValueError` and then *NOT* raising an ValueError *WILL* raise a
#           `TestingError` as a complaint.
#
#       2.  Test that calling `must_catch_ValueError` and then raising a ValueError with a different message
#           *WILL* raise a `TestingError` as a complaint.
#
@cleanup_after_test
def test_must_catch_ValueError__negative():
    def fail_to_raise_a_ValueError():
        with must_catch_ValueError('Oops'):
            pass


    correct_exception = ValueError('Correct')
    wrong_exception   = ValueError('Wrong')


    def raise_wrong_exception():
        with must_catch_ValueError('Correct'):
            raise wrong_exception


    #
    #   Test 1
    #
    with must_catch_TestingError("Failed to raise ValueError with message 'Oops'"):
        fail_to_raise_a_ValueError()


    #
    #   Test 2
    #
    with must_catch_TestingError(
            (
                  "Failed to raise ValueError with correct message"
                + '\n      Actual: {}'
                + '\n    Expected: {}'
            ).format(
                wrong_exception,
                correct_exception,
            )
    ):
        raise_wrong_exception()


#
#   test_must_catch_ValueError__positive
#       Test that `must_catch_AssertionError` properly catches an `ValueError` (with a matching message).
#
@cleanup_after_test
def test_must_catch_ValueError__positive():
    with must_catch_ValueError('Oops'):
        raise ValueError('Oops')
