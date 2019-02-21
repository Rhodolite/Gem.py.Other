#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#-<OLD>
#-from  Z.Core                          import  arrange
#-</OLD>

#+<NEW>
from    Capital.Core                    import  arrange
#+</NEW>


#
#   Python_ParseTree - A parse tree of Python Statements.
#
class Python_ParseTree(object):
    __slots__ = ((
        'python_statements',               #   List of Python_Statement_*
    ))


    def __init__(self):
        self.python_statements = []


    def append_python_statement(self, statement):
        self.python_statements.append(statement)


    def create_python_code(self, f):
        for v in self.python_statements:
            v.create_python_code(f)


#
#   Python_Statement_Comment_Many - A multiline comment
#   Python_Statement_Print_1      - A print statement
#
class Python_Statement_Comment_Many(object):
    __slots__ = ((
        'commment_tuple',               #   Tuple of String
    ))


    def __init__(self, commment_tuple):
        self.commment_tuple = commment_tuple


    def create_python_code(self, f):
        for s in self.commment_tuple:
            f.write(arrange('{}\n', s))


class Python_Statement_Print_1(object):
    __slots__ = ((
#-<OLD>
#-      'argument',                     #   Any
#-</OLD>

#+<NEW>
        'argument',                     #   String
#+</NEW>
    ))


    def __init__(self, argument):
        self.argument = argument


    def create_python_code(self, f):
#-<OLD>
#-      f.write(arrange('print({!r})\n', self.argument))
#-</OLD>

#+<NEW>
        #
        #   The "<OLD>" version used `{!r}` (i.e.: call python, internally, to get the representation of
        #   `self.argument`).
        #
        #   This "<NEW>" version uses `{}` instead, and call the specific method:
        #
        #       `.python_code()`
        #
        #   This is defined in "Capital/String.py" as:
        #
        #       s.python_code()         #   Return a `str` instance that is the python code that python will
        #                               #   compile to a `str` instance with the same characters.
        #
        #   In other words, currently, "<NEW>" is the same as "<OLD>", but this "<NEW>" code is much easier for us,
        #   later, to modify the underlying decision how to generate "python code".
        #
        #       (As "Capital/String_Implementation.py" explains, we will in fact, modify this
        #       in the future so that `.python_code()` calls our own improved `portray_python_string` function).
        #
        f.write(arrange('print({})\n', self.argument.python_code()))
#+</NEW>
