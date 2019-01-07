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
def test_can_create_unique_choices():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

    math_simple = create_Quiz(math, 'Simple')

    what_is_1_plus_1 = create_Question(math_simple, 'What is 1+1?')

    choice_1_1_1A = create_Choice(what_is_1_plus_1, False, 'One')
    choice_1_1_1B = create_Choice(what_is_1_plus_1, True,  'Two')
    choice_1_1_1C = create_Choice(what_is_1_plus_1, False, 'Three')

    assert choice_1_1_1A.letter != choice_1_1_1B.letter
    assert choice_1_1_1A.letter != choice_1_1_1C.letter
    assert choice_1_1_1B.letter != choice_1_1_1C.letter

    what_is_2_minus_2 = create_Question(math_simple, 'What is 2-2?')

    choice_1_1_2A = create_Choice(what_is_2_minus_2, True,  'Zero')
    choice_1_1_2B = create_Choice(what_is_2_minus_2, False, 'One')
    choice_1_1_2C = create_Choice(what_is_2_minus_2, False, 'Two')

    print
    print('              alice: {}'.format(alice))
    print('               math: {}'.format(math))
    print('        math_simple: {}'.format(math_simple))
    print('   what_is_1_plus_1: {}'.format(what_is_1_plus_1))
    print('      choice_1_1_1A: {}'.format(choice_1_1_1A))
    print('      choice_1_1_1B: {}'.format(choice_1_1_1B))
    print('      choice_1_1_1C: {}'.format(choice_1_1_1C))
    print('  what_is_2_minus_2: {}'.format(what_is_2_minus_2))
    print('      choice_1_1_2A: {}'.format(choice_1_1_2A))
    print('      choice_1_1_2B: {}'.format(choice_1_1_2B))
    print('      choice_1_1_2C: {}'.format(choice_1_1_2C))
