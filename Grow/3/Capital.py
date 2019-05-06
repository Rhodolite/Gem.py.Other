#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#

#
#   CAPITAL - Common Application Programming Interface, Transcending All Languages.
#
#       Since we are translating to multiple languages, we want the same API (Application Programming Interface) to
#       be available in all the languages.
#
#       Capital is that common API.
#
#   CURRENT:
#
#       To quickly develop code (and minimize lines of code to learn), we will depend on Capital, initially, a bit
#       more than neccessary.
#
#   FUTURE:
#
#       The code generator will, eventually, minimize the usage of Capital, and translate down to the native API
#       that comes with each language for features that target language supports.
#
#       For features that the target language does not support, we will continue to use Capital to emulate them.
#
import  os.path


#
#   "Capital.py" INSTEAD OF "Capital/__init__.py".
#
#       We prefer to use "Capital.py" instead of the more traditional python way of "Capital/__init__.py".
#
#       REASONS:
#
#           This makes it easier for first time readers to look at "Capital.py" and read the important notes first.
#
#           For example, the note above on the meaning of the "CAPITAL" acronym, and the purpose of the Capital
#           library is easier to locate in this "Capital.py" file, than in "Capital/__init__.py".
#
#           Also, we list all of our submodules, below, with a brief comment, so the user at a quick glance can see all
#           the submodules and their purpose.
#
#           (For the python code to work, we don't actually need to list the submodules below, but it is done for
#           documentation purposes).
#

#
#   Load Capital submodules from "Capital/" directory.
#
#       Due to using "Capital.py" instead of the more traditional python way of "Capital/__init__.py", we have to
#       modify `__path__` to point to our submodules.
#
#       Other than this one line modification to `__path__`, there is no [internal] difference to python as
#       regards using "Capital.py" instead of "Capital/__init__.py".
#
#   NOTE:
#       In python, `__path__` means a *LIST* of pathnames, not a single pathname.
#
__path__ = [os.path.join(os.path.dirname(__file__), 'Capital')]


import  Capital.Core                #   "Capital/Core.py"   - Core Capital support code.
