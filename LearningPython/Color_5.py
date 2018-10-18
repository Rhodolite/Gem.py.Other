#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_5')
def module():
    from    abc     import  ABCMeta         as  ABC_Meta
    from    abc     import  abstractmethod  as  abstract_method


    @share
    def show_color_5():
        blank()

        with indent('show_color_5:', prefix = 2):
            Metaclass_Color_5 = Type(
                    'Metaclass_Color_5',
                    ((ABC_Meta,)),
                    process_type_members(
                        'Metaclass_Color_5',
                        ABC_Meta,
                        {
                        },
                    ),
                )


            del Metaclass_Color_5.__slots__


            @abstract_method
            def xyz():
                pass


            Color_5 = ABC_Meta.__new__(
                    Metaclass_Color_5,
                    'Color_5',
                    base_classes__Object,
                    process_object_members(
                        'Color_5',
                        {
                            '__slots__': ((
                                'name',                         #   String
                            )),
                            'portray' : Color__representation,
                            'xyz'     : xyz,
                        },
                    ),
                )

            line('Color_5.__abstractmethods__: %s', Color_5.__abstractmethods__)
