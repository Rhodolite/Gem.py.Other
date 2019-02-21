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
#       NOTE:
#           `f` must have an [internal] name of `"module"`.
#
#           This is to avoid "polluting" the global namespace:
#
#           The [annotation] function `module` returns itself as a value, and then python [re-saves]
#           this value under the [internal] name of `f` (i.e.: `"module"`).
#
#           In other words, nothing changes in the global namespace.
#
#       Example:
#
#           @module
#           def module():
#               seven = 3 + 4
#
#               create_module("Example", seven = seven)
#
#       First, this will create a temporary wrapper function [internally] named `"module"`.
#
#       Then due to the annotation `@module` it will execute:
#
#               globals()["module"] = (
#                       module                  #   The [annotation] function named `"module"`.
#                           (module)            #   The temporary wrapper funtion [internally] named `"module"`.
#                   )
#
#   In other words, by using `@module` multiple times in a single python file -- a whole bunch of sub-modules can be
#   "combined" into a single python file, and be "seen" as multiple modules from other python files.
#
#   The purpose of combining a whole bunch of "sub-modules" into a single file, is for release purposes, to avoid clutter.
#
#   It allows the source code to be organized well (with multiple modules), but released as a single file.
#
def module(f):
    f()

    return module


#
#   trace mode
#
tracing = True



#
#   Imports
#
from    sys         import  modules     as  python_modules
from    os.path     import  basename    as  path_basename


#
#   Aliases for python builtins
#
length        = len
none          = None
Object        = object
static_method = staticmethod


#
#   PREPARE_value_error
#       Prepare a ValueError to throw as an exception.
#
#       A future version will emulate python 3 exception chaining, in python 2 (for now, keeping the code sinple, so
#       not doing that yet).
#
def PREPARE_value_error(message, *arguments):
    if length(arguments) > 0:
        message = message.format(*arguments)

    return ValueError(message)


#
#   ---     Nested functions    ---
#
#   Summary:
#
#       Nested functions are closures in python -- a topic we will cover later.
#
#       For now, just a brief point, that is quite proper to call a python nested function
#       a "local variable", since, in fact, that is precisly what they are in python.
#
#   Detailed Example:
#
#       Here we show that the function "example" has a local variable named `f`.
#
#           def example():
#               f = 1
#               print("f is: {}".format(f))
#       
#               def f(): return 2
#               print("f is: {}; and returns {}".format(f, f()))
#       
#               f = 3
#               print("f is: {}".format(f))
#       
#               def f(): return 4
#               print("f is: {}; and returns {}".format(f, f()))
#
#               g = f
#               print("g is: {}; and returns {}".format(g, g()))
#       
#               f = 5
#               print("f is: {}".format(f))
#
#           example()
#
#       Will output:
#
#           f is: 1
#           f is: <function example.<locals>.f at 0x222222222220>; and returns 2
#           f is: 3
#           f is: <function example.<locals>.f at 0x444444444440>; and returns 4
#           g is: <function example.<locals>.f at 0x444444444440>; and returns 4
#           f is: 5
#
#       Showing that `f` is clearly a [local] variable of `example`, and that, like any variable can be assigned to
#       multiple times (three times it is assigned an integer, and two times it is assign the two [different] functions
#       [internally] named `"f"`).
#
#       It is thus proper to say both functions [internally] named `"f"` (the one that returns `2`, and the one
#       that returns `4`) are nested functions of function `example`.
#
#       It is likewise proper to refer to the nested functions [internally] named `"f"` as local variables of function
#       `example`.
#
#       Finally notice that the local variable `g` is set to the function [internally] named `"f"`.  There is thus a
#       distinction between the variable a function is stored (`g`) in & it's [internal] name ("f").  In most cases
#       (as in `f` above) the variable a function is stored in & it's [internal] name are the same.
#
#

#
#   execute(f)      - An annotation to execute a function & store it's name in `f.__name__` (the same name as the
#                     internal function name of `f`).
#
#       Example of using `execute` as an annotation ("annotation" means with the `@` to "annotate" a function).
#    
#           @execute
#           def seven():
#               def factorial(v):
#                   if v == 1:
#                       return 1
#                   
#                   return v * (v - 1)
#
#               return factorial(3) + 1
#    
#       Means:
#           First, this will create a temporary wrapper function named `seven`.
#    
#           Then due to the annotation `@execute` it will execute `globals()["seven"] = seven()`.
#    
#           The temporary wrapper function `seven` has a return value of `7`.
#    
#           Thus the following will be executed:
#    
#               globals()["seven"] = 7
#
#           Since `globals()` will return the module's scope, then it will create a [module] variable
#           named `seven` with value `7`.
#    
#           The advantage of the temporary wrapper function `seven` above, is that it can create temporary variables
#           (such as `factorial` and `v` local variables above) to calculate the return value.
#    
#           [Finally the temporary wrapper function `seven` is thrown away, including all unused variables.
#           Above the locals variables `factorial` and `v` are thrown away, as they are no longer used; likewise
#           the function [internally] named `factorial` is thrown away, as it is no longer used].
#
def execute(f):
    return f()


#
#   Debugging
#
#       trace_prefix = "% Crystal.py: '
#
@execute
def trace_prefix():
    path = __file__

    if path.endswith('.pyc'):
        path = path[:-1]
    
    return format('% {}: '.format(path_basename(__file__)))


def trace(message, *arguments):
    if length(arguments) > 0:
        message = message.format(*arguments)

    print(trace_prefix + message)


#
#   NOTE:
#       "Vision.x" is in the code generator language (which is *temporarily* parsable by python).
#
#       Hence, we are not going to treat "Vision.x" as a normal python program, but instead do
#       some serious modifications to the python environment to make it the code generator language.
#

#
#   NOTE for the future:
#       These lessons will also be builing a parser for "Vision.x", at which point the language will become
#       a lot cleaner & easier to understand (as it will no longer be parsed by python).


#
#   Step 1:  Modifying the python environment for "Vision.x"
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

            missing_copyright = PREPARE_value_error("cannot find copyright in {!r}", path)

            raise missing_copyright


        @property
        def copyright(self):
            assert self.copyright_value is none

            copyright_value = self.extract_copyright(main_path)

            trace('Extracted copyright from {!r}', main_path)
            trace('Copyright: {!r}', copyright_value)

    main_module.X = Grow()
