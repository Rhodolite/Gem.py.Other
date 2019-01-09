#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#

#
#   CourseIdentifier    - used by Course
#   PersonIdentifier    - used by Student & Teacher.
#
#       A `SchoolIdentifier` (i.e.: a `CourseIdentifier` or a `PersonIdentifier`) has:
#
#           1.  A name          - Must be a non-empty String
#           2.  A number        - Must be a positive Integer.  Must be unique.
#
#   NOTE:
#       A `Course` and a `Person` (i.e.: A `Student` or a `Teacher`) may share the same number.
#       However a `Student` and a `Teacher` may not share the same number (since they are both a `Person`).
#
class SchoolIdentifier(object):
    __slots__ = ((
        'name',                         #   Non-empty String
        'number',                       #   Positive Integer
    ))


    def __init__(self, name, number):
        self.name   = name
        self.number = number


    def __repr__(self):
        return '<{} {!r} #{}>'.format(self.__class__.__name__, self.name, self.number)


class CourseIdentifier(SchoolIdentifier):
    __slots__ = (())


class PersonIdentifier(SchoolIdentifier):
    __slots__ = (())


#
#   create_CourseIdentifier(name, number)
#       name        - The name of the person.    Must be non-empty String.
#       number      - The number of the person.  Must be a postiive Integer.  Must be unique.
#
#   create_PersonIdentifier(name, number)
#       name        - The name of the person.    Must be non-empty String.
#       number      - The number of the person.  Must be a postive Integer.  Must be unique.
#
#   Verb choices:
#
#   1.  find
#
#           Attempt to find the item, throw an exception if not found
#
#       Hence for a python `dict`, `.find` is an alias for `.__getitem__`
#
#   2.  lookup
#
#           Attempt to find the item, but return `None` if not found (do not raise an exception).
#
#       Hence for a python `dict`, `.lookup` is an alias for `.get`
#
#   3.  produce
#
#           Create another function, typically as a closure around local variables.
#
#           A producer function can be thought of as a template (C++) or generic (Java).
#
#   4.  store
#
#           An alias for `.set`.
#
#       ".get" and "set" have a hamming distance of 1, and thus are not good choices for verbs.
#
#   3.  zap
#
#           Unconditionally remove all elements.
#
#       Hence for a python `dict`, `.zap` is an alias for `.clear`
#
#   NOTE:
#       One issue, with producer functions, is the multiple funtions they create, all have the
#       same name in stack traces -- which makes debugging harder.
#
#       In real code, I use `@rename` before all such functions, and give them unique names
#       (when running python in debug mode; but not in production mode).
#
#   produce_identifier_functions(Meta):
#       Meta        - The class to produce the `create_identifier` and `zap_identifiers` functions.
#
def produce_identifier_functions(Meta):
    identifier_cache  = {}
    find_identifier   = identifier_cache.__getitem__
    lookup_identifier = identifier_cache.get
    store_identifier  = identifier_cache.__setitem__
    zap_identifiers   = identifier_cache.clear


    def create_identifier(name, number):
        assert (type(name)   is str) and (len(name) > 0)
        assert (type(number) is int) and (number    > 0)

        if lookup_identifier(number) is not None:
            raise ValueError(
                    "Attempt to create a {} with duplicate #{} (duplicate of: {})".format(
                        Meta.__name__,
                        number,
                        find_identifier(number),
                    ),
                )

        identifier = Meta(name, number)

        store_identifier(number, identifier)

        return identifier



    return [create_identifier, find_identifier, zap_identifiers]


#
#   NOTE:
#       We could have made these class methods of the underlying classes -- but I find it
#       cleaner to use long globals names.
#
#       This would also simplify, for the first time reader, a producer function like
#       `produce_identifier_functions` (the first time some reads a producer function,
#       it is a little confusing).
#
#       However, once used to producer functions, they are actually easier to read and
#       understand than class methods.
#
#   IN GENERAL:
#       I find naming a routine `verb_noun` much clearer than naming a class method
#       named `noun.verb`.
#
#       Thus I find `create_course_identfier` to be clearer than class method
#       named `CourseIdentifier.create`.
#
#       This is a personal preference, and of course, on a team project, I would
#       follow the team guidelines.
#
#       Since no guidelines where given for this project, I just used my personal
#       preferences here.
#
[
        create_course_identifier, find_course_identifier, zap_course_identifiers,
] = produce_identifier_functions(CourseIdentifier)

[
        create_person_identifier, find_person_identifier, zap_person_identifiers,
] = produce_identifier_functions(PersonIdentifier)


def zap_school_identifiers():
    zap_course_identifiers()
    zap_person_identifiers()


#
#   Exports
#
__all__ = ((
    'create_course_identifier',
    'create_person_identifier',
    'find_course_identifier',
    'find_person_identifier',
    'zap_school_identifiers',
))
