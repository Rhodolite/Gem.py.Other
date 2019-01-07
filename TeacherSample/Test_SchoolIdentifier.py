#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
#   NOTE:
#       Because `CourseIdentifier` and `PersonIdentifier` are *so* strongly bound up with
#       `Course`, `Student` and `Teacher` ...
#
#       The actual testing code below does the tests, indirectly, using `Course`, `Student` and `Teacher`
#       (instead of on `CourseIdentifier` and `PersonIdentifier` directly).
#
#       This is mainly to make the code cleaner, and easier to understand.
#
#       Also, as an indirect benefit, it tests that `CourseIdentifier` and `PersonIdentifier`
#       work properly with their intended "consumer" classes.
#
from    Course              import  create_Course
from    MustCatch           import  must_catch_ValueError
from    Student             import  create_Student
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


#
#   Support functions
#
def must_catch_duplicate(type_name, name, number):
    return must_catch_ValueError(
            "Attempt to create a {} with duplicate #{} (duplicate of: {})".format(
                type_name,
                number,
                "<{} {!r} #{}>".format(type_name, name, number),
            ),
        )


def must_catch_duplicate_course(name, number):
    return must_catch_duplicate('CourseIdentifier', name, number)


def must_catch_duplicate_person(name, number):
    return must_catch_duplicate('PersonIdentifier', name, number)


#
#   test_can_create_course_and_student_with_same_number
#       Test that *CAN* create a `CourseIdentifier` and `PersonIdentifier` both with the same number.
#
@cleanup_after_test
def test_can_create_course_and_student_with_same_number():
    alice    = create_Teacher('Alice', 1)
    swimming = create_Course('Swimming', 1, alice)

    assert alice.number == swimming.number


#
#   test_can_remake_alice_and_swimming_without_duplicate_error
#       Tests that the `@cleanup_after_test` routine is properly working, allowing seperate tests, to remake
#       the same `CourseIdentifier` or `PersonIdentifier` as previously created in other tests.
#
@cleanup_after_test
def test_can_remake_alice_and_swimming_without_duplicate_error():
    alice    = create_Teacher('Alice', 1)
    swimming = create_Course('Swimming', 1, alice)
