#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Python_MutableMap Methods
    #
    python__mutable_map__find    = Python_MutableMap.__getitem__
    python__mutable_map__lookup  = Python_MutableMap.get
    python__mutable_map__provide = Python_MutableMap.setdefault
    python__mutable_map__stash   = Python_MutableMap.__setitem__


    #
    #   mutable_map_with_named_keys__find
    #
    if python_debug_mode:
        def mutable_map_with_named_keys__find(self, k):
            assert fact_is_interned_actual_string(k)

            return python__mutable_map__find(self, k)
    else:
        mutable_map_with_named_keys__find = python__mutable_map__find


    #
    #   mutable_map_with_named_keys__items_sorted_by_key
    #
    def mutable_map_with_named_keys__items_sorted_by_key(self):
        value = self.__getitem__

        for k in python_sorted_list(self):
            assert fact_is_interned_actual_string(k)

            yield (( k, value(k) ))


    #
    #   mutable_map_with_named_keys__lookup
    #
    if python_debug_mode:
        def mutable_map_with_named_keys__lookup(self, k):
            assert fact_is_interned_actual_string(k)

            return python__mutable_map__lookup(self, k)
    else:
        mutable_map_with_named_keys__lookup = python__mutable_map__lookup


    #
    #   mutable_map_with_named_keys__provide
    #
    if python_debug_mode:
        def mutable_map_with_named_keys__provide(self, k, v):
            assert fact_is_interned_actual_string(k)

            return python__mutable_map__provide(self, k, v)
    else:
        mutable_map_with_named_keys__provide = python__mutable_map__provide


    #
    #   mutable_map_with_named_keys__stash
    #
    if python_debug_mode:
        def mutable_map_with_named_keys__stash(self, k, v):
            assert fact_is_interned_actual_string(k)

            python__mutable_map__stash(self, k, v)
    else:
        mutable_map_with_named_keys__stash = python__mutable_map__stash


    #
    #   Unique_Named_MutableMap_with_NamedKeys
    #
    @share
    class Unique_Named_MutableMap_with_NamedKeys(Build_Unique_Named_MutableMap):
        __slots__ = (())


        __getitem__ = mutable_map_with_named_keys__find
        __setitem__ = mutable_map_with_named_keys__stash


        def __repr__(self):
            return arrange('<Unique_Named_MutableMap_with_NamedKeys` {!r}>', self.name)


        find                = mutable_map_with_named_keys__find
        items_sorted_by_key = mutable_map_with_named_keys__items_sorted_by_key
        lookup              = mutable_map_with_named_keys__lookup
        provide             = mutable_map_with_named_keys__provide
        stash               = mutable_map_with_named_keys__stash


    @share
    @creator
    def create__Unique_Named_MutableMap_with_NamedKeys(name):
        assert fact_is_actual_string(name)

        interned_name = intern_python_string(name)

        return create_unique_named_mutable_map(Unique_Named_MutableMap_with_NamedKeys, interned_name)
