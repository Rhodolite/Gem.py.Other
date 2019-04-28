#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  creator


version = 7


alias_version         = '1'
argument_version      = '1'
comprehension_version = '1'
context_version       = 1
except_version        = '1'
expression_version    = '1'
index_version         = '1'
name_version          = 1
operator_version      = 1
parameter_version     = '1'
statement_version     = 1
symbol_version        = 0
target_version        = 1


#
#   Version 2 & 3:
#
#       Introduce Enumerations
#
#           2:  Enumeration for `Tree_Context`
#           3:  Enumeration for `Tree_Operator`
#
if version >= 2:
    context_version = 2

if version >= 3:
    operator_version = 2


#
#   Version 4 & 5:
#
#       Introduce Symbols
#
#           4:  `Tree_Name`   uses symbols
#           5:  `Tree_Target` uses symbols (affects `Tree_Attribute`).
#
if version >= 4:
    name_version   = 2
    symbol_version = 1

if version >= 5:
    target_version = 2


#
#   Version 6:
#
#       No longer use contexts
#
#           6:  `Tree_Name`    no longer uses contexts.
#
#           7:  `Tree_Target`  no longer uses contexts (affects `Tree_Attribute`, `Tree_{List,Tuple}_Expression`, and
#                              `Tree_Subscript`).
#
if version >= 6:
    name_version = 3

if version >= 7:
    context_version = 0     #   Nothing uses contexts anymore ... so totally disable tree contexts
    target_version  = 3


if context_version:
    #
    #   Using `Tree_Context`:
    #
    #       Maximum allowed name   version is 2.
    #       Maximum allowed target version is 2.
    #
#   assert name_version   <= 2
#   assert target_version <= 2
    pass
else:
    #
    #   NOT Using `Tree_Context`:
    #
    #       Minimum allowed name   version is 3.
    #       Symbols must be used.
    #       Minimum allowed target version is 3.
    #
    assert name_version   >= 3
    assert symbol_version == 1
    assert target_version >= 3


if symbol_version == 0:
    #
    #   NOT using symbols:
    #
    #       Name   version must be 1.
    #       Target version must be 1.
    #
    assert name_version   == 1
    assert target_version == 1
else:
    #
    #   Using symbols:
    #
    #       Minumum allowed name   version is 2.
    #
    assert name_version   >= 2


#
#   Z.Tree.Global - Globals to affect the creation of `Tree_*` classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Tree_Globals - Globals to affect the creation of `Tree_*` classes.
#
class Tree_Globals(object):
    __slots__ = ((
        'alias_version',                #   NativeString
        'argument_version',             #   NativeString
        'comprehension_version',        #   NativeString
        'context_version',              #   SubstantialInteger
        'except_version',               #   NativeString
        'expression_version',           #   NativeString
        'index_version',                #   NativeString
        'name_version',                 #   PositiveInteger
        'operator_version',             #   PositiveInteger
        'parameter_version',            #   NativeString
        'statement_version',            #   PositiveInteger
        'symbol_version',               #   SubstantialInteger
        'target_version',               #   PositiveInteger
    ))


    def __init__(
            self, alias_version, argument_version, comprehension_version, context_version,
            except_version, expression_version, index_version, name_version,
            operator_version, parameter_version, statement_version, symbol_version,
            target_version,
    ):
        self.alias_version         = alias_version
        self.argument_version      = argument_version
        self.comprehension_version = comprehension_version
        self.context_version       = context_version
        self.except_version        = except_version
        self.index_version         = index_version
        self.name_version          = name_version
        self.operator_version      = operator_version
        self.parameter_version     = parameter_version
        self.expression_version    = expression_version
        self.statement_version     = statement_version
        self.symbol_version        = symbol_version
        self.target_version        = target_version


    def __repr__(self):
        return arrange('<Tree_Globals {!r} {!r} {!r} {} {!r} {!r} {!r} {} {} {!r} {} {} {}>',
                       self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
                       self.except_version, self.expression_version, self.index_version, self.name_version,
                       self.operator_version, self.parameter_version, self.statement_version, self.symbol_version,
                       self.target_version)

    def trace_tree_globals(self):
        trace('Tree_Globals: alias={!r} argument={!r} comprehension={!r} context={} except={!r} ...',
              self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
              self.except_version)
        trace('... expression={!r} index={!r} name={} statement={} operator={} parameter={!r} symbol={}',
              self.expression_version, self.index_version, self.name_version, self.statement_version,
              self.operator_version, self.parameter_version, self.symbol_version)
        trace('... target={}',
              self.target_version)


@creator
def create_tree_globals(
        alias_version, argument_version, comprehension_version, context_version,
        except_version, expression_version, index_version, name_version,
        operator_version, parameter_version, statement_version, symbol_version,
        target_version,
):
    assert fact_is_full_native_string (alias_version)
    assert fact_is_full_native_string (argument_version)
    assert fact_is_full_native_string (comprehension_version)
    assert fact_is_substantial_integer(context_version)
    assert fact_is_full_native_string (except_version)
    assert fact_is_full_native_string (index_version)
    assert fact_is_positive_integer   (name_version)
    assert fact_is_positive_integer   (operator_version)
    assert fact_is_full_native_string (parameter_version)
    assert fact_is_full_native_string (expression_version)
    assert fact_is_positive_integer   (statement_version)
    assert fact_is_substantial_integer(symbol_version)
    assert fact_is_positive_integer   (target_version)

    r = Tree_Globals(
            alias_version, argument_version, comprehension_version, context_version, except_version,
            expression_version, index_version, name_version,
            operator_version, parameter_version, statement_version, symbol_version,
            target_version,
        )

   #trace('Tree Globals: {}', r)
    r.trace_tree_globals()

    return r


tree_globals = create_tree_globals(
                   alias_version         = alias_version,
                   argument_version      = argument_version,
                   comprehension_version = comprehension_version,
                   context_version       = context_version,
                   except_version        = except_version,
                   expression_version    = expression_version,
                   index_version         = index_version,
                   name_version          = name_version,
                   operator_version      = operator_version,
                   parameter_version     = parameter_version,
                   statement_version     = statement_version,
                   symbol_version        = symbol_version,
                   target_version        = target_version,
               )
