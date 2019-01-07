#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    sys                 import  version_info
from    behave              import  given
from    behave              import  when
from    behave              import  then
from    behave              import  register_type
from    parse               import  with_pattern

from    Student             import  find_student
from    Course              import  find_course
from    Teacher             import  find_teacher


is_python_2 = (version_info.major is 2)
is_python_3 = (version_info.major is 3)


if is_python_3:
    unicode = str


#
#   parse_positive_integer(text)
#       Converts `text` from `unicode` to `str` (python 2)
#
@with_pattern(r'[1-9]\d*')
def parse_positive_integer(text):
    assert type(text) is unicode

    v = int(text)

    assert v > 0

    return v


register_type(PositiveInteger = parse_positive_integer)


#
#   parse_string(text)
#       Converts `text` from `unicode` to `str` (python 2)
#
if is_python_2:
    def parse_string(text):
        assert type(text) is unicode

        return str(text)
else:
    def parse_string(text):
        assert (type(text) is str)

        return text


register_type(String = parse_string)



#
#   query_actual_string(row, k)
#       Queries key `k` from `row`
#
#       Result must be a non-empty string.
#
#       Also converts the result from `unicode` to `str` (python 2)
#
if is_python_2:
    def query_actual_string(row, k):
        assert (type(k) is str) and (len(k) > 0)

        v = row[k]

        assert (type(v) is unicode) and (len(v) > 0)

        return str(v)
else:
    def query_actual_string(row, k):
        assert (type(k) is str) and (len(k) > 0)

        v = row[k]

        assert (type(v) is str) and (len(v) > 0)

        return v


#
#   query_course
#
def query_course(row, k):
    name = query_actual_string(row, k)

    return find_course(name)


#
#   query_grade(row, k)
#       Queries key `k` from `row`
#
#       Result must be an integer between 0 and 100
#
def query_grade(row, k):
    assert (type(k) is str) and (len(k) > 0)

    v = int(row[k])

    assert 0 <= v <= 100

    return v


#
#   query_none
#       Queries key `k` from `row`
#
#       Result must be an the string '.'
#
def query_none(row, k):
    assert (type(k) is str) and (len(k) > 0)
    assert row[k] == u'.'


#
#   query_no_or_yes
#
#       Queries key `k` from `row`
#
#       Result must be the string 'No' or 'Yes'
#
#       Returns 'False' or 'True'
#
def query_no_or_yes(row, k):
    assert (type(k) is str) and (len(k) > 0)

    v = row[k]

    if v == u'No':
        return False

    if v == u'Yes':
        return True

    raise ValueError(
            'Row entry {!r} unknown value {!r} (expected {!r} or {!r})'.format(
                k,
                v,
                'No',
                'Yes',
            ),
        )

#
#   query_positive_integer(row, k)
#       Queries key `k` from `row`
#
#       Result must be a positive integer (greater than 0)
#
def query_positive_integer(row, k):
    assert (type(k) is str) and (len(k) > 0)

    v = int(row[k])

    assert v > 0

    return v


#
#   query_student
#
def query_student(row, k):
    name = query_actual_string(row, k)

    return find_student(name)


#
#   query_teacher
#
def query_teacher(row, k):
    name = query_actual_string(row, k)

    return find_teacher(name)


#
#   Export
#
__all__ = ((
    'given',
    'query_actual_string',
    'query_course',
    'query_grade',
    'query_none',
    'query_no_or_yes',
    'query_positive_integer',
    'query_student',
    'query_teacher',
    'then',
    'when',
))
