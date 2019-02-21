#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   The totality of the Crystal vision summarized in one sentence:
#
#       Programming is an art to communicate clearly and concisely to fellow programmers.
#
vision = 'Programming is an art to communicate clearly and concisely to fellow programmers.'


#
#   NOTE:
#       As explained below under `module` this file is actual a bunch of modules all placed
#       in the same file for release purposes.
#


#
#   NOTE:
#       When quoting code it is quoted as follows: `print("hello world")`.
#
#       When quoting an English word it is quoted as follows: "English".
#
#       When quoting code of a string it is quoted as follows: `"a python string"`.
#


#
#   Principle #1:
#       No shortened names are ever used in Crystal:
#
#           1.  Thus `length` is an alias for the python builtin `len`.
#
#       Names are always an English word, with very few exceptions:
#
#           2.  An example of an exception is the synonym "HTML".
#
#               This is used instead of [the very long] "HyperTextMarkupLanguage".
#
#       Two english words are always seperated by '_', or with CamelCase.
#
#           1.  Thus `is_instance` is an alias for the pyton builtin `isinstance`.
#
#           2.  Words composed of two words that are acceptable in english as a single word are left alone.
#
#               Example "submodule" and "metaclass" -- Since these are acceptable as english words they are do
#               not have an '_' in them.
#


#
#   Principle #2:
#       Module are created inside a function, which is mainly a private scope for the module.
#
#       This *hides* all their members that they do not want to export.
#
#       All exports must be explicit.
#


#
#   module(f)       -- annotation around `f` to create a module.
#
#       Example:
#
#           @module
#           def Example():
#               seven = 3 + 4
#
#               return create_module("Example", seven = seven)
#
#       First, this will create a temporary wrapper function named `Example`.
#
#       Then due to the annotation `@module` it will execute `globals()["Example"] = module(Example)`.
#
#       The temporary wrapper function `Example` has a return value of `create_module("Example", seven = 7)`.
#
#       Thus the following will be executed:
#
#           globals()["Example"] = create_module("Example", seven = 7)
#
#       The advantage of the temporary wrapper function `Example` above, is that it can create temporary variables
#       (such as `seven` local variable above) to calculate the return value.
#
#       [Finally the temporary wrapper function `Example` is thrown away, including all unused variables.
#       Above the local variable `seven` is thrown away, as it is no longer used].
#
#   Since this is the `Crystal` module, then the above (which assigns to Example) can be considered the `Crystal.Example`
#   sub-module.
#
#   In other words, by using `@module` multiple times in a single python file -- a whole bunch of sub-modules can be
#   "combined" into a single python file, and be "seen" as multiple modules from other python files.
#
#   The purpose of combining a whole bunch of "sub-modules" into a single file, is for release purposes, to avoid clutter.
#
#   It allows the source code to be organized well (with multiple modules), but released as a single file.
#
def module(f):
    return f()


