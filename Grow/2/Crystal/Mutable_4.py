#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    @share
    class Mutable_4(Python_Object):
        __slots__ = ((
            'slot_1',                        #   Any
            'slot_2',                        #   Any
            'slot_3',                        #   Any
            'slot_4',                        #   Any
        ))


        if python_debug_mode:
            __new__  = raise__CANNOT__create__ERROR
            __init__ = raise__CANNOT__construct__ERROR


        def __repr__(self):
            valid = 0

            try:
                slot_1 = self.slot_1; valid = 1
                slot_2 = self.slot_2; valid = 2
                slot_3 = self.slot_3; valid = 3
                slot_4 = self.slot_4; valid = 4
            except Python_AttributeError:
                pass

            if valid == 0:
                return '<Mutable_4 vacant ...>'


            #
            #   `self.slot_1` exists
            #
            portray_1 = python_representation(slot_1)

            if valid == 1:
                return arrange('<Mutable_4 {} vacant ...>', portray_1)


            #
            #   `self.slot_2` exists
            #
            portray_2 = python_representation(slot_2)

            if valid == 2:
                return arrange('<Mutable_4 {} {} vacant ...>', portray_1, portray_2)


            #
            #   `self.slot_3` exists
            #
            portray_3 = python_representation(slot_3)

            if valid == 3:
                return arrange('<Mutable_4 {} {} {} vacant>', portray_1, portray_2, portray_3)

            #
            #   `self.slot_4` exists
            #
            portray_4 = python_representation(slot_4)

            assert valid == 4

            return arrange('<Mutable_4 {} {} {} {}>', portray_1, portray_2, portray_3, portray_4)


    #
    #   Slots of Mutable_4
    #
    mutable_4_1 = Mutable_4.slot_1
    mutable_4_2 = Mutable_4.slot_2
    mutable_4_3 = Mutable_4.slot_3
    mutable_4_4 = Mutable_4.slot_4


    #
    #   create_mutable_4
    #
    #       An *ATOMIC* create of an instance of `Classification`.
    #
    #       This is atomic, in the sense, that until the instance is *FULLY* created, its type is `Mutable_4`.
    #
    #       Once the instance is fully constructed, and no longer has any vacant (i.e.: uninitialized) slots,
    #       then it is atomically transformed to a `Classification`).
    #
    #   NOTE:
    #       `Mutable_4.__repr__` can *SAFETLY* portray an instance of `Mutable_4` during it's construction phase
    #       when it has vacant (i.e.: uninitialized) slots.
    #
    #       Frequently, `Classification.__repr__` expects all attributes to be fully set, and would die a horrible
    #       death (i.e.: throw `Python_AttributeError`) when it attempted to access the vacant (i.e.: uninitialized)
    #       slots.
    #
    @share
    @creator
    def create_mutable_4(Classification, a, b, c, d):
        self = python_new_vacant_object_instance(Mutable_4)

        self.slot_1 = a
        self.slot_2 = b
        self.slot_3 = c
        self.slot_4 = d

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
        mutable_4_1 = mutable_4_1,
        mutable_4_2 = mutable_4_2,
        mutable_4_3 = mutable_4_3,
        mutable_4_4 = mutable_4_4,
    )
