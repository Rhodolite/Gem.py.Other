#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    BehaveFramework     import  *
from    Choice              import  create_Choice
from    Course              import  create_Course
from    Question            import  create_Question
from    Question            import  find_question_by_key
from    Quiz                import  create_Quiz
from    Quiz                import  find_quiz_by_key
from    re                  import  compile         as  compile_pattern
from    Student             import  create_Student
from    Student             import  lookup_student
from    Teacher             import  create_Teacher


group_positive_integer_pattern = r'([1-9][0-9]*)'

choice_number_match = compile_pattern(
          r'^'
        + group_positive_integer_pattern        #   course number
        + '.'
        + group_positive_integer_pattern        #   question number
        + '.'
        + group_positive_integer_pattern        #   quiz number
        + r'([A-Z])'                            #   choice letter
        + '\Z'
    ).match

question_number_match = compile_pattern(
          r'^'
        + group_positive_integer_pattern        #   course number
        + '.'
        + group_positive_integer_pattern        #   question number
        + '.'
        + group_positive_integer_pattern        #   quiz number
        + '\Z'
    ).match


#
#   create_choice_and_print
#
def create_choice_and_print(i, name, number, correct, choice_text):
    m = choice_number_match(number)

    if m is None:
        raise ValueError(
                    'Unable to interpret {} as a choice number (expected format #.#.#UPPER-CASE-LETTER)'.format(
                        number,
                ),
            )

    course_number   = m.group(1)
    quiz_number     = m.group(2)
    question_number = m.group(3)
    choice_letter   = m.group(4)

    question_key = '{}.{}.{}'.format(course_number, quiz_number, question_number)

    question = find_question_by_key(question_key)

    choice = create_Choice(question, correct, choice_text)

    print('...   Created [{}]: {}'.format(i, choice))

    assert number == choice.key()

    return choice


#
#   create_course_and_print
#
def create_course_and_print(i, name, number, teacher):
    course = create_Course(name, number, teacher)

    print('...   Created [{}]: {}'.format(i, course))

    return course


#
#   create_question_and_print
#
def create_question_and_print(i, name, number, question_text):
    m = question_number_match(number)

    if m is None:
        raise ValueError('Unable to interpret {} as a question number (expected format #.#.#)'.format(number))

    course_number   = m.group(1)
    quiz_number     = m.group(2)
    question_number = m.group(3)

    quiz_key = '{}.{}'.format(course_number, quiz_number)

    quiz = find_quiz_by_key(quiz_key)

    question = create_Question(quiz, question_text)

    print('...   Created [{}]: {}'.format(i, question))

    assert number == question.key()

    return question


#
#   create_quiz_and_print
#
def create_quiz_and_print(i, name, number, course):
    quiz = create_Quiz(course, name)

    print('...   Created [{}]: {}'.format(i, quiz))

    assert number == quiz.key()

    return quiz


#
#   create_student_or_teacher__and__print
# 
def create_student_or_teacher__and__print(i, is_teacher, name, number):
    if is_teacher:
        person = create_Teacher(name, number)
    else:
        person = create_Student(name, number)

    print('...   Created [{}]: {}'.format(i, person))

    return person


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
#   iterate_rows_and_priNT
#
def iterate_rows_and_print(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 6
    assert headings[0] == 'type'
    assert headings[1] == 'name'
    assert headings[2] == 'number'
    assert headings[3] == 'parent'
    assert headings[4] == 'correct'
    assert headings[5] == 'text'

    for [i, row] in enumerate(table):
        row_type = query_actual_string(row, 'type')
        name     = query_actual_string(row, 'name')

        if row_type == 'Choice':
            number = query_actual_string(row, 'number')

            query_none(row, 'parent')

            correct     = query_no_or_yes(row, 'correct')
            choice_text = query_actual_string(row, 'text')

            yield create_choice_and_print(i, name, number, correct, choice_text)
            continue

        if row_type == 'Course':
            number  = query_positive_integer(row, 'number')
            teacher = query_teacher         (row, 'parent')

            query_none(row, 'correct')
            query_none(row, 'text')

            yield create_course_and_print(i, name, number, teacher)
            continue

        if row_type == 'Question':
            number = query_actual_string(row, 'number')

            query_none(row, 'parent')
            query_none(row, 'correct')

            question_text = query_actual_string(row, 'text')

            yield create_question_and_print(i, name, number, question_text)
            continue

            
        if row_type == 'Quiz':
            number = query_actual_string(row, 'number')
            course = query_course(row, 'parent')

            query_none(row, 'correct')
            query_none(row, 'text')

            yield create_quiz_and_print(i, name, number, course)
            continue

        if row_type == 'Student':
            number = query_positive_integer(row, 'number')

            query_none(row, 'parent')
            query_none(row, 'correct')
            query_none(row, 'text')

            yield create_student_or_teacher__and__print(i, False, name, number)
            continue

        if row_type == 'Teacher':
            number  = query_positive_integer(row, 'number')

            query_none(row, 'parent')
            query_none(row, 'correct')
            query_none(row, 'text')

            yield create_student_or_teacher__and__print(i, True, name, number)
            continue

        raise ValueError('unknown row type: {!r}'.format(row_type))


#
#   iterate_students
#
def iterate_students(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 1
    assert headings[0] == 'student'

    for row in table:
        student_name = query_actual_string(row, 'student')

        student = lookup_student(student_name)

        yield student


#
#   iterate_students_and_teachers
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
        name     = query_actual_string(row, 'name')
        number   = query_positive_integer(row, 'number')

        is_teacher = lookup_is_teacher(row_type)

        if is_teacher is None:
            raise ValueError('unknown person type: {!r}'.format(row_type))

        yield ((is_teacher, name, number))
