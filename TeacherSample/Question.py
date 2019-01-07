#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    ProduceByName       import  produce_find_lookup_verify_by_name_functions


class Question(object):
    __slots__ = ((
        'quiz',                         #   Quix
        'number',                       #   positive integer
        'question_text',                #   String+
        'choices',                      #   List of Question
        'choice_text_map',              #   Map { String } of Question
        '_next_choice_letter',          #   String
        '_key',                         #   None | String
    ))


    #
    #   Private
    #
    def __init__(self, quiz, number, question_text):
        self.quiz                = quiz
        self.number              = number
        self.question_text       = question_text
        self.choices             = []
        self.choice_text_map     = {}
        self._next_choice_letter = 'A'
        self._key                = None


    def debug_dump(self):
        print
        print('Dump of {}'.format(self))

        for [i, v] in enumerate(self.choices):
            print('  Choice [{}]:  {}'.format(i, v))


    #
    #   Public
    #
    def __repr__(self):
        return '<Question {!r} {!r} #{} {!r}>'.format(
                self.quiz.course.name,
                self.quiz.name,
                self.key(),
                self.question_text,
            )


    def add_choice(self, choice):
        assert choice.letter == chr(ord('A') + len(self.choices))

        previous = self.choice_text_map.setdefault(choice.choice_text, choice)

        if previous is not choice:
            raise ValueError("{} already has {}; cannot add {}", self, previous, choice)

        self.choices.append(choice)


    def lookup_choice_text(self, choice_text):
        return self.choice_text_map[choice_text]


    def key(self):
        key = self._key

        if key is None:
            key = self._key = '{}.{}.{}'.format(self.quiz.course.number, self.quiz.number, self.number)

        return key


    def next_choice_letter(self):
        result = self._next_choice_letter

        assert result == chr(ord('A') + len(self.choices))

        self._next_choice_letter = (None   if result == 'Z' else   chr(ord(result) + 1))

        return result


[
        find_question_by_key,
        lookup_question_by_key,
        store_question_by_key,
        verify_unique_question_by_key,
        zap_question_by_key,
] = produce_find_lookup_verify_by_name_functions('question', Question)


def insert_question_by_key(question):
    k = question.key()

    verify_unique_question_by_key(k)
    store_question_by_key(k, question)


def create_Question(quiz, question_text):
    assert (type(question_text) is str) and (len(question_text) > 0)

    number = quiz.next_question_number()

    question = Question(quiz, number, question_text)

    insert_question_by_key(question)
    quiz.add_question(question)

    return question


#
#   question_key is used as a parameter to `sorted`
#
#       Example:
#           questions = set()
#           questions.add(create_Question(quiz, 'What is 1+1?'))
#           questions.add(create_Question(quiz, 'What is 2-2?'))
#       
#           for v in enumerate(sorted(questions, key = question_key)):
#               print('Question [{}]: {}', i, v)
#
#   Obviously `question_key` is an alias for `Question.key` -- However, I prefer other files
#   not access internal methods of a class by using `Question.key` directly.
#
#   The line below can be considered a `friend` (from C++) allowing access to `Question.key`
#   using the alias `key_question`
#
question_key = Question.key


#
#   Export
#
__exports__ = ((
    'create_Question',
    'find_question_by_key',
    'question_key',
    'zap_question_by_key',
))
