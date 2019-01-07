#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
#   OBSOLETE: This test has been CONVERTED to "features/Teacher.feature"
#
#       Some comments in this file still need to be copied over to "features/Teacher.feature"
#
from    Choice              import  create_Choice
from    Course              import  create_Course
from    Fact                import  create_false_fact
from    Fact                import  create_true_fact
from    Question            import  create_Question
from    Quiz                import  create_Quiz
from    Student             import  create_Student
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_grade():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math',    1, alice)

    bob     = create_Student('Bob',     2)
    charlie = create_Student('Charlie', 3)
    david   = create_Student('David',   4)

    bob    .join_course('Math')
    charlie.join_course('Math')
    david  .join_course('Math')


    #
    #   Math quiz: Simple
    #
    math_simple = create_Quiz(math, 'Simple')
    math_final  = create_Quiz(math, 'math_final')

    what_is_1_plus_1 = create_Question(math_simple, 'What is 1+1?')

    choice_1_1_1A = create_Choice(what_is_1_plus_1, False, 'One')
    choice_1_1_1B = create_Choice(what_is_1_plus_1, True,  'Two')
    choice_1_1_1C = create_Choice(what_is_1_plus_1, False, 'Three')

    what_is_2_minus_2 = create_Question(math_simple, 'What is 2-2?')

    choice_1_1_2A = create_Choice(what_is_2_minus_2, True,  'Zero')
    choice_1_1_2B = create_Choice(what_is_2_minus_2, False, 'One')
    choice_1_1_2C = create_Choice(what_is_2_minus_2, False, 'Two')

    what_is_3_multiplied_by_3 = create_Question(math_simple, 'What is 3 multiplied by 3?')

    choice_1_1_3A = create_Choice(what_is_3_multiplied_by_3, False, 'Zero')
    choice_1_1_3B = create_Choice(what_is_3_multiplied_by_3, False, 'Three')
    choice_1_1_3C = create_Choice(what_is_3_multiplied_by_3, False, 'Six')
    choice_1_1_3D = create_Choice(what_is_3_multiplied_by_3, True,  'Nine')

    what_is_4_modulus_4 = create_Question(math_simple, 'What is 4 modulus 4?')

    choice_1_1_4A = create_Choice(what_is_4_modulus_4, True, 'Zero')
    choice_1_1_4B = create_Choice(what_is_4_modulus_4, False, 'One')

    math_simple.give_quiz_to_all_students()


    #
    #   Test 1A:
    #       Answer one exactly question
    #
    true_fact__1_plus_1__is__2 = create_true_fact ('What is 1+1?', 'Two')

    bob.teach(true_fact__1_plus_1__is__2)
    bob.answer_questions()

    assert len(bob.questions) == 1


    #
    #   Test 1B:
    #       Answer the other two questions (in opposite order)
    #
    true_fact__2_minus_2__is__0  = create_true_fact ('What is 2-2?', 'Zero')

    false_fact__3_multiplied_by_3__is__6 = create_false_fact('What is 3 multiplied by 3?', 'Six')
    true_fact__3_multiplied_by_3__is__9  = create_false_fact('What is 3 multiplied by 3?', 'Nine')

    bob.teach(false_fact__3_multiplied_by_3__is__6)
    bob.teach(true_fact__2_minus_2__is__0)

    bob.answer_questions()

    assert len(bob.questions) == 3


    #
    #   For this quiz (with 4 questions):
    #
    #       Quiz [0]: <Quiz 'Math' 'Simple' #1.1>
    #           Question [0]: <Question 'Math' 'Simple' #1.1.1 'What is 1+1?'>
    #           Question [1]: <Question 'Math' 'Simple' #1.1.2 'What is 2-2?'>
    #           Question [2]: <Question 'Math' 'Simple' #1.1.3 'What is 3 multiplied by 3?'>
    #           Question [3]: <Question 'Math' 'Simple' #1.1.4 'What is 4 modulus 4?'>
    #
    #   The answers given by Bob (3 answers given; only 2 correct):
    #
    #       Question [0]: <Question 'Math' 'Simple' #1.1.1 'What is 1+1?'>
    #           <Choice 'Math' 'Simple' #1.1.1B correct 'Two'>
    #       Question [1]: <Question 'Math' 'Simple' #1.1.2 'What is 2-2?'>
    #           <Choice 'Math' 'Simple' #1.1.2A correct 'Zero'>
    #       Question [2]: <Question 'Math' 'Simple' #1.1.3 'What is 3 multiplied by 3?'>
    #           <Choice 'Math' 'Simple' #1.1.3C incorrect 'Six'>
    #
    #   Thus Bob scores 50% on the first quiz in math class.
    #
    assert bob.grade_quiz(math_simple) == 50


    #
    #   Math quiz: Final
    #
    math_final__what_is_4_modulus_4 = create_Question(math_final, 'What is 4 modulus 4?')

    math_final__choice_1_2_1A = create_Choice(math_final__what_is_4_modulus_4, True, 'Zero')
    math_final__choice_1_2_1B = create_Choice(math_final__what_is_4_modulus_4, False, 'One')

    math_final__what_is_5_to_the_5th_power = create_Question(math_final, 'What is 5 to the 5th power?')
    math_final__choice_1_2_2A = create_Choice(math_final__what_is_5_to_the_5th_power, False, 'Five')
    math_final__choice_1_2_2B = create_Choice(math_final__what_is_5_to_the_5th_power, False, '25')
    math_final__choice_1_2_2C = create_Choice(math_final__what_is_5_to_the_5th_power, False, '125')
    math_final__choice_1_2_2D = create_Choice(math_final__what_is_5_to_the_5th_power, False, '625')
    math_final__choice_1_2_2E = create_Choice(math_final__what_is_5_to_the_5th_power, True,  '3125')
    math_final__choice_1_2_2F = create_Choice(math_final__what_is_5_to_the_5th_power, False, '15625')

    math_final.give_quiz_to_all_students()

    true_fact__4_modules_4__is__0        = create_true_fact('What is 4 modulus 4?', 'Zero')
    true_fact__5_to_the_5th_power__is__0 = create_true_fact('What is 5 to the 5th power?', '3125')

    bob.teach(true_fact__4_modules_4__is__0)
    bob.teach(true_fact__5_to_the_5th_power__is__0)


    #
    #   NOTE:
    #       Bob now knows the true fact "What is 4 modulus 4?" is "Zero".
    #
    #       Bob will *THUS* answer this question on *BOTH* the Simple & the Final!!
    #
    bob.answer_questions()

    assert bob.grade_quiz(math_simple) == 75        #   Improved to 75%!
    assert bob.grade_quiz(math_final)  == 100

    assert bob.grade_course(math) == 88             #   87.5 rounded up to 88

    #
    #   Geography
    #
    geography = create_Course('Geography', 2, alice)

    bob    .join_course('Geography')
    charlie.join_course('Geography')

    geography_simple = create_Quiz(geography, 'Simple')
    geography_final = create_Quiz(geography, 'Final')

    how_many_states_are_in_the_united_states = create_Question(
            geography_simple,
            'How many states are in the United States?',
        )

    geography_simple__choice_1_2_1A = create_Choice(how_many_states_are_in_the_united_states, False, '13')
    geography_simple__choice_1_2_1B = create_Choice(how_many_states_are_in_the_united_states, True,  '50')
    geography_simple__choice_1_2_1C = create_Choice(how_many_states_are_in_the_united_states, False, '51')

    what_is_the_capital_of_new_york = create_Question(geography_final, 'What is the capital of New York?')
    geography_final__choice__1_2_1A = create_Choice(what_is_the_capital_of_new_york, False, 'Boston')
    geography_final__choice__1_2_1B = create_Choice(what_is_the_capital_of_new_york, True,  'New York')

    what_is_the_capital_of_the_united_states = create_Question(
            geography_final,
            'What is the capital of the United States?',
        )

    geography_final__choice__1_2_2A = create_Choice(what_is_the_capital_of_the_united_states, False, 'Boston')
    geography_final__choice__1_2_2B = create_Choice(what_is_the_capital_of_the_united_states, False, 'New York')

    geography_final__choice__1_2_2C = create_Choice(
            what_is_the_capital_of_the_united_states,
            True,
            'Washington, D.C.',
        )

    what_is_the_capital_of_washington = create_Question(geography_final, 'What is the capital of Washington?')
    geography_final__choice__1_2_3A = create_Choice(what_is_the_capital_of_washington, False, 'Madison')
    geography_final__choice__1_2_3B = create_Choice(what_is_the_capital_of_washington, True,  'Olympia')
    geography_final__choice__1_2_3C = create_Choice(what_is_the_capital_of_washington, False, 'Washington, D.C.')

    true_fact__50_states_in_the_united_states  = create_true_fact ('How many states are in the United States?', '50')
    false_fact__51_states_in_the_united_states = create_false_fact('How many states are in the United States?', '51')

    true_fact__the_capital_of__new_york__is__new_york  = create_true_fact(
            'What is the capital of New York?',
            'New York',
        )

    true_fact__the_capital_of_the_united_states_is__Washington_DC = create_true_fact(
            'What is the capital of the United States?',
            'Washington, D.C.',
        )

    true_fact__the_capital_of__washington__is__olympia = create_true_fact(
            'What is the capital of Washington?',
            'Olympia',
        )

    geography_simple.give_quiz_to_all_students()
    geography_final .give_quiz_to_all_students()

    bob.teach(false_fact__51_states_in_the_united_states)
    bob.teach(true_fact__the_capital_of__new_york__is__new_york)
    bob.teach(true_fact__the_capital_of_the_united_states_is__Washington_DC)

    bob.answer_questions()

    assert bob.grade_quiz(geography_simple) == 0
    assert bob.grade_quiz(geography_final)  == 67
    assert bob.grade_course(geography)      == 34


    #
    #   Eve teaches the jogging, jumping, and swimming classes
    #
    eve = create_Teacher('Eve', 5)

    jogging  = create_Course('Jogging',  3, eve)
    jumping  = create_Course('Jumping',  4, eve)
    swimming = create_Course('Swimming', 5, eve)

    bob.join_course('Jogging')
    bob.join_course('Jumping')
    bob.join_course('Swimming')

    jumping_empty_quiz = create_Quiz(jumping, 'Empty')

    swiming_easy_quiz  = create_Quiz(swimming, 'Easy')

    do_we_use_chlorine_in_our_swimming_pool = create_Question(
            swiming_easy_quiz,
            'Do we use chlorine in our swimming pool?',
        )

    swimming_final__choice_1_5_1A = create_Choice(do_we_use_chlorine_in_our_swimming_pool, False, 'No')
    swimming_final__choice_1_5_1B = create_Choice(do_we_use_chlorine_in_our_swimming_pool, True, 'Yes')

    swiming_easy_quiz.give_quiz_to_all_students()

    assert bob.grade_course(jogging)  == 100        #   100 since the jogging class had no quizzes!
    assert bob.grade_course(jumping)  == 100        #   100 since the jumping class had a quiz with no questions 
    assert bob.grade_course(swimming) == 0          #   100 since not yet answered the question.

    true_fact__we_use_chlorine_in_our_swimming_pool = create_true_fact(
            'Do we use chlorine in our swimming pool?',
            'Yes',
        )

    bob.teach(true_fact__we_use_chlorine_in_our_swimming_pool)
    bob.answer_questions()

    assert bob.grade_course(swimming) == 100        #   100 now that answered the question.


    #
    #   Due to the super easy swimming & jogging class, Bob will now get a great grade for the
    #   semester improving his 88 from his math class to a 96 ...
    #
    #   NOTE:
    #       The specifications did not request a semester grade, but a grade for the semester
    #       by each teachers.
    #
    #       This was more added during testing...
    #
    assert bob.grade_semester_by_teacher(alice) == 61       #   Math: 88; Geography: 34.  Averge: 61
    assert bob.grade_semester_by_teacher(eve)   == 100


    #
    #   Charlie & David's answers
    #
    #   NOTE:
    #       David is *NOT* taking geography -- but still "knows" the facts about geography.
    #
    #   Both Charlie & David get 100 in Math.
    #   However, since Charlie, *also* took Geography with Alice, and did poorly, his overall grade is down to 59.
    #   David, being lazier, and only taking Math, still gets 100!
    #
    for v in [charlie, david]:
        v.teach(true_fact__1_plus_1__is__2)
        v.teach(true_fact__2_minus_2__is__0)
        v.teach(true_fact__3_multiplied_by_3__is__9)
        v.teach(true_fact__4_modules_4__is__0)
        v.teach(true_fact__5_to_the_5th_power__is__0)

        v.teach(false_fact__51_states_in_the_united_states)
        v.teach(true_fact__the_capital_of__new_york__is__new_york)

        v.answer_questions()

    assert charlie.grade_course(math)      == 100
    assert david  .grade_course(math)      == 100
    assert charlie.grade_course(geography) == 17

    assert charlie.grade_semester_by_teacher(alice) == 59   #   (100 + 17) / 2)
    assert david  .grade_semester_by_teacher(alice) == 100  #   100.  David *DID* not take & fail Geography like Charlie!

    alice.debug_dump()
    math.debug_dump()
    math_simple.debug_dump()
    what_is_1_plus_1.debug_dump()
    charlie.debug_dump()
