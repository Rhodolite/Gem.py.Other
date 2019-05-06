#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Global - Globals to affect the "Z" Parser.
#


version = 13


alias_version         = 1
argument_version      = 1
comprehension_version = '1'
context_version       = 1
except_version        = '1'
expression_version    = '1'
index_version         = '1'
module_name_version   = 0
name_version          = 1
operator_version      = 1
parameter_version     = '1'
statement_version     = 1
symbol_version        = 0
target_version        = 1


#
#   Version 2 & 3: Introduce Enumerations
#
#       2:  Enumeration for `Tree_Context`
#       3:  Enumeration for `Tree_Operator`
#
if version >= 2:
    context_version = 2

if version >= 3:
    operator_version = 2


#
#   Version 4: Split `Tree_Alias_Clause` into `Tree_{Module,Symbol}_Alias_Implementation`.
#
if version >= 4:
    alias_version = 2


#
#   Version 5 & 6: Introduce `Parser_Symbol`
#
#       5:  `Tree_Keyword_Argument` uses symbols.
#
#       6:  `Tree_Name`             uses symbols.
#
#       7:  `Tree_Target`           uses symbols (affects `Tree_Attribute`).
#
#
if version >= 5:
    argument_version = 2                #   `Tree_Keyword_Argument` uses symbols.
    symbol_version   = 1                #   Enable `Parser_Symbol`

if version >= 6:
    name_version = 2                    #   `Tree_Name` uses symbols.

if version >= 7:
    target_version = 2                  #   `Tree_Target` uses symbols (affects `Tree_Attribute`).


#
#   Version 8: Introduce `Parser_Module_Name`
#
if version >= 8:
    alias_version       = 3     #   `Tree_Module_Alias_Implementation.name` is a `Parser_Module_Name`.
    module_name_version = 1
    symbol_version      = 2     #   Symbol version 2 implements `Parser_Module_Name`


#
#   Version 9 & 10: Improve `Tree_{Module,Symbol}_Alias_Implementation`.
#
#       9: `Tree_{Module,Symbol}_Alias_Implementation` use `Parser_Symbol` and `Parser_Symbol_0`.
#
#       10: Only use `Tree_{Module,Symbol}_Alias.as_name` when it has a value.
#
if version >= 9:
    alias_version  = 4          #   `Tree_{Module,Symbol}_Alias` use `Parser_Symbol` and `Parser_Symbol_0`.
    symbol_version = 3          #   Symbol version 3 implements `Parser_Symbol_0`

if version >= 10:
    alias_version       = 5     #   Only use `Tree_{Module,Symbol}_Alias.as_name` when it has a value.
    module_name_version = 2     #   `Parser_Module_Name_With_Dot` implements `Tree_Module_Alias`.
    symbol_version      = 4     #   Symbol version 4 implements `Tree_{Module,Symbol}_Alias`.


#
#   Version 11 & 12: No longer use contexts
#
#       11: `Tree_Name`    no longer uses contexts.
#
#       12: `Tree_Target`  no longer uses contexts (affects `Tree_Attribute`, `Tree_{List,Tuple}_Expression`, and
#                          `Tree_Subscript`).
#
if version >= 11:
    name_version = 3

if version >= 12:
    context_version = 0     #   Nothing uses contexts anymore ... so totally disable tree contexts
    target_version  = 3


#
#   Version 13
#
#       Add `Tree_Suite` & `Tree_Suite_0`
#
if version >= 13:
    statement_version = 2 


#
#   Imports
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer


#
#   Parser_Globals - Globals to affect the "Z" Parser.
#
class Parser_Globals(object):
    __slots__ = ((
        'alias_version',                #   PositiveInteger
        'argument_version',             #   PositiveInteger
        'comprehension_version',        #   NativeString
        'context_version',              #   SubstantialInteger
        'except_version',               #   NativeString
        'expression_version',           #   NativeString
        'index_version',                #   NativeString
        'module_name_version',          #   SubstantialInteger
        'name_version',                 #   PositiveInteger
        'operator_version',             #   PositiveInteger
        'parameter_version',            #   NativeString
        'statement_version',            #   PositiveInteger
        'symbol_version',               #   SubstantialInteger
        'target_version',               #   PositiveInteger
    ))


    def __init__(
            self, alias_version, argument_version, comprehension_version, context_version,
            except_version, expression_version, index_version, module_name_version,
            name_version, operator_version, parameter_version, statement_version,
            symbol_version, target_version,
    ):
        self.alias_version         = alias_version
        self.argument_version      = argument_version
        self.comprehension_version = comprehension_version
        self.context_version       = context_version
        self.except_version        = except_version
        self.index_version         = index_version
        self.module_name_version   = module_name_version
        self.name_version          = name_version
        self.operator_version      = operator_version
        self.parameter_version     = parameter_version
        self.expression_version    = expression_version
        self.statement_version     = statement_version
        self.symbol_version        = symbol_version
        self.target_version        = target_version


    def __repr__(self):
        return arrange('<Parser_Globals {} {} {!r} {} {!r} {!r} {!r} {} {} {} {!r} {} {} {}>',
                       self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
                       self.except_version, self.expression_version, self.index_version, self.module_name_version,
                       self.name_version, self.operator_version, self.parameter_version, self.statement_version,
                       self.symbol_version, self.target_version)

    def trace_parser_globals(self):
        trace('Parser_Globals: alias={} argument={} comprehension={!r} context={} except={!r} ...',
              self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
              self.except_version)
        trace('... expression={!r} index={!r} module_name={} name={} statement={} operator={} parameter={!r}',
              self.expression_version, self.index_version, module_name_version,
              self.name_version, self.statement_version, self.operator_version, self.parameter_version)
        trace('... symbol={} target={}',
              self.symbol_version, self.target_version)


@creator
def create_parser_globals(
        alias_version, argument_version, comprehension_version, context_version,
        except_version, expression_version, index_version, module_name_version,
        name_version, operator_version, parameter_version, statement_version,
        symbol_version, target_version,
):
    assert fact_is_positive_integer   (alias_version)
    assert fact_is_positive_integer   (argument_version)
    assert fact_is_full_native_string (comprehension_version)
    assert fact_is_substantial_integer(context_version)
    assert fact_is_full_native_string (except_version)
    assert fact_is_full_native_string (index_version)
    assert fact_is_substantial_integer(module_name_version)
    assert fact_is_positive_integer   (name_version)
    assert fact_is_positive_integer   (operator_version)
    assert fact_is_full_native_string (parameter_version)
    assert fact_is_full_native_string (expression_version)
    assert fact_is_positive_integer   (statement_version)
    assert fact_is_substantial_integer(symbol_version)
    assert fact_is_positive_integer   (target_version)

    r = Parser_Globals(
            alias_version, argument_version, comprehension_version, context_version,
            except_version, expression_version, index_version, module_name_version, 
            name_version, operator_version, parameter_version, statement_version,
            symbol_version, target_version,
        )

   #trace('Parser Globals: {}', r)
    r.trace_parser_globals()

    return r


parser_globals = create_parser_globals(
                   alias_version         = alias_version,
                   argument_version      = argument_version,
                   comprehension_version = comprehension_version,
                   context_version       = context_version,
                   except_version        = except_version,
                   expression_version    = expression_version,
                   index_version         = index_version,
                   module_name_version   = module_name_version,
                   name_version          = name_version,
                   operator_version      = operator_version,
                   parameter_version     = parameter_version,
                   statement_version     = statement_version,
                   symbol_version        = symbol_version,
                   target_version        = target_version,
               )
