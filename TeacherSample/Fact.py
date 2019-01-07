
#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   FalseFact
#   TrueFact
#
class Fact_1(object):
    __slots__ = ((
        'question_text',                #   String+
        'choice_text'                   #   String+
    ))


    correct = False


    def __init__(self, question_text, choice_text):
        self.question_text = question_text
        self.choice_text   = choice_text


    def __repr__(self):
        return '<{} {!r} {!r}>'.format(self.__class__.__name__, self.question_text, self.choice_text)


class FalseFact(Fact_1):
    __slots__ = ((
        'question_text',                #   Inherited from Fact_1
        'choice_text'                   #   Inherited from Fact_1
    ))


    correct = False


    #.__init__                          #   Inherited from Fact_1
    #.__repr__                          #   Inherited from Fact_1


class TrueFact(Fact_1):
    __slots__ = ((
        'question_text',                #   Inherited from Fact_1
        'choice_text'                   #   Inherited from Fact_1
    ))


    correct = True


    #.__init__                          #   Inherited from Fact_1
    #.__repr__                          #   Inherited from Fact_1


def create_false_fact(question_text, choice_text):
    assert (type(question_text) is str) and (len(question_text) > 0)
    assert (type(choice_text)   is str) and (len(choice_text) > 0)

    return FalseFact(question_text, choice_text)


def create_true_fact(question_text, choice_text):
    assert (type(question_text) is str) and (len(question_text) > 0)
    assert (type(choice_text)   is str) and (len(choice_text) > 0)
   
    return TrueFact(question_text, choice_text)
