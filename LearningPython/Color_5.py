#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_5')
def module():
    from    abc     import  ABCMeta         as  ABC_Meta
    from    abc     import  abstractmethod  as  abstract_method


    @abstract_method
    def xyz():
        pass


    #
    #   show_color_5a:
    #
    #       Original code, showing:
    #
    #       1.  Creating the metaclass `Metaclass_Color_5a` using `Type`
    #       2.  Creating the class     `Color_5a`           using `Metaclass_Color_5a`
    #
    def show_color_5a():
        blank()

        with indent('show_color_5a:', prefix = 2):
            Metaclass_Color_5a = Type(
                    'Metaclass_Color_5a',
                    ((ABC_Meta,)),
                    process_type_members(
                        'Metaclass_Color_5a',
                        ABC_Meta,
                        {},

                        constructable = true,
                        abstractable  = true,
                        newable       = true,
                    ),
                )


            del Metaclass_Color_5a.__slots__


            Color_5a = Metaclass_Color_5a(
                    'Color_5a',
                    base_classes__Object,
                    process_object_members(
                        'Color_5a',
                        {
                            '__slots__': ((
                                'name',                         #   String
                            )),
                            'portray' : Color__representation,
                            'xyz'     : xyz,
                        },
                    ),
                )

            line('Color_5a.__abstractmethods__: %s', Color_5a.__abstractmethods__)


    #
    #   show_color_5b:
    #
    #       Updated code, showing:
    #
    #       1.  Creating the metaclass `Metaclass_Color_5b` using `create_metaclass`
    #       2.  Creating the class     `Color_5b`           using `Metaclass_Color_5b.create_class`
    #
    def show_color_5b():
        blank()

        with indent('show_color_5b:', prefix = 2):
            Metaclass_Color_5b = create_metaclass(
                    'Metaclass_Color_5b',

                    Parent       = ABC_Meta,
                    abstractable = true,
                )

            Color_5b = Metaclass_Color_5b.create_class(
                    'Color_5b',
                    {
                        '__slots__': ((
                            'name',                         #   String
                        )),
                        'portray' : Color__representation,
                        'xyz'     : xyz,
                    },
                )

            line('Color_5b.__abstractmethods__: %s', Color_5b.__abstractmethods__)


    #
    #   `show_color_5{a,b}` do the same thing:
    #
    #       `show_color_5a`:    Using construtors
    #       `show_color_5b`:    The new way, using `.create_metaclass` and `.create_class`
    #
    @share
    def show_color_5():
        show_color_5a()
        show_color_5b()
