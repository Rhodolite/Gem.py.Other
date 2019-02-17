#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    assert python_debug_mode


    #
    #   PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR
    #   PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR
    #   PREPARE__instances_of_type__X__cannot__Y__ERROR
    #
    if python_debug_mode:
        @share
        def PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
                self, function_name, verb_adjective, description,
        ):
            type_name = self.__class__.__name__

            return PREPARE_AttributeError("`{}.{}`: instances of type `{}` {} and cannot {}",
                                          type_name, function_name, type_name, verb_adjective, description)


    if python_debug_mode:
        def PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR(Classification):
            #
            #   This is a special version (only used by `operator new` (`__new__`) to
            #   include the phrase "instance of type" even though the first argument is a class
            #   (instead of an instance).
            #
            class_name = Classification.__name__

            return PREPARE_AttributeError("`{}.{}`: instances of type `{}` cannot be allocated with `new`",
                                          class_name, 'operator new (__new__)', class_name)


    if python_debug_mode:
        def PREPARE__instances_of_type__X__cannot__Y__ERROR(t, function_name, description):
            type_name = python_type(t).__name__

            return PREPARE_AttributeError("`{}.{}`: instances of type `{}` cannot {}",
                                          type_name, function_name, type_name, description)


    #
    #   raise__CANNOT__create__ERROR
    #   raise__CANNOT__construct__ERROR
    #
    if python_debug_mode:
        @class_method
        def raise__CANNOT__create__ERROR(Classification, *arguments, **keywords):
            attribute_error = PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR(Classification)

            raise attribute_error


        @share
        def raise__CANNOT__construct__ERROR(self, *arguments, **keywords):
            attribute_error = PREPARE__instances_of_type__X__cannot__Y__ERROR(
                    self,
                    'operator constructor (__init__)',
                    'be constructed'
                )

            raise attribute_error


        #
        #   NOTE:
        #       Due to `@class_method` we cannot use `@share` since class methods do not have a `.__name__`
        #       for `share` to use.
        #
        #       Therefore we have to call share below & provide the name with keywords arguments.
        #
        share(
                raise__CANNOT__create__ERROR = raise__CANNOT__create__ERROR,
            )


    #
    #   raise__CANNOT__{delete,set}_attribute__ERROR
    #
    #       NOTE:
    #           See also `raise__CANNOT__{delete,set}_immutable_member_in_mutable_map__ERROR` in
    #           "Crystal/Build_MutableMap.py" for a slightly different version of these two
    #           functions.
    #
    #       NOTE:
    #           Defined with `@property` since:
    #
    #               1.  It can be done.
    #
    #               2.  Even trying to use `.__delattr__` (without calling it), will result in the
    #                   exception being thrown.
    #
    #       NOTE:
    #           Due to `@property` cannot use `@share` since properties do not have a `.__name__`
    #           for `share` to use.
    #
    #           Therefore we have to call share below & provide the name with keywords arguments.
    #
    if python_debug_mode:
        @property
        def raise__CANNOT__delete_immutable_attribute__ERROR(self):
            attribute_error = PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
                    self,
                    'operator delete attribute (__delattr__)',
                    'are immutable',
                    'delete attributes'
                )

            raise attribute_error


        @property
        def raise__CANNOT__set_immutable_attribute__ERROR(self):
            attribute_error = PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
                    self,
                    'operator set attribute (__setattr__)',
                    'are immutable',
                    'set attributes'
                )

            raise attribute_error


        share(
                raise__CANNOT__delete_immutable_attribute__ERROR = raise__CANNOT__delete_immutable_attribute__ERROR,
                raise__CANNOT__set_immutable_attribute__ERROR    = raise__CANNOT__set_immutable_attribute__ERROR,
            )
