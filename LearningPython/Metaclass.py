#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Metaclass')
def module():
    abstractable = 0
    show         = 7
    show_hidden  = 0


    if abstractable:
        from    abc     import  ABCMeta         as  ABC_Meta


    @share
    def show_metaclass():
        blank()

        if abstractable:
            Parent = ABC_Meta
        else:
            Parent = Type

        with indent('show_metaclass:', prefix = 2):
            def portray_class(t):
                m = t.class_type

                if t is m:
                    #
                    #   This class is it's own metaclass
                    #
                    return arrange('<%s ...>', t.class_name)

                return arrange('<%s %s>', m.class_name, t.class_name)


            class Temporary_MetaClass(Type):
                pass


            Metaclass_Color_6 = Temporary_MetaClass(
                    'Metaclass_Color_6',
                    ((Parent,)),
                    process_type_members(
                        'Metaclass_Color_6',
                        Parent,
                        {
                            'portray' : portray_class,
                        },
                        abstractable  = abstractable,
                        constructable = true,
                        newable       = true,
                    ),
                )

            Metaclass_Color_6.__class__ = Metaclass_Color_6

            del Metaclass_Color_6.__slots__


            Color_6 = Metaclass_Color_6(
                    'Color_6',
                    base_classes__Object,
                    process_object_members(
                        'Color_6',
                        {
                            '__slots__': ((
                                'name',                         #   String
                            )),
                            'portray' : Color__representation,
                        },
                    ),
                )


            new__Color_6              = Method(Object__operator__new, Color_6)
            initialize__Color_6__name = Color_6.name.__set__


            def create__Color_6(name):
                r = new__Color_6()

                initialize__Color_6__name(r, name)

                return r


            green = create__Color_6('green')

            line('green: green')
            blank()

            with indent(arrange('%s:', Color_6.__name__), prefix = 2):
                assert Color_6.class_bases                   == ((Color_6.class_parent,))
                assert Color_6.__class__                     is Metaclass_Color_6
                assert Color_6.class_item_size               is 0
                assert Color_6.class_immediate_subclasses()  == []
                assert Color_6.class_members_offset          is 0
                assert Color_6.class_method_resolution_order == ((Color_6, Object))
                assert Color_6.class_name                    == 'Color_6'
                assert Color_6.class_type                    is Metaclass_Color_6
                assert Color_6.class_weak_reference_offset   is 0
                assert Color_6.__name__                      == 'Color_6'

                line('Color_6:                                %r', Color_6)

               #line('Color_6.class_calculate_method_resolution_order: %s',
               #     Color_6.class_calculate_method_resolution_order)

                line('Color_6.class_bases:                    (%r)', Color_6.class_bases)
                line('Color_6.class_basic_size:               %d', Color_6.class_basic_size)
                line('Color_6.class_flags:                    %#x', Color_6.class_flags)
                line('Color_6.class_immediate_subclasses:     %r', Color_6.class_immediate_subclasses())
                line('Color_6.class_item_size:                %d', Color_6.class_item_size)

                line('Color_6.class_members:                  keys<%s>',
                     ', '.join(sorted_list(Color_6.class_members.keys())))

                line('Color_6.class_members_offset:           %r', Color_6.class_members_offset)
                line('Color_6.class_method_resolution_order:  (%r)', Color_6.class_method_resolution_order)
                line('Color_6.class_name:                     %r', Color_6.class_name)
                line('Color_6.class_parent:                   %r', Color_6.class_parent)
                line('Color_6.class_type:                     %r', Color_6.class_type)
                line('Color_6.class_weak_reference_offset:    %r', Color_6.class_weak_reference_offset)

            if show:
                blank()
                show_class_members(Metaclass_Color_6, show_hidden = show_hidden)
