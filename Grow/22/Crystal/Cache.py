#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    cache_names   = create__Unique_Named_MutableMap_with_NamedKeys('cache-names')
    lookup_cache  = cache_names.get
    provide_cache = cache_names.setdefault


    @share
    def create_cache(name):
        assert fact_is_actual_string(name)
        assert lookup_cache(name) is none

        interned_name = intern_python_string(name)

        return provide_cache(
                interned_name,
                create__Unique_Named_MutableMap_with_NamedKeys(interned_name),
            )


    xyz = create_cache('xyz')

    xyz.stash(intern_python_string('hi'), 'there')


    def dump_cache(f, cache):
        f.line('===  {}  ===', cache.name)

        with f.indent_2():
            for [k, v] in cache.items_sorted_by_key():
                f.line('{!r}: {!r}', k, v)

        f.line('===  Done  ===', cache.name)


    def dump_cache_to_string(cache):
        with create_StringOutput() as f:
            dump_cache(f, cache)

        return f.result


    def print_cache(use_cache = none):
        if use_cache is none:
            trace('Total caches: {}', length(cache_names))

            for [name, cache] in cache_names.items_sorted_by_key():
                trace('  {}: {}', name, length(cache))

            return

        cache = cache_names[use_cache]

        for s in dump_cache_to_string(cache).splitlines():
            trace(s)


    print_cache('xyz')
