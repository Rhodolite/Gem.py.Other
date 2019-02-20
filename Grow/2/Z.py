#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
__path__ = ['Z/']               #   Load Z submodules from "Z/" directory.


import  Z.Core                  #   "Z/Core.py"                 - Core Z support code
import  Z.Crystal_ParseTree     #   "Z/Crystal_ParseTree.py"    - A parse tree of Crystal statements.
import  Z.Extract               #   "Z/Extract.py"              - Extract a parse tree from "Vision.z"
import  Z.Python_ParseTree      #   "Z/Python_ParseTree.py"     - A parse tree of Python statements.
import  Z.Transform_Crystal_to_Python #                         - Transform Crystal statements to Python statements.
import  Z.CodeGenerator_OnExit  #   "Z/CodeGenerator_OnExit.py" - Generate code when the program exits.


#
#   Replace this (currently loading) Z module with a *NEW* Z Module that does the "extraction" phase.
#
#   This implements the following commands:
#
#       Z.copyright         - Add a copyright.
#       Z.output            - Output a line of text.
#
#   The reason we have to replace this (currently loading) Z module with a *NEW* Z Module is so that we can
#   add attributes to the module (a normal python module doesn't allow us to add attributes).
#
#       Specifically, we have added the `.copyright` attribute to call the function "copyright" defined
#       in "Z/Extract.py" (see the line marked `@property` in "Z/Extract.py").
#
Z.Extract.if_main_path_ends_in_dot_z__replace_Z_module()


#
#   After "Vizion.z" has fully run (and generated the Crsytal parse tree using the Z commands):
#
#       We run the code generator:
#
#       1.  Transform Crystal to Python.
#       2.  Output Python (to "Vision.py").
#
Z.CodeGenerator_OnExit.if_main_path_ends_in_dot_z__register_code_generator()
