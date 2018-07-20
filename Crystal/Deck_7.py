#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Crystal.Deck_7')
def gem():
    @export
    class Deck_7(Object):
        __slots__ = ((
            'a',                        #   Card+
            'b',                        #   Card+
            'c',                        #   Card+
            'd',                        #   Card+
            'e',                        #   Card+
            'f',                        #   Card+
            'g',                        #   Card+
        ))


        def __init__(t, a, b, c, d, e, f, g):
            t.a = a
            t.b = b
            t.c = c
            t.d = d
            t.e = e
            t.f = f
            t.g = g


    Deck_7.k1 = Deck_7.a
    Deck_7.k2 = Deck_7.b
    Deck_7.k3 = Deck_7.c
    Deck_7.k4 = Deck_7.d
    Deck_7.k5 = Deck_7.e
    Deck_7.k6 = Deck_7.f
   #Deck_7.k7 = Deck_7.g
