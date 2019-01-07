#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Person              import  Person
from    SchoolIdentifier    import  create_person_identifier
from    ProduceByName       import  produce_find_lookup_verify_by_name_functions


#
#   Teacher
#
class Teacher(Person):
    __slots__ = ((
    #   'identifier',                   #   Inherited from Person
        'courses',                      #   List of Course
    ))


    is_teacher = True


    #
    #   Private
    #
    def __init__(self, identifier):
        super(Teacher, self).__init__(identifier)

        self.courses = []


    def debug_dump(self):
        print
        print('Dump of {}'.format(self))

        for [i, v] in enumerate(self.courses):
            print('  Course [{}]:  {}'.format(i, v))

            
    #
    #   Public
    #


    #.__repr__                          #   Inherited from Person


    def add_course(self, course):
        assert course.is_course

        assert course not in self.courses

        self.courses.append(course)


    #.name                              #   Inherited from Person
    #.number                            #   Inherited from Person


[
        find_teacher, lookup_teacher, store_teacher, verify_unique_teacher, zap_teachers,
] = produce_find_lookup_verify_by_name_functions('teacher', Teacher)


def create_Teacher(name, number):
    identifier = create_person_identifier(name, number)

    verify_unique_teacher(name)

    teacher = Teacher(identifier)

    store_teacher(name, teacher)

    return teacher


#
#   Exports
#
__all__ = ((
    'create_Teacher',
    'find_teacher',
    'zap_teachers',
))
