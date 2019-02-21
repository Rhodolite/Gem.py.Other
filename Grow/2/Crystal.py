#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


vision = 'Programming is an art to communicate clearly and concisely to fellow programmers.'


#
#   trace mode
#
tracing = True


#
#   Show Crystal Globals
#
show_crystal_globals = False


def module(f):
    f()


@module
def module():
    import  sys     as  Python_System
    import  os.path as  Python_Path


    #
    #   NOTE:
    #       We call this `Python_Exceptions_Module` instead of `Python_Exceptions` to avoid confusion with
    #       `Python_Exception` (a python type (i.e.: `exceptions.Exception`)).
    #
    is_python_2              = (Python_System.version_info.major is 2)
    is_python_3              = (Python_System.version_info.major is 3)
    Python_BuiltIn           = __import__('__builtin__'  if is_python_2 else   'builtins')
    Python_Exceptions_Module = (__import__('exceptions')   if is_python_2 else  Python_BuiltIn)


    #
    #   Python keywords
    #
    false = False
    none  = None
    true  = True


    #
    #   Python Types
    #
    #       Python_Function     - The type of a python function; extracted from the type of `module`
    #                             (which is obviously a python function)
    #
    #       Python_Module       - The type of a python module; extracted from the type of `Python_System`
    #                             (which is obviously a python module)
    #
    Python_ImportError = Python_Exceptions_Module.ImportError
    Python_Function    = module.__class__                #   See comment above.
    Python_MutableMap  = Python_BuiltIn.dict
    Python_Module      = Python_System.__class__         #   See comment above.
    Python_String      = Python_BuiltIn.str


    #
    #   Python Functions
    #
    path_basename               = Python_Path.basename
    python_intern_python_string = (Python_BuiltIn   if is_python_2 else   Python_System).intern
    static_method               = Python_BuiltIn.staticmethod   #   Actually a type, but used as if a function


    #
    #   Python Methods
    #
    python__mutable_map__operator__delete_item = Python_MutableMap.__delitem__
    python__mutable_map__operator__find_item   = Python_MutableMap.__getitem__
    python__mutable_map__operator__stash_item  = Python_MutableMap.__setitem__


    python__mutable_map__lookup  = Python_MutableMap.get
    python__mutable_map__pop     = Python_MutableMap.pop



    #
    #   Python Values
    #
    python_debug_mode = Python_BuiltIn.__debug__


    #
    #   `ActualString` is an alias for `Python_String`.
    #
    #       It means a non-empty `Python_String`
    #
    ActualString = Python_String


    #
    #   python_loaded_modules (also python_{lookup,pop,store}_loaded_module)
    #
    python_loaded_modules = Python_System.modules

    python_delete_loaded_module = python_loaded_modules.__delitem__
    python_find_loaded_module   = python_loaded_modules.__getitem__
    python_lookup_loaded_module = python_loaded_modules.get
    python_stash_loaded_module  = python_loaded_modules.__setitem__


    #
    #   Copy my module name [being constructed] into `temporary_crystal`
    #
    #   NOTE:
    #       This is called `temporary_crystal` instead of `temporary_crystal_module` to avoid confusion with
    #       `temporary_crystal_submodule` (defined below).
    #
    temporary_crystal = python_loaded_modules['Crystal']


    #
    #   Trace mode & `show_crystal_globals` (copy from module scope)
    #
    show_crystal_globals = temporary_crystal.show_crystal_globals
    tracing              = temporary_crystal.tracing


    #
    #   limited_arrange
    #
    #   NOTE:
    #       Called by `trace_prefix` below, hence cannot, internally, call `trace`.
    #
    #   NOTE:
    #       Not exported by us, since it cannot, internally, call `trace`.
    #
    #       A *duplicate* version is defined later (alled `arrange`), that one, can be modified to call `trace`.
    #
    if tracing:
        def limited_arrange(message, *arguments):
            return message.format(*arguments)


    #
    #   limited_calculate
    #
    #   NOTE:
    #       Called by `trace_prefix` below, hence cannot, internally, call `trace`.
    #
    #   NOTE:
    #       Not exported by us, since it cannot, internally, call `trace`.
    #
    if tracing:
        def limited_calculate(f):
            return f()


    #
    #   creator(f)   - Doesn't do anything at all!
    #
    #                  Use to document that the function is a "create" function and calls a constructor.
    #
    def creator(f):
        return f


    #
    #   trace
    #
    #   NOTE:
    #       trace_prefix = "% Crystal.py: "
    #
    if tracing:
        @limited_calculate
        def trace_prefix():
            path = __file__

            if path.endswith('.pyc'):
                path = path[:-1]

            return limited_arrange('% {}: ', path_basename(path))


        def trace(message, *arguments):
            if arguments:
                message = message.format(*arguments)

            print(trace_prefix + message)
    else:
        def trace(message, *arguments):
            pass


    #
    #   fact_is_actual_string(s)
    #
    #       Assert the fact that `s` is a `ActualString` (that is a non-empty python string)
    #
    if python_debug_mode:
        def fact_is_actual_string(s):
            assert python_type(s) is ActualString
            assert length(s) > 0

            return true


    #
    #   create_Python_Function__using__crystal_global
    #
    #
    #   NOTE:
    #       As can be seen, the members of `Python_Function` are named "func_*" in python 2, but "__*__" in python 3.
    #
    #       To avoid this problem, we simply turn the `.__get__` methods of the descriptors into bound methods.
    #
    #       Example:
    #
    #           `python_query_function_closure` is a binding of method `.__get__` to `Python_function.func_closure`
    #
    #           Thus `python_query_function_closure(f)` is the same as using `f.func_closure` in a read context
    #           where the `.__get__` method is called.
    #
    #   NOTE:
    #       We cannot use `Python_Function.__name__` since the metaclass of `Python_Function` (i.e.: `Python_Type`)
    #       defines a `.__name__` descriptor that returns the class name.
    #
    #       Thus the value of `Python_Function.__name__` is `"function"`.
    #
    #       Instead we have to look in the class symbols ourselves for the `.__name__` class member.
    #
    if is_python_2:
        python_query_function_closure  = Python_Function.func_closure .__get__
        python_query_function_code     = Python_Function.func_code    .__get__
        python_query_function_defaults = Python_Function.func_defaults.__get__
        python_query_function_globals  = Python_Function.func_globals .__get__
    else:
        python_query_function_closure  = Python_Function.__closure__ .__get__
        python_query_function_code     = Python_Function.__code__    .__get__
        python_query_function_defaults = Python_Function.__defaults__.__get__
        python_query_function_globals  = Python_Function.__globals__ .__get__

    python_function_class_members = Python_Function.__dict__

    python_query_function_name = python_function_class_members['__name__'].__get__


    #
    #   crystal_global
    #
    #   SUMMARY:
    #       We are very limited in what we can do here, we have to be inherited from `Python_MutableMap` (i.e.: `dict`)
    #       and cannot overwrite `.__getitem__` and `.__setitem__` (in Python 2.*)
    #
    #   Details:
    #       A global symbol table, at least on Python 2.*, must be inherited from `dict`.
    #
    #       Furthermore, under Python 2.*, reading global symbols, and writing global symbols
    #       bypasses `.__getitem__` and `.__setitem__` methods we declare (on Python 3.*
    #       it does call these methods).
    #
    #       Due to these limitations, the only thing different about our `CrystalGlobals` is
    #       our own version of `.__repr__` (and the alias `.provide` for the python method `.setdefault`)
    #
    class CrystalGlobals(Python_MutableMap):
        __slots__ = (())


        #
        #   `.__eq__`, `.__hash__`, and `.__ne__` are assigned later in "Crystal/Fixup_CrystalGlobals.py"
        #
        #__eq__   = operator_equal__by_identity
        #__hash__ = python_hash__by_identity
        #__ne__   = operator_not_equal__by_identity


        __delattr__      = python__mutable_map__operator__delete_item
        __getattribute__ = python__mutable_map__operator__find_item
        __setattr__      = python__mutable_map__operator__stash_item


        #
        #   NOTE:
        #       Due to overriding of `__getattribute__` above we can't actually access a `.lookup` and
        #       `.provide` methods that we can find using `.` ...
        #
        #       .... Therefore, don't define them, but instead use `lookup_crystal_global`, `pop_crystal_global`,
        #       and `provide_crystal_global` (defined below).
        #
        #lookup  = python__mutable_map__lookup
        #pop     = python__mutable_map__pop


        #@crystalize                        #   Done below once `crystalize` is defined.
        @static_method
        def __repr__():
            return '<CrystalGlobals>'


    #@crystalize                            #   Not done since `crystalize` is not yet defined, and function only called once.
    @creator
    def create_crystal_global():
        crystal_global = CrystalGlobals(
                #
                #   If we don't provide a `__name__` member, then it will find `__builtins__.__name__` when the user
                #   tries to access `__name__` (often done implicitly by python when creating classes) -- not what we
                #   want!
                #
                __name__ = 'Crystal',

                #
                #   Python's import mechanism will define `__package__` if we don't ...
                #
                __package__ = 'Crystal',


                #
                #   Python builtins (required, unmodified, to allow usage of `import`)
                #
                #   NOTE:
                #       A different `__builtins__` can be used, with `__import__` placed there, and will work sometimes.
                #
                #       However, sometimes, for some import, it will complain about:
                #
                #           "unmarshling objects not allowed in restricted mode".
                #
                #       To avoid this, have to use the original `Python_BuiltIn` module -- which is how python detects
                #       we are not in restricted mode.
                #
                __builtins__ = Python_BuiltIn,


                #
                #   Python_BuiltIn  - Above saved under the key `__builtins__`; here, also, saved under the name we
                #                     use to access them; i.e.: `Python_BuiltIn`
                #
                Python_BuiltIn = Python_BuiltIn,


                #
                #   Python Keywords
                #
                false = false,
                none  = none,
                true  = true,


                #
                #   Python Types
                #
                Python_Function   = Python_Function,
                Python_Module     = Python_Module,
                Python_MutableMap = Python_MutableMap,
                Python_String     = Python_String,


                #
                #   Python Functions
                #
                python_intern_python_string = python_intern_python_string,
                static_method               = static_method,


                #
                #   Python Bound Methods (i.e.: A python method bound to a python instance [as it's first argument]).
                #
                python_find_loaded_module   = python_find_loaded_module,
                python_lookup_loaded_module = python_lookup_loaded_module,
                python_stash_loaded_module  = python_stash_loaded_module,

                python_query_function_closure  = python_query_function_closure,
                python_query_function_code     = python_query_function_code,
                python_query_function_defaults = python_query_function_defaults,
                python_query_function_globals  = python_query_function_globals,
                python_query_function_name     = python_query_function_name,


                #
                #   Python Values
                #
                python_debug_mode = python_debug_mode,


                #
                #   Our Types
                #
                ActualString   = ActualString,
                CrystalGlobals = CrystalGlobals,


                #
                #   Our functions
                #
                #       NOTE:
                #           These are done below once the functions are rewritten with `crystalize`.
                #
                #creator               = creator,
                #fact_is_actual_string = fact_is_actual_string,
                #trace                 = trace,


                #
                #   Our values
                #
                #crystal_global      = crystal_global    #   Done below, once `crystal_global` exists
                is_python_2          = is_python_2,
                is_python_3          = is_python_3,
                show_crystal_globals = show_crystal_globals,
            )

        #
        #   A reference to ourself (can use instead of `python_globals()` in a function).
        #
        crystal_global.crystal_global = crystal_global

        return crystal_global


    crystal_global = create_crystal_global()


    #
    #   NOTE:
    #       Read `.__get__` below to mean "bind" (i.e.: bind the argument as the first argument to
    #       the method that appears before the `.`).
    #
    #   lookup_crystal_global   - Emulate what `crystal_global.lookup` (*IF* we had not overridden the
    #                             `.__getattribute__` method) would normally be.
    #
    #                             This would normally be done by calling `.__get__` method of
    #                             `python__mutable_map__lookup` (i.e.: `dict.get`) to create a binding of
    #                             `crystal_global` to `python__mutable_map__lookup`.
    #
    #                             Therefore, that is what we do here.
    #
    #   pop_crystal_global      - Emulate what `crystal_global.get` (*IF* we had not overridden the
    #                             `.__getattribute__` method) would normally be.
    #
    #                             See comments above on `lookup_crystal_global`.
    #
    #   stash_crystal_global     - Emulate what `crystal_global.__setitem__` (*IF* we had not overridden the
    #                             `.__getattribute__` method) would normally be.
    #
    #
    lookup_crystal_global = python__mutable_map__lookup              .__get__(crystal_global)
    pop_crystal_global    = python__mutable_map__pop                 .__get__(crystal_global)
    stash_crystal_global  = python__mutable_map__operator__stash_item.__get__(crystal_global)

    crystal_global.lookup_crystal_global = lookup_crystal_global
    crystal_global.pop_crystal_global    = pop_crystal_global
    crystal_global.stash_crystal_global  = stash_crystal_global


    #
    #   crystalize(f)     - Creates a new function from `f`, but with it's globals set to `crystal_global`
    #                       (i.e.: Make it a crystal, which means use `crystal_global`).
    #
    @creator
    def crystalize(f):
        return Python_Function(
                   python_query_function_code(f),
                   crystal_global,
                   python_query_function_name(f),
                   python_query_function_defaults(f),
                   python_query_function_closure(f),
               )


    #
    #   Rewrite `crystalize` to use `crystal_global` by:
    #
    #       1.  Using itself on itself!
    #
    crystalize = crystalize(crystalize)


    #
    #   Rewrite `creator`, `trace`, and `fact_is_actual_string` to use `crystal_global`>
    #
    #   Also, store our "rewritten" `creator`, `trace`, and `fact_is_actual_string` functions in
    #   `crystal_global`.
    #
    creator = crystalize(creator)
    trace   = crystalize(trace)

    crystal_global.creator = creator
    crystal_global.trace   = trace

    if python_debug_mode:
        fact_is_actual_string = crystalize(fact_is_actual_string)

        crystal_global.fact_is_actual_string = fact_is_actual_string


    #
    #   Rewrite `CrystalGlobals.__repr__` to use `crystal_global`
    #
    #   NOTE:
    #       We have to wrap it, again, using `static_method`.
    #
    #   NOTE:
    #       Due to how descriptors work in python the expression `CrystalGlobals.__repr__` when used in a
    #       query context (read context) as below automatically unwraps the `static_method`.
    #
    CrystalGlobals.__repr__ = static_method(crystalize(CrystalGlobals.__repr__))


    #
    #   NOTE:
    #       From here on, in this file, *ALL* functions will be defined with the annotation:
    #
    #           `@crystalize`
    #
    #       To make sure they use `crystal_global`
    #
    #   NOTE:
    #       For consistency sake, this is done to *ALL* functions, from here on, defined in this file, even those that
    #       are temporary, and don't need it (since they are discarded).
    #
    #   NOTE:
    #       In other files, this is not neccessary, as they use `@module` which makes them use `crystal_global`
    #       for the main module function, and hence to all functions declared inside it.
    #


    #
    #   module__execute__function__using__crystal_global(f)
    #
    #       Execute `f` in `crystal_global`.
    #
    #   NOTE:
    #       `
    #       `crystalize` is used twice:
    #
    #           1.  `@crystalize` to make sure
    #               `module__execute__function__using__crystal_global` uses `crystal_global`
    #
    #           2.  `crystalize(f)` to make sure `f` uses `crystal_global`
    #
    #               As per above, this means all functions defined inside `f` also use `crystal_global`.
    #
    #   NOTE:
    #       When used as an annotation, `@module` returns `none`.
    #
    #       Since we use it as follows:
    #
    #           @module
    #           def module():
    #               ...
    #
    #       This means that `module` is reset to `none` after being used once ...
    #
    #       This doesn't matter, since we only call it once, and the temporary module scope in which it is
    #       defined is is immediatly discarded after being used.
    #
    #       *IF* we wanted to call `@module` twice, we could, instead return ourselves as our
    #       value ... (but again this is unnecessary since we only all it once per temporary
    #       module socpe)
    #
    @crystalize
    def module__execute__function__using__crystal_global(f):
        f = crystalize(f)

        f()


    #
    #   temporary_PREPARE_ImportError
    #
    @crystalize
    @creator
    def temporary_PREPARE_ImportError(message, *arguments):
        assert fact_is_actual_string(message)

        if arguments:
            message = message.format(*arguments)

        import_error = Python_ImportError(message)

        trace('temporary_PREPARE_ImportError => {}', import_error)

        return import_error


    #
    #   TemporaryCrystalSubmodule
    #       A temporary module used while building the real module.
    #
    #       NOTE:
    #           Normally, the `.__dict__` member of the temporary module, becomes the permenant `globals()` of the
    #           functions created while importing the module.
    #
    #           That is, the temporary module is discarded after the import, but it's `.__dict__` member is retained
    #           (if any functions are defined in the module).
    #
    #       PROBLEM:
    #           This is a serious problem, because classes inherited from `Python_Module` also *REPLACE* the values
    #           (while keeping the keys) of the `.__dict__` member with `none` when the module is reclaimed
    #           (this happens for us, since we remove the module from `sys.modules` and do not keep a reference
    #           count to it).
    #
    #       SOLUTION:
    #           We provide a module annotation `module`
    #           (i.e.: `module__execute__function__using__crystal_global`)
    #           that *rewrites* the function defined while importing the module to use `crystal_global`
    #           as the function's global symbols.
    #
    #       RESULT:
    #           The global values of `crystal_global` are never replaced by `none`, and thus can continue
    #           to be used in any functions defined in the module.
    #
    #   MEMORY CLEANUP:
    #       The reason python replaces the values of the `.__dict__` member with `none` is to avoid memory loops,
    #       and make recycling memory faster.
    #
    #       We are, of course, bypassing, this optimization with the above.
    #
    #       See:
    #
    #           Crystal Principle #4:
    #               An instance should have an easy to understand lifecycle as possible.
    #
    #               The easist lifecycle to understand is for an instance to be fully immutable:
    #
    #               1.  Thus it only has one state: it exists & all it's members are immutable.
    #
    #               The more states an object has, the more prone it is to having bugs.
    #
    #           Crystal Principle #5:
    #               Unexpected states in an instance of an object's lifecycle, means, these are often not unit tested
    #               (since they are unexpected).
    #
    #       In generaly, in Crystal, all globals are considered "fixed" (immutable) -- and thus only have one state.
    #
    #           Them, suddendly, acquiring a second value of `none` is unacceptable (and for this to only happen
    #           in rare, very hard to test cases, is even worse).
    #
    #       An optimization that introduces unexpected states, that are untested, and therefore unexpected bugs
    #       into a program is a really bad idea.
    #
    #       Thus, we are *DELIBERATELY* disabling this python optimization with all this -- reducing the number of
    #       unexpected, untested, bugs in our program.
    #
    class TemporaryCrystalSubmodule(Python_Module):
        __slots__ = (())


        @crystalize
        def __repr__(self):
            return '<BuildCrystalSubmodule {!r}>'.format(self.__name__)


    @crystalize
    @creator
    def create_temporary_crystal_submodule(name):
        #
        #   `r` means "result".  To make it easier to read the code when repeating the variable a lot.
        #
        r = TemporaryCrystalSubmodule(name)

        r.module = module__execute__function__using__crystal_global

        return r


    #
    #   import_crystal_submodule
    #


    #
    #   crystal_module_path_list    - "/full/path/to/Crystal"
    #
    #       Tell `python_lookup_module_blueprint` that Crystal submodules are found inside the "Crystal/" directory
    #       (i.e.: "Crystal.py" with the ".py" removed; or for Python 2.* maybe "Crystal.pyc" with ".pyc" removed).
    #
    #   NOTE:
    #       `crystal_module_path_list` is a `Python_List` of path names (hence the external `[` and `]`).
    #
    @limited_calculate
    def crystal_module_path_list():
        path = __file__

        if path.endswith('.pyc'):
            chop = -4
        else:
            chop = -3

        return [python_intern_python_string(path[:chop])]


    if is_python_2:
        #
        #   Python 2.* method of loading a module with `module` pre-initialized
        #
        #       This is messy -- see below for the Python 3.0 method which is much cleaner.
        #
        import  imp     as  Python_OldImport


        python_find_module = Python_OldImport.find_module
        python_load_module = Python_OldImport.load_module


        @crystalize
        def import_crystal_submodule(module_name, submodule_name, module):
            #
            #   Temporarily store our module in `sys.modules[module_name]`.
            #
            #   This is needed in python 2.*, as the way to pass the "pre-initialized" module to `python_load_module`
            #   (i.e.: `imp.load_module`)
            #
            #       (In the cleaner python 3.* version below, we pass the modules directly to
            #       `blueprint.loader.exec_module` and thus do not need to store the module in
            #       `sys.modules[module_name]`).
            #
            #   NOTE:
            #       If this was real import implementation we would need to cleanup
            #       `sys.modules[module_name]` when an exception is thrown.
            #
            #       However, this is not a true import mechanism.  If it fails, our program will simply
            #       exit.
            #
            #       Therefore, there is no `try` clause below to cleanup if `python_find_module` (i.e.: `imp.load_module`)
            #       throws `ImportError`
            #
            python_stash_loaded_module(module_name, module)

            [f, pathname, description] = python_find_module(submodule_name, crystal_module_path_list)

            #
            #   CAREFUL here:
            #       We *MUST* close `f` if any exception is thrown.
            #
            #       So ASAP use `f` within a `with` clause (this ensures `f` is always closed, whether
            #       an exception is thrown or not)
            #
            if f is not none:
                with f:
                    python_load_module(module_name, f, pathname, description)
            else:
                #
                #   Throw an error here.
                #
                python_load_module(module_name, f, pathname, description)

            python_delete_loaded_module(module_name)
    else:
        #
        #   Python 3.* method of loading a module with `module` pre-initialized
        #
        import  importlib.machinery  as  Python_ImportMachinery

        Python_PathFinder              = Python_ImportMachinery.PathFinder
        python_lookup_module_blueprint = Python_PathFinder.find_spec


        @crystalize
        def import_crystal_submodule(module_name, submodule_name, module):
            blueprint = python_lookup_module_blueprint(module_name, crystal_module_path_list)

            if blueprint is none:
                #
                #   `PREPARE_ImportError` is defined in "Crystal/Exception.py"
                #
                #   It is also wiped by "Crystal/Wipe_CrystalGlobals.py"
                #
                #   Hence, before loading "Crystal/Share.py" and after loading "Crystal/Wipe_CrystalGlobal.py"
                #   we don't have a value for `PREPARE_ImportError` (so we use `temporary_PREPARE_ImportError` instead).
                #
                PREPARE_ImportError = lookup_crystal_global('PREPARE_ImportError', temporary_PREPARE_ImportError)

                import_error = PREPARE_ImportError("can't find crystal submodule {}", submodule_name)

                raise import_error

            #
            #   NOTE:
            #       We don't want to call `importlib.util.module_from_spec` as it will create a *new* module.
            #
            #       Instead we want to use our already supplied `module`.
            #
            #       Also, although `importlib.util.module_from_spec` supplies the following members, none of them, other
            #       than `.__name__` (which we supply above) are actually needed for our temporary module (i.e.: nothing
            #       uses them):
            #
            #           module.__name__    = blueprint.name
            #           module.__loader__  = blueprint.loader
            #           module.__package__ = blueprint.parent
            #           module.__spec__    = blueprint
            #           module.__path__    = blueprint.submodule_search_locations
            #           module.__file__    = blueprint.origin
            #           module.__cached__  = blueprint.cached
            #
            #   NOTE# 2:
            #       Even though we don't supply the above names (by calling `importlib.util.module_from_spec`) the
            #       following names are supplied anyway by Python, apparently in `blueprint.loader.exec_module`:
            #
            #           module.__builtins__
            #           module.__loader__
            #           module.__package__
            #           module.__spec__
            #

            blueprint.loader.exec_module(module)


    @crystalize
    def load_crystal_submodule(submodule_name):
        #
        #   `intern_python_string` is defined in "Crystal/Share.py"
        #
        #   It is also wiped by "Crystal/Wipe_CrystalGlobals.py"
        #
        #   Hence, before loading "Crystal/Share.py" and after loading "Crystal/Wipe_CrystalGlobal.py"
        #   we don't have a value for `intern_python_string` (so we use `python_intern_python_string` instead).
        #
        intern_python_string = lookup_crystal_global('intern_python_string', python_intern_python_string)

        module_name = intern_python_string('Crystal.' + submodule_name)

        trace('loading submodule {!r}', module_name)

        assert python_lookup_loaded_module(module_name) is none

        temporary_crystal_submodule = create_temporary_crystal_submodule(module_name)

        #
        #   Change `.__name__` temporarily & immediately (after the import is done) restore it.
        #
        #   (see comment in `import_crystal_submodule` about not catching `ImportError`).
        #
        #   NOTE:
        #       We use `previous_name` here, so that, we grab the interned name `"Crystal"`
        #       (after it has been interned by "Crystal/Fixup_GlobalSymbols.py")
        #
        previous_name           = crystal_global.__name__
        crystal_global.__name__ = module_name

        import_crystal_submodule(module_name, submodule_name, temporary_crystal_submodule)

        crystal_global.__name__ = previous_name

        #
        #   If the module called `save_crystal_submodule` (which saves it as a crystal global) then return this value.
        #
        return lookup_crystal_global(submodule_name)


    for module_name in ((
            'Share', 'Core', 'Fixup_CrystalGlobals', 'Fact', 'Cannot', 'Exception', 'ObjectMembers',
            'Fixed_3', 'Fixed_5', 'Mutable_10', 'Mutable_12',
            'ReusableContextLifecycle', 'SimpleContextLifecycle',
            'ChangePrefix', 'StringOutput', 'Build_MutableMap', 'MutableMap',
#           'Cache',
            'Module', 'Z_Mode',
    )):
        load_crystal_submodule(module_name)


    replace_crystal_module = pop_crystal_global('replace_crystal_module')


    #
    #   NOTE:
    #       For consistency we assign the return value to `Crystal`
    #
    #       We don't actually use the value `Crystal` after we assign it ...
    #
    Crystal = replace_crystal_module(
            vision = vision,
#           Z_Mode = load_crystal_submodule('Z_Mode')
        )

    if false:
        load_crystal_submodule('Show_Portray')

    if python_debug_mode:
        load_crystal_submodule('Verify_CrystalGlobals')

    load_crystal_submodule('Wipe_CrystalGlobals')

    if show_crystal_globals:
        load_crystal_submodule('Show_CrystalGlobals')
