#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Module_V2 - Convert Python Abstract Syntax Tree Module to `Tree_Module`, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Native_AbstractSyntaxTree    import  native__compile__to__native__abstract_syntax_tree


if __debug__:
    from    Capital.Fact                        import  fact_is_native_list
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__module
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Module


#
#   convert_module(z, v)
#
#       Convert an instance of `Native_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`) to an instance of
#       `SyntaxTree_Module`.
#
assert Native_AbstractSyntaxTree_Module._attributes == (())
assert Native_AbstractSyntaxTree_Module._fields     == (('body',))


def convert_module(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is__native__abstract_syntax_tree__module(v)
    assert fact_is_native_list                          (v.body)

    return z.create_Tree_Module(
               z.convert_some_list_of_statements(z, v.body),
           )


#
#   compile_to_syntax_tree_v2 - Compile `source` to an instance of `SyntaxTree_Module`.
#
#       Two step process:
#
#       1.  Compile `source` to a `Native_AbstractSyntaxTree_Module (i.e.: `_ast.Module`) instance.
#
#       2.  Convert the `Native_AbstractSyntaxTree_Module` (i.e.: `_ast.Module`) instance to an instance of
#           `SyntaxTree_Module`.
#
def compile_to_syntax_tree_v2(z, source, filename):
    assert fact_is_convert_zone(z)

    native__abstract_syntax_tree = native__compile__to__native__abstract_syntax_tree(source, filename)

    return convert_module(z, native__abstract_syntax_tree)
