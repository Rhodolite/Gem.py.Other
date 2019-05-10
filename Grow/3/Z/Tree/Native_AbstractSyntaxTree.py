#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Native_AbstractSyntaxTree - Wrapper around python `_ast` module.
#


from    _ast                            import  PyCF_ONLY_AST   as  native__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE


if __debug__:
    from    Capital.Native_String       import  fact_is_some_native_string
    from    Capital.Native_String       import  fact_is_full_native_string


#
#   Export the names in `_ast` as full names
#
#       In `_ast_` classes that represent statements are in Capital Case:
#
#           _ast.ClassDef           Class Definition.         Example: `class a(object): pass`
#           _ast.Expr               Expression Statement.     Example: `a = b;`
#           _ast.FunctionDef        Function Definition.      Example: `def a(b): pass`
#           _ast.If                 If Statement.             Example: `if a: pass`
#           _ast.Import             Import Statement.         Example: `import a`
#           _ast.ImportFrom         From Statement.           Example: `from a import b`
#           _ast.Pass               Pass Statement.           Example: `pass`
#
#       Likewise, classes that represent expressions are in Capital Case:
#
#           _ast.Attribute       - Attribute expression.     Example: `a.b`
#           _ast.Call            - Function call.            Example: `a(b, c)`
#           _ast.Name            - A symbol (variable name)  Example: `a(b, c)`  -- Here `a`, `b`, and `c` are "Names".
#           _ast.Num             - A number.                 Example: `7`
#           _ast.Str             - A string.                 Example: `"seven"`
#
#       Some other classes are also in Capital Case:
#
#           _ast.Module          - A whole module (i.e.: a list of statements).
#
#       The following contexts (The `_ast.Name._ctx` member) are in Capital Case:
#
#           _ast.Delete          - Delete an attribute
#
#                                 Example:
#
#                                     #
#                                     #   `.b` and `c` are in a delete context.
#                                     #
#                                     del a.b, c
#
#           _ast.Load            - Query (get) an attribute
#
#                                 Example:
#
#                                     #
#                                     #   `a`, `c`, and `.d` are in query (get) context.
#                                     #
#                                     a.b = c.d
#
#           _ast.Param           - Parameter
#
#                                 Example:
#
#                                     #
#                                     #   `a` and `b` are in a parameter context.
#                                     #
#                                     def f(a, b = 2:
#                                         pass
#
#           _ast.Store           - Save an attribute
#
#                                 Example:
#
#                                     #
#                                     #   `.b` and `c` are in a store context.
#                                     #
#                                     [a.b, c] = [d, e.g]
#
#
#       The following "phrases" are in lower case:
#
#           _ast.alias           - An alias in a from or import statement.
#
#                                 Example:
#
#                                     import a, b as c                      #   `a` and `b as c` are "aliseas".
#                                     from d import e, g as h               #   `e` and `g as h` are "aliases".
#
#           _ast.arguments       - Parameters in a function definition.
#
#                                 Example:
#
#                                     def a(b, c): pass                     #   `b` and `c` are "parameters".
#
#                                 NOTE:
#                                     See "PARAMETERS .VS. ARGUMENTS" below for why `_ast.arguments` is really
#                                     parameters, not arguments.
#
#   NOTE:
#       `ast.Name` is mostly used in expressions as a symbol.
#
#       It can also be used as a parameter in a function definition
#
#       Example:
#
#           def f(a):                   #   `a` is a `_ast.Name` with a parameter context.
#               return a                #   `a` is a `_ast.Name` with a query (get) context.
#

