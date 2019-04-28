#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


default_alias_version         = '1'
default_argument_version      = '1'
default_comprehension_version = '1'
default_context_version       = 1
default_except_version        = '1'
default_expression_version    = '1'
default_index_version         = '1'
default_name_version          = 3
default_operator_version      = '1'
default_parameter_version     = '1'
default_statement_version     = 2
default_symbol_version        = 2
default_target_version        = 3


if default_context_version:
    #
    #   Using `Tree_Context`:
    #
    #       Maximum allowed name   version is 2.
    #       Maximum allowed target version is 2.
    #
#   assert default_name_version   <= 2
#   assert default_target_version <= 2
    pass
else:
    #
    #   NOT Using `Tree_Context`:
    #
    #       Minimum allowed name   version is 3.
    #       Symbols must be used.
    #       Minimum allowed target version is 3.
    #
    assert default_name_version   >= 3
    assert default_symbol_version == 1
    assert default_target_version >= 3


if default_symbol_version == 0:
    #
    #   NOT using symbols:
    #
    #       Name   version must be 1.
    #       Target version must be 1.
    #
    assert default_name_version   == 1
    assert default_target_version == 1
else:
    #
    #   Using symbols:
    #
    #       Minumum allowed name   version is 2.
    #       Minumum allowed target version is 3.
    #
    assert default_name_version   >= 2
    assert default_target_version >= 2


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
        'operator_version',             #   NativeString
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
        return arrange('<Tree_Globals {!r} {!r} {!r} {} {!r} {!r} {!r} {} {!r} {!r} {} {} {}>',
                       self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
                       self.except_version, self.expression_version, self.index_version, self.name_version,
                       self.operator_version, self.parameter_version, self.statement_version, self.symbol_version,
                       self.target_version)

    def trace_tree_globals(self):
        trace('Tree_Globals: alias={!r} argument={!r} comprehension={!r} context={} except={!r} ...',
              self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
              self.except_version)
        trace('... expression={!r} index={!r} name={} statement={} operator={!r} parameter={!r} symbol={}',
              self.expression_version, self.index_version, self.name_version, self.statement_version,
              self.operator_version, self.parameter_version, self.symbol_version)
        trace('... target={}',
              self.target_version)


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
    assert fact_is_full_native_string (operator_version)
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
                   alias_version         = default_alias_version,
                   argument_version      = default_argument_version,
                   comprehension_version = default_comprehension_version,
                   context_version       = default_context_version,
                   except_version        = default_except_version,
                   expression_version    = default_expression_version,
                   index_version         = default_index_version,
                   name_version          = default_name_version,
                   operator_version      = default_operator_version,
                   parameter_version     = default_parameter_version,
                   statement_version     = default_statement_version,
                   symbol_version        = default_symbol_version,
                   target_version        = default_target_version,
               )
