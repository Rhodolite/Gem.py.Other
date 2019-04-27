#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    os.path                     import  dirname     as  python_path_directory_name
from    os.path                     import  join        as  python_path_join


#
#   Z.Parser
#


#
#   Load Z.Parser submodules from "Z/Parser" directory.
#
__path__ = [python_path_join(python_path_directory_name(__file__), 'Parser')]
