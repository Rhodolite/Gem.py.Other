#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Choice              import  create_Choice
from    Course              import  create_Course
from    Question            import  create_Question
from    Quiz                import  create_Quiz
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_debug_dump():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

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

    what_is_3_times_3 = create_Question(math_simple, 'What is 3*3?')

    choice_1_1_3A = create_Choice(what_is_3_times_3, False, 'Zero')
    choice_1_1_3B = create_Choice(what_is_3_times_3, False, 'Three')
    choice_1_1_3C = create_Choice(what_is_3_times_3, False, 'Six')
    choice_1_1_3D = create_Choice(what_is_3_times_3, True,  'Nine')

    print
    print('        alice: {}'.format(alice))
    print('         math: {}'.format(math))
    print('  math_simple: {}'.format(math_simple))

    alice           .debug_dump()
    math            .debug_dump()
    math_simple     .debug_dump()
    what_is_1_plus_1.debug_dump()
