#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    Python_Exceptions_Module = (__import__('exceptions')   if is_python_2 else  Python_BuiltIn)


    #
    #   Python Types
    #
    Python_NameError = Python_Exceptions_Module.NameError
    Python_Object    = Python_BuiltIn          .object
    Python_Type      = Python_BuiltIn          .type


    #
    #   Python Functions
    #
    length             = Python_BuiltIn.len
    python_is_instance = Python_BuiltIn.isinstance
    python_type        = Python_BuiltIn.type


    #
    #   Python Slot Wrappers
    #
    #       NOTE:
    #           The default hashing mechanism (from `Python_Object` (i.e.: `object`)) is to hash by identity.
    #
    #           Certain classes, like `Python_MutuableMap` (i.e.: `dict`) override this to make themselves
    #           unhashable.
    #
    #           To restore class inherited from `Python_MutuableMap` to be hashable, we do the following:
    #
    #               Set their `.__hash__` member to `python_hash__by_identity`      (i.e.: `object.__hash__`).
    #               Set their `.__eq__`   member to `operator_equal__by_identity`
    #
    #           Also for consistency (not needed to be hashable, but to be consistent with the `.__eq__` member):
    #
    #               Set their `.__ne__`   member to `operator_not_equal__by_identity`
    #
    python_hash__by_identity = Python_Object.__hash__


    #
    #   is_python_string
    #
    def is_python_string(s):
        return python_type(s) is Python_String


    #
    #   fact_is__python_class__or__python_function(v)
    #
    #       Assert the fact that `v` is a python class or a python function.
    #
    if python_debug_mode:
        def fact_is__python_class__or__python_function(v):
            assert python_is_instance(python_type(v), ((Python_Type, Python_Function)) )

            return true


    #
    #   fact_is_python_string(s)
    #
    #       Assert the fact that `s` is a python string
    #
    if python_debug_mode:
        def fact_is_python_string(s):
            assert python_type(s) is Python_String

            return true


    #
    #   operator_equal__by_identity
    #
    #       An implementation of `.__eq__` that compares by identity.
    #
    #       This is what the `.__eq__` defaults to in python if not defined.
    #
    #       However, once defined (for example in `Python_MututableMap` (i.e.: `dict`)), the only way to get back this
    #       behavor in an inherited class is to define it ourselves -- there is no `Python_Object.__eq__` method we
    #       can "borrow" (at least not in Python 2.*, there is in Python 3.*, but there are problems with "borrowing"
    #       that method, so we don't).
    #
    def operator_equal__by_identity(self, other):
        return self is other


    #
    #   operator_not_equal__by_identity
    #
    #       An implementation of `.__ne__` that compares by identity.
    #
    #       This is what the `.__ne__` defaults to in python if not defined.
    #
    #       (See comments in `operator_equal__by_identity`).
    #
    def operator_not_equal__by_identity(self, other):
        return self is not other


    #
    #   intern_python_string(s)     - Intern python string `s`
    #
    #       In debug mode we keep track of these strings in `map_of_interned_python_string` so that we can
    #       implement the following two functions:
    #
    #           `debug_test__is_interned_python_string`
    #           `fact_is_interned_actual_string`.
    #
    #       In release mode we don't bother to track these, but simply call the python built in function `intern`.
    #
    if python_debug_mode:
        class MutableMap_of_InternedPythonString(Python_MutableMap):
            __slots__ = (())


            __eq__   = operator_equal__by_identity
            __ne__   = operator_not_equal__by_identity
            __hash__ = python_hash__by_identity


            @static_method
            def __repr__():
                return '<MutableMap_of_InternedPythonString>'


        def create_MutableMap_of_InternedPythonString():
            return MutableMap_of_InternedPythonString()


        map_of_interned_python_string  = create_MutableMap_of_InternedPythonString()
        lookup_interned_python_string  = map_of_interned_python_string.get
        provide_interned_python_string = map_of_interned_python_string.setdefault


        def intern_python_string(s):
            interned_s = lookup_interned_python_string(s)

            if interned_s:
                return interned_s

            interned_s = python_intern_python_string(s)

            return provide_interned_python_string(interned_s, interned_s)


        def debug_test__is_interned_python_string(s):
            assert fact_is_python_string(s)

            return lookup_interned_python_string(s) is not none

            #r = lookup_interned_python_string(s) is not none
            #trace('debug_test__is_interned_python_string({!r}) => {}', s, r)
            #return r
    else:
        intern_python_string = python_intern_python_string


    #
    #   fact_is_interned_actual_string(s)
    #
    #       Assert that `s` is an actual string (a non empty string) that has been interned.
    #
    if python_debug_mode:
        def fact_is_interned_actual_string(s):
            assert s is lookup_interned_python_string(s)
            assert length(s) > 0

            return true


    #
    #   Code
    #
    #       Python_Code     - The type of a `code` object that python uses.
    #
    #                         This is done by taking the `code` object from the `is_python_string` function, and then taking
    #                         it's class.
    #
    #       NOTE:
    #           "code_symbols" is symbols the code uses (globaal variables, names after `.`, and [for class member
    #           wrapper functions] local variables).
    #
    #           For example in a class member wrapper creation function, it is mixture of global variabls & the name of
    #           class members (the class member wrapper creation function is creating a map of the class members)
    #
    #           Example (Python 2.* code):
    #
    #               Python_Object = object
    #
    #               def f():
    #                   class XYZ(Python_Object):
    #                       abc = 22
    #
    #
    #               f_code__constants = f.func_code.co_consts
    #
    #               print('f_code__constants: {}'.format(f_code__constants))
    #
    #               #
    #               #   Code object to create the class body `XYZ` is third constants in `f`.
    #               #
    #               wrapper_XYZ_code = f.func_code.co_consts[2]
    #
    #               print('wrapper_XYZ_code.co_names: {}'.format(wrapper_XYZ_code.co_names))
    #
    #               import dis
    #
    #               dis.dis(wrapper_XYZ_code)
    #
    #           In the class member wrapper creation function `XYZ`, it will have `"abc"` in as one of the
    #           "code_symbols".
    #
    #           Specifically the above will print:
    #
    #               f_code__constants: (None, 'XYZ', <code object XYZ at 0x7fc311c9f8b0, file "/tmp/x.py", line 4>)
    #
    #               wrapper_XYZ_code.co_names: ('__name__', '__module__', 'abc')
    #
    #                     4           0 LOAD_NAME                0 (__name__)
    #                                 3 STORE_NAME               1 (__module__)
    #                     5           6 LOAD_CONST               0 (22)
    #                                 9 STORE_NAME               2 (abc)
    #                                12 LOAD_LOCALS
    #                                13 RETURN_VALUE
    #
    #           Which shows the class member wrapper creation function `XYZ` uses 3 symbols:
    #
    #               __name__        -  Reads the global module name
    #               __module__      -  Stores the global module name as the local variable `__module__`
    #               __abc__         -  Stores the value 22 as the local variable `abc`
    #
    #           Finally the wrapper will return a map of the locals it created (i.e.: `__module__` & `abc`).
    #
    Python_Code = python_query_function_code(is_python_string).__class__


    python_query_code_cell_variables    = Python_Code.co_cellvars   .__get__
    python_query_code_constants         = Python_Code.co_consts     .__get__
    python_query_code_filename          = Python_Code.co_filename   .__get__
    python_query_code_first_line_number = Python_Code.co_firstlineno.__get__
    python_query_code_flags             = Python_Code.co_flags      .__get__
    python_query_code_free_variables    = Python_Code.co_freevars   .__get__
    python_query_code_line_number_table = Python_Code.co_lnotab     .__get__
    python_query_code_name              = Python_Code.co_name       .__get__
    python_query_code_stack_size        = Python_Code.co_stacksize  .__get__
    python_query_code_symbol_names      = Python_Code.co_names      .__get__
    python_query_code_total_arguments   = Python_Code.co_argcount   .__get__
    python_query_code_total_locals      = Python_Code.co_nlocals    .__get__
    python_query_code_variable_names    = Python_Code.co_varnames   .__get__
    python_query_code_virtual_code      = Python_Code.co_code       .__get__

    if is_python_3:
        python_query_code_total_keyword_arguments = Python_Code.co_kwonlyargcount.__get__


    #
    #   rename_code
    #
    #   NOTE:
    #       This is a "create" function for `Python_Code` (i.e.: the replacement for a constructor).
    #
    if python_debug_mode:
        if is_python_2:
            def rename_code(code, interned_name):
                return Python_Code(
                           python_query_code_total_arguments  (code),
                           python_query_code_total_locals     (code),
                           python_query_code_stack_size       (code),
                           python_query_code_flags            (code),
                           python_query_code_virtual_code     (code),
                           python_query_code_constants        (code),
                           python_query_code_symbol_names     (code),
                           python_query_code_variable_names   (code),
                           python_query_code_filename         (code),
                           interned_name,
                           python_query_code_first_line_number(code),
                           python_query_code_line_number_table(code),
                           python_query_code_free_variables   (code),
                           python_query_code_cell_variables   (code),
                      )
        else:
            def rename_code(code, interned_name):
                return Python_Code(
                           python_query_code_total_arguments        (code),
                           python_query_code_total_keyword_arguments(code),     #   Only use in Python 3.*
                           python_query_code_total_locals           (code),
                           python_query_code_stack_size             (code),
                           python_query_code_flags                  (code),
                           python_query_code_virtual_code           (code),
                           python_query_code_constants              (code),
                           python_query_code_symbol_names           (code),
                           python_query_code_variable_names         (code),
                           python_query_code_filename               (code),
                           interned_name,
                           python_query_code_first_line_number      (code),
                           python_query_code_line_number_table      (code),
                           python_query_code_free_variables         (code),
                           python_query_code_cell_variables         (code),
                      )


    #
    #   rename
    #
    #   NOTE:
    #       This is a "create" function for `Python_Function` (i.e.: the replacement for a constructor).
    #
    #   NOTE:
    #       The debug version of `rename_function` creates a closure around `interned_name`, hence it
    #       needs to be defined inside `rename`.
    #
    #       The release version of `rename_function` does not need a closure; hence it is defined outside
    #       of `rename`.
    #
    if python_debug_mode:
        def rename(name, *arguments):
            if arguments:
                name = name.format(arguments)

            interned_name = intern_python_string(name)


            def rename_function(f):
                code = python_query_function_code(f)

                return Python_Function(
                           rename_code(code, interned_name),
                           python_query_function_globals (f),
                           interned_name,                           #   Access `interned_name` in enclosing function
                           python_query_function_defaults(f),
                           python_query_function_closure (f),
                       )


            return rename_function
    else:
        def rename_function(f):
            return f


        def rename(name, *arguments):
            return rename_function


    #
    #   produce_PREPARE_Exception
    #
    #   NOTE:
    #       See note in "Crystal/Exception.py" on `PREPARE_*Error` being "create" functions.
    #
    def produce_PREPARE_Exception(function_name, Exception_Class):
        @rename(function_name)
        @creator
        def PREPARE_Exception(message, *arguments):
            if arguments:
                message = message.format(*arguments)

            error = Exception_Class(message)

            trace('{} => {}', function_name, error)

            return error


        return PREPARE_Exception


    #
    #   PREPARE_NameError
    #
    #   NOTE:
    #       See note in "Crystal/Exception.py" on `PREPARE_NameError` being a "create" functions.
    #
    PREPARE_NameError = produce_PREPARE_Exception('PREPARE_NameError', Python_NameError)


    #
    #   share(f [...] [, name = value] ...)
    #       Share a value "globally" -- that is, in `crystal_global` -- which is shared by all Crystal submodules.
    #
    #   NOTE:
    #       If exactly one [non-keyword] argument is given, then maybe `share` is being used as an annotation
    #       (i.e.: `@share`).
    #
    #       In this case, the return value is the first argument (in all other cases the return value is `none`).
    #
    if python_debug_mode:
        def RAISE__crystal_global_X_already_exists__ERROR(name, previous, value):
            duplicate_name_error = PREPARE_NameError(
                    "crystal global `{}` already exists ({!r}): can't insert {!r} also",
                    name, previous, value,
                )

            #
            #   Since the next line will appear in stack traces, make it look prettier by using
            #   `duplicate_name_error` (to make the line shorter & more readable)
            #
            #   THis is better than the call to `RAISE__crystal_global_X_already_exists__ERROR` appearing in
            #   the stack traces.
            #
            raise duplicate_name_error


        def insert_crystal_global(name, v):
            assert fact_is_interned_actual_string(name)

            if name in crystal_global:
                previous = crystal_global[name]

                RAISE__crystal_global_X_already_exists__ERROR(name, previous, v)

            crystal_global[name] = v
    else:
        insert_crystal_global = stash_crystal_global


    def share_class_or_function(v):
        assert fact_is__python_class__or__python_function(v)

        name          = v.__name__
        interned_name = intern_python_string(name)

        if name is not interned_name:
            v.__name__ = interned_name

        insert_crystal_global(interned_name, v)


    def share(*classes_or_functions, **name_value_map):
        assert (classes_or_functions) or (name_value_map)

        if classes_or_functions:
            if length(classes_or_functions) == 1:
                v = classes_or_functions[0]

                share_class_or_function(v)

                if length(name_value_map) == 0:
                    #
                    #   In case this `@share` is being called, make sure to return the first argument (see note above).
                    #
                    return v
            else:
                for v in classes_or_functions:
                    share_class_or_function(v)

        if name_value_map:
            value = name_value_map.__getitem__

            for k in name_value_map:
                v = value(k)

                interned_k = intern_python_string(k)

                if is_python_string(v):
                    v = intern_python_string(v)

                insert_crystal_global(interned_k, v)


    #
    #   Share
    #
    if python_debug_mode:
        share(
                debug_test__is_interned_python_string,
                fact_is_interned_actual_string,
                fact_is__python_class__or__python_function,
                fact_is_python_string,
            )


    share(
            #
            #   Our Functions (without keywords)
            #
            insert_crystal_global,
            is_python_string,
            operator_equal__by_identity,
            operator_not_equal__by_identity,
            produce_PREPARE_Exception,
            share,


            #
            #   Python Types
            #
            Python_Code   = Python_Code,
            Python_Object = Python_Object,
            Python_Type   = Python_Type,


            #
            #   Python Functions
            #
            length             = length,
            python_is_instance = python_is_instance,
            python_type        = python_type,


            #
            #   Python Methods
            #
           #python_query_code_cell_variables    = python_query_code_cell_variables,
            python_query_code_constants         = python_query_code_constants,
           #python_query_code_filename          = python_query_code_filename,
           #python_query_code_first_line_number = python_query_code_first_line_number,
           #python_query_code_flags             = python_query_code_flags,
           #python_query_code_free_variables    = python_query_code_free_variables,
           #python_query_code_line_number_table = python_query_code_line_number_table,
            python_query_code_name              = python_query_code_name,
           #python_query_code_stack_size        = python_query_code_stack_size,
            python_query_code_symbol_names      = python_query_code_symbol_names,
           #python_query_code_total_arguments   = python_query_code_total_arguments,
           #python_query_code_total_locals      = python_query_code_total_locals,
           #python_query_code_variable_names    = python_query_code_variable_names,
           #python_query_code_virtual_code      = python_query_code_virtual_code,


            #
            #   Python Slot Wrappers
            #
            python_hash__by_identity = python_hash__by_identity,


            #
            #   Our Functions (have to use keywords as function name might not match what we want to store it as)
            #
            intern_python_string  = intern_python_string,       #   In release mode is [internally] named `intern`
            PREPARE_NameError     = PREPARE_NameError,          #   In release mode is [internally] named `PREPARE_Exception`
        )

    if is_python_3:
        share(
                python_query_code_total_keyword_arguments = python_query_code_total_keyword_arguments,
            )
