#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


version = 1
version = 16


#
#   Imports
#
from    sys                             import  argv            as  python_program_arguments

from    Capital.Core                    import  arrange
from    Capital.Core                    import  ERROR
from    Capital.Core                    import  FATAL
from    Capital.Core                    import  NativeBoolean
from    Capital.Core                    import  trace
from    Capital.Global                  import  capital_globals
from    Capital.String                  import  conjure_string
from    Capital.String                  import  empty_string
from    Z.Build_DumpToken               import  build_dump_token
from    Z.Path                          import  path_to_file_in_Z_directory


#
#   parent_path__good_enough_for_now - return the ABSOLUTE path name to the parent directory
#
#       There is no easy way to calculate the parent path without having ".."
#       stuck as part of the path path.
#
#       For now, we take the easy way out and just call `python_path_absolute`
#       to remove any ".." in the path name.
#
#       FUTURE:
#           We'll do this better.
#
#           But for now, we don't want to concentrate too much on a module to
#           deal with path names, so we just take the easy way out.
#
def parent_path__good_enough_for_now(path):
    return python_path_absolute(python_path_join(path, '..'))


def command_parse(version):
    vision_path = path_to_file_in_Z_directory('ParseTest.py')

    with open(vision_path) as f:
        source = f.read()

    if version == 1:
        from    Z.Tree.Convert_Module_V1    import  compile_to_syntax_tree_v1

        tree = compile_to_syntax_tree_v1(source, vision_path)
    else:
        from    Z.Tree.Convert_Module_V2    import  compile_to_syntax_tree_v2
        from    Z.Tree.Convert_Zone         import  fill_convert_zone

        z = fill_convert_zone(version)

        tree = compile_to_syntax_tree_v2(z, source, vision_path)

    #trace('tree: {}', tree)

    with build_dump_token() as f:
        tree.dump_module_tokens(f)

    for s in f:
        trace('{}', s)


def command_string():
    hello   = conjure_string("hello")
    crystal = conjure_string("crystal")

    assert empty_string is conjure_string("")
    assert hello        is conjure_string("hello")
    assert crystal      is conjure_string("crystal")

    assert NativeBoolean(empty_string) is False
    assert NativeBoolean(hello)        is True
    assert NativeBoolean(crystal)      is True

    assert len(empty_string) == 0
    assert len(hello)        == 5
    assert len(crystal)      == 7

    assert "hello crystal" == arrange('{} {}', hello, crystal)

    trace('Passed: String Test (version {})', capital_globals.string_version)


def command_development(version):
    command_parse(version)
   #command_string()


def USAGE(format, *arguments):
    program_name = python_program_arguments[0]

    ERROR(format, *arguments)
    FATAL("usage: python {} development", program_name)


def Z_main():
    command_line_arguments = python_program_arguments[1:]   #   Ignore the program name for command line arguments

    total_command_line_arguments = len(command_line_arguments)

    if total_command_line_arguments != 1:
        return USAGE("expected exactly 1 command line argument (got {} instead): {!r}",
                     total_command_line_arguments,
                     command_line_arguments)

    command = command_line_arguments[0]

    if command == 'development':
        return command_development(version)

    try:
        v = int(command)
    except ValueError:
        v = None

    if 1 <= v <= 16:
        return command_development(v)

    return USAGE('unknown command: {}', command)