#
#   RENAMING
#
#       The following renames of classes are done:
#
#           Name in _ast            Renamed to                              Reason
#           ------------            ----------                              ------
#           Num                     *_Number                                Spell out word.
#           Str                     *_String                                Spell out word.
#           Expression              *_ExpressionStatement                   Clarify this is really a "Statement".
#           Param                   *_Parameter_1                           Spell out word.  Add `_1_ to easily see
#                                                                               difference from `*_Parameters`.
#           alias                   *_Alias                                 Change to "Capital" case for consistency.
#           arguments               *_Parameters                            Rename to "Parameters" (see below).
#
#       Other renames of member are also done:
#
#           Name in _ast            Renamed to                              Reason
#           ------------            ----------                              ------
#           .asname                 .as_name                                Add "_" for clarity.
#           .attr                   .attribute                              Spell out word.
#           .col_offset             .column                                 Spell out word (also remove "_offset").
#           .ctx                    .context                                Spell out word.
#           .func                   .function                               Spell out word.
#           .kwargs                 .keyword_arguments                      Spell out word.
#           .lineno                 .line_number                            Spell out words.
#           .starargs               .star_arguments                         Spell out word.
#
#           Call     .args          Call              .arguments            Spell out word.
#           FuncDef  .args          FunctionDefinition.parameters           Rename to `.parameters`
#           Arguments.args          Parameters        .parameters           Rename to `.parameters`
#           Arguments.vararg        Parameters        .variable_parameter   Spell out words.
#           Arguments.kwarg         Parameters        .keyword_parameter    Spell out words.
#
#   See the next section for an explanation of why `arguments`, `.args`, `.vararg`, and `.kwarg` are all renamed from
#   "arguments" to "parameters".
#

#
#   PARAMETERS .VS. ARGUMENTS
#
#       Function are defined with parameters & called with arguments.
#
#       Example:
#
#           def f(a):
#               pass
#
#           f(7)
#
#       Here: `a` is a parameter, and `7` is an argument.
#
#       The Python grammer [mostly] follows this naming convention:
#
#           1)  https://docs.python.org/2/reference/grammar.html
#
#                   "funcdef: 'def' NAME parameters ':' suite"
#
#           2)  https://docs.python.org/3/reference/grammar.html
#
#                   "funcdef: 'def' NAME parameters ['->' test] ':' suite"
#
#       See also:
#
#           3)  https://en.wikipedia.org/wiki/Parameter_(computer_programming)
#
#                   "For example, if one defines the add subroutine as
#
#                       def add(x, y):
#                           return x + y
#
#                   then x, y are parameters, while if this is called as
#
#                       add(2, 3)
#
#                   then 2, 3 are the arguments."
#
#   HENCE
#
#       We rename `_ast.arguments` (which are function parameters) to `Tree_All_Parameters`.
#
#       Likewise we rename `_ast.FuncDef.args` (which are function parameters) to `Tree_FunctionDefinition.parameters`.
#
#   NOTE:
#
#       `_ast.arguments` (which as mentioned above are actually funtion parameters) has a `.args` member which are each
#       a `_ast.name` with a context of `_ast.Param`.
#
#       So even though `_ast.arguments` and `.args` members ... are oddly named "arguments", the "context" is properly
#       named a "parameter".
#

#
#   The following appears in `_ast_` but not in the following list:
#
#       `_ast.AST`              Base class of `alias`, `arguments`, `boolop`, `compop`, `comprehension`,
#                                             `excepthandler`, `expr`, `expr_context`, `keyword`, `mod`, `operator`,
#                                             `slice`, `stmt`, and `unaryop`.
#
#       `_ast.boolop`           Base class of `And`, and `Or`.
#
#       `_ast.cmpop`            Base class of `Eq`, `Gt`, `GtE`, `In`, `Is`, `IsNot`, `Lt`, `LtE`, `NotEq`,
#                                             and `NotIn`.
#
#       `_ast.expr`             Base class of `Attribute`, `BinOp`, `BoolOp`, `Call`, `Compare`, `Dict`, `DictComp`,
#                                             `GeneratorExp`, `IfExp`, `Lambda`, `List`, `ListComp`, `Name`, `Num`,
#                                             `Repr`, `Set`, `SetComp`, `Str`, `Subscript`, `Tuple`, `UnaryOp`,
#                                             and `Yield`.
#
#       `_ast.excepthandler`    Base class of `ExceptHandler`,
#
#       `_ast.expr_context`     Base class of `Del`, `Load`, `Param`, and `Store`.
#
#       `_ast.mod`              Base class of `Expression`, `Interactive`, `Module`, and `Suite`.
#
#       `_ast.keyword`          Unknown -- apparently not used in current implementation of `_ast`.
#
#       `_ast.operator`         Base class of `Add`, `BitAnd`, `BitOr`, `BitXor`, `Div`, `FloorDiv`, `LShift`, `Mod`,
#                                             `Mult`, `Pow`, `RShift`, and `Sub`.
#
#       `_ast.slice`            Base clase of `Ellipsis`, `ExtSlice`, `Index`, and `Slice`.
#
#       `_ast.stmt`             Base class of `Assert`, `Assign`, `AugAssign`, `AugLoad`, `AugStore`, `Break`,
#                                             `ClassDef`, `Continue`, `Delete`, `Exec`, `Expr`, `For`, `FunctionDef`,
#                                             `Global`, `If`, `Import`, `ImportFrom`, `Pass`, `Print`, `Raise`,
#                                             `Return`, `TryExcept`, `TryFinally`, `While`, and `With`.
#
#       `unaryop`               Base class of `Invert`, `Not`, `UAdd`, and `USub`.
#
#       `AugLoad`               *NOT* used in current implementation of `_ast`.
#
#       `AugStore`              *NOT* used in current implementation of `_ast`.
#
#   TODO:
#
#       `Expression',   -   mod
#       `Interactive`   -   mod
#       `Suite`         -   mod
#

