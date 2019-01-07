#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    ProduceByName       import  produce_find_lookup_verify_by_name_functions


class Quiz(object):
    __slots__ = ((
        'course',                       #   Course
        'name',                         #   non empty String+
        'number',                       #   positive integer
        'questions',                    #   List of Question
        '_next_question_number',        #   Integer
        '_key',                         #   None | String
    ))


    #
    #   Private
    #
    def __init__(self, course, name, number):
        self.course                = course
        self.name                  = name
        self.number                = number
        self.questions             = []
        self._next_question_number = 1
        self._key                  = None


    def debug_dump(self):
        print
        print('Dump of {}'.format(self))

        for [i, v] in enumerate(self.questions):
            print('  Question [{}]:  {}'.format(i, v))


    #
    #   Public
    #
    def __repr__(self):
        return '<Quiz {!r} {!r} #{}>'.format(self.course.name, self.name, self.key())


    def add_question(self, question):
        self.questions.append(question)

        assert self._next_question_number == len(self.questions) + 1


    def key(self):
        key = self._key

        if key is None:
            key = self._key = '{}.{}'.format(self.course.number, self.number)

        return key


    def give_quiz_to_all_students(self):
        self.course.give_quiz_to_all_students(self)


    def next_question_number(self):
        result = self._next_question_number

        assert result == len(self.questions) + 1

        self._next_question_number = result + 1

        return result


[
        find_quiz_by_key, lookup_quiz_by_key, store_quiz_by_key, verify_unique_quiz_by_key, zap_quiz_by_key,
] = produce_find_lookup_verify_by_name_functions('quiz', Quiz)


def insert_quiz_by_key(quiz):
    k = quiz.key()

    verify_unique_quiz_by_key(k)
    store_quiz_by_key(k, quiz)


def create_Quiz(course, name):
    number = course.next_quiz_number()

    quiz = Quiz(course, name, number)

    insert_quiz_by_key(quiz)
    course.add_quiz(quiz)

    return quiz


#
#   Export
#
__exports__ = ((
    'create_Quiz',
    'find_quiz_by_key',
    'zap_quiz_by_key'
))
