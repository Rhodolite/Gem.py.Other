#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    BehaveFramework     import  *
from    Course              import  create_Course
from    Course              import  find_course
from    MustCatch           import  must_catch_ValueError
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


def must_catch_duplicate_course_by_name(previous):
    return must_catch_ValueError(
            'Attempt to create course with duplicate name {!r} (already exists: {})'.format(
                previous.name,
                previous,
            ),
        )


@given("<{teacher_name:String}> is teaching a <{course_name:String}> course")
def implementation(context, teacher_name, course_name):
    teacher = create_Teacher(teacher_name, 1)

    create_Course(course_name, 1, teacher)


@when("<{teacher_name:String}> attempts to also teach a <{course_name:String}> course")
def implementation(context, teacher_name, course_name):
    teacher = create_Teacher(teacher_name, 2)

    with must_catch_duplicate_course_by_name(find_course(course_name)) as context.caught:
        create_Course(course_name, 2, teacher)


@then("an error is thrown")
def implementation(context):
    assert context.caught is not None
