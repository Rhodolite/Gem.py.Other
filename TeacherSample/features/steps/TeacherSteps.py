#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    BehaveFramework     import  *
from    Fact                import  create_false_fact
from    Fact                import  create_true_fact
from    IterateRow          import  iterate_rows_and_print
from    IterateRow          import  iterate_students
from    Student             import  student_key
from    Quiz                import  find_quiz_by_key


def iterate_students_and_courses(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 2
    assert headings[0] == 'student'
    assert headings[1] == 'course'

    for row in table:
        student = query_student(row, 'student')
        course  = query_course(row, 'course')

        yield ((student, course))


def iterate_students_and_course_grades(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 3
    assert headings[0] == 'student'
    assert headings[1] == 'course'
    assert headings[2] == 'grade'

    for row in table:
        student = query_student(row, 'student')
        course  = query_course (row, 'course')
        grade   = query_grade  (row, 'grade')

        yield [student, course, grade]


def iterate_students_and_quiz_grades(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 5
    assert headings[0] == 'student'
    assert headings[1] == 'course'
    assert headings[2] == 'name'
    assert headings[3] == 'number'
    assert headings[4] == 'grade'

    for row in table:
        student   = query_student      (row, 'student')
        course    = query_course       (row, 'course')
        quiz_name = query_actual_string(row, 'name')
        quiz_key  = query_actual_string(row, 'number')
        grade     = query_grade        (row, 'grade')

        quiz = find_quiz_by_key(quiz_key)

        assert quiz.course == course
        assert quiz.name   == quiz_name

        yield [student, quiz, grade]


def iterate_students_and_semester_grades(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 3
    assert headings[0] == 'student'
    assert headings[1] == 'teacher'
    assert headings[2] == 'grade'

    for row in table:
        student = query_student(row, 'student')
        teacher = query_teacher(row, 'teacher')
        grade   = query_grade  (row, 'grade')

        yield [student, teacher, grade]


def iterate_students_and_facts(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 4
    assert headings[0] == 'student'
    assert headings[1] == 'correct'
    assert headings[2] == 'question_text'
    assert headings[3] == 'choice_text'

    for row in table:
        student       = query_student(row, 'student')
        correct       = query_no_or_yes    (row, 'correct')
        question_text = query_actual_string(row, 'question_text')
        choice_text   = query_actual_string(row, 'choice_text')


        yield ((student, correct, question_text, choice_text))


def iterate_teachers_give_quizes(context):
    table = context.table

    headings = table.headings

    assert len(headings) == 4
    assert headings[0] == 'teacher'
    assert headings[1] == 'course'
    assert headings[2] == 'name'
    assert headings[3] == 'number'

    for row in table:
        teacher      = query_teacher      (row, 'teacher')
        course       = query_course       (row, 'course')
        quiz_name    = query_actual_string(row, 'name')
        quiz_key     = query_actual_string(row, 'number')

        quiz = find_quiz_by_key(quiz_key)

        assert quiz.course.teacher == teacher
        assert quiz.course         == course
        assert quiz.name           == quiz_name

        yield quiz


def common_code__load_a_unique_set_of_rows(context):
    print

    for row in iterate_rows_and_print(context):
        #
        #   Nothing to do here, `row` has been created
        #
        pass

    print


@given('a unique set of choices, courses, quizes, students and teachers')
def load_a_unique_set_of_rows(context):
    common_code__load_a_unique_set_of_rows(context)


@when('students join courses')
def students_join_courses(context):
    print

    for [i, [student, course]] in enumerate(iterate_students_and_courses(context)):
        student.join_course(course.name)

        print('...   {} joined {}'.format(student, course))

    print


use_step_matcher('re')


@when('(?:other )?students learn (?:more )?facts(?:, .*)?')
def students_learn_facts(context):
    print

    for [i, [student, correct, question_text, choice_text]] in enumerate(iterate_students_and_facts(context)):
        if correct:
            fact = create_true_fact(question_text, choice_text)
        else:
            fact = create_false_fact(question_text, choice_text)

        student.teach(fact)

        print('...   {} learned {}'.format(student, fact))

    print


@when('teachers gives (?:more )?quizzes')
def teachers_give_quizzes(context):
    print

    for [i, quiz] in enumerate(iterate_teachers_give_quizes(context)):
        quiz.give_quiz_to_all_students()

        print('...  {} gave quiz {} to all students'.format(quiz.course.teacher, quiz))
        print('  ...   in course {}'.format(quiz.course))

    print


@when('(?:other )?students answer questions')
def students_answer_questions(context):
    print

    for [i, student] in enumerate(iterate_students(context)):
        student.answer_questions()

        print('...   {} answered questions'.format(student))

    print


@then('students get their quiz grades(?:, .*)?')
def students_get_their_quiz_grades(context):
    print

    for [i, [student, quiz, grade]] in enumerate(iterate_students_and_quiz_grades(context)):
        actual = student.grade_quiz(quiz)

        print('...   {} got quiz grade {} on {}'.format(student, actual, quiz))
        print('  ...   in course {}'.format(quiz.course))

        if actual != grade:
            print('  ...   BUT EXPECTED GRADE {}'.format(grade))

        assert actual == grade

    print


@when('teachers create more (?:courses and )?quizzes')
def teachers_create_more_quizzes(context):
    common_code__load_a_unique_set_of_rows(context)


@then('students get their course grades')
def students_get_their_course_grades(context):
    print

    for [i, [student, course, grade]] in enumerate(iterate_students_and_course_grades(context)):
        actual = student.grade_course(course)

        print('...   {} got course grade {} on {}'.format(student, actual, course))

        if actual != grade:
            print('  ...   BUT EXPECTED GRADE {}'.format(grade))

        assert actual == grade

    print


@then('students get their semester grades, for a particular teacher')
def students_get_their_semester_grades__for_a_particular_teacher(context):
    print

    for [i, [student, teacher, grade]] in enumerate(iterate_students_and_semester_grades(context)):
        actual = student.grade_semester_by_teacher(teacher)

        print('...   {} got semester grade {} from {}'.format(student, actual, teacher))

        if actual != grade:
            print('  ...   BUT EXPECTED GRADE {}'.format(grade))

        assert actual == grade

    print
