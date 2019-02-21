#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    BehaveFramework     import  *
from    MustCatch           import  must_catch_ValueError
from    SchoolIdentifier    import  find_person_identifier
from    Course              import  create_Course
from    Student             import  create_Student
from    Teacher             import  create_Teacher


def must_catch_duplicate(type_name, previous):
    return must_catch_ValueError(
            "Attempt to create a {} with duplicate #{} (duplicate of: {})".format(
                type_name,
                previous.number,
                previous,
            ),
        )


def must_catch_duplicate_person_identifier(number):
    return must_catch_duplicate('PersonIdentifier', find_person_identifier(number))



#
#   create_course__and__print
#
def create_course__and__print(i, name, number, parent):
    course = create_Course(name, number, parent)

    print('      Created: Course [{}]: {}'.format(i, course))

#
#   create_student_or_teacher__and__print
#
def create_student_or_teacher__and__print(i, is_teacher, name, number):
    if is_teacher:
        person = create_Teacher(name, number)
    else:
        person = create_Student(name, number)

    print('      Created: Person [{}]: {}'.format(i, person))


#
#   iterate_courses
#
def iterate_courses(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 4
    assert headings[0] == 'type'
    assert headings[1] == 'name'
    assert headings[2] == 'number'
    assert headings[3] == 'parent'

    for row in table:
        row_type = query_actual_string   (row, 'type')
        name     = query_actual_string   (row, 'name')
        number   = query_positive_integer(row, 'number')
        teacher  = query_teacher         (row, 'parent')

        if row_type != 'Course':
            raise ValueError('unknown row type: {!r}'.format(row_type))

        yield ((name, number, teacher))

#
#   lookup_is_teacher(row_type)
#       A quick test that the `row_type` is a student.
#
#       Results:
#           None    - An error, not a "Student" or a "Teacher"
#           False   - A student
#           True    - A teacher
#
lookup_is_teacher = { 'Student' : False, 'Teacher' : True }.get


def iterate_students_and_teachers(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 3
    assert headings[0] == 'type'
    assert headings[1] == 'name'
    assert headings[2] == 'number'

    for row in table:
        row_type = query_actual_string(row, 'type')
        name        = query_actual_string(row, 'name')
        number      = query_positive_integer(row, 'number')

        is_teacher = lookup_is_teacher(row_type)

        if is_teacher is None:
            raise ValueError('unknown person type: {!r}'.format(row_type))

        yield ((is_teacher, name, number))


@given('a set of people that includes a <{invalid_person_type:String}> instead of all students and teachers')
def attempt_to_load_a_set_of_people_that_includes_an_invalid_person_type(context, invalid_person_type):
    with must_catch_ValueError(
            'unknown person type: {!r}'.format(invalid_person_type)
    ) as context.caught:
        for [i, [is_teacher, name, number]] in enumerate(iterate_students_and_teachers(context)):
            create_student_or_teacher__and__print(i, is_teacher, name, number)


@given('a unique set of students and teachers')
def load_students_and_teachers(context):
    for [i, [is_teacher, name, number]] in enumerate(iterate_students_and_teachers(context)):
        create_student_or_teacher__and__print(i, is_teacher, name, number)


@when('other students or teachers attempt to use the same number')
def attempt_to_load_duplicate_students_and_teachers(context):
    print

    context.total_caught = 0

    for [i, [is_teacher, name, number]] in enumerate(iterate_students_and_teachers(context)):
        with must_catch_duplicate_person_identifier(number):
            create_student_or_teacher__and__print(i, is_teacher, name, number)

        context.total_caught += 1


@then('a unique set of courses can be created, using the same numbers assigned to the students or teacher')
def load_courses(context):
    print

    for [i, [name, number, parent]] in enumerate(iterate_courses(context)):
        create_course__and__print(i, name, number, parent)


@then('<{total_caught:PositiveInteger}> errors are thrown')
def errors_are_thrown(context, total_caught):
    assert context.total_caught == total_caught
