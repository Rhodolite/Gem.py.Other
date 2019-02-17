#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    assert python_debug_mode

    sorted_keys = python_sorted_list(crystal_global)

    for k in sorted_keys:
        assert debug_test__is_interned_python_string(k)

        v = crystal_global[k]

        if is_python_string(v):
            if not debug_test__is_interned_python_string(v):
                value_error = PREPARE_ValueError(
                                    'crystal_global[{}] is not interened (value: {!r})',
                                    k, v
                                )

                raise value_error
