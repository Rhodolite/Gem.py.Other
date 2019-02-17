#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    @share
    class Mutable_12(Python_Object):
        __slots__ = ((
            'slot_1',                        #   Any
            'slot_2',                        #   Any
            'slot_3',                        #   Any
            'slot_4',                        #   Any
            'slot_5',                        #   Any
            'slot_6',                        #   Any
            'slot_7',                        #   Any
            'slot_8',                        #   Any
            'slot_9',                        #   Any
            'slot_10',                       #   Any
            'slot_11',                       #   Any
            'slot_12',                       #   Any
        ))


        if python_debug_mode:
            __new__  = raise__CANNOT__create__ERROR
            __init__ = raise__CANNOT__construct__ERROR


        def __repr__(self):
            valid = 0

            try:
                slot_1  = self.slot_1;  valid = 1
                slot_2  = self.slot_2;  valid = 2
                slot_3  = self.slot_3;  valid = 3
                slot_4  = self.slot_4;  valid = 4
                slot_5  = self.slot_5;  valid = 5
                slot_6  = self.slot_6;  valid = 6
                slot_7  = self.slot_7;  valid = 7
                slot_8  = self.slot_8;  valid = 8
                slot_9  = self.slot_9;  valid = 9
                slot_10 = self.slot_10; valid = 10
                slot_11 = self.slot_11; valid = 11
                slot_12 = self.slot_12; valid = 12
            except Python_AttributeError:
                pass

            if valid == 0:
                return '<Mutable_12 vacant ...>'


            #
            #   `self.slot_1` exists
            #
            portray_1 = python_representation(slot_1)

            if valid == 1:
                return arrange('<Mutable_12 {} vacant ...>', portray_1)


            #
            #   `self.slot_2` exists
            #
            portray_2 = python_representation(slot_2)

            if valid == 2:
                return arrange('<Mutable_12 {} {} vacant ...>', portray_1, portray_2)


            #
            #   `self.slot_3` exists
            #
            portray_3 = python_representation(slot_3)

            if valid == 3:
                return arrange('<Mutable_12 {} {} {} vacant ...>', portray_1, portray_2, portray_3)

            #
            #   `self.slot_4` exists
            #
            portray_4 = python_representation(slot_4)

            if valid == 4:
                return arrange('<Mutable_12 {} {} {} {} vacant ...>', portray_1, portray_2, portray_3, portray_4)

            #
            #   `self.slot_5` exists
            #
            portray_5 = python_representation(slot_5)

            if valid == 5:
                return arrange('<Mutable_12 {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5)

            #
            #   `self.slot_6` exists
            #
            portray_6 = python_representation(slot_6)

            if valid == 6:
                return arrange('<Mutable_12 {} {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6)

            #
            #   `self.slot_7` exists
            #
            portray_7 = python_representation(slot_7)

            if valid == 7:
                return arrange('<Mutable_12 {} {} {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7)

            #
            #   `self.slot_8` exists
            #
            portray_8 = python_representation(slot_8)

            if valid == 8:
                return arrange('<Mutable_12 {} {} {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7, portray_8)

            #
            #   `self.slot_9` exists
            #
            portray_9 = python_representation(slot_9)

            if valid == 9:
                return arrange('<Mutable_12 {} {} {} {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7, portray_8,
                               portray_9)

            #
            #   `self.slot_10` exists
            #
            portray_10 = python_representation(slot_10)

            if valid == 10:
                return arrange('<Mutable_12 {} {} {} {} {} {} {} {} {} vacant ...>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7, portray_8,
                               portray_9, portray_10)

            #
            #   `self.slot_11` exists
            #
            portray_11 = python_representation(slot_11)

            if valid == 11:
                return arrange('<Mutable_12 {} {} {} {} {} {} {} {} {} {} vacant>',
                               portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7, portray_8,
                               portray_9, portray_10, portray_11)

            #
            #   `self.slot_12` exists
            #
            portray_12 = python_representation(slot_12)

            assert valid == 12

            return arrange('<Mutable_12 {} {} {} {} {} {} {} {} {} {} {}>',
                           portray_1, portray_2, portray_3, portray_4, portray_5, portray_6, portray_7, portray_8,
                           portray_9, portray_10, portray_11, portray_12)



    #
    #   Slots of Mutable_12
    #
    mutable_12_1  = Mutable_12.slot_1
    mutable_12_2  = Mutable_12.slot_2
    mutable_12_3  = Mutable_12.slot_3
    mutable_12_4  = Mutable_12.slot_4
    mutable_12_5  = Mutable_12.slot_5
    mutable_12_6  = Mutable_12.slot_6
    mutable_12_7  = Mutable_12.slot_7
    mutable_12_8  = Mutable_12.slot_8
    mutable_12_9  = Mutable_12.slot_9
    mutable_12_10 = Mutable_12.slot_10
    mutable_12_11 = Mutable_12.slot_11
    mutable_12_12 = Mutable_12.slot_12


    #
    #   create_Mutable_12
    #
    #       See comments in "Crystal/Mutable_3.py"
    #
    #
    @share
    @creator
    def create_mutable_12(Classification, a, b, c, d, e, f, g, h, i, j, k, l):
        self = python_new_vacant_object_instance(Mutable_12)

        self.slot_1  = a
        self.slot_2  = b
        self.slot_3  = c
        self.slot_4  = d
        self.slot_5  = e
        self.slot_6  = f
        self.slot_7  = g
        self.slot_8  = h
        self.slot_9  = i
        self.slot_10 = j
        self.slot_11 = k
        self.slot_12 = l

        #
        #   An atomic transformation of `self` to `Classification` ...
        #
        self.__class__ = Classification

        return self


    #
    #   Share
    #
    share(
        #
        #   Out slots
        #
        mutable_12_1  = mutable_12_1,
        mutable_12_2  = mutable_12_2,
        mutable_12_3  = mutable_12_3,
        mutable_12_4  = mutable_12_4,
        mutable_12_5  = mutable_12_5,
        mutable_12_6  = mutable_12_6,
        mutable_12_7  = mutable_12_7,
        mutable_12_8  = mutable_12_8,
        mutable_12_9  = mutable_12_9,
        mutable_12_10 = mutable_12_10,
        mutable_12_11 = mutable_12_11,
        mutable_12_12 = mutable_12_12,
    )
