#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Color_1')
def module():
    @share
    def Color__constructor(t, name):
        t.name = name


    @share
    def Color__representation(t):
        return arrange('<%s %s>', t.__class__.__name__, t.name)


    @share
    def show_color_1():
        blank()

        with indent('show_color_1:', prefix = 2):
            #
            #   Consider the following class `Color_1A`.
            #
            #   The following can be stated:
            #
            #       1.  `purple`  is an instance of `Color_1A`
            #
            #       2.  The type of `purple` is `Color_1A`
            #
            #       3A  The type of `Color_1A` is `Type`
            #       3B. The metaclass of `Color_1A` is `Type`   (same statement as 3A).
            #       3C. `Color_1A` is an instance of `Type`     (same statement as 3A & 3B).
            #
            #       4A. The type of `Type` is `Type`            (i.e: `Type` is it's own metaclass).
            #       4B. The metaclass of `Type` is `Type`       (same statement as 4A).
            #       4C. `Type` is an instance of `Type`         (same statement as 4A & 4B).
            #
            #   See the `line` statements below which show these four cases.
            #
            class Color_1A(Object):
                __slots__ = ((
                    'name',
                ))


                def __init__(t, name):
                    t.name = name


                def __repr__(t):
                    return arrange('<Color_1A %s>', t.name)


            purple = Color_1A('purple')

            line('1.  purple:                                %r', purple)
            line('2.  purple.__class__:                      %r', purple.__class__)
            line('3.  purple.__class__.__class__:            %r', purple.__class__.__class__)
            line('4.  purple.__class__.__class__.__class__:  %r', purple.__class__.__class__.__class__)


            #
            #   Consider the following class `Color_1B`.
            #
            #   It is identical to `Color_1A` (other than the small change in the class name).
            #
            #   We can create `Color_1B` using a call to `Type`:
            #
            #       In other words, since `Color_1A` and `Color_1B` are *both* instances of `Type`,
            #       we can create them in multiple ways:
            #
            #       A.  Using the `class` keyword (`Color_1A`);
            #
            #       B.  Or by calling `Type` to create a `Type` instance (`Color_1B`).
            #
            #   See the `line` statements below, which show that `Color_1A` and `Color_1B` are identical
            #   (other than the small change in the class name).
            #
            Color_1B = Type(
                    'Color_1B',
                    ((Object,)),
                    {
                        '__slots__': ((
                            'name',                         #   String
                        )),
                        '__init__' : Color__constructor,
                        '__repr__' : Color__representation,
                    },
                )

            violet = Color_1B('violet')

            line()
            line('1.  violet:                                %r', violet)
            line('2.  violet.__class__:                      %r', violet.__class__)
            line('3.  violet.__class__.__class__:            %r', violet.__class__.__class__)
            line('4.  violet.__class__.__class__.__class__:  %r', purple.__class__.__class__.__class__)


            #
            #   Consider the following class `Color_1C`.
            #
            #   It is identical to `Color_1B` (other than the small change in the class name).
            #
            #   `Color_1B` was create using a call to `Type`.  A call to `Type` really means:
            #
            #       `type(Type).__dict__["__call__"](Type, ...)`
            #
            #
            #   In other words:
            #
            #       i.  Take the `type` of `Type` (which happens to be `Type`, since `Type` is it's own metaclass);
            #
            #       ii. Then find the `__call__` method; and call it.
            #
            #   Thus we can create `Color_1C` by calling `Type__Operator__call` directly.
            #
            #       `Type__operator__call` is `Type.__dict__["__call__"]`
            #       (See "Capital/Class_Type.py")
            #
            #   The first parameter to `Type__operator__call` will be the metaclass (in this case `Type`)
            #
            Color_1C = Type__operator__call(
                    Type,
                    'Color_1C',
                    ((Object,)),
                    {
                        '__slots__': ((
                            'name',                         #   String
                        )),
                        '__init__' : Color__constructor,
                        '__repr__' : Color__representation,
                    },
                )

            indigo = Color_1C('indigo')

            line()
            line('1.  indigo:                                %r', indigo)
            line('2.  indigo.__class__:                      %r', indigo.__class__)
            line('3.  indigo.__class__.__class__:            %r', indigo.__class__.__class__)
            line('4.  indigo.__class__.__class__.__class__:  %r', purple.__class__.__class__.__class__)
