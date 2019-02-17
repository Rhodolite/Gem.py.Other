#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    @share
    class Fixed_6(Python_Object):
        __slots__ = ((
            'slot_1',                        #   Any
            'slot_2',                        #   Any
            'slot_3',                        #   Any
            'slot_4',                        #   Any
            'slot_5',                        #   Any
            'slot_6',                        #   Any
        ))


        if python_debug_mode:
            __new__     = raise__CANNOT__create__ERROR
            __init__    = raise__CANNOT__construct__ERROR
            __delattr__ = raise__CANNOT__delete_immutable_attribute__ERROR
            __setattr__ = raise__CANNOT__set_immutable_attribute__ERROR


        def __repr__(self):
            valid = 0

            try:
                slot_1 = self.slot_1; valid = 1
                slot_2 = self.slot_2; valid = 2
                slot_3 = self.slot_3; valid = 3
                slot_4 = self.slot_4; valid = 4
                slot_5 = self.slot_5; valid = 5
                slot_6 = self.slot_6; valid = 6
            except Python_AttributeError:
                pass

            if valid == 0:
                return '<Fixed_6 vacant ...>'

            #
            #   `self.slot_1` exists
            #
            portray_1 = python_representation(slot_1)

            if valid == 1:
                return arrange('<Fixed_6 {} vacant ...>', portray_1)

            #
            #   `self.slot_2` exists
            #
            portray_2 = python_representation(slot_2)

            if valid == 2:
                return arrange('<Fixed_6 {} {} vacant ...>', portray_1, portray_2)

            #
            #   `self.slot_3` exists
            #
            portray_3 = python_representation(slot_3)

            if valid == 3:
                return arrange('<Fixed_6 {} {} {} vacant ...>', portray_1, portray_2, portray_3)

            #
            #   `self.slot_4` exists
            #
            portray_4 = python_representation(slot_4)

            if valid == 4:
                return arrange('<Fixed_6 {} {} {} {} vacant ...>', portray_1, portray_2, portray_3, portray_4)

            #
            #   `self.slot_5` exists
            #
            portray_5 = python_representation(slot_5)

            if valid == 5:
                return arrange('<Fixed_6 {} {} {} {} {} vacant>',
                               portray_1, portray_2, portray_3, portray_4, portray_5)

            #
            #   `self.slot_6` exists
            #
            portray_6 = python_representation(slot_6)

            assert valid == 6

            return arrange('<Fixed_6 {} {} {} {} {} {}>',
                           portray_1, portray_2, portray_3, portray_4, portray_5, portray_6)



    #
    #   Slots of Fixed_6
    #
    fixed_6_1 = Fixed_6.slot_1
    fixed_6_2 = Fixed_6.slot_2
    fixed_6_3 = Fixed_6.slot_3
    fixed_6_4 = Fixed_6.slot_4
    fixed_6_5 = Fixed_6.slot_5
    fixed_6_6 = Fixed_6.slot_6


    #
    #   Stash to slots of fixed_6
    #
    stash_6_1 = fixed_6_1.__set__
    stash_6_2 = fixed_6_2.__set__
    stash_6_3 = fixed_6_3.__set__
    stash_6_4 = fixed_6_4.__set__
    stash_6_5 = fixed_6_5.__set__
    stash_6_6 = fixed_6_6.__set__


    #
    #   create_fixed_6
    #
    #       An *ATOMIC* create of an instance of `Classification`.
    #
    #       This is atomic, in the sense, that until the instance is *FULLY* created, its type is `Fixed_6`.
    #
    #       Once the instance is fully constructed, and no longer has any vacant (i.e.: uninitialized) slots,
    #       then it is atomically transformed to a `Classification`).
    #
    #   NOTE:
    #       `Fixed_6.__repr__` can *SAFETLY* portray an instance of `Fixed_6` during it's construction phase
    #       when it has vacant (i.e.: uninitialized) slots.
    #
    #       Frequently, `Classification.__repr__` expects all attributes to be fully set, and would die a horrible
    #       death (i.e.: throw `Python_AttributeError`) when it attempted to access the vacant (i.e.: uninitialized)
    #       slots.
    #
    #   NOTE:
    #       Because we disabled `.__setattr__` above (by setting it to `raise__CANNOT__set_immutable_attribute__ERROR`)
    #       we have to bypass the normal `self.name = value` way of initializing values.
    #
    #       We do this via the methods `stash_6_*` and `python_stash_class_attribute`.
    #
    #       (Compare and constrast with `created_mutable_3` which just does the assignments normally since `Mutable_3`
    #       did ot disable `.__setattr__`).
    #
    @share
    @creator
    def create_fixed_6(Classification, a, b, c, d, e, f):
        self = python_new_vacant_object_instance(Fixed_6)

        stash_6_1(self, a)                                      #   `self.slot_1 = a`
        stash_6_2(self, b)                                      #   `self.slot_2 = b`
        stash_6_3(self, c)                                      #   `self.slot_3 = c`
        stash_6_4(self, d)                                      #   `self.slot_4 = d`
        stash_6_5(self, e)                                      #   `self.slot_5 = e`
        stash_6_6(self, f)                                      #   `self.slot_6 = f`

        #
        #   An atomic transformation of `self` to `Classification` ...
        #
        python_stash_class_attribute(self, Classification)      #   `self.__class__ = Classification`

        return self


    #
    #   Share
    #
    share(
            fixed_6_1 = fixed_6_1,
            fixed_6_2 = fixed_6_2,
            fixed_6_3 = fixed_6_3,
            fixed_6_4 = fixed_6_4,
            fixed_6_5 = fixed_6_5,
            fixed_6_6 = fixed_6_6,
        )
