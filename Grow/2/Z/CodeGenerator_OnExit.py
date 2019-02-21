#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
import  atexit
import  sys


#-<OLD>
#-from  Z.Core                          import  arrange
#-from  Z.Core                          import  trace
#-</OLD>

#+<NEW>
from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace
#+</NEW>

from    Z.Extract                       import  crystal_input


#
#   Register `code_generator` to run when "*.z" exits.
#
def register_code_generator(crystal_input_path):
    python_output_path = arrange('{}.py', crystal_input_path[:-2])


    @atexit.register
    def code_generator():
        python_parse_tree = crystal_input.convert_crystal_to_python(crystal_input_path)

        with open(python_output_path, 'w') as f:
            python_parse_tree.create_python_code(f)

        trace('Created {}', python_output_path)


#
#   if main path ends in ".z":
#       register_code_generator(main_path)
#
def if_main_path_ends_in_dot_z__register_code_generator():
    if len(sys.argv) == 1:
        crystal_input_path = sys.argv[0]

        if crystal_input_path.endswith('.z'):
            register_code_generator(crystal_input_path)
