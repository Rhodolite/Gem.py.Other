#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('Chess5x2.VoidSquare')
def module():
    class VoidSquare(Object):
        __slots__       = (())
        ally            = false
        enemy           = false
        is_blank_square = false
        is_card         = false
        is_void_square  = true


        @static_method
        def __repr__():
            return arrange('<VoidSquare>')


    void_square = VoidSquare()



    share(
        'void_square',  void_square,
    )
