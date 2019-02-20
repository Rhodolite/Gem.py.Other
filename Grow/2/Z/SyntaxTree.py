#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace
from    Z.BuiltIn                       import  python_debug_mode
from    Z.BuiltIn                       import  Python_Integer
from    Z.BuiltIn                       import  python_length
from    Z.BuiltIn                       import  Python_List
from    Z.BuiltIn                       import  python_none
from    Z.BuiltIn                       import  Python_NoneType
from    Z.BuiltIn                       import  Python_Object
from    Z.BuiltIn                       import  Python_String
from    Z.BuiltIn                       import  Python_Tuple
from    Z.BuiltIn                       import  python_type
from    Z.Fact                          import  fact_is_empty_python_list
from    Z.Fact                          import  fact_is_full_python_string
from    Z.Fact                          import  fact_is_python_none
from    Z.Fact                          import  fact_is_python_string
from    Z.Python_AbstractSyntaxTree     import  python__compile__to__python_abstract_syntax_tree
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Alias
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Attribute
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Call
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Expression
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Import
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Load
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Module
from    Z.Python_AbstractSyntaxTree     import  PythonTree_Name
from    Z.Python_AbstractSyntaxTree     import  PythonTree_String
from    Z.TreeContext                   import  TreeContext


if python_debug_mode:
    from    Z.Fact                      import  fact_is_python_integer
    from    Z.Fact                      import  fact_is_full_exact_python_list
    from    Z.Python_AbstractSyntaxTree import  fact_is_python_abstract_syntax_tree_alias
    from    Z.Python_AbstractSyntaxTree import  fact_is_python_abstract_syntax_tree_load
    from    Z.Python_AbstractSyntaxTree import  fact_is_python_abstract_syntax_tree_module


#
#   Empty Tuple of SyntaxTree
#
class EmptyTuple_of_SyntaxTree(Python_Tuple):
    __slots__ = (())


    def __repr__(self):
        return '<EmptyTuple_of_SyntaxTree>'


empty_tuple_of_syntax_tree = EmptyTuple_of_SyntaxTree()


#
#   SyntaxTree_Attribute
#
class SyntaxTree_Attribute(Python_Object):
    __slots__ = ((
        'value',                        #   Token_Name
        'attribute',                    #   Python_String
        'context',                      #   TreeContext
    ))


    def __init__(self, value, attribute, context):
        self.value     = value
        self.attribute = attribute
        self.context   = context


    def __repr__(self):
        return arrange('<SyntaxTree.Attribute {!r}.{} {}>', self.value, self.attribute, self.context)


#
#   SyntaxTree_Call
#
class SyntaxTree_Call(Python_Object):
    __slots__ = ((
        'function',                     #   SyntaxTree_*
        'arguments',                    #   Python_String
        'keywords',                     #   EmptyTuple
        'star_arguments',               #   SyntaxTree_None
        'keywords_arguments',           #   SyntaxTree_None
    ))


    def __init__(self, function, arguments, keywords, star_arguments, keywords_arguments):
        self.function           = function
        self.arguments          = arguments
        self.keywords           = keywords
        self.star_arguments     = star_arguments
        self.keywords_arguments = keywords_arguments


    def __repr__(self):
        return arrange('<SyntaxTree.call {!r} {} {}>',
                       self.function, self.arguments, self.keywords, self.star_arguments, self.keywords_arguments)


#
#   SyntaxTree_Import_1
#
class SyntaxTree_Import_1(Python_Object):
    __slots__ = ((
        'name_or_alias',                #   SyntaxTree_Alias | Token_Name
    ))


    def __init__(self, name_or_alias):
        self.name_or_alias = name_or_alias


    def __repr__(self):
        return arrange('<SyntaxTree.Import_1 {!r}>', self.name_or_alias)


#
#   SyntaxTree_ExpressionStatement
#
class SyntaxTree_ExpressionStatement(Python_Object):
    __slots__ = ((
        'value',                        #   SyntaxTree_*
    ))


    def __init__(self, value):
        self.value = value


    def __repr__(self):
        return arrange('<SyntaxTree.ExpressionStatement {!r}>', self.value)


#
#   SyntaxTree_Module
#
class SyntaxTree_Module(Python_Object):
    __slots__ = ((
        'body',                         #   SyntaxTree_*
    ))


    def __init__(self, body):
        self.body = body


    def __repr__(self):
        return arrange('<SyntaxTree.Module {!r}>', self.body)


#
#   SyntaxTree_Name
#
class SyntaxTree_Name(Python_Object):
    __slots__ = ((
        'id',                           #   Token_Name
        'context',                      #   TreeContext
    ))


    def __init__(self, id, context):
        self.id      = id
        self.context = context


    def __repr__(self):
        return arrange('<SyntaxTree.Name {!r} {}>', self.id, self.context)


#
#   SyntaxTree_None
#
class SyntaxTree_None(Python_Object):
    __slots__ = (())


    def __bool__(self):
        return False


    def __repr__(self):
        return '<SyntaxTree.None>'


syntax_tree_none = SyntaxTree_None()


