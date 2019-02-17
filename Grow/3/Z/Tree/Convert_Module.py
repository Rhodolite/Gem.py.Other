#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Module - Convert Python Abstract Syntax Tree Module to `Tree_Module`.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Z.Tree.Convert_Statement            import  convert_some_list_of_statements
from    Z.Tree.Module                       import  create_Tree_Module
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Module
from    Z.Tree.Native_AbstractSyntaxTree    import  native__compile__to__native__abstract_syntax_tree


if __debug__:
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__module


#
#   convert_module
#
#       Convert an instance of `Native_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`) to an instance of
#       `SyntaxTree_Module`.
#
assert Native_AbstractSyntaxTree_Module._attributes == (())
assert Native_AbstractSyntaxTree_Module._fields     == (('body',))


def convert_module(self):
    assert fact_is__native__abstract_syntax_tree__module(self)
    assert fact_is_some_native_list                     (self.body)

    return create_Tree_Module(
               convert_some_list_of_statements(self.body),
           )


#
#   compile_to_syntax_tree - Compile `source` to an instance of `SyntaxTree_Module`.
#
#       Two step process:
#
#       1.  Compile `source` to a `Native_AbstractSyntaxTree_Module (i.e.: `_ast.Module`) instance.
#
#       2.  Convert the `Native_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`) instance to an instance of
#           `SyntaxTree_Module`.
#
def compile_to_syntax_tree(source, filename):
    native__abstract_syntax_tree = native__compile__to__native__abstract_syntax_tree(source, filename)

    return convert_module(native__abstract_syntax_tree)