from    _ast                            import (
            Add             as  Native_AbstractSyntaxTree_Add_Operator,
            alias           as  Native_AbstractSyntaxTree_Alias_Clause,
            And             as  Native_AbstractSyntaxTree_Logical_And_Operator,
            arguments       as  Native_AbstractSyntaxTree_All_Parameters,
            Assert          as  Native_AbstractSyntaxTree_Assert_Statement,
            Assign          as  Native_AbstractSyntaxTree_Assign_Statement,
            Attribute       as  Native_AbstractSyntaxTree_Attribute_Expression,
            AugAssign       as  Native_AbstractSyntaxTree_Modify_Statement,
            BinOp           as  Native_AbstractSyntaxTree_Binary_Expression,
            BitAnd          as  Native_AbstractSyntaxTree_Binary_And_Operator,
            BitXor          as  Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator,
            BoolOp          as  Native_AbstractSyntaxTree_Logical_Expression,
            Break           as  Native_AbstractSyntaxTree_Break_Statement,
            Call            as  Native_AbstractSyntaxTree_Call_Expression,
            ClassDef        as  Native_AbstractSyntaxTree_Class_Definition,
            Compare         as  Native_AbstractSyntaxTree_Compare_Expression,
            comprehension   as  Native_AbstractSyntaxTree_Comprehension_Clause,
            Continue        as  Native_AbstractSyntaxTree_Continue_Statement,
            Del             as  Native_AbstractSyntaxTree_Delete_Context,
            Delete          as  Native_AbstractSyntaxTree_Delete_Statement,
            Dict            as  Native_AbstractSyntaxTree_Map_Expression,
            DictComp        as  Native_AbstractSyntaxTree_Map_Comprehension,
            Div             as  Native_AbstractSyntaxTree_Divide_Operator,
            Ellipsis        as  Native_AbstractSyntaxTree_Ellipsis_Index,
            Eq              as  Native_AbstractSyntaxTree_Compare_Equal_Operator,
            Exec            as  Native_AbstractSyntaxTree_Execute_Statement,
            ExceptHandler   as  Native_AbstractSyntaxTree_Except_Handler,
            Expr            as  Native_AbstractSyntaxTree_Expression_Statement,
            ExtSlice        as  Native_AbstractSyntaxTree_Extended_Slice_Index,
            FloorDiv        as  Native_AbstractSyntaxTree_Floor_Divide_Operator,
            For             as  Native_AbstractSyntaxTree_For_Statement,
            FunctionDef     as  Native_AbstractSyntaxTree_Function_Definition,
            GeneratorExp    as  Native_AbstractSyntaxTree_Generator_Comprehension,
            Global          as  Native_AbstractSyntaxTree_Global_Statement,
            Gt              as  Native_AbstractSyntaxTree_Compare_Greater_Than_Operator,
            GtE             as  Native_AbstractSyntaxTree_Compare_Greater_Than_Or_Equal_Operator,
            If              as  Native_AbstractSyntaxTree_If_Statement,
            IfExp           as  Native_AbstractSyntaxTree_If_Expression,
            Import          as  Native_AbstractSyntaxTree_Import_Statement,
            ImportFrom      as  Native_AbstractSyntaxTree_From_Import_Statement,
            In              as  Native_AbstractSyntaxTree_Contains_Operator,
            Index           as  Native_AbstractSyntaxTree_Simple_Index,
            Invert          as  Native_AbstractSyntaxTree_Invert_Operator,
            Is              as  Native_AbstractSyntaxTree_Compare_Identity_Operator,
            IsNot           as  Native_AbstractSyntaxTree_Compare_Different_Operator,
            keyword         as  Native_AbstractSyntaxTree_Keyword_Argument,
            Lambda          as  Native_AbstractSyntaxTree_Lambda_Expression,
            List            as  Native_AbstractSyntaxTree_List_Expression,
            ListComp        as  Native_AbstractSyntaxTree_List_Comprehension,
            Load            as  Native_AbstractSyntaxTree_Load_Context,
            LShift          as  Native_AbstractSyntaxTree_Left_Shift_Operator,
            Lt              as  Native_AbstractSyntaxTree_Compare_Less_Than_Operator,
            LtE             as  Native_AbstractSyntaxTree_Compare_Less_Than_Or_Equal_Operator,
            Mod             as  Native_AbstractSyntaxTree_Modulus_Operator,
            Module          as  Native_AbstractSyntaxTree_Module,
            Mult            as  Native_AbstractSyntaxTree_Multiply_Operator,
            Name            as  Native_AbstractSyntaxTree_Name,
            Not             as  Native_AbstractSyntaxTree_Not_Operator,
            NotEq           as  Native_AbstractSyntaxTree_Compare_Not_Equal_Operator,
            NotIn           as  Native_AbstractSyntaxTree_Excludes_Operator,
            Num             as  Native_AbstractSyntaxTree_Number,
            Or              as  Native_AbstractSyntaxTree_Logical_Or_Operator,
            Param           as  Native_AbstractSyntaxTree_Parameter_Context,
            Pass            as  Native_AbstractSyntaxTree_Pass_Statement,
            Pow             as  Native_AbstractSyntaxTree_Power_Operator,
            Print           as  Native_AbstractSyntaxTree_Print_Statement,
            Raise           as  Native_AbstractSyntaxTree_Raise_Statement,
            Repr            as  Native_AbstractSyntaxTree_Backquote_Expression,
            Return          as  Native_AbstractSyntaxTree_Return_Statement,
            RShift          as  Native_AbstractSyntaxTree_Right_Shift_Operator,
            Set             as  Native_AbstractSyntaxTree_Set_Expression,
            SetComp         as  Native_AbstractSyntaxTree_Set_Comprehension,
            Slice           as  Native_AbstractSyntaxTree_Slice_Index,
            Store           as  Native_AbstractSyntaxTree_Store_Context,
            Str             as  Native_AbstractSyntaxTree_String,
            Sub             as  Native_AbstractSyntaxTree_Subtract_Operator,
            Subscript       as  Native_AbstractSyntaxTree_Subscript_Expression,
            TryExcept       as  Native_AbstractSyntaxTree_Try_Except_Statement,
            TryFinally      as  Native_AbstractSyntaxTree_Try_Finally_Statement,
            Tuple           as  Native_AbstractSyntaxTree_Tuple_Expression,
            UAdd            as  Native_AbstractSyntaxTree_Positive_Operator,
            UnaryOp         as  Native_AbstractSyntaxTree_Unary_Expression,
            USub            as  Native_AbstractSyntaxTree_Negative_Operator,
            While           as  Native_AbstractSyntaxTree_While_Statement,
            With            as  Native_AbstractSyntaxTree_With_Statement,
            Yield           as  Native_AbstractSyntaxTree_Yield_Expression,
        )