#
#   SyntaxTree_String
#
class SyntaxTree_String(Python_Object):
    __slots__ = ((
        's',                            #   Python_String
    ))


    def __init__(self, s):
        self.s = s


    def __repr__(self):
        return arrange('<SyntaxTree.String {!r}>', self.s)


#
#   Token_Name
#
class Token_Name(Python_String):
    __slots__ = (())


    def __repr__(self):
        return arrange('<Token_Name {}>', self)


#
#   Tuple_of_SyntaxTree_Alias
#
class Tuple_of_SyntaxTree_Alias(Python_Tuple):
    __slots__ = (())


    def __repr__(self):
        return arrange('<Tuple_of_SyntaxTree_Alias {}>',
                       ' '.join(repr(v)   for v in self))


#
#   Tuple_of_SyntaxTree_Any
#
class Tuple_of_SyntaxTree_Any(Python_Tuple):
    __slots__ = (())


    def __repr__(self):
        return arrange('<Tuple_of_SyntaxTree_Any {}>',
                       ' '.join(repr(v)   for v in self))


#
#   convert_alias
#
#       Convert an instance of `PythonTree_Alias`
#       (i.e.: `_ast.alias`) to a `Token_Name` instance.
#
#   NOTE:
#       Currently, can only handle non-aliased names (i.e.: does not have a `as`
#       clause in the `from` or `import` statement).
#
#       Does, not yet, handle aliased names (i.e.: has a `as` claues in the
#       `from` or `import` statement).
#
assert PythonTree_Alias._attributes == (())
assert PythonTree_Alias._fields     == (('name', 'asname'))


def convert_alias(self):
    as_name = self.asname

    if as_name is python_none:
        return Token_Name(self.name)

    assert 0, "convert_alias: incomplete to handle `.as_name` that is not none"


#
#   convert_attribute
#
#       Convert an instance of `PythonTree_Attribute`
#       (i.e.: `_ast.Expr`) to a `SyntaxTree_Attribute`
#
assert PythonTree_Attribute._attributes == (('lineno', 'col_offset'))
assert PythonTree_Attribute._fields     == (('value', 'attr', 'ctx'))


def convert_attribute(self):
    assert fact_is_full_python_string(self.attr)

    return SyntaxTree_Attribute(
               convert(self.value),
               self.attr,
               convert_context(self.ctx),
          )


#
#   convert_call
#
#       Convert an instance of `PythonTree_Call`
#       (i.e.: `_ast.Expr`) to a `SyntaxTree_Call`
#
assert PythonTree_Call._attributes == (('lineno', 'col_offset'))
assert PythonTree_Call._fields     == (('func', 'args', 'keywords', 'starargs', 'kwargs'))


def convert_call(self):
    if 7:
        #
        #   Copy this disabled code into a new convert method, to trace the
        #   attributes & fields and help write the new method.
        #
        #   This code was used to write most of the convert methods in this file :)
        #
        function_name = 'convert_call'

        trace('{}._attributes: {}', function_name, self._attributes)
        trace('{}.lineno       {}', function_name, self.lineno)
        trace('{}.col_offset   {}', function_name, self.col_offset)

        trace('{}._fields:     {}', function_name, self._fields)
        trace('{}.func:        {}', function_name, self.func)
        trace('{}.args:        {}', function_name, self.args)
        trace('{}.keywords:    {}', function_name, self.keywords)
        trace('{}.starargs:    {}', function_name, self.starargs)
        trace('{}.kwargs:      {}', function_name, self.kwargs)

    return SyntaxTree_Call(
               convert                 (self.func),
               convert_list_of_any     (self.args),
               convert_list_of_keywords(self.keywords),
               convert                 (self.starargs),
               convert                 (self.kwargs),
           )


#
#   convert_context
#
#       Convert a context to a `TreeContext` enumerator.
#
#       The following conversions are preformed:
#
#           python type          converted to
#           -----------          ------------
#           PythonTree_Delete    TreeContext.delete
#           PythonTree_Load      TreeContext.load
#           PythonTree_Store     TreeContext.store
#
assert PythonTree_Load._attributes == (())
assert PythonTree_Load._fields     == (())


map__PythonTree_Type__to__TreeContext = {
        PythonTree_Load : TreeContext.load,
    }


def convert_context(self):
    return map__PythonTree_Type__to__TreeContext[python_type(self)]




#
#   convert_expression
#
#       Convert an instance of `PythonTree_Expression`
#       (i.e.: `_ast.Expr`) to an instance of `SyntaxTree_Expression`
#
assert PythonTree_Expression._attributes == (('lineno', 'col_offset'))
assert PythonTree_Expression._fields     == (('value',))


def convert_expression(self):
    return SyntaxTree_ExpressionStatement(
               convert(self.value),
           )


#
#   convert_import
#
#       Convert an instance of `PythonTree_Import` (i.e.: `_ast.Import`) to an instance of `SyntaxTree_Import_1`
#
#   NOTE:
#       Currently, Can only handle a single `.names` (i.e.: an import of a single module), does not yet handle
#       multiple `.names` (i.e.: an import of multiple modules).
#
assert PythonTree_Import._attributes == (('lineno', 'col_offset'))
assert PythonTree_Import._fields     == (('names',))


