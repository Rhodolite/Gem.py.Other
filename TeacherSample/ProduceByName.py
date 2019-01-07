#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   produce_find_lookup_verify_by_name_functions(type_name, Meta)
#       type_name   - used for error message to indentify the type
#
#       Managed a Map { String } of Meta
#
#       - Returns the following functions:
#
#           find_by_name            - Find the cached item; throw an exception if not found.
#           lookup_by_name          - Lookup the cached item; return None if not found.
#           story_by_name           - Store an a Meta
#           verify_unique_by_name   - Verify the name has not already been created; throw expection if it has
#           zap                     - clear the cache (used for unit testing)
#
def produce_find_lookup_verify_by_name_functions(type_name, Meta):
    #
    #   Map { name } of *
    #
    cache          = {}
    lookup_by_name = cache.get
    store_by_name  = cache.__setitem__
    zap            = cache.clear


    def find_by_name(name):
        assert (type(name) is str) and (len(name) > 0)

        result = lookup_by_name(name)

        if result is None:
            print('cache: {}'.format(cache))
            raise ValueError('Failed to find a {} named {!r}'.format(type_name, name))

        return result


    def verify_unique_by_name(name):
        if lookup_by_name(name) is not None:
            raise ValueError(
                    'Attempt to create {} with duplicate name {!r} (already exists: {})'.format(
                        type_name,
                        name,
                        lookup_by_name(name),
                    ),
                )


    return [find_by_name, lookup_by_name, store_by_name, verify_unique_by_name, zap]


#
#   Exports
#
__all__ = ((
    'produce_find_lookup_verify_by_name_functions',
))