#
#  submodule Crystal.Boot
#
#       Used to boot `Crystal`.
#
#       Later, deleted, once `Crystal` is booted.
#
@module
def Boot()
    #
    #   Principle #3:
    #       Wrappers are created around all imports:
    #
    #           Thus a wrapper named `System` will be created around python `sys`.
    #
    #           Inside the wrapper we rename `sys` as `Python_System` to access the underlying python module.
    #           (See principle #1 on always using an English word).
    #
    #   Here in the `Crystal.Boot` submodule ... things are not quite as organized ... still for consistency
    #   the same names are used as in the rest of Crystal.
    #
    import  sys     as  Python_System


    is_python_2 = (Python_System.version_info.major == 2)


    #
    #   Python Builtins
    #
    #       The line below calling `__import__` directly is equivalent to:
    #
    #           if is_python_2:
    #               import  builtins        as  Python_BuiltIn
    #           else:
    #               import  __builtin__     as  Python_BuiltIn
    #
    Python_BuiltIn = __import__('__builtin__'  if is_python_2 else   'builtins')


    #
    #   ===  About `classification`  ===
    #
    #       It's hard to decide what to call a variable whose type is a class, as we can't use `class`
    #       (since that is a reserved word).
    #
    #       And using `Class` is way too easy to confuse with `class`.
    #
    #       There is no good solution to this.
    #
    #       Some people use `cls` or `klass` -- both attempted workarounds this problem ...
    #
    #       Due to lack of any better ideas, this code, and comments, uses `classification` as the name of a variable
    #       whose type is a class.
    #
    #       NOTE:
    #           Looking for synonyms for "class" did not help either, again the best choice seems
    #           to be "classification" [and admittedly, this is *NOT* a good choice, just the best choice of many
    #           bad choices].
    #


    #
    #   ===  About `type` .vs. `Type`  ===
    #
    #       In python, the builtin `type` is a type (the base metaclass of all classes and types).
    #
    #       When called with three arguments, as a normal constructor, it constructs a new type.
    #
    #       However, when `type` is called with one argument, it instead behaves as a function,
    #       returning the type of it's first argument.
    #
    #       To distinguish between these two cases, in Crystal code, the following is used:
    #
    #           type        - A function that returns the type of something.
    #           Type        - A type (the base metaclass of all classes and types).
    #
    #       Both `type` and `Type` are mapped to the python builtin `type`.
    #
    #   Example from below:
    #
    #       assert is_instance(type(classification), Type)
    #
    #   Here we are taking the type of `classification` and verifying it is an instance of `Type`
    #   (in other words verifying that `classification` is a class -- like all classes it's base
    #   metaclass will be `Type`).
    #
    #   Thus we are using the two different meanings (`type` .vs. `Type`) of the underlying python `type` in
    #   a single asserttion.
    #


    #
    #   Python Types (as per Principle #1, fully spelled out).
    #
    #   NOTE:
    #       `ActualString` is a non-empty string.
    #       `EmptyString`  is the empty string.
    #
    #       Both `ActualString` and `EmptyString` are mapped to the underlying Python type `str`
    #
    #   NOTE:
    #       In the code below we don't really need `EmptyString` so it is commented out.
    #       (however is left in comments for anyone reading the code to explain other concepts).
    #
    Module       = Python_System.__class__      #   Same type as python `import` normally creates.
    ActualString = Python_BuiltIn.str           #   `ActualString` is an alias for `str`
   #EmptyString  = Python_BuiltIn.str           #   `EmptyString`  is an alias for `str`
    Type         = Python_BuiltIn.type


    #
    #   Python Functions (as per Principle #1, fully spelled out).
    #
    #   NOTES:
    #
    is_instance = Python_BuiltIn.isinstance         #   `is_instance` is an alias for python builtin `isinstance`
    length      = Python_BuiltIn.len                #   `length` is an alias for python builtin `len`
    type        = Python_BuiltIn.type               #   See comment above on `Type` .vs. `type`.


    #
    #   Python values
    #
    python_debug_mode = Python_BuiltIn.__debug__


    #
    #   iterate_values
    #
    #       As per principle #1, we always spell out words.
    #
    #       `iterate_values` is an alias for `dict.itervalues`
    #
    iterate_values = dict.itervalues


    #
    #   next_method
    #       Access the `.__next__` method of an iterator
    #
    #       (Deals with the annoyance of `.__next__` method named `.next` in python 2.0, but `.__next__` in python 3.0)
    #
    if is_python_2:
        def next_method(iterator):
            return iterator.next
    else:
        def next_method(iterator):
            return iterator.__next__

    #
    #   fact_is_actual_string(s)        - Assert the fact that `s` is an `ActualString`
    #   fact_is_class(classification)   - Assert the fact that `classification` is a class
    #                                     (i.e.: It's metaclass is an instance of `Type`)
    #   fact_is_none(v)                 - Assert the fact that `v` is `none`
    #   fact_is_not_none(v)             - Assert the fact that `v` is not `none`
    #
    #   NOTE:
    #       "Facts" are only called in assertions (so they are removed when not in python debug mode).
    #
    #       Internally facts do their *own* assertions & always return `true`.
    #
    #           1.  Only these [internal] assertions trigger when the fact fails;
    #
    #           2.  [the initial] assert never triggers -- only the internal ones do.
    #
    #       Again, the purpose of [the initial] assert, is so they are removed when not in debug mode.
    #
    if python_debug_mode:
        def fact_is_actual_string(s):
            assert type(s) is ActualString
            assert length(s) > 0

            return true


        def fact_is_class(classification)
            assert is_instance(type(classification), Type)

            return true


        def fact_is_class_or_function(v)
            assert is_instance(type(v), ((Function, Type)) )

            return true


        def fact_is_none(v):
            assert v is none

            return true


        def fact_is_not_none(v)
            assert v is not none

            return true


    #
    #   NOTE:
    #       In the sentences below "instance" means "an instance of a class".
    #
    #       Example:
    #
    #               class Color(object):
    #                   __slots__ = ((
    #                       'name',                 #   ActualString
    #                   ))
    #
    #                   def __init__(self, name):
    #                       self.name = name
    #
    #
    #               def create_Color(name):
    #                   assert (type(name) is ActualString) and (length(name) > 0)
    #
    #                   return Color(name)
    #
    #
    #               purple = create_Color('Purple')
    #
    #       Here we say "`purple` is an instance of class `Color`".
    #
    #       However, we often just shorten it to say "`purple` is an instance".
    #


    #
    #   Principle #4
    #       An instance should have an easy to understand lifecycle as possible.
    #
    #       The easist lifecycle to understand is for an instance to be fully immutable:
    #
    #           1.  Thus it only has one state: it exists & all it's members are immutable.
    #
    #       The more states an object has, the more prone it is to having bugs.
    #


    #
    #   Principle #5
    #       Unexpected states in an instance of an object's lifecycle, means, these are often not unit tested
    #       (since they are unexpected).
    #
    #       Thus, it is very important to avoid unexpected state in the instance of an object.
    #


    #
    #   Principle #6:
    #       Never call constructors directly (based on principles #4 & #5 mostly):
    #
    #       There is always a wrapper funtion named "create_Name" (in rare cases the "create" function is named
    #       slightly differently than "create_*" -- for example see `capture_standard_output` below).
    #
    #       This achieves two things:
    #
    #           1.  It is  *WAY* easier to modify & refactor the code later.
    #
    #           2.  Any exceptions are thrown in the the wrapper function.
    #
    #               Thus, if an exception occurs, then the exception is thrown *BEFORE* the `instance` is created
    #               (and likewise the instance does need to be destroyed if an exception is thrown).
    #
    #       See "ConstructorError.txt" for a longer explanation of why it is such a problem for exceptions to occur in
    #       constructors.
    #


    #
    #   create_module                                   -   Create a new module
    #       name                 : ActualString
    #       classes_or_functions : Zero or more classes or functions
    #       named_values         : Zero or more values (each as a name/value pair).
    #
    #   This wrapper does two things:
    #
    #       1.  Never call a constructor (Principle #4).
    #
    #       2.  Verify the first argument is an `InternedActualString`.
    #
    def create_module(name, *classes_or_functions, **values):
        assert fact_is_actual_string(name)

        module = Python_Module_Type(name)


        #
        #   provide
        #
        #       NOTE #1:
        #           "provide" is chosen as a verb to mean:
        #
        #               Provide X to Y, if Y doesn't already have an X.
        #
        #           In other words, "provide" is an English word for the python `dict.setdefault` method.
        #
        #   NOTE #2:
        #       Here we are setting the variable `provide` to a binding of `module.__dict__` to the
        #       python method `dict.setdefault`
        #
        #       In other words, provide, has the same meaning as:
        #
        #           def provide(k, v)
        #               return module.__dict__.setdefault(k, v)
        #
        #       Both versions (the one below and the example above) will call `dict.setdefault` with three
        #       parameters and are equivalent to:
        #
        #               dict.setdefault(module.__dict__, k, v)
        #
        #
        provide = module.__dict__.setdefault


        #
        #   insert_into_module
        #
        #       Implements an "insert" into `module.__dict__` (using `provide` which is bound to `module.__dict__`).
        #
        #       It uses `provide` to attempt the insert -- if the result comes back DIFFERENT than the value
        #        we attempted to insert -- then no insert happen (due to a previous value in the mapping).
        #
        #       In this case we throw an exception to indicate the insert failed.
        #
        def insert_into_module(k, v):
            assert fact_is_actual_string(k)

            previous = provide(v.__name__, v)

            if previous is not v:
                RAISE_module_member_already_exists(module, name, previous, value)


        if length(classes_or_functions) > 0:
            for v in classes_or_functions:
                assert fact_is_class_or_function(v)

                insert_into_module(k, v)

        if length(values):
            for [k, v] in values.itervalues():
                insert_into_module(k, v)


    #
    #   create_StringOutput     -   Create a string to catpure file output.
    #
    #   This wrapper does two things:
    #
    #       1.  Never call a constructor (Principle #4).
    #
    #       2.  Can only be called with zero parameters.
    #
    #           This avoids the ability to pass in one parameter to the underlyign type `Python_StringIO_Type`.
    #
    #   NOTE:
    #       Uses the underlying `Python_StringIO_Type` which does *BOTH* input & output.
    #
    #       However the intent is that `create_StringOutput` is used to create a `StringOutput`, which is only
    #       used for string output.
    #
    Python_StringIO = __import__('StringIO'   if is_python_2 else   'io')


    Python_StringIO_Type = Python_StringIO.StringIO


    def create_StringOutput()
        return Python_StringIO_Type()


    #
    #   Simple Context Lifecycles:
    #       simple_context_lifecycle_changing   - The context is changing states
    #       simple_context_lifecycle_created    - The context has been created.
    #       simple_context_lifecycle_entered    - The context has been entered.
    #       simple_context_lifecycle_exited     - The context has been exited.
    #       simple_context_lifecycle_closed     - The context has been closed.
    #
    #   NOTE:
    #       These `lifecycles` are only used for assertions in context handlers ...
    #
    #       Context handlers are quite complex to write properly (especially handling exceptions in the exception
    #       function of a context hander).
    #
    #       Hence the importance of [debugging] lifecycle management for context handlers.
    #
    class SimpleContextLifecycle(Object):
        __slots__ = ((
            'name',                     #   ActualString

            'changing',                 #   Boolean
            'created',                  #   Boolean
            'entered',                  #   Boolean
            'exited',                   #   Boolean
            'closed',                   #   Boolean
        ))


        def __init__(
                self, name,

                changing = false,
                created  = false,
                entered  = false,
                exited   = false,
                closed   = false,
        ):
            self.name = name

            self.changing = changing
            self.created  = created
            self.entered  = entered
            self.exited   = exited
            self.closed   = closed


        def __repr__(self):
            return '<SimpleContextLifecycle {}>'.format(self.name)


    def create_SimpleContextLifecycle(
            self, name,

            changing = false,
            created  = false,
            entered  = false,
            exited   = false,
            closed   = false,
    ):
        assert fact_is_actual_string(name)

        return SimpleContextLifecycle(
                intern_string(name),

                changing = changing,
                created  = created,
                entered  = entered,
                exited   = exited,
                closed   = closed,
            )


    simple_context_lifecycle_changing = create_SimpleContextLifecycle('changing', created = true)
    simple_context_lifecycle_created  = create_SimpleContextLifecycle('created',  created = true)
    simple_context_lifecycle_entered  = create_SimpleContextLifecycle('entered',  entered = true)
    simple_context_lifecycle_exited   = create_SimpleContextLifecycle('exited',   exited  = true)
    simple_context_lifecycle_closed   = create_SimpleContextLifecycle('closed',   closed  = true)


    if python_debug_mode:
        def fact_is_simple_context_lifecycle_created(v):
            assert v is simple_context_lifecycle_created

            return true


        def fact_is_simple_context_lifecycle_entered(v):
            assert v is simple_context_lifecycle_entered

            return true


        def fact_is_simple_context_lifecycle_exited(v):
            assert v is simple_context_lifecycle_exited

            return true



    #
    #   Get rid of the constructor, it is no longer neeed, since no more `SimpleContextLifeCycle` instances will be
    #   created.
    #
    #   NOTE:
    #       Functions like `create_SimpleContextLifecycle` are automatically reclaimed by python when funtion `module`
    #       exists -- but constructors need to be deleted by hand as below...
    #
    del Lifecycle.__init__


    #
    #   capture_standard_output     - Capture Standard output
    #
    #   NOTE:
    #       Here the "create" function is named "capture_standard_output".
    #
    #       (instead of "create_CaptureStandandOutput" since the [use of the internal class `CaptureStandardOutput` is not
    #       really relevant to the caller of this class.  In fact the class `CaptureStandardOutput` only exists for one
    #       purpose -- to be the return type of `capture_standard_output`).
    #
    class CaptureStandardOutput(object):
        __slots__ = ((
            'lifecycle',                    #   SimpleClntext_Lifecycle
            'f',                            #   None | Python_StringIO
            'previous_standard_output',     #   None | ?
        ))


        def __init__(self, f):
            self.lifecycle                = simple_context_lifecycle_changing
            self.f                        = f
            self.previous_standard_output = none
            self.lifecycle                = simple_context_lifecycle_created


        def __enter__(self, f):
            assert fact_is_simple_context_lifecycle_created(self.lifecycle)
            assert fact_is_not_none                        (self.f)
            assert fact_is_none                            (self.previous_standard_output)

            self.lifecycle = simple_context_lifecycle_changing

            self.previous_standard_output = Python_System.stdout

            Python_System.stdout = f

            self.lifecycle = simple_context_lifecycle_entered

            return self


        def __exit__(self, e_type, e, e_traceback):
            assert fact_is_simple_context_lifecycle_entered(self.lifecycle)
            assert fact_is_not_none                        (self.f)
            assert fact_is_not_none                        (self.previous_standard_output)

            self.lifecycle = simple_context_lifecycle_changing

            Python_System.stdout = self.previous_standard_output

            self.previous_standard_output = none

            self.lifecycle = simple_context_lifecycle_exited


        def finish(self, f):
            assert fact_is_simple_context_lifecycle_exited(self.lifecycle)
            assert fact_is_not_none                       (self.f)
            assert fact_is_none                           (self.previous_standard_output)

            self.lifecycle = simple_context_lifecycle_changing

            result = self.f.getvalue()

            self.f         = none
            self.lifecycle = simple_context_lifecycle_closed

            return result


    def capture_standard_output():
        f = create_StringOutput()

        return CaptureStandardOutput(f)


    #
    #   PREPARE_name_error
    #
    #   NOTE:
    #       This is the create function for `NameError`.
    #
    #       It is *NOT* called `create_NameError` since it takes different arguments
    #       than the `NameError` constructor does.
    #
    if python_debug_mode:
        def PREPARE_name_error(message, *arguments):
            name_error = NameError(value.format(*arguments)   if length(arguments) else   value)

            return name_error


    #
    #   RAISE_already_exists
    #
    if python_debug_mode:
        def RAISE_already_exists(name, previous, value):
            name_error = PREPARE_name_error(
                             "{} already exists ({!r}): can't insert {!r} also", name, previous, value),
                         )

            #
            #   Since the next line will appear in stack traces, make it look prettier by using 'name_error'
            #   (to make the line shorter & more readable)
            #
            raise name_error


    #
    #   share(f)                                -- Share a function globally
    #   share(name, value, [name, value] ...)   -- Share a list of values globally
    #
    provide_global = globals().setdefault


    if python_debug_mode:
        def insert_global(name, v):
            previous = provide_global(name, v)

            if previous is not v:
                raise_already_exists(name, previous, v)
    else:
        insert_global = provide_global


    def share(f, *arguments):
        if length(arguments) is 0:
            if f.__class__ is Function:
                name = intern_string(function_name(f))

                return insert_global(
                           name,
                           Function(
                               function_code(f),
                               function_scope(f),
                               name,
                               function_defaults(f),
                               function_closure(f),
                           ),
                       )

            return insert_global(intern_string(function_name(f), f))

        argument_iterator = iterate(arguments)
        next_argument     = next_method(argument_iterator)

        insert(intern_string(f), next_argument())

        for name in argument_iterator:
            insert(intern_string(name), next_argument())




def test_vision():
    Python_System    = __import__('sys')

    if is_python_2:
        StringIO = __import__('io').StringIO
    else:
        StringIO = __import__('StringIO').StringIO
