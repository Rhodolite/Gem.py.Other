#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    fix_all    = true
    trace_wipe = false


    import  Crystal


    #
    #   Later on we wipe `crystal_global`, `Python_MethodWrapper`, `python_representation`, `python_type`,
    #   and `trace`
    #
    #       ... hence make local copies of these first!
    #
    crystal_global = python_globals()

    Python_MethodWrapper  = crystal_global.Python_MethodWrapper
    python_representation = crystal_global.python_representation
    python_type           = crystal_global.python_type
    trace                 = crystal_global.trace


    #
    #   Python Types
    #
    #       Python_Slot         - The type of a python slot; extracted from the type of `Crystal.__class__.vision`
    #                             (in other words from the `vision` slot of the class `Crystal.__class__`).
    #
    #
    Python_FrozenSet     = Python_BuiltIn.frozenset
    Python_None_Type     = python_type(none)
    Python_Slot          = python_type(Crystal.__class__.vision)
    Python_Property      = Python_BuiltIn.property
    Python_Static_Method = Python_BuiltIn.staticmethod
    Python_Tuple         = Python_BuiltIn.tuple


    assert Python_Slot.__name__ == 'member_descriptor'


    #
    #   Python Types (part II)
    #
    #       Python_Cell     - The type of a python cell (i.e.: a variable used in an inner funtion from an outer funtion).
    #
    #                         We get the "closure" of `use_cell_variable` which is a tuple of length 1.
    #
    #                         The first element of the tuple is a cell that encloses `cell_variable`
    #
    #                         We thus take the type of the first element of the tuple to get `Python_Cell`.
    #                         We thus take the type of the first element of the tuple to get `Python_Cell`
    #
    cell_variable = 0

    def use_cell_variable():
        return cell_variable

    Python_Cell = python_type(python_query_function_closure(use_cell_variable)[0])


    assert Python_Cell.__name__ == 'cell'


    #
    #   Python functions
    #
    python_address_of = Python_BuiltIn.id


    #
    #   Python Methods
    #
    python_delete_type_attribute = Python_Type.__delattr__
    python_stash_type_attribute  = Python_Type.__setattr__


    #
    #   create_Python_List__empty
    #   create_Python_List__from__iterable
    #
    @creator
    def create_Python_List__empty():
        return []


    @creator
    def create_Python_List__from__iterable(iterable):
        return Python_List(iterable)


    #
    #   create_Python_FrozenSet__from_multiple_arguments(argument ...)
    #
    #       Converts the multiple arguments into a tuple & then constructs a `Python_FrozenSet` from the tuple.
    #
    #       This is achieved by *NOT* using a `*` before passing `arguments` as the first parameter to
    #       `Python_FrozenSet`.
    #
    @creator
    def create_Python_FrozenSet__from_multiple_arguments(*arguments):       #   `*` here to convert arguments to tuple.
        return Python_FrozenSet(arguments)                                  #   No `*` here -- See comment above.


    #
    #   wipe
    #
    if trace_wipe:
        wipe = trace
    else:
        def wipe(message, *arguments):
            pass


    #
    #   lookup_crystal_global   - Look for a crystal global symbol; OR return `absent_sentinel`
    #   absent_sentinel         - A value guarenteed not to be in `crystal_global`
    #
    #lookup_crystal_global - defined in "Crystal.py"

    absent_sentinel = lookup_crystal_global


    #
    #   scan_many
    #
    scan_many = []

    append_scan = scan_many.append


    #
    #   squash_none
    #
    def squash_none(v):
        pass


    #
    #   squash_python_property
    #
    def squash_python_property(v):
        documentation   = v.__doc__
        delete_function = v.fdel
        query_function  = v.fget
        stash_function  = v.fset

        replace = false

        if is_python_string(documentation):
            interned_documentation = intern_python_string(documentation)

            if (fix_all) or (documentation is not interned_documentation):
                documentation = interned_documentation
                replace       = true

        if delete_function is not none:
            push_scan_python_function(delete_function)

        if query_function is not none:
            push_scan_python_function(query_function)

        if stash_function is not none:
            push_scan_python_function(stash_function)

        if replace:
            return create_Python_Property(query_function, stash_function, delete_function, documentation)

        #return none                    #   `return none` is implied by python.


    #
    #   squash_python_slot_in_instance
    #
    def squash_python_slot_in_instance(v, instance):
        w = v.__get__(instance)

        squash_function = lookup_squash_function(python_type(w))

        if squash_function is none:
            push_scan_instance(w)
            return

        new_w = squash_function(w)

        if new_w is not none:
            wipe("Replacing {!r}.{} = {!r}", instance, v.__name__, new_w)

            v.__set__(instance, new_w)


    #
    #   squash_python_static_method
    #
    def squash_python_static_method(v):
        f = v.__get__(0)

        push_scan_python_function(f)


    #
    #   squash_python_string
    #
    def squash_python_string(s):
        interend_s = intern_python_string(s)

        if (fix_all) or (interend_v is not s):
            return interend_s

        #return none                    #   `return none` is implied by python.


    #
    #   squash_python_tuple
    #
    def squash_python_tuple(v):
        many  = none
        index = 0

        for w in v:
            new_w = squash_table[python_type(w)](w)

            if new_w is not none:
                break

            index += 1
        else:
            return none

        #
        #   NOTE:
        #       The `break` in the previous `for` loop comes here when it finds an entry that needs to be
        #       replaced.
        #
        #       1.  We copy the previous scanned entries (unmodified)
        #       2.  We copy the current  scanned entry   (modified)
        #       3.  We copy the new entries (after scanning them).
        #
        #       We return a new `Python_Tuple` from #1, #2, & #3.
        #
        many   = create_Python_List__empty()
        append = many.append

        v_iterator = iterate(v)

        if index:
            #
            #   1.  Copy previous entries already scanned
            #
            index_2 = 0

            for w in v_iterator:
                append(w)

                index_2 += 1

                if index == index_2:
                    break

        #
        #   2.  Copy the current entry's new value.
        #
        append(new_w)


        #
        #   3.  Copy the new entries (not yet scanned).
        #
        for w in v_iterator:
            new_w = squash_table[python_type(w)](w)

            if new_w is not none:
                append(new_w)
            else:
                append(w)

        r = create_Python_Tuple(many)

        wipe('before: {!r}', v)
        wipe(' after: {!r}', r)

        return r


    #
    #   lookup_pushed
    #   stash_pushed
    #
    pushed_map = {}                     #   Python_Mutable_Map {
                                        #         CrystalModule   : CrystalModule
                                        #       | Python_Function : Python_Function
                                        #       | Python_Integer  : Python_Code
                                        #       | Python_String   : True
                                        #   }


    lookup_pushed = pushed_map.get
    stash_pushed  = pushed_map.__setitem__


    def initialize_pushed():
        for v in ((
                #
                #   Ignore the symbols:
                #       __builtins__
                #       __class__
                #       __name__
                #       __package__
                #
                '__builtins__',
                '__class__',
                '__name__',
                '__package__',

                #
                #   Ignore types
                #
                Python_AttributeError,
                Python_String,
                Python_Type,
        )):
            stash_pushed(v, true)


    initialize_pushed()


    #
    #   scan_constants
    #
    def scan_constants(name, constants):
        assert fact_is_python_tuple(constants)

        for v in constants:
            v_type = python_type(v)

            push_function = lookup_push_function(v_type, push_scan_instance)

            if push_function:
                wipe('function {} uses constant {!r}', name, v)

                push_function(v)


    #
    #   scan_symbol_names
    #
    def scan_symbol_names(code_name, symbol_names):
        assert fact_is_python_tuple(symbol_names)

        for name in symbol_names:
            if lookup_pushed(name):
                continue

            stash_pushed(name, true)

            #
            #   NOTE:
            #       We use `absent_sentinel` as a "sentinel" to detect if the value was found or not.
            #
            v = lookup_crystal_global(name, absent_sentinel)

            if v is absent_sentinel:
                wipe('code for {} uses symbol {!r} (does NOT appear to be a global)', code_name, name)
                continue

            wipe('code for {} uses symbol {!r} with value {!r}', code_name, name, v)

            v_type = python_type(v)

            push_function = lookup_push_function(v_type, push_scan_instance)

            if push_function:
                push_function(v)


    #
    #   scan_closure
    #
    def scan_closure(name, closure):
        assert fact_is_python_tuple(closure)

        for cell in closure:
            contents = cell.cell_contents

            contents_type = python_type(contents)

            push_function = lookup_push_function(contents_type, push_scan_instance)

            if push_function:
                wipe('function {} uses closure on {!r}', name, contents)

                push_function(contents)


    #
    #   scan_python_code
    #
    def scan_python_code(code):
        code_constants    = python_query_code_constants   (code)
        code_symbol_names = python_query_code_symbol_names(code)

        if (code_constants) or (code_symbol_names):
            name = python_query_code_name(code)

        if code_constants:
            scan_constants(name, code_constants)

        if code_symbol_names:
            scan_symbol_names(name, code_symbol_names)


    #
    #   scan_python_function
    #
    def scan_python_function(f):
        symbols = python_query_function_globals(f)

        if symbols is not crystal_global:
            wipe('f: {}; .symbols: {}', f, symbols)

            assert 0

        name = python_query_function_name(f)

        interned_name = intern_python_string(name)

        if name is not interned_name:
            f.__name__ = interned_name


        closure  = python_query_function_closure(f)
        code     = python_query_function_code(f)
        defaults = python_query_function_defaults(f)

        if closure is not none:
            scan_closure(name, closure)

        #
        #<code_name>
        #
        code_name = python_query_code_name(code)

        if name != code_name:
            wipe('function {} uses code {}', name, code_name)
        #</code_name>

        push_scan_python_code(code)

        if defaults is not none:
            scan_defaults(name, defaults)


    #
    #   scan_instance
    #   push_scan_instance
    #
    is_protected_name = create_Python_FrozenSet__from_multiple_arguments(
                            '__doc__',
                            '__module__',
                            '__name__'
                        ).__contains__


    def scan_instance(instance):
        item_type = python_type(instance)

        item_type_name = item_type.__name__

        wipe('Scanning: {} of type {}', instance, item_type)

        item_symbols = item_type.__dict__

        for k in python_sorted_list(item_symbols):
            v = item_symbols[k]

            if is_protected_name(k):
                #
                #   Python does not allow us to delete the `.__doc__`, `.__module__`, or `.__name__` attribute of a class.
                #
                fix = false
            else:
                interned_k = intern_python_string(k)

                if (fix_all) or (interned_k is not k):
                    fix = true
                    k   = interned_k

            wipe('Scanning {}[{}]: {!r}', item_type, k, v)

            v_type = python_type(v)

            if v_type is Python_Slot:
                new_v = squash_python_slot_in_instance(v, instance)
            else:
                new_v = squash_table[v_type](v)

            if fix:
                if new_v is not none:
                    v = new_v

                wipe('Fixing {}[{}] = {!r}', item_type, k, v)

                python_delete_type_attribute(item_type, k)
                python_stash_type_attribute(item_type, k, v)
            elif new_v is not none:
                wipe('Replacing {}[{}] = {!r}', item_type, k, new_v)

                python_stash_type_attribute(item_type, k, new_v)


    #
    #   push_scan_python_built_in_function_or_method
    #
    def push_scan_python_built_in_function_or_method(v):
        self = v.__self__

        if self is none:
            #
            #   Python_BuiltInFunction
            #
            return

        #
        #   Python_BuiltInMethod
        #
        self_type = python_type(self)

        push_function = lookup_push_function(self_type, push_scan_instance)

        if push_function:
            wipe('python built in method is bound to {!r}', self)

            push_function(self)


    #
    #   push_scan_python_code
    #
    #   NOTE:
    #       `Python_Code` objects have their own `.__eq__` and `.__hash__` methods which we *DO* not want to use.
    #
    #       Hence we store the adress of the `code` object as a key, so as to avoid these methods.
    #
    def push_scan_python_code(code):
        code_address = python_address_of(code)

        if lookup_pushed(code_address):
            return

        stash_pushed(code_address, code)
        append_scan(code)


    def push_scan_python_function(f):
        if lookup_pushed(f):
            return

        stash_pushed(f, f)
        append_scan(f)


    is_known_class_name = create_Python_FrozenSet__from_multiple_arguments(
                              'CrystalModule',
                              'MutableMap_of_InternedPythonString',
                         ).__contains__


    def push_scan_instance(instance):
        classification = python_type(instance)

        wipe("instance: {}; classification: {}, .__hash__: {}", instance, classification, classification.__hash__)

        if lookup_pushed(instance):
            return

        class_name = classification.__name__

        if not (is_known_class_name(class_name) or (class_name.startswith('Crystal_Submodule_'))):
            name_error = PREPARE_NameError('push_scan_instance: {!r} has an unknown class name: {!r}',
                                           instance, class_name)

            raise name_error

        stash_pushed(instance, instance)
        append_scan(instance)


    #
    #   push table
    #
    lookup_push_function = {
                               Python_BuiltIn_Function_or_Method : push_scan_python_built_in_function_or_method,
                               Python_Code                       : push_scan_python_code,
                               Python_Function                   : push_scan_python_function,
                               Python_Boolean                    : none,
                               Python_None_Type                  : none,
                               Python_String                     : none,
                           }.get


    #
    #   scan_table
    #
    lookup_scan_function = {
                               Python_Code     : scan_python_code,
                               Python_Function : scan_python_function,
                           }.get

    #
    #   squash_table
    #
    squash_table = {
            Python_Function      : push_scan_python_function,       #   `push_scan_*` on purpose
            Python_Integer       : squash_none,
            Python_None_Type     : squash_none,
            Python_Property      : squash_python_property,
            Python_SlotWrapper   : squash_none,
            Python_Static_Method : squash_python_static_method,
            Python_String        : squash_python_string,
            Python_Tuple         : squash_python_tuple,
        }


    lookup_squash_function = squash_table.get


    #
    #   scan_all
    #
    def scan_all():
        while length(scan_many):
            v = scan_many.pop()

            v_type = python_type(v)

            lookup_scan_function(v_type, scan_instance)(v)



    #
    #   wipe_globals
    #
    #   NOTE:
    #       Above, We made a local copy of `crystal_global` & `trace` since we will wipe them out while running ...
    #
    def wipe_globals():
        sorted_keys = python_sorted_list(crystal_global)

        for k in sorted_keys:
            if lookup_pushed(k):
                continue

            v = crystal_global[k]

            if python_type(v) is Python_MethodWrapper:
                #
                #   See comment in "Crystal/Core.py" as to `Python_MethodWrapper` not defining `.__format__`.
                #
                representation_v = python_representation(v)

                wipe('Wiping crystal global {}: {}', k, representation_v)
            else:
                wipe('Wiping crystal global {}: {!r}', k, v)

            del crystal_global[k]


    #
    #   Keep `trace` if "Crystal/Show_Globals.py" is going to be loaded ...
    #
    if show_crystal_globals:
        stash_pushed('trace', true)


    #
    #   And ... wipe ...
    #
    push_scan_instance(Crystal)
    scan_all()
    wipe_globals()
