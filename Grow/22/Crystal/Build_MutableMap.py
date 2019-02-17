#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   python_new_vacant_mutable_map_instance
    #
    #       See `python_new_vacant_object_instance` (in "Crystal/Core.py") for an explanation of
    #       `python_new_vacant_*_instance`.
    #
    python_new_vacant_mutable_map_instance = Python_MutableMap.__new__


    #
    #   raise__CANNOT__delete_immutable_member_in_mutable_map__ERROR
    #   raise__CANNOT__set_immutable_member_in_mutable_map__ERROR
    #
    #       NOTE:
    #           There is a subtle difference between these functions:
    #
    #           1.  raise__CANNOT__{delete,set}_attribute__ERROR (defined in "Crystal/Cannot.py")
    #
    #                   Used for immutable classes
    #
    #           2.  raise__CANNOT__{delete,set}_immutable_member_in_mutable_map__ERROR (defined here)
    #
    #                   Used for mutable map with immutable members.
    #
    #                   For example `Build_Unique_Named_MutableMap` and classes derived from it are mutable, in that
    #                   the keys & values can be changed; however, it's members (`.__name__`) are immutable and cannot
    #                   be changed.
    #
    @property
    def raise__CANNOT__delete_immutable_member_in_mutable_map__ERROR(self):
        attribute_error = PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
                self,
                'operator delete attribute (__delattr__)',
                'have immutable members (although they have mutable key/value pairs)' ,
                'delete members (attributes)'
            )

        raise attribute_error


    @property
    def raise__CANNOT__set_immutable_member_in_mutable_map__ERROR(self):
        attribute_error = PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
                self,
                'operator set attribute (__setattr__)',
                'have immutable members (although they have mutable key/value pairs)' ,
                'set members (attributes)'
            )

        raise attribute_error



    #
    #   Build_Unique_Named_MutableMap
    #
    @share
    class Build_Unique_Named_MutableMap(Python_MutableMap):
        __slots__ = ((
            'name',                             #   String+
        ))


        __eq__   = operator_equal__by_identity
        __ne__   = operator_not_equal__by_identity
        __hash__ = python_hash__by_identity


        if python_debug_mode:
            __new__     = raise__CANNOT__create__ERROR
            __init__    = raise__CANNOT__construct__ERROR
            __delattr__ = raise__CANNOT__delete_immutable_member_in_mutable_map__ERROR
            __setattr__ = raise__CANNOT__set_immutable_member_in_mutable_map__ERROR


        def __repr__(self):
            try:
                name = self.name
            except Python_AttributeError:
                return '<Build_Unique_Named_MutableMap vacant>'

            #
            #   `self.name` exists
            #
            return arrange('<Build_Unique_Named_MutableMap {!r}>', name)


    stash__Build_Unique_Named_MutableMap__name = Build_Unique_Named_MutableMap.name.__set__


    #
    #   create_unique_named_mutable_map
    #
    #       NOTE:
    #           This is named without "Build_" in the name, as it is not creating a `Build_Unique_Named_MutableMap`
    #           (except temporarily) but some other class which can be described as a "unique named mutable map".
    #
    @share
    @creator
    def create_unique_named_mutable_map(Classification, name):
        assert fact_is_actual_string(name)

        #
        #   NOTE:
        #       We do not need to call `Python_MutableMap.__init__` (i.e.: `dict.__init__`) here,
        #       since for no arguments it doesn't do anything (everything is initialized in
        #       `python_new_vacant_mutable_map_instance` (i.e.: `dict.__new__`)).
        #
        #       What `Python_MutableMap.__init__` does do, is initialize any extra arguents or
        #       keywords to the constructor to create values in the initial mapping.
        #
        #       However, we have no extra arguments or keywords to pass to the constructor
        #       (we just want to start with a blank mapping, which is what
        #       `python_new_vacant_mutable_map_instance` creates for us).
        #
        self = python_new_vacant_mutable_map_instance(Build_Unique_Named_MutableMap)

        stash__Build_Unique_Named_MutableMap__name(self, name)          #   `self.name = name`

        #
        #   An atomic transformation of `self` to `Classification` ...
        #
        python_stash_class_attribute(self, Classification)              #   `self.__class__ = Classification`

        return self
