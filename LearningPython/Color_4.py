#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_4')
def module():
    show        = 0
    show_hidden = 0


    @share
    def show_color_4():
        blank()

        with indent('show_color_4:', prefix = 2):
            Color_4 = Type(
                    'Color_4',
                    base_classes__Object,
                    process_object_members(
                        'Color_4',
                        {
                            '__slots__': ((
                                'name',                         #   String
                            )),
                            'portray' : Color__representation,
                        },
                    ),
                )


            del Color_4.__slots__

            new__Color_4              = Method(new_instance, Color_4)
            initialize__Color_4__name = Color_4.name.__set__


            def create__Color_4(name):
                r = new__Color_4()

                initialize__Color_4__name(r, name)

                return r


            yellow = create__Color_4('yellow')

            line('yellow: %s', yellow)

            #yellow.name = 'blue'

            if show:
                blank()

                introspect_function = (introspect_hidden   if show_hidden else   introspect)
                symbol_table        = Color_4.__dict__

                with indent(arrange('%s:', Color_4.__name__), prefix = 2):
                    for k in introspect_function(Color_4):
                        if k in symbol_table:
                            v = symbol_table[k]
                        else:
                            v = attribute(Color_4, k)

                        line('%s: %r', k, v)