#
#   fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR(v)
#
#       Assert that `v` is a `_ast.*` class that represents a binary operator.
#
#       (see `ANY__native__abstract_syntax_tree__BINARY_OPERATOR` below for the `_ast.*` classes that represent a
#       binary operator).
#
if __debug__:
    ANY__native__abstract_syntax_tree__BINARY_OPERATOR = ((
            Native_AbstractSyntaxTree_Add_Operator,
            Native_AbstractSyntaxTree_Binary_And_Operator,
            Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator,
            Native_AbstractSyntaxTree_Divide_Operator,
            Native_AbstractSyntaxTree_Floor_Divide_Operator,
            Native_AbstractSyntaxTree_Left_Shift_Operator,
            Native_AbstractSyntaxTree_Modulus_Operator,
            Native_AbstractSyntaxTree_Multiply_Operator,
            Native_AbstractSyntaxTree_Power_Operator,
            Native_AbstractSyntaxTree_Right_Shift_Operator,
            Native_AbstractSyntaxTree_Subtract_Operator,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__BINARY_OPERATOR(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__BINARY_OPERATOR)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v)
#
#       Assert that `v` is a `_ast.*` class that represents a "delete", "load", or "store" context.
#
if __debug__:
    ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT = ((
            Native_AbstractSyntaxTree_Delete_Context,
            Native_AbstractSyntaxTree_Load_Context,
            Native_AbstractSyntaxTree_Store_Context,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__INDEX(v)
#
#       Assert that `v` is a `_ast.*` class that represents a subscript clause.
#
#       (see `ANY__native__abstract_syntax_tree__INDEX` below for the `_ast.*` classes that represent a
#       subscript clause).
#
if __debug__:
    ANY__native__abstract_syntax_tree__INDEX = ((
            Native_AbstractSyntaxTree_Ellipsis_Index,
            Native_AbstractSyntaxTree_Extended_Slice_Index,
            Native_AbstractSyntaxTree_Simple_Index,
            Native_AbstractSyntaxTree_Slice_Index,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__INDEX(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__INDEX)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v)
#
#       Assert that `v` is a `_ast.*` class that represents a "load" or "store" context.
#
if __debug__:
    ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT = ((
            Native_AbstractSyntaxTree_Load_Context,
            Native_AbstractSyntaxTree_Store_Context,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__LOAD_OR_STORE_CONTEXT)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR(v)
#
#       Assert that `v` is a `_ast.*` class that represents a boolean operator.
#
#       (see `ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR` below for the `_ast.*` classes that represent a
#       boolean operator).
#
if __debug__:
    ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR = ((
            Native_AbstractSyntaxTree_Logical_And_Operator,
            Native_AbstractSyntaxTree_Logical_Or_Operator,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__LOGICAL_OPERATOR)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR(v)
#
#       Assert that `v` is a `_ast.*` class that represents a modify operator (i.e.: `+=`, `*=`, etc.)
#
#       (see `ANY__native__abstract_syntax_tree__MODIFY_OPERATOR` below for the `_ast.*` classes that represent a
#       modify operator).
#
if __debug__:
    ANY__native__abstract_syntax_tree__MODIFY_OPERATOR = ((
            Native_AbstractSyntaxTree_Add_Operator,
            Native_AbstractSyntaxTree_Binary_Exclusive_Or_Operator,
            Native_AbstractSyntaxTree_Multiply_Operator,
            Native_AbstractSyntaxTree_Subtract_Operator,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__MODIFY_OPERATOR)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__TARGET(v)
#
#       Assert that `v` is a `_ast.*` class that represents a target (i.e.: on the left hand side of `=`, `+=`, `*=`,
#       etc.).
#
#       (see `ANY__native__abstract_syntax_tree__TARGET` below for the `_ast.*` classes that represent a target).
#
if __debug__:
    ANY__native__abstract_syntax_tree__TARGET = ((
            Native_AbstractSyntaxTree_Attribute_Expression,
            Native_AbstractSyntaxTree_List_Expression,
            Native_AbstractSyntaxTree_Name,
            Native_AbstractSyntaxTree_Subscript_Expression,
            Native_AbstractSyntaxTree_Tuple_Expression,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__TARGET(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__TARGET)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR(v)
#
#       Assert that `v` is a `_ast.*` class that represents a unary operator.
#
#       (see `ANY__native__abstract_syntax_tree__UNARY_OPERATOR` below for the `_ast.*` classes that represent a
#       unary operator).
#
if __debug__:
    ANY__native__abstract_syntax_tree__UNARY_OPERATOR = ((
            Native_AbstractSyntaxTree_Invert_Operator,
            Native_AbstractSyntaxTree_Negative_Operator,
            Native_AbstractSyntaxTree_Not_Operator,
            Native_AbstractSyntaxTree_Positive_Operator,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__UNARY_OPERATOR(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__UNARY_OPERATOR)

        return True


#
#   fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v)
#
#       Assert that `v` is a `_ast.*` class that represents a value expression.
#
#       (see `ANY__native__abstract_syntax_tree__VALUE_EXPRESSION` below for the `_ast.*` classes that represent a
#       value expression).
#
if __debug__:
    ANY__native__abstract_syntax_tree__VALUE_EXPRESSION = ((
            Native_AbstractSyntaxTree_Attribute_Expression,
            Native_AbstractSyntaxTree_Backquote_Expression,
            Native_AbstractSyntaxTree_Binary_Expression,
            Native_AbstractSyntaxTree_Call_Expression,
            Native_AbstractSyntaxTree_Compare_Expression,
            Native_AbstractSyntaxTree_Generator_Comprehension,
            Native_AbstractSyntaxTree_If_Expression,
            Native_AbstractSyntaxTree_Lambda_Expression,
            Native_AbstractSyntaxTree_List_Comprehension,
            Native_AbstractSyntaxTree_List_Expression,
            Native_AbstractSyntaxTree_Logical_Expression,
            Native_AbstractSyntaxTree_Map_Comprehension,
            Native_AbstractSyntaxTree_Map_Expression,
            Native_AbstractSyntaxTree_Name,
            Native_AbstractSyntaxTree_Number,
            Native_AbstractSyntaxTree_Set_Comprehension,
            Native_AbstractSyntaxTree_Set_Expression,
            Native_AbstractSyntaxTree_String,
            Native_AbstractSyntaxTree_Subscript_Expression,
            Native_AbstractSyntaxTree_Tuple_Expression,
            Native_AbstractSyntaxTree_Unary_Expression,
        ))


    def fact_is__ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v):
        assert isinstance(v, ANY__native__abstract_syntax_tree__VALUE_EXPRESSION)

        return True


#
#   fact_is__native__abstract_syntax_tree__all_parameters(v)
#
#       Assert that `v` is a `Native_AbstractSyntaxTree_All_Parameters` instance.
#
if __debug__:
    def fact_is__native__abstract_syntax_tree__all_parameters(v):
        assert type(v) is Native_AbstractSyntaxTree_All_Parameters

        return True


#
#   fact_is__native__abstract_syntax_tree__delete_context(v)
#
#       Assert that `v` is a `Native_AbstractSyntaxTree_Delete_Context` (i.e.: `_ast.Del`)
#
if __debug__:
    def fact_is__native__abstract_syntax_tree__delete_context(v):
        assert type(v) is Native_AbstractSyntaxTree_delete_Context

        return True


#
#   fact_is__native__abstract_syntax_tree__module(v)
#
#       Assert that `v` is a `Native_AbstractSyntaxTree_Module` instance.
#
if __debug__:
    def fact_is__native__abstract_syntax_tree__module(v):
        assert type(v) is Native_AbstractSyntaxTree_Module

        return True


#
#   fact_is__native__abstract_syntax_tree__name(v)
#
#       Assert that `v` is a `Native_AbstractSyntaxTree_Name` instance.
#
if __debug__:
    def fact_is__native__abstract_syntax_tree__name(v):
        assert type(v) is Native_AbstractSyntaxTree_Name

        return True


#
#   fact_is__native__abstract_syntax_tree__parameter_context(v)
#
#       Assert that `v` is a `Native_AbstractSyntaxTree_Parameter_Context` (i.e.: `_ast.Param`)
#
if __debug__:
    def fact_is__native__abstract_syntax_tree__parameter_context(v):
        assert type(v) is Native_AbstractSyntaxTree_Parameter_Context

        return True


#
#   fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET(v)
#
#       Assert that `v` is either `None` or a `_ast.*` class that represents an target.
#
#       (see `ANY__native__abstract_syntax_tree__TARGET` above for the `_ast.*` classes that represent a target).
#
if __debug__:
    def fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET(v):
        if v is None:
            return True

        assert isinstance(v, ANY__native__abstract_syntax_tree__TARGET)

        return True


#
#   fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v)
#
#       Assert that `v` is either `None` or a `_ast.*` class that represents a value expression.
#
#       (see `ANY__native__abstract_syntax_tree__VALUE_EXPRESSION` above for the `_ast.*` classes that represent a
#       value expression).
#
if __debug__:
    def fact_is___native_none___OR___ANY__native__abstract_syntax_tree__VALUE_EXPRESSION(v):
        if v is None:
            return True

        assert isinstance(v, ANY__native__abstract_syntax_tree__VALUE_EXPRESSION)

        return True


#
#   native__compile__to__native__abstract_syntax_tree(source, filename)
#
#       Compile the `source` (a `Some_Native_String` that represents the source code) to an python abstract syntax tree.
#
#       Use `filename` as the filename for error purposes only (`filename` is not read, instead the code is supplied in
#       the argument `source`).
#
def native__compile__to__native__abstract_syntax_tree(source, filename):
    assert fact_is_some_native_string(source)
    assert fact_is_full_native_string(filename)

    return compile(                                 #   Call the python built-in `compile` function.
               source   = source,
               filename = filename,
               mode     = 'exec',
               flags    = native__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE,
           )
