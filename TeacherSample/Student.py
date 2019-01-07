#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Course              import  find_course
from    Percentage          import  percentage__with_considering_0_of_0_as_100
from    Person              import  Person
from    ProduceByName       import  produce_find_lookup_verify_by_name_functions
from    Question            import  question_key
from    SchoolIdentifier    import  create_person_identifier


class Student(Person):
    __slots__ = ((
    #   'identifier',                   #   Inherited from Person
        'courses',                      #   List of Course
        'quizzes',                      #   List of Quiz
        'facts',                        #   Map { String } of *Fact
        'questions',                    #   Map { Question } of Choice
    ))


    is_student = True


    #
    #   Private
    #
    def __init__(self, identifier):
        super(Student, self).__init__(identifier)

        self.courses   = []
        self.quizzes   = []
        self.facts     = {}
        self.questions = {}


    def debug_dump(self):
        print
        print('Dump of {}'.format(self))

        for [i, v] in enumerate(self.courses):
            print('  Course [{}]: {}'.format(i, v))

        for [i, quiz] in enumerate(self.quizzes):
            print('  Quiz [{}]: {}'.format(i, quiz))

            for [j, question] in enumerate(quiz.questions):
                print('    Question [{}]: {}'.format(j, question))

                for [k, choice] in enumerate(question.choices):
                    print('      Choice [{}]: {}'.format(k, choice))

        for [i, k] in enumerate(sorted(self.facts)):
            v = self.facts[k]

            print('  Fact [{}]: {}'.format(i, v))

        for [i, k] in enumerate(sorted(self.questions, key = question_key)):
            v = self.questions[k]

            print('  Question [{}]: {}'.format(i, k))
            print('    {}'.format(v))


    #
    #   Public
    #

    
    #.__repr__                          #   Inherited from Person


    def answer_one_question(self, question):
        question_text = question.question_text

        fact = self.facts.get(question_text)

        if fact is None:
            return

        choice = question.lookup_choice_text(fact.choice_text)

        if choice is None:
            return

        self.questions[question] = choice

        
    def answer_questions(self):
        for quiz in self.quizzes:
            for question in quiz.questions:
                if question not in self.questions:
                    self.answer_one_question(question)


    def give_quiz(self, quiz):
        assert quiz not in self.quizzes

        self.quizzes.append(quiz)


    def grade_course(self, course):
        correct = 0
        total   = 0

        for quiz in course.quizzes:
            correct += self.grade_quiz(quiz)
            total   += 100

        return percentage__with_considering_0_of_0_as_100(correct, total)


    def grade_quiz(self, quiz):
        correct = 0
        total   = 0

        for question in quiz.questions:
            choice = self.questions.get(question)

            if (choice is not None) and (choice.correct):
                correct += 1

            total += 1

        return percentage__with_considering_0_of_0_as_100(correct, total)


    def grade_semester_by_teacher(self, teacher):
        correct = 0
        total   = 0

        for course in self.courses:
            if course.teacher is not teacher:
                continue

            correct += self.grade_course(course)
            total   += 100

        return percentage__with_considering_0_of_0_as_100(correct, total)


    def join_course(self, name):
        for v in self.courses:
            if v.name == name:
                raise ValueError('{} has already joined course {}; cannot join a second time'.format(self, v))

        course = find_course(name)

        self.courses.append(course)
        course.add_student(self)


    def teach(self, fact):
        previous = self.facts.setdefault(fact.question_text, fact)

        if fact is not previous:
            raise ValueError('{} already knows {}; cannot be taught {}'.format(self, self.facts[fact.question_text], fact))


    #.name                              #   Inherited from Person
    #.number                            #   Inherited from Person


[
        find_student, lookup_student, store_student, verify_unique_student, zap_students,
] = produce_find_lookup_verify_by_name_functions('student', Student)


def create_Student(name, number):
    verify_unique_student(name)

    identifier = create_person_identifier(name, number)

    student = Student(identifier)

    store_student(name, student)

    return student


#
#   student_key
#       - See comments in "Question" for `question_key`
#
def student_key(student):
    return student.name


#
#   Exports
#
__all__ = ((
    'create_Student',
    'find_student',
    'zap_students',
    'student_key',
))
