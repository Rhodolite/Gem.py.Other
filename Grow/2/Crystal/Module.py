#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Python types
    #
    Python_List       = Python_BuiltIn.list
    Python_MutableSet = Python_BuiltIn.set
    Python_Tuple      = Python_BuiltIn.tuple


    #
    #   sorted_tuple
    #
    def sorted_tuple(iterable):
        return create_Python_Tuple(python_sorted_list(iterable))


    #
    #   MutableSet_of_Slots
    #
    if python_debug_mode:
        def RAISE__class_X_declares_duplicate_slot_Y__ERROR(class_name, name):
            attribute_error = PREPARE_AttributeError(
                                  "class `{}` declares duplicate slot `{}`",
                                  class_name,
                                  name,
                              )

            raise attribute_error


        class MutableSet_of_Slots(Python_MutableSet):
            __slots__ = ((
                'class_name',               #   ActualString
                'total',                    #   Integer
            ))


            def __init__(self, class_name, name_value_map):
                if name_value_map:
                    super(MutableSet_of_Slots, self).__init__()
                else:
                    super(MutableSet_of_Slots, self).__init__(name_value_map)

                self.class_name = class_name
                self.total      = 0


            @static_method
            def __repr__():
                return '<MutableSet_of_Slots>'


            def insert(self, name):
                self.add(name)

                total = self.total + 1

                if total != length(self):
                    RAISE__class_X_declares_duplicate_slot_Y__ERROR(self.class_name, name)

                self.total = total


        def create_MutableSet_of_Slots(class_name, name_value_map):
            return MutableSet_of_Slots(class_name, name_value_map)


    #
    #  create_immutable_module
    #
    python_stash_object_attribute = Python_Object.__setattr__
    string_starts_with            = Python_String.startswith
    string_replace                = Python_String.replace


    if python_debug_mode:
        def verify_unique_slots(class_name, classes_and_functions, name_value_map):
            slots = create_MutableSet_of_Slots(class_name, name_value_map)

            for v in classes_and_functions:
                slots.insert(v.__name__)


    def create_immutable_module(
            class_name, module_name, portrait,

            classes_and_functions = none,
            name_value_map        = none,
    ):
        if classes_and_functions:
            verify_unique_slots(class_name, classes_and_functions, name_value_map)

        slots = create_empty_list()

        append_slot = slots.append

        if classes_and_functions:
            for v in classes_and_functions:
                name = v.__name__

                interned_name = intern_python_string(name)

                if name is not interned_name:
                    v.__name__ = interned_name

                append_slot(interned_name)

        if name_value_map:
            for k in name_value_map:
                interned_k = intern_python_string(k)

                append_slot(interned_k)

        slots.sort()

        slots = create_Python_Tuple(slots)


        @property
        def query_module_name(self):
            return module_name


        @static_method
        def portray_module():
            return portrait


        #
        #   Summary:
        #       This is very confusing, but there are *TWO* `.__name__` members of `Fixed_Class`:
        #
        #           1.  It's class name provided by `Python_Type.__dict__["__name__"]`;
        #           2.  The module name provided by `Fixed_Class.__dict__["__name__"]`
        #               (i.e.: `query_module_name`)
        #
        #       The interaction of descriptors & metaclasses in python is, initially, very confusing.
        #
        #   Details:
        #       In the code below we set `.__name__` (for instances of `Fixed_Class`) to return the
        #       module name (using `query_module_name`).
        #
        #       However `Fixed_class.__name__` continues to be `class_name`, since this is effected
        #       by the metaclass (in this case `Python_Type`) which has a descriptor in
        #       `Python_Type.__dict__["__name__"]`.
        #
        members = {
                      intern_python_string('__slots__')   : slots,
                      intern_python_string('__name__')    : query_module_name,
                      intern_python_string('__repr__')    : portray_module,
                  }

        if python_debug_mode:
            members[intern_python_string('__delattr__')] = raise__CANNOT__delete_immutable_attribute__ERROR
            members[intern_python_string('__setattr__')] = raise__CANNOT__set_immutable_attribute__ERROR

        Fixed_Class = Python_Type(class_name, ((Python_Object,)), members)


        #
        #   `python_stash_object_attribute` would *normally* be what `Fixed_Class.__setattr__` method would be when
        #   inherited from `Object`.
        #
        #   However, we disabled setting attribute (using `raise__CANNOT__set_immutable_attribute__ERROR`), so here,
        #   during construction of the object, we call `python_stash_object_attribute` directly.
        #
        instance = python_new_vacant_object_instance(Fixed_Class)

        if classes_and_functions:
            for v in classes_and_functions:
                name = v.__name__

                python_stash_object_attribute(instance, name, v)

        if name_value_map:
            for k in name_value_map:
                v = name_value_map[k]

                if is_python_string(v):
                    v = intern_python_string(v)

                python_stash_object_attribute(instance, k, v)

        return instance


    #
    #   replace_crystal_module
    #
    #   NOTE:
    #       See note under `save_crystal_submodule` for subtle differences between this function and
    #       `save_crystal_submodule`.
    #
    #   NOTE:
    #       The protrait is `"<CrystalModule Crystal>"` instead of the briefer `"<CrystalModule>"` to show
    #       a bettr contrast wtih submodules like `"<CrystalSubmodule Crystal.Z_Mode>"`
    #
    #       Since it's a singleton, omitting "Crystal", from the portrait seems to make sense; but on usage,
    #       it's more readable with the name "Crystal" in the portrait.
    #
    @share
    def replace_crystal_module(*classes_and_functions, **name_value_map):
        class_name  = 'CrystalModule'
        module_name = 'Crystal'
        portrait    = '<CrystalModule Crystal>'

        crystal_module = create_immutable_module(
                    class_name            = class_name,
                    module_name           = module_name,
                    portrait              = portrait,
                    classes_and_functions = classes_and_functions,
                    name_value_map        = name_value_map,
                )

        assert python_lookup_loaded_module(module_name) is not none     #   Verify previous module exists

        python_stash_loaded_module(module_name, crystal_module)         #   Replace previous module

        return crystal_module


    #
    #   save_crystal_submodule
    #
    #   NOTE:
    #       There is a subtle difference between:
    #
    #           1.  replace_crystal_module      - Replaces the module in `python_loaded_modules` (i.e.: `sys.modules`)
    #           2.  save_crystal_submodule      - Saves the submodule in crystal globals.
    #
    #       This is due to the fact that the Crystal Module belongs in `python_loaded_modules` (i.e.: `sys.modules`),
    #       while the Crystal Submodules do not (as they are not treated as real python modules).
    #
    #       [For purposes of this note, it is not relevant, as the next note discusses, that in python 2.*
    #       a temporary module with this name is in `python_loaded_modules` (i.e.: `sys.modules`).
    #
    #       It isn't the real module this note is disucssing, but just a temporary module required by python.]
    #
    #   NOTE #2:
    #       In python 2.* code, a temporary module with this name is in `python_loaded_modules`
    #       (i.e.: `sys.modules`).
    #
    #       In python 3.* code, a temporary module with this name is *NOT* in `python_loaded_modules`
    #       (i.e.: `sys.modules`)>
    #
    #       These differences are due to different behavior of `import_crystal_submodule` in
    #       python 2.* code .vs. python 3.* code (in python 2.* code, `import_crystal_submodule`
    #       has to, temporarily, save the original module in `python_loaded_modules` (i.e.: `sys.modules`)
    #       while in the python 3.* code it doesn't).
    #
    #       See comments in "Crystal.py" under `import_crystal_submodule` for more details.
    #
    @share
    def save_crystal_submodule(module_name, *classes_and_functions, **name_value_map):
        assert string_starts_with(module_name, 'Crystal.')

        if is_python_2:
            assert python_lookup_loaded_module(module_name)             #   See comment above for Python 2.*
        else:
            assert python_lookup_loaded_module(module_name) is none     #   See comment above for Python 3.*

        submodule_name = intern_python_string(module_name[8:])          #   Remove the "Crystal." prefix

        class_name = arrange('Crystal_Submodule_{}', submodule_name)

        portrait = arrange('<CrystalSubmodule {}>', module_name)

        crystal_submodule = create_immutable_module(
                    class_name            = class_name,
                    module_name           = module_name,
                    portrait              = portrait,
                    classes_and_functions = classes_and_functions,
                    name_value_map        = name_value_map,
                )

        #
        #   Store in Crystal Gloabls as `submodule_name`
        #
        #   NOTE:
        #       Not the same as `crystal_submodule.__name__` which has the "Crystal." prefix, hence we
        #       have to use a keyword arguments to pass `submodule_name` in.
        #
        insert_crystal_global(submodule_name, crystal_submodule)
