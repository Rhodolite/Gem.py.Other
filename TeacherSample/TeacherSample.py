#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#

#
#   The section below between <copyright> and </copyright> was received as a quiz for a job interview.
#
#       Thus it is copyrighted by whoever created the quiz.
#

#
#   Sample program that meets the following specifications:
#
#   <copyright>
#       Copyright (c) Unknown.  All rights reserved.
#
#       There are Teachers
#
#       There are Students
#
#       Students are in classes that teachers teach
#
#       Teachers can create multiple quizzes with many questions (each question is multiple choice)
#
#       Teachers can assign quizzes to students
#
#       Students solve/answer questions to complete the quiz, but they don't have to complete it at once.
#       (Partial submissions can be made).
#
#       Quizzes need to get graded
#
#       For each teacher, they can calculate each student's total grade accumulated over a semester
#   </copyright>
#


#
#   Clarification:
#
#       "classes" are named "courses" (to avoid confusion with the python `class` keyword).
#
#       As per the original specification, Teachers *CAN* assign quizzes to students who are not taking
#       one of their classes -- HOWEVER, these quizes are not part of their grade.
#
#   Assumptions (added to the above specifications):
#
#       A Teacher cannot be a Student.
#
#       Each course is taught by exactly one Teacher.
#
#       A quiz is associated with a course.
#
#           For example a teacher that is teaching "Math" and "Geometry" cannot create an "Numbers"
#           quiz and assign it to both courses.
#
#           Reasoning:
#
#               The same student could be taking both courses, thus getting the same quiz twice.
#
#       A teacher gives the quiz to all the students in the course (not to only some students and not others).
#
#           For example, there is no concept of "make up quiz" that only some students get.
#
#       A Student joining a course, is immediatly given all previous quizzes given to students in that course.
#
#       A question must appear on only one quiz, and only once on that quiz.
#
#       Grading is super simple, one point for a correct answer, 0 points for an incomplete answer or incorrect
#       answer.
#
#               In other words, some questions are not worth more than others.
#
#               Also there is no penalty for when a quiz question is submitted, time of submission is irrelevant for
#               grading.
#
#       A quiz is graded as the (rounded) percentage of all the questions on the quiz.
#
#           A quiz with 0 questions, is given a grade of 100%.
#
#       A course grade is given as the (rounded) percentage of all quizzes in that course.
#
#           NOTE:  Students *ARE* graded on quizzes that are not given to them!!!
#
#                  Yes, this is totally unfair -- that's life.
#
#                  [The specfiications did not say otherwise -- and unit tests shows that to be the case].
#
#       A semester grade is given as the (rounded) percentage of all the courses.
#
#       We only handle one semester, and all courses are assumed to be in that semester.
#
#       Hence, questions on quizzes with few questions are worth more than questions on quizzes with many questions
#       (likewize quizzes on courses with few quizzes are worth more than quizzes on courses with many quizzes).
#
#           Example:
#
#               math course:
#                   math quiz #1 has 1 question.
#                   math quiz #2 has 2 questions.
#
#                   The question  on math quiz #1 is worth 50% of the math grade.
#                   The questions on math quiz #2 are both worth 25% of the math grade.
#
#               english course
#                   english quiz #1 has 1 question
#                   The question on english quiz #1 is worth 100% of the english grade.
#
#               If the student takes both math & english:
#
#                   The student only answers math quiz #1, question #1, and english quiz #1, question #1.
#                   The grade is 75% (average of 50% for math course and 100% for english course).
#
#                   The student only answers math quiz #2, question #1 & question #2
#                   The grade is 25% (average of 50% for math course and 0% for english course).
#
#       Grade Percentage numbers are not converted, currently, to an alphanumeric grade (i.e.: "A", "B", "C", etc.).
#
#       "Each question is multiple choice" means there can be ONLY be one answers on a multiple choice question."
#
#           An alternative meaning of "multiple choice" is there can be multiple answers; however this choice was
#           not chosen.
#
#       A quiz answer, once submitted, may not be submitted a second time.
#
#   Added Specifications:
#
#       A teacher or a student is uniqely identified by a number.
#
#           The number must be a positive integer.
#
#           The number must be unique (Teachers & students share this number).
#
#           For debugging purposes a teacher or student also has a name (though this is not part of it's unique
#           identficiation).
#
#       A course is uniqely identified by a number.
#
#           The number must be a positive integer.
#
#           The number must be unique
#
#       A course is also uniquly identified by a name.
#
#           (Students use a course's name to find the course they want to join).
#
#       A quiz is uniqely identified by a course and a number.
#
#           For debugging purposes a quiz also has a name (though this is not part of it's unique identficiation).
#
#       A question is uniqely identified by a quiz and a number.
#
#           A question has a `question_text` which is the question to ask the student.
#
#       A person and course can share the same number with no conflicts.
#
#       A choice (on a question) is uniquely identified by a quiz and an upper case letter.
#
#           A choice has a `choice_text` which is the choice to present to the user.
#
