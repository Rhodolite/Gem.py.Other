#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Course              import  create_Course
from    MustCatch           import  must_catch_AssertionError
from    MustCatch           import  must_catch_ValueError
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_cannot_call_next_quiz_number_twice():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

    quiz_number_1 = math.next_quiz_number()

    with must_catch_AssertionError():
        quiz_number_2 = math.next_quiz_number()


@cleanup_after_test
def test_cannot_create_course_with_duplciate_name():
    alice = create_Teacher('Alice', 1)

    math_by_alice = create_Course('Math', 1, alice)

    bob = create_Teacher('Bob', 2)

    with must_catch_ValueError(
            'Attempt to create course with duplicate name {!r} (already exists: {})'.format(
                'Math',
                math_by_alice
            ),
    ):
        math_by_bob = create_Course('Math', 2, bob)
