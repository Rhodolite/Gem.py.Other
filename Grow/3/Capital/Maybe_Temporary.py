#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Maybe_Temporary - "Maybe" Temporary Interface (Only used internally to help create other unique objects).
#
#   See long explnation below.
#


#
#   interface Maybe_Temporary_0
#       attribute
#           definitively_not_temporary : Native_Boolean
#
class TRAIT_Maybe_Temporary_0(object):
    __slots__ = (())


   #@virtual
    definitively_not_temporary = True


#
#   LONG EXPLANATION
#
#       A temporary key is not unique, as multiple threads may create the same temporary key at [approximately] the
#       same time.
#
#       Temporary key's are used to help create unique objects:
#
#           1)  A cache exists with unique objects; a mixture of:
#
#               1A)     Unique objects (of the proper class)
#
#               1B)     "Unique" Temporary keys (that need to be transformed to the proper class).
#
#                       NOTE:
#                           Temporary Keys are *NOT* unique; but the temporary keys that are in the cache are unique
#                           with respect to the other keys that are in the cache.
#
#                           For example, there may be two or more threads with the non-unique temporary key with a
#                           value of "X".
#
#                           However only one of these "X" temporary keys will be in the cache, this temporary
#                           key with a value of "X" is "unique with respect to the other keys that are in the cache"
#                           (there are no other keys in the cache with a value of "X").
#
#           2)  OPTIONAL to lookup a unique object:
#
#               2A)     Do a lookup of the unique object with a native key.
#
#               2B)     This might succeed, in which case, we don't need to create a temporary key.
#
#                       NOTE:   The lookup *might* return a temporary key, in which case we
#                               still need to transform it to the proper class.
#
#           3)  To create a unique object:
#
#               3A)     We create a temporary key (may not be unique).
#
#               3B)     We use the python built-in `.setdefault` to simultaneously lookup & insert
#                       the temporary key.
#
#               3C)     We get back a "unique" object (this is what `.setdefault` guarentees).
#
#                       "Unique with respect to other keys that are in the cache" -- (see fuller explanation
#                       of this in 1B above).
#
#               3D)     If neccessary, we transform the temporary key to the class of the unique objects.
#
#
#       Example (this example shows Steps 1 & 3 from above, skips the optional step 2 from above to make the example
#       simplier):
#
#
#           class Temporary_String_Key(
#                   str,
#                   TRAIT_Maybe_Temporary_0,
#           ):
#               __slots__ = (())
#
#               #
#               #   Interface Maybe_Temporary
#               #
#              #@replace
#               definitively_not_temporary = False
#
#
#           def create_temporary_string_key(s):
#               return Temporary_String_Key(s)
#
#
#           class Unique_String_Example(
#                   str,
#                   TRAIT_String,
#                   TRAIT_Maybe_Temporary_0,
#           ):
#               __slots__ = (())
#
#               #
#               #   Inherited from `TRAIT_Maybe_Temporary_0`:
#               #
#               #       `definitively_not_temporary = True`
#               #
#              #definitively_not_temporary = True
#
#
#
#           #
#           #   Step #1 (as explained above).
#           #
#           #   The type of `cache` is:
#           #
#           #       Map { Temporary_String_Key | Unique_String_Example }
#           #        of { Temporary_String_Key | Unique_String_Example }
#           #
#           cache = {}
#
#
#           @creator
#           def conjure_unique_string_example(s):
#               #
#               #   Step #3A (as explained above).
#               #
#               #   `k` is not unique -- the same key can exist in multiple threads.
#               #
#               k = create_temporary_string_key(s)
#
#               #
#               #   Step #3B & #3C (as explained above).
#               #
#               #   `r` will be "unique" due to how `.setdefault` works.
#               #
#               #       "Unique with respect to other keys that are in the cache" -- (see fuller explanation of this in
#               #       1B above).
#               #
#               #   Also the python built in `.setdefault` is thread safe.
#               #
#               r = cache.setdefault(k, k)
#
#               #
#               #   Step #3D (as explained above) is rest of this function.
#               #
#               #   Has `r` already been transformed, and is no longer a temporary key?
#               #
#               if r.definitively_not_temporary:
#                   return r
#
#               #
#               #   Transform `r` to a `Unique_String_Example`.
#               #
#               #   This is thread safe -- multiple threads can do the same transformation at
#               #   [approximately] the same time:
#               #
#               #       1)  One thread will do the actual transformation (i.e.: transform a `String_Key_1` to a
#               #           `Unique_String_Example);
#               #
#               #       2)  All the other threads will do a "null operation"  (i.e.: the null operation of
#               #           transforming a `Unique_String_Example` to the same `Unique_String_Example`).
#               #
#               r.__class__ = Unique_String_Example
#
#               #
#               #   After the transformation `r` had *BETTER* be known to have definitively transformed.
#               #
#               assert r.definitively_not_temporary
#
#               return r
#
#
#       The above example will guarentee that all instances of type `Unique_String_Example`
#       (created with `conjure_unique_string_example`) are unique.
#


#
#   USAGE:
#
#       #
#       #   NOTE:
#       #       This is named `.definitively_not_temporary` instead of `.not_temporary` to *STRONLY* indicate that the
#       #       test may be *INCONCLUSIVE* when returning false.
#       #
#       #       I.E.:  A value of false means the key is not definitively known to have transformed; but it *MAY* have
#       #              have transformed (although we don't know it yet)!
#       #
#       #       If the above test returns false; then at any moment (including right after the above test), `v` may be
#       #       transformed by another thread, and no longer be a temporary key.
#       #
#       #       Thus, if `v.definitively_not_temporary` returns true:
#       #
#       #           1.  We can say "v was a temporary key; but has been transformed, and is no longer a temporary key".
#       #
#       #       However, if `v.definitively_not_temporary` returns false:
#       #
#       #           2.  We *CANNOT* say that "v has not transformed and is still a temporary key"
#       #               (it may have been transformed to a non-temporary key by another thread since our test);
#       #
#       #           3.  All we can say is that "v was a temporary key, may or may not have transformed, and may or
#       #               may not still be a temporary key".
#       #
#       v.definitively_not_temporary        #   Test if `v` is definitively known to not be a temporary key.
#