def convert_import(self):
    assert fact_is_python_integer        (self.lineno)
    assert fact_is_python_integer        (self.col_offset)
    assert fact_is_full_exact_python_list(self.names)

    names = self.names

    if python_length(names) == 1:
        return SyntaxTree_Import_1(convert_alias(names[0]))

    assert 0, 'convert_import: incomplete: import of multiple modulesin'


#
#   convert_list_of_any
#
#       Convert an instance of `Python_List` of `PythonTree_*` (i.e.: `list` of `_ast.AST`) to an instance of
#       `Tuple_of_SyntaxTree_Any`
#
def convert_list_of_any(sequence):
    assert fact_is_full_exact_python_list(sequence)

    return Tuple_of_SyntaxTree_Any(convert(v)   for v in sequence)



#
#   convert_list_of_keywords
#
#       Convert an EMPTY instance of `list` of ? to `empty_tuple_of_syntax_tree`.
#
#   CURRENT:
#       Currently can only handle an empty list.
#
#   FUTURE:
#       Will handle a full list.
#
def convert_list_of_keywords(sequence):
    assert fact_is_empty_python_list(sequence)

    return empty_tuple_of_syntax_tree



#
#   convert_module
#
#       Convert a `PythonTree_Module` (i.e.: `_ast.Module`)
#       instance to a `SyntaxTree_Module` instance.
#
assert PythonTree_Module._attributes == (())
assert PythonTree_Module._fields     == (('body',))


def convert_module(self):
    assert fact_is_python_abstract_syntax_tree_module(self)

    return SyntaxTree_Module(
               convert_list_of_any(self.body),
           )


#
#   convert_name
#
#       Convert an instance of `PythonTree_Import`
#       (i.e.: `_ast.Import`) to an instance of `SyntaxTree_Import_1`
#
#   NOTE:
#       Can only handle a single `.names` (i.e.: an import of a single
#       module), does not yet handle multiple `.names` (i.e.: an import of
#       multiple modules).
#
assert PythonTree_Name._attributes == (('lineno', 'col_offset'))
assert PythonTree_Name._fields     == (('id', 'ctx'))


def convert_name(self):
    assert fact_is_full_python_string(self.id)

    return SyntaxTree_Name(self.id, convert_context(self.ctx))



def convert_none(self):
    assert fact_is_python_none(self)

    return syntax_tree_none



#
#   convert_string
#
#       Convert an instance of `PythonTree_String` (i.e.: `_ast.Str`) to
#       an instance of `SyntaxTree_String`.
#
#assert PythonTree_String._attributes == (('lineno', 'col_offset'))
#assert PythonTree_String._fields     == (('func', 'args', 'keywords', 'starargs', 'kwargs'))


def convert_string(self):
    if 7:
        #
        #   Copy this disabled code into a new convert method, to trace the
        #   attributes & fields and help write the new method.
        #
        #   This code was used to write most of the convert methods in this file :)
        #
        function_name = 'convert_string'

        trace('{}._attributes: {}', function_name, self._attributes)
        trace('{}.lineno       {}', function_name, self.lineno)
        trace('{}.col_offset   {}', function_name, self.col_offset)

        trace('{}._fields:     {}', function_name, self._fields)
        trace('{}.s:           {!r}', function_name, self.s)

    assert fact_is_python_string(self.s)

    return SyntaxTree_String(self.s)


#
#   map__PythonTree_Type__to__psuedo_method : Map { PythonTree_* : Function }
#
#       This maps a `PythonTree_*` (i.e.: `_ast.AST`) type to a
#       "convert" psuedo method (actually to a function).
#
map__PythonTree_Type__to__convert_pseudo_method = {
        Python_NoneType       : convert_none,
        PythonTree_Attribute  : convert_attribute,
        PythonTree_Call       : convert_call,
        PythonTree_Expression : convert_expression,
        PythonTree_Import     : convert_import,
        PythonTree_Name       : convert_name,
        PythonTree_String     : convert_string,
    }


#
#   convert
#
#       Convert a `PythonTree_*` (i.e.: `_ast.AST`) instance
#       to a `SyntaxTree_*` instance.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert(v):
    convert_pseudo_method = map__PythonTree_Type__to__convert_pseudo_method[python_type(v)]

    return convert_pseudo_method(v)



#
#   compile_to_syntax_tree - Compile `source` to a `SyntaxTree_Module` instance.
#
#       Two step process:
#
#       1.  Compile `source` to a `PythonTree_Module (i.e.: `_ast.Module`) instance.
#
#       2.  Convert the `PythonTree_Module` (i.e.: `_ast.Module`) instance to
#           a `SyntaxTree_Module` instance.
#
def compile_to_syntax_tree(source, filename):
    python_abstract_syntax_tree = python__compile__to__python_abstract_syntax_tree(source, filename)

    return convert_module(python_abstract_syntax_tree)
