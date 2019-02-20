    #
    #   Python Functions (as per Principle #1, fully spelled out).
    #
    #   NOTES:
    #       `intern_string`     is an alias for `sys.intern`
    #       `length`            is an alias for python builtin `len`
    #
    intern_string = (Python_BuiltIn   if is_python_2 else   Python_System).intern
    length        = Python_BuiltIn.len


    #
    #   `InternedActualString` is an alias for `ActualString`.
    #
    #   It means the `ActualString` has been interned with `intern_string`.
    #
    InternedActualString = ActualString


    #
    #   fact_is_interned_actual_string(s)   - Assert the fact that `s` is an `InternedActualString`
    #
    if python_debug_mode:
        def fact_is_interned_actual_string(s):
            assert type(s) is InternedActualString
            assert length(s) > 0
            assert intern_string(s) is s

            return true


    #
    #   rename_function(f, name)    - Rename the [internal] name of a funtion to `name`.
    #       Only useful in debug mode.
    #
    #   Function                - python type for a function
    #   function_closure        - get the closure of a function
    #   function_code           - get the code of a function
    #   function_defaults       - get the defaults of a function
    #   function_globals        - get the globals of a function.
    #
    #   NOTE:
    #       To avoid the different naming of the `func_closure` (python 2) .vs. `__closure__` (python 3) these are
    #       mapped to function names.
    #
    #   NOTE:
    #       Actually these are not exactly functions (technically they are bound methods in python), however, they
    #       behave as functions.
    #
    #   NOTE:
    #       Regarding `function_name` we can't use `Function.__name__` as this is overriden by the descriptor in
    #       the metaclass of `Function`; i.e.: `type(Function).__name__` to return `"function"`) -- thus we have to
    #       look in the mapping for `Function` and extract `__name__` from there.
    #
    Function = boot.__class__

    if is_python_2:
        function_closure  = Function.func_closure .__get__
        function_code     = Function.func_code    .__get__
        function_defaults = Function.func_defaults.__get__
        function_globals  = Function.func_globals .__get__
    else:
        function_closure  = Function.__closure__ .__get__
        function_code     = Function.__code__    .__get__
        function_defaults = Function.__defaults__.__get__
        function_globals  = Function.__globals__ .__get__

    function_name = Function.__dict__['__name__'].__get__


    if python_debug_mode:
        def fact_is_function(f)
            assert type(f) is Function

            return true


    if python_debug_mode:
    def rename_function(f, interned_name):
        assert fact_is_function              (f)
        assert fact_is_interned_actual_string(interned_name)

        return Function(
                    function_code(f),
                    function_scope(f),
                    interned_name,
                    function_defaults(f),
                    function_closure(f),
              )


    #
    #   Classes
    #
    #       Summary:
    #
    #           We use `class_name` below to always get the actual name of a class.
    #
    #       Details:
    #
    #           The name of a class can be found normally as `classification.__name__`
    #
    #               Example:
    #
    #                   class Empty(object):
    #                       __slots__ = ((
    #                       ))
    #
    #                   assert Empty.__name__ == "Empty"
    #
    #               Using `.__name__` actually looks for a `"__name__"` in the metaclass mapping
    #               (in this case `Type`), and when it finds a descriptor then calling the `.__get__`
    #               method of the descriptor.
    #
    #               For class `Empty` above it find the descriptor `Type.__dict__["__name__"]`,
    #               and calls its `.__get__` method to get the class name of `"Empty"`.
    #
    #           However, a class can choose to be annoying and have it's metaclass override `.__name__`
    #
    #               Example:
    #
    #                   Object = object
    #                   Type   = type
    #
    #                   class MetaAnnoying(Type):
    #                       @property
    #                       def __name__(self):
    #                           return 'Delightful'
    #
    #
    #                   class Annoying(
    #                       Object,
    #                       metaclass     = MetaAnnoying,       #   Python 3 method to use a metaclasses
    #                   ):
    #                      #__metaclass__ = MetaAnnoying        #   Python 2 method to use a metaclasses
    #
    #                       __slots__ = ((
    #                       ))
    #
    #                   assert Annoying.__name__                           == "Delightful"
    #                   assert Type.__dict__['__name__'].__get__(Annoying) == "Annoying"
    #
    #               In the above example `Annoying.__name__` does not properly return the class name
    #               `"Annoying"` but instead the [fake] class name `"Delightful"`.
    #
    #               However, we can call the descriptor directly, to still get the [proper] class name
    #               `"Annoying"`.)
    #
    #   NOTE:
    #       Also we can't use `Type.__name__` (since this is override by the descriptor in the metaclass of Type;
    #       i.e.: `type(Type).__name__` to return `"type"`) -- thus we have to look in the mapping for `Type` and
    #       extract `__name__` from there.
    #
    class_name = Type.__dict__['__name__'].__get__




    #GROW
    #
    #   main module
    #
    main_module = python_modules['__main__']


    main_path = main_module.__file__
    main_name = main_module.__name__


    if (main_path.endswith('.x')) and (main_name == '__main__'):
        trace('Detected that the main module is: {!r}', main_path)

        class Grow(Object):
            __slots__ = ((
                'copyright_value',          #   None | String
            ))


            def __init__(self):
                self.copyright_value = none


            @static_method
            def extract_copyright(path):
                with open(path) as f:
                    data = f.read()

                text_lines = data.splitlines()

                if (
                        length(text_lines) >= 2
                    and text_lines[0] == '#'
                    and text_lines[1].startswith('#   Copyright (c) ')
                    and text_lines[2] == '#'
                ):
                    return text_lines[1][4:]

                missing_copyright = PREPARE_value_error('cannot find copyright in {!r}', path)

                raise missing_copyright


            @property
            def copyright(self):
                assert self.copyright_value is none

                copyright_value = self.extract_copyright(main_path)

                trace('Extracted copyright from {!r}', main_path)
                trace('Copyright: {!r}', copyright_value)

        main_module.X = Grow()
    #
    #   Preferred future method:
    #
    #       build_crystal_submodule = BuildCrystalSubmodule(name)
    #
    #       using build_crystal_submodule:
    #           .false = false
    #           .none  = none
    #
    #       return build_crystal_submodule
    #
    #   Here the `.` operator without a left-hand value would take the left hand value from the `using` clause.
    #
    #   Would make the code a lot more readable ...




    Python_Slice     = Python_BuiltIn.slice
    #
    #   Our values
    #
    slice_all = Python_Slice(none, none)


    #
    #   fixup_keys
    #       append_fixup_key
    #       zap_fixup_keys
    #
    fixup_keys       = []
    append_fixup_key = fixup_keys.append
    zap_fixup_keys   = Python_Method(fixup_keys.__delitem__, slice_all)     #   `del fixup_keys[:]`


    #
    #   create_Python_Method(f, first)
    #       Bind `first` as the first parameter to funtion `f`
    #
    #   NOTE:
    #       This is the "create" method for `Python_Method` (i.e.: the replacement for the constructor)
    #
    def bind(f, first):
        return Python_Method(f, first)

    #
    #   create_Python_MutableMap
    #
    @creator
    def create_Python_MutableMap(**name_value_pairs):
        return Python_MutableMap(name_value_pairs)



    #
    #   Python Types (Part XXX?)
    #
    #       Python_Slot     - The type of a python slot (i.e.: what is created from `__slots__` in a class).
    #
    Python_Slot = python_type(fixed_6_1)


    assert Python_Slot.__name__ == 'member_descriptor'


    @crystalize
    def __getattribute__(self, name):
        value = object.__getattribute__(self, name)

        trace('TemporaryCrystalSubmodule.__getattribute__({!r}) => {!r}', name, value)

        return value


    exit_due_to_exception = [false]

    previous_except_hook = sys.excepthook


    def crystal_except_hook(type, value, traceback):
        global  exit_due_to_exception

        exit_due_to_exception[0] = True

        sys.excepthook = previous_except_hook               #   Forward reference, defined below

        previous_except_hook(type, value, traceback)



    sys.excepthook = crystal_except_hook
