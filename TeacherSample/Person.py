#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Person
#       Base class of Student and Teacher
#
class Person(object):
    __slots__ = ((
        'identifier',                   #   PersonIdentifier
    ))


    is_student = False
    is_teacher = False


    def __init__(self, identifier):
        self.identifier = identifier


    def __repr__(self):
        return '<{} {!r} #{}>'.format(self.__class__.__name__, self.name, self.number)


    @property
    def name(self):
        return self.identifier.name


    @property
    def number(self):
        return self.identifier.number


#
#   Exports
#
__all__ = ((
    'Person',
))
