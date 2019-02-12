#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
vision = 'Programming is an art to communicate clearly and concisely to fellow programmers.'


#
#   trace mode
#
tracing = True



#
#   Imports
#
import  sys


#
#   The code generator -- only called if main file is named "*.x"
#
def code_generator(input_path):
    import  atexit


    #
    #   trace
    #
    if tracing:
        trace_prefix = '% Crystal.py: '


        def trace(message, *arguments):
            if arguments:
                message = message.format(*arguments)

            print(trace_prefix + message)
    else:
        def trace(message, *arguments):
            pass


    #
    #   arrange - A simple wrapper around `.format`
    #
    #       This makes the code more readable, instead of:
    #
    #           'hello {} #{}'.format('world', 7)
    #
    #       We can use:
    #
    #           arrange('hello {} #{}', 'world', 7)
    #
    def arrange(message, *arguments):
        return message.format(*arguments)


    #
    #   crystal_parse_tree
    #
    class Crystal_ParseTree(object):
        __slots__ = ((
            'statement_list',               #   List of Crystal_Statement_*
        ))


        def __init__(self):
            self.statement_list = []


        def append_statement(self, statement):
            self.statement_list.append(statement)


        def convert_crystal_to_python(self, input_path):
            python_parse_tree = Python_ParseTree()

            for v in self.statement_list:
                statement = v.convert_crystal_to_python(input_path)

                if statement:
                    python_parse_tree.append_statement(statement)

            return python_parse_tree


    #
    #   Crystal_Statement_Copyright     - A copyright statement
    #   Crystal_Statement_Line_1        - Output a line of text
    #   Crystal_Statement_Package       - Use a package
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


        def convert_crystal_to_python(self, path):
            copyright = self.extract_copyright(path)

            return Python_Statement_Comment_Many(
                       tuple([
                           '#',
                           arrange('#   {}', copyright),
                           '#',
                       ]),
                   )
                        

    class Crystal_Statement_Line_1(object):
        __slots__ = ((
            'argument',                     #   Any
        ))


        def __init__(self, argument):
            self.argument = argument


        def convert_crystal_to_python(self, path):
            return Python_Statement_Print_1(self.argument)

        
    class Crystal_Statement_Package(object):
        __slots__ = ((
            'name',                         #   String
        ))


        def __init__(self, name):
            self.name = name


        def convert_crystal_to_python(self, path):
            return Python_Statement_Import(self.name)


    #
    #   Python_ParseTree
    #
    class Python_ParseTree(object):
        __slots__ = ((
            'statement_list',               #   List of Python_Statement_*
        ))


        def __init__(self):
            self.statement_list = []


        def append_statement(self, statement):
            self.statement_list.append(statement)


        def create_python_code(self, f):
            for v in self.statement_list:
                v.create_python_code(f)


    #
    #   Python_Statement_Comment_Many   - A multiline comment
    #   Python_Statement_Import         - An import
    #   Python_Statement_Print_1        - A print statement
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


    class Python_Statement_Import(object):
        __slots__ = ((
            'name',                         #   String
        ))


        def __init__(self, name):
            self.name = name


        def create_python_code(self, f):
            f.write(arrange('import {}\n', self.name))


    class Python_Statement_Print_1(object):
        __slots__ = ((
            'argument',                     #   Any
        ))


        def __init__(self, argument):
            self.argument = argument


        def create_python_code(self, f):
            f.write(arrange('print({!r})\n', self.argument))


    #
    #   Z_Package
    #
    class Z_Package(object):
        __slots__ = ((
            'crystal_parse_tree',           #   Crystal_ParseTree
        ))


        def __init__(self, crystal_parse_tree):
            self.crystal_parse_tree = crystal_parse_tree


        #
        #   Z.package.Crystal (line 9 for "Vision.x")
        #
        def __getattribute__(self, name):
            if name == "crystal_parse_tree":
                return object.__getattribute__(self, name)

            self.crystal_parse_tree.append_statement(Crystal_Statement_Package(name))


    #
    #   Z
    #
    class Z_Mode(object):
        __slots__ = ((
            'crystal_parse_tree',           #   Crystal_ParseTree
            'package',                      #   Z_Package
        ))


        def __init__(self, crystal_parse_tree, package):
            self.crystal_parse_tree = crystal_parse_tree
            self.package            = package

        
        #
        #   Z.copyright (line 7 for "Vision.x")
        #
        @property
        def copyright(self):
            self.crystal_parse_tree.append_statement(Crystal_Statement_Copyright())


        #
        #   Z.line (line 9 for "Vision.x")
        #
        def line(self, argument):
            self.crystal_parse_tree.append_statement(Crystal_Statement_Line_1(argument))


    def create_Z():
        crystal_parse_tree = Crystal_ParseTree()

        package = Z_Package(crystal_parse_tree)
        
        Z = Z_Mode(crystal_parse_tree, package)

        return Z


    #
    #   Z
    #
    Z = create_Z()


    #
    #   Main Module (i.e.: "Vision.x")
    #
    main_module  = sys.modules['__main__']
    main_symbols = main_module.__dict__


    #
    #   Insert `Z` into the main module ("Vision.x")
    #
    def insert_main_symbol(k, v):
        assert k not in main_symbols

        main_symbols[k] = v


    insert_main_symbol('Z', Z)


    #
    #   Register `run_code_generator` to run when "*.x" exits.
    #
    @atexit.register
    def run_code_generator():
        python_parse_tree = Z.crystal_parse_tree.convert_crystal_to_python(input_path)

        python_path = arrange('{}.py', input_path[:-2])

        with open(python_path, 'w') as f:
            python_parse_tree.create_python_code(f)

        trace('Created {}', python_path)


#
#   if main path ends in ".x":
#       code_generator(main_path)
#
#   Other times, like when we run "python Vision.py" -- we don't run the code generator.
#
def call_code_generator__if_main_path_ends_in_dot_x():
    if len(sys.argv) == 1:
        main_path = sys.argv[0]

        if main_path.endswith('.x'):
            code_generator(main_path)


call_code_generator__if_main_path_ends_in_dot_x()
