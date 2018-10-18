#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.ObjectParts')
def module():
    show_all = 0
    show_dot = 0


    #
    #   NOTE:
    #       This was used to develop "Capital/Class_Object.py".
    #
    #       Shared or Exported names are similiar to the names there; except here they are prefixed with "learning__"
    #       to distinguish them.
    #
    learning__Object__map         = Object.__dict__
    learning__Object__find_member = learning__Object__map.__getitem__


    find_member = learning__Object__find_member


    learning__known_Object_members__python_2 = ((
            '__class__',
            '__delattr__',
            '__doc__',
            '__format__',
            '__getattribute__',         #   tp_getattr
            '__hash__',                 #   tp_hash
            '__init__',                 #   tp_init
            '__new__',                  #   tp_new
            '__reduce__',
            '__reduce_ex__',
            '__repr__',                 #   tp_repr
            '__setattr__',              #   tp_setattr
            '__sizeof__',
            '__str__',                  #   tp_str
            '__subclasshook__',
        ))


    known_Object_members = learning__known_Object_members__python_2


    if is_python_3:
        known_Object_members += ((
                '__dir__',
                '__eq__',
                '__ge__',
                '__gt__',
                '__le__',
                '__lt__',
                '__ne__',
            ))


    #
    #   Access all the members
    #
    #   NOTE:
    #       There also *might* exist a `__getattr__` which will be named:
    #
    #           `operator conditional get attribute` (__getattr__)
    #
    #       To distinguish it from:
    #
    #           `operator get attribute` (__getattribute__)
    #
    learning__Object__member__class_type         = find_member('__class__')
    learning__Object__operator__delete_attribute = find_member('__delattr__')
    learning__Object__member__documentation      = find_member('__doc__')
    learning__Object__operator__format           = find_member('__format__')
    learning__Object__operator__get_attribute    = find_member('__getattribute__')
    learning__Object__operator__hash             = find_member('__hash__')
    learning__Object__operator__constructor      = find_member('__init__')
    learning__Object__operator__new              = find_member('__new__')
    learning__Object__operator__reduce           = find_member('__reduce__')
    learning__Object__operator__reduce_extended  = find_member('__reduce_ex__')
    learning__Object__operator__representation   = find_member('__repr__')
    learning__Object__operator__set_attribute    = find_member('__setattr__')
    learning__Object__operator__size_of          = find_member('__sizeof__')
    learning__Object__operator__string           = find_member('__str__')
    learning__Object__operator__subclass_hook    = find_member('__subclasshook__')


    if is_python_3:
        learning__Object__operator__introspection = find_member('__dir__')


    #
    #   Comparison operators
    #
    if is_python_3:
        learning__Object__operator__equal                 = find_member('__eq__')
        learning__Object__operator__greater_than          = find_member('__gt__')
        learning__Object__operator__greater_than_or_equal = find_member('__ge__')
        learning__Object__operator__less_than             = find_member('__lt__')
        learning__Object__operator__less_than_or_equal    = find_member('__le__')
        learning__Object__operator__not_equal             = find_member('__ne__')
    else:
        #
        #   Have to set these in python 2, since it tries to compare them to the `Type` operators
        #   (in `show_compare_members` when processing the `Type` members)
        #
        learning__Object__operator__equal                 = \
            learning__Object__operator__greater_than          = \
            learning__Object__operator__greater_than_or_equal = \
            learning__Object__operator__less_than             = \
            learning__Object__operator__less_than_or_equal    = \
            learning__Object__operator__not_equal             = none


    def show_dot_Object_member(k):
        v1 = attribute(Object, k)
        v2 = find_member(k)

        line('%41s:  %r', arrange('Object.%s', k), v1)

        if v1 != v2:
            line('%41s:  %r', arrange('Object.__dict__[%r]', k), v2)
            blank()


    @share
    def show_one_member(show_same, name, member, object_member):
        if (show_same) or (member is not object_member):
            line('%41s:  %r', name, member)


    @share
    def show_compare_members(
            name,
            show_same,
            operator__equal,
            operator__greater_than,
            operator__greater_than_or_equal,
            operator__less_than,
            operator__less_than_or_equal,
            operator__not_equal,
    ):
        blank()

        if show_same:
            line('%s comparison members:', name)
        else:
            line('%s comparison members (different from Object):', name)

        with indent(prefix = 2):
            show_one_member(
                    show_same,
                    '== (__eq__)',
                    operator__equal,
                    learning__Object__operator__equal,
                )

            show_one_member(
                    show_same,
                    '> (__gt__)',
                    operator__greater_than,
                    learning__Object__operator__greater_than,
                )

            show_one_member(
                    show_same,
                    '>= (__ge__)',
                    operator__greater_than_or_equal,
                    learning__Object__operator__greater_than_or_equal,
                )

            show_one_member(
                    show_same,
                    '< (__lt__)',
                    operator__less_than,
                    learning__Object__operator__less_than,
                )

            show_one_member(
                    show_same,
                    '<= (__le__)',
                    operator__less_than_or_equal,
                    learning__Object__operator__less_than_or_equal,
                )

            show_one_member(
                    show_same,
                    '!= (__ne__)',
                    operator__not_equal,
                    learning__Object__operator__not_equal,
                )


    @share
    def show_Object_members(
            name,
            show_same,
            member__class_type,
            operator__delete_attribute,
            member__documentation,
            operator__format,
            operator__get_attribute,
            operator__hash,
            operator__constructor,
            operator__new,
            operator__reduce,
            operator__reduce_extended,
            operator__representation,
            operator__set_attribute,
            operator__size_of,
            operator__string,
            operator__subclass_hook,
    ):
        blank()

        if show_same:
            line('%s members:', name)
        else:
            line('%s members (different from Object):', name)

        with indent(prefix = 2):
            show_one_member(
                    show_same,
                    'class type (__class__)',
                    member__class_type,
                    learning__Object__member__class_type,
                )

            show_one_member(
                    show_same,
                    'delete attribute (__delattr__)',
                    operator__delete_attribute,
                    learning__Object__operator__delete_attribute,
                )

            show_one_member(
                    show_same,
                    'documentation (__doc__)',
                    member__documentation,
                    learning__Object__member__documentation,
                )


            show_one_member(
                    show_same,
                    'format (__format__)',
                    operator__format,
                    learning__Object__operator__format,
                )

            show_one_member(
                    show_same,
                    'get attribute (__getattribute__)',
                    operator__get_attribute,
                    learning__Object__operator__get_attribute,
                )

            show_one_member(
                    show_same,
                    'hash (__hash__)',
                    operator__hash,
                    learning__Object__operator__hash
                )

            show_one_member(
                    show_same,
                    'constructor (__init__)',
                    operator__constructor,
                    learning__Object__operator__constructor,
                )

            show_one_member(
                    show_same,
                    'new (__new__)',
                    operator__new,
                    learning__Object__operator__new,
                )

            show_one_member(
                    show_same,
                    'reduce (__reduce__)',
                    operator__reduce,
                    learning__Object__operator__reduce,
                )

            show_one_member(
                    show_same,
                    'reduce extended (__reduce_ex__)',
                    operator__reduce_extended,
                    learning__Object__operator__reduce_extended,
                )

            show_one_member(
                    show_same,
                    'representation (__repr__)',
                    operator__representation,
                    learning__Object__operator__representation,
                )

            show_one_member(
                    show_same,
                    'set attribute (__setattr__)',
                    operator__set_attribute,
                    learning__Object__operator__set_attribute,
                )

            show_one_member(
                    show_same,
                    'size of (__sizeof__)',
                    operator__size_of,
                    learning__Object__operator__size_of,
                )

            show_one_member(
                    show_same,
                    'string (__str__)',
                    operator__string,
                    learning__Object__operator__string,
                )

            show_one_member(
                    show_same,
                    'sub class hook (__subclasshook__)',
                    operator__subclass_hook,
                    learning__Object__operator__subclass_hook,
                )


    @share
    def show_Object_members_3(name, show_same, operator__introspection):
        blank()

        if show_same:
            line('%s members (python 3 only):', name)
        else:
            line('%s members (different from Object) (python 3 only):', name)

        with indent(prefix = 2):
            show_one_member(
                    show_same,
                    'introspect (__dir__)',
                    operator__introspection,
                    learning__Object__operator__introspection,
                )


    @share
    def show_object_parts():
        blank()

        with indent('show_object_parts:', prefix = 2):
            blank_suppress()

            known_members_set  = FrozenSet(known_Object_members)
            actual_members_set = FrozenSet(introspect_hidden(Object))

            extra_members   = actual_members_set - known_members_set
            missing_members = known_members_set  - actual_members_set

            if extra_members:
                raise_runtime_error("extra members in `Object`: %s", sorted_list(extra_members))

            if missing_members:
                raise_runtime_error("missing members in `Object`: %s", sorted_list(missing_members))


            #
            #   Using python 2.2.12, the following:
            #
            #       for k in sorted_list(introspect(Object)):
            #           line('%18s: %r', k, find_member(k))
            #
            #   returns:
            #
            #              __class__: <attribute '__class__' of 'object' objects>
            #            __delattr__: <slot wrapper '__delattr__' of 'object' objects>
            #                __doc__: 'The most base type'
            #             __format__: <method '__format__' of 'object' objects>
            #       __getattribute__: <slot wrapper '__getattribute__' of 'object' objects>
            #               __hash__: <slot wrapper '__hash__' of 'object' objects>
            #               __init__: <slot wrapper '__init__' of 'object' objects>
            #                __new__: <built-in method __new__ of type object at 0x8f8740>
            #             __reduce__: <method '__reduce__' of 'object' objects>
            #          __reduce_ex__: <method '__reduce_ex__' of 'object' objects>
            #               __repr__: <slot wrapper '__repr__' of 'object' objects>
            #            __setattr__: <slot wrapper '__setattr__' of 'object' objects>
            #             __sizeof__: <method '__sizeof__' of 'object' objects>
            #                __str__: <slot wrapper '__str__' of 'object' objects>
            #       __subclasshook__: <method '__subclasshook__' of 'object' objects>
            #
            #   Uncomment the following to print under another version of python:
            #
            if show_all:
                with indent('All Object members:', prefix = 2):
                    for k in sorted_list(introspect(Object)):
                        line('%18s: %r', k, find_member(k))


            #
            #   NOTE:
            #       When accessing a member using the `.` notation, in certain cases the value is changed
            #       from what is stored inside the map (`__dict__` member)
            #
            #       The best known examples are:
            #
            #           1.  A method.
            #
            #               Accessing the method using the `.` returns a bound method.
            #
            #           2.  A property.
            #
            #               Accessing the property using the `.` causes the property value to be calculated
            #               (often by calling a function).
            #
            #       Likewise when accessing `Object.__class__`, this returns a different value than
            #       `Object.__dict__["class"]`.
            #
            #           1.  In the map is stored `<attribute '__class__' of 'object' objects>`
            #
            #           2.  While accessing `Object.__class__` calculates the `__class__` value
            #               (in this case `Type` which is the type of `Object`).
            #
            #       Overall for `Object` there are two attributes that need to be accessed via
            #       the mapping instead of using `.` notation, these are:
            #
            #           1.  __class__
            #
            #           2.  __subclasshook__
            #
            #               (Although here the difference is very subtle between `built-in method` .vs.
            #               `method` -- and both seem to behave the same).
            #
            #       However, to be consistent (and support future changes to python) all attributes are
            #       accessed via the map for safety).
            #
            if show_dot :
                blank()

                with indent('Object members __class__ & __subclasshook__:', prefix = 2):
                    show_dot_Object_member('__class__')
                    show_dot_Object_member('__subclasshook__')


            #
            #   Output
            #
            show_Object_members(
                    'Object',
                    true,
                    learning__Object__member__class_type,
                    learning__Object__operator__delete_attribute,
                    learning__Object__member__documentation,
                    learning__Object__operator__format,
                    learning__Object__operator__get_attribute,
                    learning__Object__operator__hash,
                    learning__Object__operator__constructor,
                    learning__Object__operator__new,
                    learning__Object__operator__reduce,
                    learning__Object__operator__reduce_extended,
                    learning__Object__operator__representation,
                    learning__Object__operator__set_attribute,
                    learning__Object__operator__size_of,
                    learning__Object__operator__string,
                    learning__Object__operator__subclass_hook,
                )


            if is_python_3:
                show_compare_members(
                        'Object',
                        true,
                        learning__Object__operator__equal,
                        learning__Object__operator__greater_than,
                        learning__Object__operator__greater_than_or_equal,
                        learning__Object__operator__less_than,
                        learning__Object__operator__less_than_or_equal,
                        learning__Object__operator__not_equal
                    )

                show_Object_members_3('Object', true, learning__Object__operator__introspection)


    share(
            'learning__known_Object_members__python_2',       learning__known_Object_members__python_2,
            'learning__Object__find_member',                  learning__Object__find_member,
            'learning__Object__member__class_type',           learning__Object__member__class_type,
            'learning__Object__member__documentation',        learning__Object__member__documentation,
            'learning__Object__operator__constructor',        learning__Object__operator__constructor,
            'learning__Object__operator__delete_attribute',   learning__Object__operator__delete_attribute,
            'learning__Object__operator__format',             learning__Object__operator__format,
            'learning__Object__operator__get_attribute',      learning__Object__operator__get_attribute,
            'learning__Object__operator__hash',               learning__Object__operator__hash,
            'learning__Object__operator__new',                learning__Object__operator__new,
            'learning__Object__operator__reduce_extended',    learning__Object__operator__reduce_extended,
            'learning__Object__operator__reduce',             learning__Object__operator__reduce,
            'learning__Object__operator__representation',     learning__Object__operator__representation,
            'learning__Object__operator__set_attribute',      learning__Object__operator__set_attribute,
            'learning__Object__operator__size_of',            learning__Object__operator__size_of,
            'learning__Object__operator__string',             learning__Object__operator__string,
            'learning__Object__operator__subclass_hook',      learning__Object__operator__subclass_hook,
        )


    if is_python_3:
        share(
                'learning__Object__operator__equal',                  learning__Object__operator__equal,
                'learning__Object__operator__greater_than',           learning__Object__operator__greater_than,

                'learning__Object__operator__greater_than_or_equal',
                    learning__Object__operator__greater_than_or_equal,

                'learning__Object__operator__introspection',          learning__Object__operator__introspection,
                'learning__Object__operator__less_than',              learning__Object__operator__less_than,
                'learning__Object__operator__less_than_or_equal',     learning__Object__operator__less_than_or_equal,
                'learning__Object__operator__not_equal',              learning__Object__operator__not_equal,
            )
