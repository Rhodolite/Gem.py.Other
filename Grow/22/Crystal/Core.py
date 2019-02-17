#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    import  types   as  Python_Types_Module


    #
    #   Python Types (Part I)
    #
    #       NOTE:
    #           In python, an attribute, is implemented by a descriptor.
    #
    #           A descriptor has `.__get__`, `.__set__`, and `.__delete__` methods.
    #
    #           Hence `Python_Types_Module.GetSetDescriptorType` (i.e.: `types.GetSetDescriptorType`) is more
    #           accuratly called an "Attribute Descriptor".
    #
    Python_AttributeDescriptor = Python_Types_Module.GetSetDescriptorType
    Python_Integer             = Python_BuiltIn.int
    Python_Method              = Python_Types_Module.MethodType


    #
    #   Python Types (Part II)
    #
    #   Python_BuiltIn_Function_or_Method   - A pythod built in function.
    #
    #                                         Can be bound to an instance, in which case it is a python built in
    #                                         method.
    #
    #                                         The `.__self__` member is `Python_None` if it is a python function,
    #                                         or the value of the bound instance if it is a python method.
    #
    #       NOTE:
    #           `Python_Types_Module` spells it `Builtin` with a lowercase `i`.
    #
    #           We spell it `BuiltIn` with a capital `I`.
    #
    Python_BuiltIn_Function = Python_Types_Module.BuiltinFunctionType
    Python_BuiltIn_Method   = Python_Types_Module.BuiltinMethodType

    assert Python_BuiltIn_Function is Python_BuiltIn_Method

    Python_BuiltIn_Function_or_Method = Python_BuiltIn_Function

    assert Python_BuiltIn_Function_or_Method.__name__ == 'builtin_function_or_method'


    #
    #   Python Types (Part III)
    #
    #       Python_MethodWrapper    - An annoying internal python type used to wrap [internal python] methods.
    #
    #                                 When used in `.format` returns the exception:
    #
    #                                       TypeError: Type method-wrapper doesn't define __format__
    #
    #                                 Very annoying, so we use `Python_MethodWrapper` to detect this
    #                                 type, and avoid passing it to `.format`.
    #
    Python_MethodWrapper = python_type( (()).__getitem__ )

    assert Python_MethodWrapper.__name__ == 'method-wrapper'


    #
    #   Python Types (Part IV)
    #
    #       Python_SlotWrapper      - A wrapper around an [internal] python slot.
    #
    #                                 We take the type of `Python_Object.__delattr__` (i.e.: `object.__delattr__`)
    #                                 since that is an [internal] python slot.
    #
    Python_SlotWrapper = python_type(Python_Object.__delattr__)

    assert Python_SlotWrapper.__name__ == 'wrapper_descriptor'


    #
    #   python_new_vacant_object_instance(Classification)
    #
    #       Create a new vacant instance of `Classification`.
    #
    #       "Vacant" means all the slots are uninitialized & throw `Python_AttributeError` if accessed.
    #
    #       Normal python construction happens as follows:
    #
    #           class Point(Python_Object):
    #               __slots__ = ((
    #                   'x',
    #                   'y',
    #               ))
    #
    #               def __init__(self, x, y):
    #                   self.x = x
    #                   self.y = y
    #
    #           #
    #           #   The call to `Point(3, 4)` means:
    #           #
    #           #       1.  python_type(Point).__call__(Point, 3, 4)
    #           #
    #           #   Since the metaclass of `Point` is `Python_Type` then this means:
    #           #
    #           #       2.  Python_Type.__call__(Point, 3, 4)
    #           #
    #           #   `Python_Type.__call__` does the following:
    #           #
    #           #       def emulate__Python_Type__call(Classification, *arguments, **keywords):
    #           #           result = Classification.__new__(Classification, *arguments, **keywords)
    #           #
    #           #           if python_type(result) is Classifiation:
    #           #               Classification.__init__(result, *arguments, **keywords)
    #           #
    #           #           return result
    #           #
    #           #   Since we have not overridden `.__new__` in `Point` then the call
    #           #   `Classification.__new__` will resolve to `Python_Object.__new__`
    #           #
    #           instance = Point(3, 4)
    #
    #       Thus, the first normal step of python instance construction is to call:
    #
    #           `Python_Object.__new__` (i.e.: `object.__new__`)
    #
    #       Followed by a call to the `.__init__` method.
    #
    #   We often bypass all this & call `python_new_vacant_object_instance` directly,
    #   and the construct the object ourselves, without ever calling a constructor.
    #
    #   There are many reasons for this, but the main one, is to avoid extra states during the
    #   instances lifecycle (see Crystal Principles #4 & #5).
    #
    python_new_vacant_object_instance = Python_Object.__new__


    #
    #   Python Slot Wrappers
    #
    #python_delete_with_attribute_descriptor = Python_AttributeDescriptor.__delete__
    #python_query_with_attribute_descriptor  = Python_AttributeDescriptor.__get__
    #python_stash_with_attribute_descriptor  = Python_AttributeDescriptor.__set__


    #
    #   arrange
    #
    @share
    def arrange(message, *arguments):
        return message.format(*arguments)


    #
    #   create_empty_list
    #
    @share
    @creator
    def create_empty_list():
        return []


    #
    #   bind_instance
    #
    #       Creates a new python method.
    #
    @share
    @creator
    def bind_method(method, instance):
        return Python_Method(method, instance)


    #
    #   create_Python_Tuple
    #
    @share
    @creator
    def create_Python_Tuple(iterable):
        return Python_Tuple(iterable)


    share(
            #
            #   Python Types
            #
            Python_Boolean                    = Python_BuiltIn.bool,
            Python_BuiltIn_Function_or_Method = Python_BuiltIn_Function_or_Method,
            Python_Integer                    = Python_Integer,
            Python_MethodWrapper              = Python_MethodWrapper,
            Python_SlotWrapper                = Python_SlotWrapper,
            Python_Tuple                      = Python_BuiltIn.tuple,


            #
            #   Python Functions
            #
            #       NOTE:
            #           `class_method` and `property` are actually types, but they are used as if they are functions.
            #
            class_method                      = Python_BuiltIn.classmethod,
            iterate                           = Python_BuiltIn.iter,
            property                          = Python_BuiltIn.property,
            python_globals                    = Python_BuiltIn.globals,
            python_is_subclass                = Python_BuiltIn.issubclass,
            python_representation             = Python_BuiltIn.repr,
            python_sorted_list                = Python_BuiltIn.sorted,
            python_new_vacant_object_instance = python_new_vacant_object_instance,

            #python_delete_with_attribute_descriptor = python_delete_with_attribute_descriptor,
            #python_query_with_attribute_descriptor  = python_query_with_attribute_descriptor,
            #python_stash_with_attribute_descriptor  = python_stash_with_attribute_descriptor,
        )
