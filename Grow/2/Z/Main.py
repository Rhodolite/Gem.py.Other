#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    _ast                            import  PyCF_ONLY_AST   as  python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE
from    sys                             import  argv            as  python_program_arguments

from    Z.Core                          import  arrange
from    Z.Core                          import  ERROR
from    Z.Core                          import  FATAL
from    Z.Core                          import  trace
from    Z.Path                          import  path_to_file_in_Z_directory


python_compile = compile                #   python builtin `compile`


def python__compile__to__abstract_syntax_tree(source, filename):
    return python_compile(
               source   = source,
               filename = filename,
               mode     = 'exec',
               flags    = python__COMPILE_FLAGS__ONLY__ABSTRACT_SYNTAX_TREE,
           )


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


def command_development():
    vision_path = path_to_file_in_Z_directory('Vision.z')

    with open(vision_path) as f:
        source = f.read()

    tree = python__compile__to__abstract_syntax_tree(source, vision_path)

    trace('tree: {}', tree)


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
        return command_development()

    return USAGE('unknown command: {}', command)
