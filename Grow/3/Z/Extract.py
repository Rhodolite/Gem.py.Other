#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


import  sys


from    Z.Crystal_ParseTree             import  Crystal_ParseTree
from    Z.Crystal_ParseTree             import  Crystal_Statement_Copyright
from    Z.Crystal_ParseTree             import  Crystal_Statement_Output_1
from    Z.Transform_Crystal_to_Python   import  Crystal_ParseTree__convert_crystal_to_python


class CrystalInput(object):
    __slots__ = ((
        'crystal_parse_tree',           #   Crystal_ParseTree
    ))


    def __init__(self, crystal_parse_tree):
        self.crystal_parse_tree = crystal_parse_tree


    @staticmethod
    def __repr__():
        return '<CrystalInput>'


    def append_crystal_statement(self, statement):
        self.crystal_parse_tree.append_crystal_statement(statement)


    def convert_crystal_to_python(self, crystal_input_path):
        return Crystal_ParseTree__convert_crystal_to_python(self.crystal_parse_tree, crystal_input_path)


crystal_input = CrystalInput(Crystal_ParseTree())


#
#   Extract_ParseTree_by_using_Z_Commands - A class to extract a parse tree by using `Z` commands in python code.
#
class Extract_ParseTree_by_using_Z_Commands(object):
    __slots__ = (())


    @staticmethod
    def __repr__():
        return '<Z>'


    #
    #   Z.copyright (line 7 of "Vision.z")
    #
    #       By using `@property` here, we declare `Z.copyright` as an attribute.
    #
    #       This means when `Z.copyright` (at line 7 of "Vision.z") is used, this function gets called
    #       (even without the usual `()` used for function calls).
    #
    @property                           #   Declare `.copyright` as an attribute.
    def copyright(self):
        crystal_input.append_crystal_statement(Crystal_Statement_Copyright())


    #
    #   Z.output (line 8 for "Vision.z")
    #
    def output(self, argument):
        crystal_input.append_crystal_statement(Crystal_Statement_Output_1(argument))


#
#   replace_Z_module - Replaces the Z module with code to extract a parse tree by using `Z` commands.
#
#       As "Z.py" explains, normal python modules don't allow us to add attributes.
#
#       Hence, we replace the normal python module with our module.
#
#       As explained above, our module implementes `Z.copyright` as an attribute (i.e.: does not need the
#       usual `()` used for function calls).
#
def replace_Z_module():
    Z = Extract_ParseTree_by_using_Z_Commands()

    #
    #   Replace the current Z module with our new extraction code ...
    #
    sys.modules['Z'] = Z



#
#   if main path ends in ".z":
#       replace_Z_module()
#
def if_main_path_ends_in_dot_z__replace_Z_module():
    if len(sys.argv) == 1:
        crystal_input_path = sys.argv[0]

        if crystal_input_path.endswith('.z'):
            replace_Z_module()
