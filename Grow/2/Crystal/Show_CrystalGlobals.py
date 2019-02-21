#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   NOTE:
    #       This is called after "Crystal/Wipe_CrystalGlobals.py" hence quite a few globals
    #       are missing ...
    #
    #       ... Therefore ... we need to "refind" them from "python".
    #
    #   NOTE:
    #       The only exception is `trace` which is purposefully not wiped, when this module
    #       is going to be loaded.
    #
    import  sys     as  Python_System


    is_python_2    = (Python_System.version_info.major is 2)
    Python_BuiltIn = __import__('__builtin__'  if is_python_2 else   'builtins')


    #
    #   Python Functions
    #
    python_globals     = Python_BuiltIn.globals
    python_sorted_list = Python_BuiltIn.sorted


    #
    #   Python Values
    #
    python_debug_mode = Python_BuiltIn.__debug__


    #
    #   crystal_global
    #
    crystal_global = python_globals()


    #
    #   Show crystal_global
    #
    assert python_debug_mode

    trace('===  Dump of crystal_global  ===')

    sorted_keys = python_sorted_list(crystal_global)

    for k in sorted_keys:
        v = crystal_global[k]

        trace('{!r}: {!r}', k, v)

    trace('===  Done  ===')
