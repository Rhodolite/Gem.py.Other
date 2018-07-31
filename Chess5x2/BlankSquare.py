#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.BlankSquare')
def module():
    require_module('Chess5x2.Square')


    class BlankSquare(Object):
        __slots__ = ((
            'square',                   #   Square
        ))


        adjust          = 0
        ally            = false
        enemy           = false
        heal_1          = 0
        is_blank_square = true
        is_card         = false
        prepare         = 0
        reset           = 0


        def __init__(t, square):
            t.square = square


        def __repr__(t):
            return arrange('<BlankSquare %s>', t.square)


        def mirror(t, square):
            return square.blank


        def portray(t):
            return arrange('<%s: blank>', t.square.name)


        def portray_abbreviation(t):
            return arrange('%s: blank', t.square.name)


        @static_method
        def portray_numbers():
            return ''


    def produce_blank_square(square):
        r            = BlankSquare(square)
        square.blank = r

        return r


    blank_square_a2 = produce_blank_square(square_a2)
    blank_square_b2 = produce_blank_square(square_b2)
    blank_square_c2 = produce_blank_square(square_c2)
    blank_square_d2 = produce_blank_square(square_d2)
    blank_square_e2 = produce_blank_square(square_e2)

    blank_square_a1 = produce_blank_square(square_a1)
    blank_square_b1 = produce_blank_square(square_b1)
    blank_square_c1 = produce_blank_square(square_c1)
    blank_square_d1 = produce_blank_square(square_d1)
    blank_square_e1 = produce_blank_square(square_e1)


    del BlankSquare.__init__


    share(
        'blank_square_a2',  blank_square_a2,
        'blank_square_b2',  blank_square_b2,
        'blank_square_c2',  blank_square_c2,
        'blank_square_d2',  blank_square_d2,
        'blank_square_e2',  blank_square_e2,

        'blank_square_a1',  blank_square_a1,
        'blank_square_b1',  blank_square_b1,
        'blank_square_c1',  blank_square_c1,
        'blank_square_d1',  blank_square_d1,
        'blank_square_e1',  blank_square_e1,
    )
