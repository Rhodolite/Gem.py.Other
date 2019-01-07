#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#

from    SchoolIdentifier    import  create_course_identifier
from    ProduceByName       import  produce_find_lookup_verify_by_name_functions


#
#   NOTE:
#       Although `Course` and `Person` *SHARE* a lot of similiar information (member named `.identifier` and
#       all the common code around it), they are purposefully left with duplicate code.
#
#       This, appears to violate the DRY (DO NOT REPEAT yourself) principle, and be the dreadful WET (WRITE EVERYTHING
#       TWICE) error.
#
#       However, here, this duplication is on purpose, as "refactoring" them to a common class (just because they look
#       alike now) actually makes the code harder to read, understand, and maintain long term.
#
#       These classes, may very well diverge in the future, and no longer look alike.
#
#       They should not have a common base class to "share" the same base code -- when they represent
#       something that is totally different.
#
#       (on the other hand `Person` and `Student` do share a common base class of `Person`, since
#       that makes sense in what they are).
#
#   NOTE:
#       Really a trait based langauge would solve the issues above, since `Course` and `Person` do share
#       the trait of having an identifier.
#
#       However, sharing a trait, is not the same as using inheritance -- although it is often tempting
#       to do so, when two classes share all the same traits, it is very tempting to move these traits
#       to a base class & make them both of the classes derived from that base class -- since this avoids
#       code duplication.
#

#
#   Course
#
class Course(object):
    __slots__ = ((
        'identifier',                   #   CourseIdentifier
        'teacher',                      #   Teacher
        'students',                     #   List of Student
        'quizzes',                      #   List of Quiz
        '_next_quiz_number',            #   Integer
    ))


    is_course = True


    #
    #   Private
    #
    def __init__(self, identifier, teacher):
        self.identifier        = identifier
        self.teacher           = teacher
        self.students          = []
        self.quizzes           = []
        self._next_quiz_number = 1


    def debug_dump(self):
        print
        print('Dump of {}'.format(self))

        for [i, v] in enumerate(self.students):
            print('  Student [{}]:  {}'.format(i, v))

        for [i, v] in enumerate(self.   quizzes):
            print('  Quiz [{}]:  {}'.format(i, v))


    #
    #   Public
    #
    def __repr__(self):
        return '<{} {!r} #{} {}>'.format(self.__class__.__name__, self.name, self.number, self.teacher)


    @property
    def name(self):
        return self.identifier.name


    def add_student(self, student):
        assert student not in self.students

        self.students.append(student)


    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

        assert self._next_quiz_number == len(self.quizzes) + 1


    def give_quiz_to_all_students(self, quiz):
        assert quiz in self.quizzes

        for v in self.students:
            v.give_quiz(quiz)


    def next_quiz_number(self):
        result = self._next_quiz_number

        assert result == len(self.quizzes) + 1

        self._next_quiz_number = result + 1

        return result


    @property
    def number(self):
        return self.identifier.number


[
        find_course, lookup_course, store_course, verify_unique_course, zap_courses,
] = produce_find_lookup_verify_by_name_functions('course', Course)


def create_Course(name, number, teacher):
    assert teacher.is_teacher

    verify_unique_course(name)

    identifier = create_course_identifier(name, number)

    course = Course(identifier, teacher)

    store_course(name, course)
    teacher.add_course(course)

    return course


#
#   Exports
#
__all__ = ((
    'create_Course',
    'find_course',
    'zap_courses',
))
