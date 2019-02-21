#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Z.Core  import  arrange


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
        'argument',                     #   Any
    ))


    def __init__(self, argument):
        self.argument = argument


    def create_python_code(self, f):
        f.write(arrange('print({!r})\n', self.argument))
