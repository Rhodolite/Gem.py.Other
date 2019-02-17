#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.System - A wrapper around python `sys` module
#
import  sys     as  Python_System


#
#   exit_thread  - exit the thread  [throw's a catchable exception]
#
exit_thread  = Python_System.exit


#
#   is_python_2 - Running under python 2.*
#   is_python_3 - Running under python 3.*
#
is_python_2 = (Python_System.version_info.major == 2)
is_python_3 = (Python_System.version_info.major == 3)




assert (is_python_2 ^ is_python_3)              #   Must be [exclusive] either python 2.* or python 3.*
