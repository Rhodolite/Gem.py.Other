#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Course              import  create_Course
from    Quiz                import  create_Quiz
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_can_create_unique_quizzes():
    alice = create_Teacher('Alice', 1)

    math = create_Course('Math', 1, alice)

    addition    = create_Quiz(math, 'Addition')
    subtraction = create_Quiz(math, 'Subtraction')
    math_final  = create_Quiz(math, 'math_final')

    assert addition.number     != subtraction.number
    assert addition.number    != math_final.number
    assert subtraction.number != math_final.number

    print
    print('        alice: {}'.format(alice))
    print('         math: {}'.format(math))
    print('     addition: {}'.format(addition))
    print('  subtraction: {}'.format(subtraction))
    print('   math_final: {}'.format(math_final))
