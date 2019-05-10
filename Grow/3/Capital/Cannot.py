#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  export
from    Capital.Exception               import  PREPARE_AttributeError


#
#   PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR - currently disabled, will be used in future.
#   PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR
#   PREPARE__instances_of_type__X__cannot__Y__ERROR
#
if 0:
    #
    #   Currently disabled, will be used in future.
    #
    #   Only shown here to compare to `PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR` below.
    #
    def PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR(
            self, function_name, verb_adjective, description,
    ):
        type_name = self.__class__.__name__

        return PREPARE_AttributeError("`{}.{}`: instances of type `{}` {} and cannot {}",
                                      type_name, function_name, type_name, verb_adjective, description)


if __debug__:
    def PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR(Classification):
        #
        #   This is a special version of `PREPARE__instances_of_type__X__VERB_ADJECTIVE__and_cannot__Y__ERROR` (only
        #   used by `operator new` (`__new__`) to include the phrase "instance of type" even though the first argument
        #   is a class (instead of an instance).
        #
        class_name = Classification.__name__

        return PREPARE_AttributeError("`{}.{}`: instances of type `{}` cannot be allocated with `new`",
                                      class_name, 'operator new (__new__)', class_name)


if __debug__:
    def PREPARE__instances_of_type__X__cannot__Y__ERROR(t, function_name, description):
        type_name = type(t).__name__

        return PREPARE_AttributeError("`{}.{}`: instances of type `{}` cannot {}",
                                      type_name, function_name, type_name, description)


#
#   raise__CANNOT__create__ERROR
#   raise__CANNOT__construct__ERROR
#
if __debug__:
    @export
    @classmethod
    def raise__CANNOT__create__ERROR(Classification, *arguments, **keywords):
        attribute_error = PREPARE__instances_of_type__X__cannot_be_allocated_with_new__ERROR(Classification)

        raise attribute_error


    @export
    def raise__CANNOT__construct__ERROR(self, *arguments, **keywords):
        attribute_error = PREPARE__instances_of_type__X__cannot__Y__ERROR(
                self,
                'operator constructor (__init__)',
                'be constructed'
            )

        raise attribute_error
