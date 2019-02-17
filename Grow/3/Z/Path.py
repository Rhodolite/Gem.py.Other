#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    os.path                         import  dirname         as  python_path_directory_name
from    os.path                         import  join            as  python_path_join


#
#   NOTE:
#       Do *NOT* confuse `Z_path` (below) with `Z.__path__`
#       (something totally diferent that has *NOTHING* to do with this file!).
#
#   CLARIFICATION:
#
#       `Z.__file__` - python auto generated value, which is the path to the
#                      "Z.py" source file.
#
#       `Z_source_path` - The import statement below imports `Z.__file__` as
#                         `Z_source_path`.
#
#       `Z.__path__` - A python list of directories to search for `Z`
#                      submodules.
#
#                      `Z.__path__` has *NOTHING* to do with `Z_source_path`
#                      (defined below).
#
#                      See "Z.py" for how "`Z.__path__`" is used
#                      (named `__path__` there).
#
#   Z_source_path
#
#       Why do we name the variable `Z_source_path` when it *MIGHT* be confused
#       with `Z.__path__`.
#
#       REASON:
#           `Z_source_path` is a clear & accurate description of the variable,
#           and thus what it's name should be.
#
#       HISTORICALLY NAMED `.__path__` instead of `.__path_list__`.
#
#           It is not our fault that `Z.__path__` is misnamed.
#
#           Despite it being named `Z.__path__` is is *NOT* a path name, but
#           a list of path names.
#
#           It should thus be named `Z.__path_list__` (or maybe
#           `Z.__path_directory_list__`) to make it clear it is a list of
#           paths, and not a path.
#
#           However, it is historically named `.__path__` and we can't change
#           that.
#
#           This history comes from `sys.path` which come from the environment
#           variable "$PATH" in sh, bash, ksh, etc ... so it has a long long
#           history of being named "path" (or "$PATH") instead of "path_list"
#           or ("$PATH_LIST") before people thought as carefully about proper
#           variable naming.
#
#   P.S.:
#       Yes, I am annoyed at the misnaming of `.__path__`, it took me more than
#       an hour to squash a bug related to this, since it is misnamed, and it
#       misled me as to what it was :(
#
#   MORALE:
#       Name your variables properly!
#
#       Help the reader of your code!
#
#       Or put differently:
#
#           Programming is an art to communicate clearly and concisely
#           to fellow programmers.
#
#       Take the time to communicate clearly and consicely to your
#       fellow programers.
#
#       Name your variables properly!
#       
#       Thanks, much appreciated.
#


#
#   Z_source_path - The path to the "Z.py" source file.
#
#       SIMPLE CASE:
#           Normally we execute the program as follows:
#
#               $ python Z.py
#
#           In this, simple case, then `Z_source_path` is `"Z.py"`.
#
#       COMPLEX CASE:
#           However, if we execute the program as follows:
#
#               python /home/me/Grow/2/Z.py
#
#           In this, more complex case, Then `Z_source_path` will be
#           `"/home/me/Grow/2/Z.py"`.
#
#       We use `Z_source_path` to handle both the simple case & complex case.
#
from    Z                               import  __file__        as  Z_source_path


#
#   `Z_directory_path` - The path to the directory "Z.py" is in.
#
Z_directory_path = python_path_directory_name(Z_source_path)


#
#   path_to_file_in_Z_directory(filename)
#
#       - Return a path to `filename`, relative to the directory "Z.py" is in.
#
def path_to_file_in_Z_directory(filename):
    return python_path_join(Z_directory_path, filename)
