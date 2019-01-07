#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
class Choice(object):
    __slots__ = ((
        'question',                     #   Question
        'letter',                       #   String (length 1, capital letter)
        'correct',                      #   Boolean
        'choice_text',                  #   String+
        '_key',                         #   None | String
    ))


    def __init__(self, question, letter, correct, choice_text):
        self.question    = question
        self.letter      = letter
        self.correct     = correct
        self.choice_text = choice_text
        self._key        = None


    def __repr__(self):
        return '<Choice {!r} {!r} #{} {} {!r}>'.format(
                self.question.quiz.course.name,
                self.question.quiz.name,
                self.key(),
                ('correct'   if self.correct else   'incorrect'),
                self.choice_text,
            )


    def key(self):
        key = self._key

        if key is None:
            key = self._key = '{}.{}.{}{}'.format(
                                      self.question.quiz.course.number,
                                      self.question.quiz.number,
                                      self.question.number,
                                      self.letter,
                                  )

        return key


def create_Choice(question, correct, choice_text):
    assert (type(choice_text) is str) and (len(choice_text) > 0)

    letter = question.next_choice_letter()

    result = Choice(question, letter, correct, choice_text)

    question.add_choice(result)

    return result
