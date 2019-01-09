#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   When enabled, prints the following:
    #
    #       % Crystal.py: ===  Example of `.__repr__`  ====
    #       % Crystal.py:                       Crystal: <CrystalModule>
    #       % Crystal.py:                Crystal.Z_Mode: <CrystalSubmodule 'Crystal.Z_Mode'>
    #       % Crystal.py:              Crystal.__name__: Crystal
    #       % Crystal.py:          python_type(Crystal): <class 'Crystal.CrystalModule'>
    #       % Crystal.py: python_type(Crystal).__name__: CrystalModule
    #       % Crystal.py:                crystal_global: <CrystalGlobals>
    #       % Crystal.py: ===  Done  ====
    #
    #   It is mainly left here, to show what `.__repr__` returns for `Crystal` and `Crystal.Z_Mode`
    #
    import  Crystal

    trace('===  Example of `.__repr__`  ====')
    trace('                      Crystal: {}', Crystal)
    trace('               Crystal.Z_Mode: {}', Crystal.Z_Mode)
    trace('             Crystal.__name__: {}', Crystal.__name__)
    trace('         python_type(Crystal): {}', python_type(Crystal))
    trace('python_type(Crystal).__name__: {}', python_type(Crystal).__name__)
    trace('               crystal_global: {}', crystal_global)
    trace('===  Done  ====')
