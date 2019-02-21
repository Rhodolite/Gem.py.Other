#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    CrystalGlobals.__eq__   = operator_equal__by_identity
    CrystalGlobals.__ne__   = operator_not_equal__by_identity
    CrystalGlobals.__hash__ = python_hash__by_identity


    sorted_keys = python_sorted_list(crystal_global)

    for k in sorted_keys:
        interned_k = intern_python_string(k)

        if interned_k is not k:
            v = pop_crystal_global(k)

            if is_python_string(v):
                v = intern_python_string(v)

            crystal_global[k] = v
            continue

        v = crystal_global[k]

        if is_python_string(v):
            crystal_global[k] = intern_python_string(v)
