#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Symbol - An identifier used in the Z parser.
#


#
#   The "proper" value for `conjure_symbol_version` is `3`.
#
#       Other possible values to use (only when reading the code to understand it):
#
#           1)  `conjure_symbol_version = 1`    --  Simple   version implemented in `Z.Parser.Conjure_Symbol_V1.py`
#
#           2)  `conjure_symbol_version = 2`    --  Produced version implemented in `Z.Parser.Conjure_Symbol_V2.py`
#
#           3)  `conjure_symbol_version = 3`    --  Produced version implemented in `Z.Parser.Conjure_Symbol_V3.py`
#
#       By:
#
#           Reading `*_V1` first, then 
#           reading `*_V2` second, and finally
#           reading `*_V3` ... it will make it a lot clearer how `*_V3` is implemented.
#
conjure_symbol_version = 3


from    Capital.Core                        import  FATAL
from    Capital.StringKey_V7                import  create_string_key
from    Capital.Temporary_Key               import  TRAIT_Temporary_Key
from    Capital.Produce_ConjureFullString   import  produce_conjure_full_name


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


class Symbol(
        str,
        TRAIT_Temporary_Key,
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        def __new__(Meta, s):
            FATAL("Symbol.operator new (`__new__`): A Symbol may not be created");


    if __debug__:
        def __init__(self, s):
            FATAL("Symbol.constructor (`__init__`): A Symbol may not be contructed");


    #__init__    - inherited from `str.__init__`        #   Not Used.
    #__new__     - inherited from `str.__new__`         #   Not Used.
    #__nonzero__ - inherited from `str.__nonzero__`     #   Returns `True`.


    #
    #   Public
    #
    is_symbol = True


    def __repr__(self):
        return '$' + self



if __debug__:
    #
    #   fact_is_symbol(v) - Assert the fact that `v` is a `Symbol`.
    #
    def fact_is_symbol(v):
        assert v.is_symbol

        return True


#
#   Import the version of `conjure_symbol` we want to use.
#
conjure_symbol_version = 3


if conjure_symbol_version == 1:
    from    Z.Parse.Conjure_Symbol_V1   import  conjure_symbol
elif conjure_symbol_version == 2:
    from    Z.Parse.Conjure_Symbol_V2   import  conjure_symbol
elif conjure_symbol_version == 3:
    from    Z.Parse.Conjure_Symbol_V3   import  conjure_symbol
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Parser/Symbol.py: unknown `conjure_symbol_versoin`: {}', conjure_symbol_version)
