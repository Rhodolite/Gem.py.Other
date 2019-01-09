#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    @share
    class Mutable_3(Python_Object):
        __slots__ = ((
            'slot_1',                        #   Any
            'slot_2',                        #   Any
            'slot_3',                        #   Any
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
            except Python_AttributeError:
                pass

            if valid == 0:
                return '<Mutable_3 vacant ...>'

            #
            #   `self.slot_1` exists
            #
            portray_1 = python_representation(slot_1)

            if valid == 1:
                return arrange('<Mutable_3 {} vacant ...>', portray_1)

            #
            #   `self.slot_2` exists
            #
            portray_2 = python_representation(slot_2)

            if valid == 2:
                return arrange('<Mutable_3 {} {} vacant>', portray_1, portray_2)

            #
            #   `self.slot_3` exists
            #
            portray_3 = python_representation(slot_3)

            assert valid == 3

            return arrange('<Mutable_3 {} {} {}>', portray_1, portray_2, portray_3)


    #
    #   Slots of Mutable_3
    #
    mutable_3_1 = Mutable_3.slot_1
    mutable_3_2 = Mutable_3.slot_2
    mutable_3_3 = Mutable_3.slot_3


    #
    #   create_mutable_3
    #
    #       An *ATOMIC* create of an instance of `Classification`.
    #
    #       This is atomic, in the sense, that until the instance is *FULLY* created, its type is `Mutable_3`.
    #
    #       Once the instance is fully constructed, and no longer has any vacant (i.e.: uninitialized) slots,
    #       then it is atomically transformed to a `Classification`).
    #
    #   NOTE:
    #       `Mutable_3.__repr__` can *SAFETLY* portray an instance of `Fixed_6` during it's construction phase
    #       when it has vacant (i.e.: uninitialized) slots.
    #
    #       Frequently, `Classification.__repr__` expects all attributes to be fully set, and would die a horrible
    #       death (i.e.: throw `Python_AttributeError`) when it attempted to access the vacant (i.e.: uninitialized)
    #       slots.
    #
    @share
    @creator
    def create_mutable_3(Classification, a, b, c):
        self = python_new_vacant_object_instance(Fixed_6)

        self.slot_1 = a
        self.slot_2 = b
        self.slot_3 = c

        #
        #   An atomic transformation of `self` to `Classification` ...
        #
        self.__class__ = Classification
        python_TRANSFORM(self, Classification)      #   `self.__class__ = Classification`

        return self


    #
    #   Share
    #
    share(
        #
        #   Out slots
        #
        mutable_3_1 = mutable_3_1,
        mutable_3_2 = mutable_3_2,
        mutable_3_3 = mutable_3_3,
    )
