#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Crystal_ParseTree - A parse tree of Crystal Statements.
#
class Crystal_ParseTree(object):
    __slots__ = ((
        'crystal_statements',               #   List of Crystal_Statement_*
    ))


    def __init__(self):
        self.crystal_statements = []


    def append_crystal_statement(self, statement):
        self.crystal_statements.append(statement)


    #
    #   convert_crystal_to_python - defined in "Z/Transform_Crystal_to_Python.py"
    #
    #       The reason the `convert_crystal_to_python` method is defined in a different file
    #       is so that when we have 15+ language converters, they each have their own file.
    #
    #       That is a better organization than having each of the convertors spread in
    #       little bits (a little bit in each different class) throughout this file.
    #


#
#   Crystal_Statement_Copyright - A copyright statement.
#   Crystal_Statement_Output_1  - Output a line of text.
#
class Crystal_Statement_Copyright(object):
    __slots__ = (())


    @staticmethod
    def extract_copyright(path):
        with open(path) as f:
            data = f.read()

        text_lines = data.splitlines()

        if (
                len(text_lines) >= 2
            and text_lines[0] == '#'
            and text_lines[1].startswith('#   Copyright (c) ')
            and text_lines[2] == '#'
        ):
            return text_lines[1][4:]

        value_message = arrange("cannot find copyright in {!r}", path)

        missing_copyright = ValueError(value_message)

        raise missing_copyright


    #
    #   convert_crystal_to_python - defined in "Z/Transform..."
    #


class Crystal_Statement_Output_1(object):
    __slots__ = ((
        'argument',                     #   String
    ))


    def __init__(self, argument):
        self.argument = argument

    #
    #   convert_crystal_to_python - defined in "Z/Transform..."
    #
