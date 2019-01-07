#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Choice              import  create_Choice
from    Course              import  create_Course
from    MustCatch           import  must_catch_ValueError
from    Question            import  create_Question
from    Quiz                import  create_Quiz
from    Student             import  create_Student
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_can_join_course():
    alice = create_Teacher('Alice', 1)

    math    = create_Course('Math',    1, alice)
    english = create_Course('English', 2, alice)

    bob     = create_Student('Bob', 2)
    charlie = create_Student('Charlie', 3)

    bob.join_course('Math')
    bob.join_course('English')
    charlie.join_course('English')

    math.debug_dump()
    english.debug_dump()

    bob.debug_dump()
    charlie.debug_dump()


@cleanup_after_test
def test_cannot_join_same_course_twice():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

    bob = create_Student('Bob', 2)

    bob.join_course('Math')

    with must_catch_ValueError('{} has already joined course {}; cannot join a second time'.format(bob, math)):
        bob.join_course('Math')


@cleanup_after_test
def test_cannot_join_nonexistent_course():
    alice = create_Student('Alice', 1)

    stamp_collecting = 'How to collect stamps for fun & profit'

    with must_catch_ValueError('Failed to find a course named {!r}'.format(stamp_collecting)):
        alice.join_course(stamp_collecting)