#
#
#        3.  Declaring methods for a class in a *DIFFERENT* module than where
#            the class is defined.
#
#                The Crystal Parse tree is declared in "Z/Crystal_ParseTree.py".
#
#                However, the methods `convert_crystal_to_python" are declared
#                in "Z/Transform_Crystal_to_Python.py".
#
#                Normally methods should be declared inside their class, not
#                outside their class, and certaily not in a different module.
#
#            REASON:
#
#                The intent is to be able to convert to 15+ languages.
#
#                It's much more readable to have each converter in it's own
#                file, instead of them all jammed into "Z/Crystal_ParseTree.py".
#
#                Realistically, we should probably not declare them as methods
#                on the "Z/Crystal_ParseTree.py".
#
#                I WILL GO CHANGE THE CODE TO DO THAT!
#

#   convert_context
#
#       Convert a context to a specific instance.
#
#       The following conversions are preformed:
#
#           python type                         converted to
#           -----------                         ------------
#           Python_AbstractSyntaxTree_Load      syntax_tree_query
#
assert Python_AbstractSyntaxTree_Load._attributes == (())
assert Python_AbstractSyntaxTree_Load._fields     == (())


def convert_context(self):
    assert fact_is_python_abstract_syntax_tree_load(self)

    return syntax_tree_query



class SyntaxTree_QueryAttribute(Python_Object):
    __slots__ = ((
        'left',                         #   SyntaxTree_*
        'attribute',                    #   Python_String
    ))


    def __init__(self, left, attribute):
        self.left      = left
        self.attribute = attribute


    def __repr__(self):
        return arrange('<SyntaxTree.QueryAttribute {!r} {!r}>', self.left, self.attribute)

