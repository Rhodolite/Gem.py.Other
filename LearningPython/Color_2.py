#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_2')
def module():
    @share
    def produce_color_call(class_name):
        def call(metaclass, *arguments):
            total_arguments = length(arguments)

            if total_arguments is 0:
                line('  %s.__call__(%s)', class_name, metaclass)

                return Type__operator__call(metaclass)

            if total_arguments is 1:
                [name] = arguments

                line('  %s.__call__(%s, %r)', class_name, metaclass, name)

                return Type__operator__call(metaclass, name)

            [name, bases, members] = arguments

            line('%s.__call__(%s, %r, %r, keys<%r>)',
                 class_name,
                 metaclass,
                 name,
                 bases,
                 sorted_list(members.keys()))

            return Type__operator__call(metaclass, name, bases, members)


        return call


    @share
    def produce_color_representation(class_name):
        def representation(t):
            return arrange('<%s %s>', class_name, t.__name__)

        return representation


    #
    #   To call a class:
    #
    #           `X()`
    #
    #   means:
    #
    #           type(X).__call__()
    #
    #
    #   In other words:
    #
    #       The `.__call__` is found in the scope of the *METACLASS* of `x` *NOT* in `x`.
    #
    @share
    def show_color_2():
        blank()

        with indent('show_color_2:', prefix = 2):
            class Meta_Metaclass_Color_2(Type):
                __call__ = produce_color_call          ('Meta_Metaclass_Color_2')
                __repr__ = produce_color_representation('Meta_Metaclass_Color_2')


            #
            #   NOTE:
            #       Due to the difference in `metaclass` keyword in python 2 & python 3, we don't use the
            #       keyword, but instead just call `Type` directly.
            #
            #       In other words:
            #
            #           Python 2 (does *NOT* work in Python 3):
            #
            #               class Metaclass_Color_2(Type):
            #                   __metaclass__ = Meta_Metaclass_Color_2
            #                   __call__      = produce_color_call          ('Meta_Metaclass_Color_2')
            #                   __repr__      = produce_color_representation('Meta_Metaclass_Color_2')
            #
            #           Python 3 (does *NOT* work in Python 2):
            #
            #               class Metaclass_Color_2(Type, metaclass = Meta_Metaclass_Color_2):
            #                   __call__      = produce_color_call          ('Meta_Metaclass_Color_2')
            #                   __repr__      = produce_color_representation('Meta_Metaclass_Color_2')
            #
            #
            #           How we do it (works in both Python 2 & Python 3):
            #
            #               Metaclass_Color_2 = Meta_Metaclass_Color_2(
            #                       'Metaclass_Color_2',
            #                       ((Type,)),
            #                       {
            #                           '__call__' : produce_color_call          ('Metaclass_Color_2'),
            #                           '__repr__' : produce_color_representation('Metaclass_Color_2'),
            #                       },
            #                   )
            #

            #
            #   `Metaclass_Color_2`:
            #
            #       Uses `Meta_Metaclass_Color_2.__class__.__call__` to create the class.
            #
            #       In other words uses `Type__operator__call` to create the class
            #       [since `Type` is the metaclass of `Meta_Metaclass_Color_2`]
            #
            Metaclass_Color_2 = Meta_Metaclass_Color_2(
                    'Metaclass_Color_2',
                    ((Type,)),
                    {
                        '__call__' : produce_color_call          ('Metaclass_Color_2'),
                        '__repr__' : produce_color_representation('Metaclass_Color_2'),
                    },
                )


            #
            #   `Color_2`:
            #
            #       Uses `Metaclass_Color_2.__class__.__call__` to create the class.
            #
            #       In other words uses `Meta_Metaclass_Color_2.__call__` to create the class
            #       [since `Meta_Metaclass_Color_2` is the metaclass of `Metaclass_Color_2`]
            #
            #   NOTE:
            #
            #       See comment above in can't use `metaclass` keyword in Python 2 & Python 3.
            #
            #       The equivalent Python 3 code is
            #
            #           class Color_2(Object, metaclass = Metaclass_Color_2):
            #               __slots__ = ((
            #                   'name',                     #   String
            #               ))
            #
            #
            #               def __init__(t, name):
            #                   t.name = name
            #
            #
            #               def __call__(t):
            #                   line('Color_2.__call__(%s)', t)
            #
            #
            #               def __repr__(t):
            #                   return arrange('<Color_2 %s>', t.name)
            #
            @share
            def Color__call(t):
                line('%s.__call__(%s)', t.__class__.__name__, t)


            Color_2 = Metaclass_Color_2(                    #   Uses Meta_Metaclass_Color_2.__call__
                    'Color_2',
                    ((Object,)),
                    {
                        '__slots__': ((
                            'name',                         #   String
                        )),
                        '__init__' : Color__constructor,
                        '__call__' : Color__call,
                        '__repr__' : Color__representation,
                    },
                )

            blue = Color_2('blue')                          #   Uses MetaColor_2.__call__

            blue()                                          #   Uses Color_2.__call__
            Color_2.__call__(blue)                          #   Also uses Color_2.__call__

            line('blue:                                          %r', blue)
            line('blue.__class__:                                %r', blue.__class__)
            line('blue.__class__.__class__:                      %r', blue.__class__.__class__)
            line('blue.__class__.__class__.__class__:            %r', blue.__class__.__class__.__class__)
            line('blue.__class__.__class__.__class__.__class__:  %r', blue.__class__.__class__.__class__.__class__)
