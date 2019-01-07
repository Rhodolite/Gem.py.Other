#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Course              import  zap_courses
from    SchoolIdentifier    import  zap_school_identifiers
from    Quiz                import  zap_quiz_by_key
from    Question            import  zap_question_by_key
from    Teacher             import  zap_teachers
from    Student             import  zap_students



#
#   cleanup_after_test(f)
#           f       - A function used as a test with pytest.
#
#       Call `f` -- followed by a teardown (even if `f` throws an exception).
#
#       (i.e.: clear any temporary course and person identifiers created).
#
#   NOTE:
#       For initially learning "pytest" it seemed simplier to use global test functions.
#
#       I tried these as a class with methods, however that seemed to do one `setup` and one `teardown` for *ALL* the
#       tests in a class (which is *very* useful in other cases) -- here, instead, I wanted a `teardown` for each test.
#
#       Wrapping each of these tests in a class seemed to make the code too wordy ...
#
#       There might be better ways to do this with "pytest" which I will learn later.
#
def cleanup_after_test(f):
    def call_f_and_then_teardown():
        try:
            f()
        finally:
            teardown()

    return call_f_and_then_teardown


def teardown():
    zap_courses()
    zap_question_by_key()
    zap_quiz_by_key()
    zap_school_identifiers()
    zap_students()
    zap_teachers()


#
#   Export
#
__all__ = ((
    'cleanup_after_test',
    'teardown',
))
