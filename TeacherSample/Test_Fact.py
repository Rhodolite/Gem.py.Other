#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Choice              import  create_Choice
from    Course              import  create_Course
from    Fact                import  create_false_fact
from    Fact                import  create_true_fact
from    MustCatch           import  must_catch_ValueError
from    Question            import  create_Question
from    Quiz                import  create_Quiz
from    Student             import  create_Student
from    Teacher             import  create_Teacher
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_cannot_learn_fact_with_same_name_twice():
    alice = create_Student('Alice', 1)

    false_fact__1_plus_1__is__1 = create_false_fact('What is 1+1?', 'One')
    true_fact__1_plus_1__is__2  = create_true_fact ('What is 1+1?', 'Two')

    alice.teach(false_fact__1_plus_1__is__1)

    with must_catch_ValueError(
            '{} already knows {}; cannot be taught {}'.format(
                alice,
                false_fact__1_plus_1__is__1,
                true_fact__1_plus_1__is__2,
            ),
    ):
        alice.teach(true_fact__1_plus_1__is__2)
