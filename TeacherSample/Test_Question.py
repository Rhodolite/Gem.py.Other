#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Quiz                import  create_Quiz
from    Course              import  create_Course
from    Question            import  create_Question
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_can_create_unique_questions():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

    math_simple = create_Quiz(math, 'Simple')

    what_is_1_plus_1  = create_Question(math_simple, 'What is 1+1?')
    what_is_2_minus_2 = create_Question(math_simple, 'What is 2-2?')
    what_is_3_times_3 = create_Question(math_simple, 'What is 3*3?')

    assert what_is_1_plus_1.number  != what_is_2_minus_2.number
    assert what_is_1_plus_1.number  != what_is_3_times_3.number
    assert what_is_2_minus_2.number != what_is_3_times_3.number

    print
    print('              alice: {}'.format(alice))
    print('               math: {}'.format(math))
    print('        math_simple: {}'.format(math_simple))
    print('   what_is_1_plus_1: {}'.format(what_is_1_plus_1))
    print('  what_is_2_minus_2: {}'.format(what_is_2_minus_2))
    print('  what_is_3_times_3: {}'.format(what_is_3_times_3))
