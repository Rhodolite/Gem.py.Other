#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    @share
    class Fixed_3(Python_Object):
        __slots__ = ((
            'slot_1',                        #   Any
            'slot_2',                        #   Any
            'slot_3',                        #   Any
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
            except Python_AttributeError:
                pass

            if valid == 0:
                return '<Fixed_3 vacant ...>'

            #
            #   `self.slot_1` exists
            #
            portray_1 = python_representation(slot_1)

            if valid == 1:
                return arrange('<Fixed_3 {} vacant ...>', portray_1)

            #
            #   `self.slot_2` exists
            #
            portray_2 = python_representation(slot_2)

            if valid == 2:
                return arrange('<Fixed_3 {} {} vacant>', portray_1, portray_2)

            #
            #   `self.slot_3` exists
            #
            portray_3 = python_representation(slot_3)

            assert valid == 3

            return arrange('<Fixed_3 {} {} {}>', portray_1, portray_2, portray_3)



    #
    #   Slots of Fixed_3
    #
    fixed_3_1 = Fixed_3.slot_1
    fixed_3_2 = Fixed_3.slot_2
    fixed_3_3 = Fixed_3.slot_3


    #
    #   Stash to slots of fixed_3
    #
    stash_3_1 = fixed_3_1.__set__
    stash_3_2 = fixed_3_2.__set__
    stash_3_3 = fixed_3_3.__set__


    #
    #   create_fixed_3
    #
    #       An *ATOMIC* create of an instance of `Classification`.
    #
    #       This is atomic, in the sense, that until the instance is *FULLY* created, its type is `Fixed_3`.
    #
    #       Once the instance is fully constructed, and no longer has any vacant (i.e.: uninitialized) slots,
    #       then it is atomically transformed to a `Classification`).
    #
    #   NOTE:
    #       `Fixed_3.__repr__` can *SAFETLY* portray an instance of `Fixed_3` during it's construction phase
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
    #       We do this via the methods `stash_3_*` and `python_stash_class_attribute`.
    #
    #       (Compare and constrast with `created_mutable_3` which just does the assignments normally since `Mutable_3`
    #       did ot disable `.__setattr__`).
    #
    @share
    @creator
    def create_fixed_3(Classification, a, b, c):
        self = python_new_vacant_object_instance(Fixed_3)

        stash_3_1(self, a)                                      #   `self.slot_1 = a`
        stash_3_2(self, b)                                      #   `self.slot_2 = b`
        stash_3_3(self, c)                                      #   `self.slot_3 = c`

        #
        #   An atomic transformation of `self` to `Classification` ...
        #
        python_stash_class_attribute(self, Classification)      #   `self.__class__ = Classification`

        return self


    #
    #   Share
    #
    share(
            fixed_3_1 = fixed_3_1,
            fixed_3_2 = fixed_3_2,
            fixed_3_3 = fixed_3_3,
        )
