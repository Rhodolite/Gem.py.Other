#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Crystal.Square')
def gem():
    class Square(Object):
        __slots__ = ((
            'name',                 #   String+
            'column',               #   Integer
            'row',                  #   Integer
            'blank',                #   Vacant | BlankSquare

            'load_center',          #   Vacant | MethodWrapper
            'load_north_ww',        #   Vacant | MethodWrapper
            'load_north_west',      #   Vacant | MethodWrapper
            'load_north',           #   Vacant | MethodWrapper
            'load_north_east',      #   Vacant | MethodWrapper
            'load_north_ee',        #   Vacant | MethodWrapper
            'load_west',            #   Vacant | MethodWrapper
            'load_east',            #   Vacant | MethodWrapper

            'store_center',         #   Vacant | MethodWrapper
            'store_north_ww',       #   Vacant | MethodWrapper
            'store_north_west',     #   Vacant | MethodWrapper
            'store_north',          #   Vacant | MethodWrapper
            'store_north_east',     #   Vacant | MethodWrapper
            'store_north_ee',       #   Vacant | MethodWrapper
            'store_west',           #   Vacant | MethodWrapper
            'store_east',           #   Vacant | MethodWrapper
        ))


        def __init__(t, name, column, row):
            t.name   = name
            t.column = column
            t.row    = row
           #t.blank  = blank                #   Done in produce_blank_square


        def __repr__(t):
            return arrange('<Square %s>', t.name)


    square_a2 = Square('a2', 2, 1)
    square_b2 = Square('b2', 2, 2)
    square_c2 = Square('c2', 2, 3)
    square_d2 = Square('d2', 2, 4)
    square_e2 = Square('e2', 2, 5)

    square_a1 = Square('a1', 1, 1)
    square_b1 = Square('b1', 1, 2)
    square_c1 = Square('c1', 1, 3)
    square_d1 = Square('d1', 1, 4)
    square_e1 = Square('e1', 1, 5)


    del Square.__init__


    share(
        'square_a2',         square_a2,
        'square_b2',         square_b2,
        'square_c2',         square_c2,
        'square_d2',         square_d2,
        'square_e2',         square_e2,

        'square_a1',         square_a1,
        'square_b1',         square_b1,
        'square_c1',         square_c1,
        'square_d1',         square_d1,
        'square_e1',         square_e1,
    )
