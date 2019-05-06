#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Zone - Functions to convert Python Abstract Syntax Tree Statements to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Core                    import  FATAL
from    Z.Parser.Global                 import  parser_globals


class Convert_Zone(object):
    __slots__ = ((
        #
        #   Aliases
        #
        'convert_full_list_of_module_aliases',      #   Function
        'convert_full_list_of_symbol_aliases',      #   Function
        'create_Tree_Module_Alias',                 #   Function
        'create_Tree_Symbol_Alias',                 #   Function
    ))


    is_convert_zone = True


#
#   fact_is_convert_zone(v)     - Assert that `v` is a convert zone.
#
if __debug__:
    def fact_is_convert_zone(v):
        assert v.is_convert_zone

        return True



def FATAL_unknown_version(name, version):
    FATAL('Z/Tree/Convert_Zone.py: unknown tree {} version: {}', name, version)


def fill_convert_zone():
    alias_version         = parser_globals.alias_version
    argument_version      = parser_globals.argument_version
    comprehension_version = parser_globals.comprehension_version
    context_version       = parser_globals.context_version
    except_version        = parser_globals.except_version
    expression_version    = parser_globals.expression_version
    index_version         = parser_globals.index_version
    module_name_version   = parser_globals.module_name_version
    name_version          = parser_globals.name_version
    operator_version      = parser_globals.operator_version
    parameter_version     = parser_globals.parameter_version
    statement_version     = parser_globals.statement_version
    symbol_version        = parser_globals.symbol_version
    target_version        = parser_globals.target_version


    #
    #   Alias Version
    #
    if alias_version == 2:
        #
        #   Next two lines use "_V1" on purpose
        #
        from    Z.Tree.Alias_V1             import  create_Tree_Alias_Clause            as  create_Tree_Module_Alias
        from    Z.Tree.Alias_V1             import  create_Tree_Alias_Clause            as  create_Tree_Symbol_Alias

        from    Z.Tree.Convert_Alias_V2     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V2     import  convert_full_list_of_symbol_aliases
    elif alias_version == 3:
        from    Z.Tree.Alias_V3             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V3             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V3     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V3     import  convert_full_list_of_symbol_aliases
    elif alias_version == 4:
        from    Z.Tree.Alias_V4             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V4             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V4     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V4     import  convert_full_list_of_symbol_aliases
    elif alias_version == 5:
        from    Z.Tree.Alias_V5             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V5             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V5     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V5     import  convert_full_list_of_symbol_aliases
    elif alias_version == 6:
        from    Z.Tree.Alias_V6             import  create_Tree_Module_Alias
        from    Z.Tree.Alias_V6             import  create_Tree_Symbol_Alias
        from    Z.Tree.Convert_Alias_V6     import  convert_full_list_of_module_aliases
        from    Z.Tree.Convert_Alias_V6     import  convert_full_list_of_symbol_aliases
    else:
        FATAL_unknown_version('alias', alias_version)


    #
    #   Aliases
    #
    z = convert_zone

    z.convert_full_list_of_module_aliases = convert_full_list_of_module_aliases
    z.convert_full_list_of_symbol_aliases = convert_full_list_of_symbol_aliases
    z.create_Tree_Module_Alias            = create_Tree_Module_Alias
    z.create_Tree_Symbol_Alias            = create_Tree_Symbol_Alias


@creator
def create_convert_zone():
    return Convert_Zone()


convert_zone = create_convert_zone()
