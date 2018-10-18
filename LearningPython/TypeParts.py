#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.TypeParts')
def module():
    require_module('LearningPython.ObjectParts')


    show_all  = 0
    show_same = 7


    #
    #   NOTE:
    #       This was used to develop "Capital/Class_Type.py".
    #
    #       Shared or Exported names are similiar to the names there; except here they are prefixed with "learning__"
    #       to distinguish them.
    #
    learning__Type__map             = Type.__dict__
    learning__Type__find_member     = learning__Type__map.__getitem__
    learning__Type__contains_member = learning__Type__map.__contains__


    def find_member(k):
        if learning__Type__contains_member(k):
            return learning__Type__find_member(k)

        return learning__Object__find_member(k)


    known_Type_members = (
              learning__known_Object_members__python_2
            + ((
                  '__abstractmethods__',
                  '__base__',
                  '__bases__',
                  '__basicsize__',
                  '__call__',
                  '__dict__',
                  '__dictoffset__',
                  '__eq__',
                  '__flags__',
                  '__ge__',
                  '__gt__',
                  '__instancecheck__',
                  '__itemsize__',
                  '__le__',
                  '__lt__',
                  '__module__',
                  '__mro__',
                  'mro',
                  '__name__',
                  '__ne__',
                  '__subclasscheck__',
                  '__subclasses__',
                  '__weakrefoffset__',
              ))
        )


    if is_python_3:
        known_Type_members += ((
                '__dir__',
                '__prepare__',
                '__qualname__',
                '__text_signature__',
            ))


    @share
    def show_type_parts():
        blank()

        with indent('show_type_parts:', prefix = 2):
            blank_suppress()

            known_members_set  = FrozenSet(known_Type_members)
            actual_members_set = FrozenSet(introspect_hidden(Type))

            extra_members   = actual_members_set - known_members_set
            missing_members = known_members_set  - actual_members_set

            if extra_members:
                raise_runtime_error("extra members in `Type`: %s", sorted_list(extra_members))

            if missing_members:
                raise_runtime_error("missing members in `Type`: %s", sorted_list(missing_members))


            #
            #   Using python 2.2.12, the following:
            #
            #       for k in sorted_list(introspect(Object)):
            #           line('%19s: %r', k, find_member(k))
            #
            #   returns:
            #
            #       __abstractmethods__: <attribute '__abstractmethods__' of 'type' objects>
            #                  __base__: <member '__base__' of 'type' objects>
            #                 __bases__: <attribute '__bases__' of 'type' objects>
            #             __basicsize__: <member '__basicsize__' of 'type' objects>
            #                  __call__: <slot wrapper '__call__' of 'type' objects>
            #                 __class__: <attribute '__class__' of 'object' objects>
            #               __delattr__: <slot wrapper '__delattr__' of 'type' objects>
            #                  __dict__: <attribute '__dict__' of 'type' objects>
            #            __dictoffset__: <member '__dictoffset__' of 'type' objects>
            #                   __doc__: <attribute '__doc__' of 'type' objects>
            #                    __eq__: <slot wrapper '__eq__' of 'type' objects>
            #                 __flags__: <member '__flags__' of 'type' objects>
            #                __format__: <method '__format__' of 'object' objects>
            #                    __ge__: <slot wrapper '__ge__' of 'type' objects>
            #          __getattribute__: <slot wrapper '__getattribute__' of 'type' objects>
            #                    __gt__: <slot wrapper '__gt__' of 'type' objects>
            #                  __hash__: <slot wrapper '__hash__' of 'type' objects>
            #                  __init__: <slot wrapper '__init__' of 'type' objects>
            #         __instancecheck__: <method '__instancecheck__' of 'type' objects>
            #              __itemsize__: <member '__itemsize__' of 'type' objects>
            #                    __le__: <slot wrapper '__le__' of 'type' objects>
            #                    __lt__: <slot wrapper '__lt__' of 'type' objects>
            #                __module__: <attribute '__module__' of 'type' objects>
            #                   __mro__: <member '__mro__' of 'type' objects>
            #                  __name__: <attribute '__name__' of 'type' objects>
            #                    __ne__: <slot wrapper '__ne__' of 'type' objects>
            #                   __new__: <built-in method __new__ of type object at 0x8f9780>
            #                __reduce__: <method '__reduce__' of 'object' objects>
            #             __reduce_ex__: <method '__reduce_ex__' of 'object' objects>
            #                  __repr__: <slot wrapper '__repr__' of 'type' objects>
            #               __setattr__: <slot wrapper '__setattr__' of 'type' objects>
            #                __sizeof__: <method '__sizeof__' of 'object' objects>
            #                   __str__: <slot wrapper '__str__' of 'object' objects>
            #         __subclasscheck__: <method '__subclasscheck__' of 'type' objects>
            #            __subclasses__: <method '__subclasses__' of 'type' objects>
            #          __subclasshook__: <method '__subclasshook__' of 'object' objects>
            #         __weakrefoffset__: <member '__weakrefoffset__' of 'type' objects>
            #                       mro: <method 'mro' of 'type' objects>
            #
            #   Uncomment the following to print under another version of python:
            #
            if show_all:
                blank()

                with indent('All Type members:', prefix = 2):
                    for k in sorted_list(introspect(Type)):
                        line('%19s: %r', k, find_member(k))


            #
            #   NOTE:
            #       See note in `ObjectParts.py` on difference in accessing a type with `.` notation from
            #       what is stored inside the map (`__dict__` member).
            #
            #       For `Type` there are a lot more members that behave this way (since as a metaclass it
            #       supports a lot of members that for the underlying class; and as the metaclass for itself,
            #       all these members have different values when accessed as `.` notation instead of via
            #       the map).
            #


            #
            #   Access the members shared with `Object`
            #
            learning__Type__member__class_type         = find_member('__class__')
            learning__Type__operator__delete_attribute = find_member('__delattr__')
            learning__Type__member__documentation      = find_member('__doc__')
            learning__Type__operator__format           = find_member('__format__')
            learning__Type__operator__get_attribute    = find_member('__getattribute__')
            learning__Type__operator__hash             = find_member('__hash__')
            learning__Type__operator__constructor      = find_member('__init__')
            learning__Type__operator__new              = find_member('__new__')
            learning__Type__operator__reduce           = find_member('__reduce__')
            learning__Type__operator__reduce_extended  = find_member('__reduce_ex__')
            learning__Type__operator__representation   = find_member('__repr__')
            learning__Type__operator__set_attribute    = find_member('__setattr__')
            learning__Type__operator__size_of          = find_member('__sizeof__')
            learning__Type__operator__string           = find_member('__str__')
            learning__Type__operator__subclass_hook    = find_member('__subclasshook__')

            if is_python_3:
                learning__Type__operator__introspection = find_member('__dir__')


            #
            #   Compare to `Object` .vs. `Type` members
            #
            assert learning__Object__member__class_type         is     learning__Type__member__class_type
            assert learning__Object__operator__delete_attribute is not learning__Type__operator__delete_attribute
            assert learning__Object__member__documentation      is not learning__Type__member__documentation
            assert learning__Object__operator__format           is     learning__Type__operator__format
            assert learning__Object__operator__get_attribute    is not learning__Type__operator__get_attribute

            if is_python_2:
                assert learning__Object__operator__hash         is not learning__Type__operator__hash

            if is_python_3:
                assert learning__Object__operator__hash         is     learning__Type__operator__hash

            assert learning__Object__operator__constructor      is not learning__Type__operator__constructor
            assert learning__Object__operator__new              is not learning__Type__operator__new
            assert learning__Object__operator__reduce           is     learning__Type__operator__reduce
            assert learning__Object__operator__reduce_extended  is     learning__Type__operator__reduce_extended
            assert learning__Object__operator__representation   is not learning__Type__operator__representation
            assert learning__Object__operator__set_attribute    is not learning__Type__operator__set_attribute


            if is_python_2:
                assert learning__Object__operator__size_of      is     learning__Type__operator__size_of

            if is_python_3:
                assert learning__Object__operator__size_of      is not learning__Type__operator__size_of

            assert learning__Object__operator__string           is     learning__Type__operator__string
            assert learning__Object__operator__subclass_hook    is     learning__Type__operator__subclass_hook

            if is_python_3:
                assert learning__Object__operator__introspection is not learning__Type__operator__introspection


            #
            #   Comparison operators
            #
            learning__Type__operator__equal                 = find_member('__eq__')
            learning__Type__operator__greater_than          = find_member('__gt__')
            learning__Type__operator__greater_than_or_equal = find_member('__ge__')
            learning__Type__operator__less_than             = find_member('__lt__')
            learning__Type__operator__less_than_or_equal    = find_member('__le__')
            learning__Type__operator__not_equal             = find_member('__ne__')


            if is_python_3:
                assert learning__Object__operator__equal                 is learning__Type__operator__equal
                assert learning__Object__operator__greater_than          is learning__Type__operator__greater_than
                assert learning__Object__operator__greater_than_or_equal is learning__Type__operator__greater_than_or_equal
                assert learning__Object__operator__less_than             is learning__Type__operator__less_than
                assert learning__Object__operator__less_than_or_equal    is learning__Type__operator__less_than_or_equal
                assert learning__Object__operator__not_equal             is learning__Type__operator__not_equal


            #
            #   Output
            #
            show_Object_members(
                    'Type',
                    show_same,
                    learning__Type__member__class_type,
                    learning__Type__operator__delete_attribute,
                    learning__Type__member__documentation,
                    learning__Type__operator__format,
                    learning__Type__operator__get_attribute,
                    learning__Type__operator__hash,
                    learning__Type__operator__constructor,
                    learning__Type__operator__new,
                    learning__Type__operator__reduce,
                    learning__Type__operator__reduce_extended,
                    learning__Type__operator__representation,
                    learning__Type__operator__set_attribute,
                    learning__Type__operator__size_of,
                    learning__Type__operator__string,
                    learning__Type__operator__subclass_hook,
                )

            show_compare_members(
                    'Type',
                    show_same,
                    learning__Type__operator__equal,
                    learning__Type__operator__greater_than,
                    learning__Type__operator__greater_than_or_equal,
                    learning__Type__operator__less_than,
                    learning__Type__operator__less_than_or_equal,
                    learning__Type__operator__not_equal
                )

            if is_python_3:
                show_Object_members_3('Type', show_same, learning__Type__operator__introspection)


            #
            #   `Type` *NOT* shared with `Object`
            #
            learning__Type__member__abstract_methods                        = find_member('__abstractmethods__')
            learning__Type__member__class_parent                            = find_member('__base__')
            learning__Type__member__class_bases                             = find_member('__bases__')
            learning__Type__member__class_basic_size                        = find_member('__basicsize__')
            learning__Type__operator__call                                  = find_member('__call__')
            learning__Type__member__class_members                           = find_member('__dict__')
            learning__Type__member__class_members_offset                    = find_member('__dictoffset__')
            learning__Type__member__class_flags                             = find_member('__flags__')
            learning__Type__operator__instance_check                        = find_member('__instancecheck__')
            learning__Type__member__class_item_size                         = find_member('__itemsize__')
            learning__Type__member__class_calculate_method_resolution_order = find_member('mro')
            learning__Type__member__method_resolution_order                 = find_member('__mro__')
            learning__Type__member__class_name                              = find_member('__name__')
            learning__Type__operator__subclass_check                        = find_member('__subclasscheck__')
            learning__Type__operator__subclasses                            = find_member('__subclasses__')
            learning__Type__member__weak_reference_offset                   = find_member('__weakrefoffset__')

            blank()

            with indent("Type members *NOT* shared with Object:", prefix = 2):
                show_one_member(
                        true,
                        'abstract methods (__abstractmethods__)',
                        learning__Type__member__abstract_methods,
                        learning__Type__member__abstract_methods,
                    )

                show_one_member(
                        true,
                        'parent (__base__)',
                        learning__Type__member__class_parent,
                        learning__Type__member__class_parent,
                    )

                show_one_member(
                        true,
                        'bases (__bases__)',
                        learning__Type__member__class_bases,
                        learning__Type__member__class_bases,
                    )

                show_one_member(
                        true,
                        'basic size (__basicsize__)',
                        learning__Type__member__class_basic_size,
                        learning__Type__member__class_basic_size,
                    )

                show_one_member(
                        true,
                        'call (__call__)',
                        learning__Type__operator__call,
                        learning__Type__operator__call,
                    )

                show_one_member(
                        true,
                        'map (__dict__)',
                        learning__Type__member__class_members,
                        learning__Type__member__class_members,
                    )

                show_one_member(
                        true,
                        'map offset (__dictoffset__)',
                        learning__Type__member__class_members_offset,
                        learning__Type__member__class_members_offset,
                    )

                show_one_member(
                        true,
                        'flags (__flags__)',
                        learning__Type__member__class_flags,
                        learning__Type__member__class_flags,
                    )

                show_one_member(
                        true,
                        'instance check (__instancecheck__)',
                        learning__Type__operator__instance_check,
                        learning__Type__operator__instance_check,
                    )

                show_one_member(
                        true,
                        'item size (__itemsize__)',
                        learning__Type__member__class_item_size,
                        learning__Type__member__class_item_size,
                    )

                show_one_member(
                        true,
                        'calculate method resolution order (mro)',
                        learning__Type__member__class_calculate_method_resolution_order,
                        learning__Type__member__class_calculate_method_resolution_order,
                    )

                show_one_member(
                        true,
                        'method resolution order (__mro__)',
                        learning__Type__member__method_resolution_order,
                        learning__Type__member__method_resolution_order,
                    )

                show_one_member(
                        true,
                        'name (__name__)',
                        learning__Type__member__class_name,
                        learning__Type__member__class_name,
                    )

                show_one_member(
                        true,
                        'sub class check (__subclasscheck__)',
                        learning__Type__operator__subclass_check,
                        learning__Type__operator__subclass_check,
                    )

                show_one_member(
                        true,
                        'subclasses (__subclasses__)',
                        learning__Type__operator__subclasses,
                        learning__Type__operator__subclasses,
                    )

                show_one_member(
                        true,
                        'weak reference offset (__weakrefoffset__)',
                        learning__Type__member__weak_reference_offset,
                        learning__Type__member__weak_reference_offset,
                    )
