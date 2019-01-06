#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_3')
def module():
    @share
    def show_color_3():
        blank()

        with indent('show_color_3:', prefix = 2):
            #
            #   We need `Temporary_Metaclass` to avoid:
            #
            #       `TypeError: __class__ assign: only for heap types`                                       (Python 2)
            #       `TypeError: __class__ assignment only supported for heap types or ModuleType subclasses` (Python 3)
            #
            #   That is:
            #       To *REASSIGN* `__class__` below it *FIRST* has to be a heap type.
            #
            #       Thus we use `Temporary_Metaclass` (which is a heap type) instead of `Type` which is *NOT* a heap type.
            #
            class Temporary_Metaclass(Type):
                pass


            #
            #   NOTE:
            #       `Metaclass_Color_3` metaclass is `Temporary_Metaclass` [changed later]
            #
            #       `Metaclass_Color_3` is *DERIVED* from `Type`.
            #
            #       (i.e.: Don't confuse it's metaclass with its base parent).
            #
            Metaclass_Color_3 = create_python_type(
                    Temporary_Metaclass,                        #   `Temporary_Metaclass` is a "heap type".
                    'Metaclass_Color_3',
                    ((Type,)),
                    {
                        '__call__' : produce_color_call          ('Metaclass_Color_3'),
                        '__repr__' : produce_color_representation('Metaclass_Color_3'),
                    },
                )


            assert Metaclass_Color_3.__class__ is Temporary_Metaclass


            #
            #   Now we make `Metaclass_Color_3` its own metaclass ...
            #
            Metaclass_Color_3.__class__ = Metaclass_Color_3

            Color_3 = Metaclass_Color_3(
                    'Color_3',
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

            cyan = Color_3('cyan')          #   Uses MetaColor_3.__call__

            cyan()                          #   Uses Color_3.__call__
            Color_3.__call__(cyan)          #   Also uses Color_3.__call__

            line('cyan:                               %r', cyan)
            line('cyan.__class__:                     %r', cyan.__class__)
            line('cyan.__class__.__class__:           %r', cyan.__class__.__class__)
            line('cyan.__class__.__class__.__class__: %r', cyan.__class__.__class__.__class__)
