#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Z.BuiltIn                       import  Python_Integer
from    Z.BuiltIn                       import  Python_List
from    Z.BuiltIn                       import  Python_Tuple
from    Z.BuiltIn                       import  python_type
from    Z.BuiltIn                       import  python_debug_mode
from    Z.Core                          import  arrange
from    Z.Core                          import  trace
from    Z.Python_AbstractSyntaxTree     import  Python_AbstractSyntaxTree_Import
from    Z.Python_AbstractSyntaxTree     import  Python_AbstractSyntaxTree_Module
from    Z.Python_AbstractSyntaxTree     import  Python_AbstractSyntaxTree_Expression
from    Z.Python_AbstractSyntaxTree     import  python__compile__to__python_abstract_syntax_tree


if python_debug_mode:
    from    Z.Fact                      import  fact_is_python_integer
    from    Z.Fact                      import  fact_is_python_list


class SyntaxTree_Module(object):
    __slots__ = ((
        'body',                         #   SyntaxTree_*
    ))


    def __init__(self, body):
        self.body = body


    def __repr__(self):
        return arrange('<SyntaxTree.Module {!r}>', self.body)


class Tuple_of_SyntaxTree_Alias(Python_Tuple):
    __slots__ = (())


    def __repr__(self):
        return arrange('<Tuple_of_SyntaxTree_Alias {}>',
                       ' '.join(repr(v)   for v in self))


class Tuple_of_SyntaxTree_Any(Python_Tuple):
    __slots__ = (())


    def __repr__(self):
        return arrange('<Tuple_of_SyntaxTree_Any {}>',
                       ' '.join(repr(v)   for v in self))


def convert_expression(self):
    return None


def convert_import(self):
    if 0:
        #
        #   Copy this disabled code into a new convert method, to trace the
        #   attributes & fields and help write the new method.
        #
        #   This code was used to write most of the convert methods in this file :)
        #
        function_name = 'convert_import'

        trace('{}._attributes: {}', function_name, self._attributes)
        trace('{}.lineno:      {}', function_name, self.lineno)
        trace('{}.col_offset:  {}', function_name, self.col_offset)

        trace('{}._fields:     {}', function_name, self._fields)
        trace('{}.names:       {}', function_name, self.names)

    assert self._attributes == (('lineno', 'col_offset'))
    assert self._fields     == (('names',))

    assert fact_is_python_integer(self.lineno)
    assert fact_is_python_integer(self.col_offset)
    assert fact_is_python_list   (self.names)


#
#   convert_list_of_any - 
#
#       Convert a `Python_List` of `Python_AbstractSyntaxTree_*`
#       (i.e.: `list` of `_ast.AST`) instance to a `Tuple_of_SyntaxTree_Any`
#       instance.
#
def convert_list_of_any(sequence):
    assert type(sequence) is Python_List

    return Tuple_of_SyntaxTree_Any(convert(v)   for v in sequence)



#
#   convert_module
#
#       Convert a `Python_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`)
#       instance to a `SyntaxTree_Module` instance.
#
assert Python_AbstractSyntaxTree_Module._attributes == (())
assert Python_AbstractSyntaxTree_Module._fields     == (('body',))


def convert_module(self):
    assert type(self) is Python_AbstractSyntaxTree_Module

    return SyntaxTree_Module(
               convert_list_of_any(self.body),
           )


#
#   map__Python_AbstractSyntaxTree_Type__to__psuedo_method : Map { Python_AbstractSyntaxTree_* : Function }
#
#       This maps a `Python_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) type to a
#       "convert" psuedo method (actually to a function).
#
map__Python_AbstractSyntaxTree_Type__to__convert_pseudo_method = {
        Python_AbstractSyntaxTree_Expression : convert_expression,
        Python_AbstractSyntaxTree_Import     : convert_import,
    }


#
#   convert
#
#       Convert a `Python_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) instance
#       to a `SyntaxTree_*` instance.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert(v):
    convert_pseudo_method = map__Python_AbstractSyntaxTree_Type__to__convert_pseudo_method[python_type(v)]

    return convert_pseudo_method(v)



#
#   compile_to_syntax_tree - Compile `source` to a `SyntaxTree_Module` instance.
#
#       Two step process:
#
#       1.  Compile `source` to a `Python_AbstractSyntaxTree_Module (i.e.: `_ast.Module`) instance.
#
#       2.  Convert the `Python_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`) instance to
#           a `SyntaxTree_Module` instance.
#
def compile_to_syntax_tree(source, filename):
    python_abstract_syntax_tree = python__compile__to__python_abstract_syntax_tree(source, filename)

    return convert_module(python_abstract_syntax_tree)
