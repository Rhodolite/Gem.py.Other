#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


default_alias_version         = '1'
default_argument_version      = '1'
default_comprehension_version = '1'
default_context_version       = '1'
default_except_version        = '1'
default_expression_version    = '1'
default_index_version         = '1'
default_name_version          = '2'
default_operator_version      = '1'
default_parameter_version     = '1'
default_statement_version     = '1'
default_target_version        = '1'


#
#   Z.Tree.Global - Globals to affect the creation of `Tree_*` classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   Tree_Globals - Globals to affect the creation of `Tree_*` classes.
#
class Tree_Globals(object):
    __slots__ = ((
        'alias_version',                #   NativeString
        'argument_version',             #   NativeString
        'comprehension_version',        #   NativeString
        'context_version',              #   NativeString
        'except_version',               #   NativeString
        'expression_version',           #   NativeString
        'index_version',                #   NativeString
        'name_version',                 #   NativeString
        'operator_version',             #   NativeString
        'parameter_version',            #   NativeString
        'statement_version',            #   NativeString
        'target_version',               #   NativeString
    ))


    def __init__(
            self, alias_version, argument_version, comprehension_version, context_version,
            except_version, expression_version, index_version, name_version,
            operator_version, parameter_version, statement_version, target_version,
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
        self.target_version        = target_version


    def __repr__(self):
        return arrange('<Tree_Globals {!r} {!r} {!r} {!r} {!r} {!r} {!r} {!r} {!r} {!r} {!r} {!r}>',
                       self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
                       self.except_version, self.expression_version, self.index_version, self.name_version,
                       self.operator_version, self.parameter_version, self.statement_version, self.target_version)

    def trace_tree_globals(self):
        trace('Tree_Globals: alias={!r} argument={!r} comprehension={!r} context={!r} except={!r} ...',
              self.alias_version, self.argument_version, self.comprehension_version, self.context_version,
              self.except_version)
        trace('... expression={!r} index={!r} name={!r} statement={!r} operator={!r} parameter={!r} target={!r}',
              self.expression_version, self.index_version, self.name_version, self.statement_version,
              self.operator_version, self.parameter_version, self.target_version)


def create_tree_globals(
        alias_version, argument_version, comprehension_version, context_version,
        except_version, expression_version, index_version, name_version,
        operator_version, parameter_version, statement_version, target_version,
):
    assert fact_is_full_native_string(alias_version)
    assert fact_is_full_native_string(argument_version)
    assert fact_is_full_native_string(comprehension_version)
    assert fact_is_full_native_string(context_version)
    assert fact_is_full_native_string(except_version)
    assert fact_is_full_native_string(index_version)
    assert fact_is_full_native_string(name_version)
    assert fact_is_full_native_string(operator_version)
    assert fact_is_full_native_string(parameter_version)
    assert fact_is_full_native_string(expression_version)
    assert fact_is_full_native_string(statement_version)
    assert fact_is_full_native_string(target_version)

    r = Tree_Globals(
            alias_version, argument_version, comprehension_version, context_version, except_version,
            expression_version, index_version, name_version,
            operator_version, parameter_version, statement_version, target_version,
        )

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
                   target_version        = default_target_version,
               )
