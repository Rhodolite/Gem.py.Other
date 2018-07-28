#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    path_0 = module_path[0]

    module_path.insert(0, path_absolute(path_join(path_0, '../')))
    module_path.insert(1, path_absolute(path_join(path_0, '../../Gem')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Tremolite')))


    import Gem


@gem('LearningPython.Main')
def gem():
    require_gem('Gem.Exception')                                        #   Adds `exit_clause` as a built-in
    require_gem('Gem.Output')
    require_gem('Gem.Traceback')


    from Gem import SystemExit                                          #   See Gem.Exception
    from Gem import flush_standard_output                               #   See Gem.Output      = sys.stderr.flush
    from Gem import write_standard_output                               #   See Gem.Output      = sys.stdout.write
    from Gem import print_exception_chain                               #   See Gem.Traceback


    #
    #   arrange
    #
    def arrange(format, *arguments):
        return format % arguments


    #
    #   line
    #
    position_cache  = [0]
    position        = Method(position_cache.__getitem__, 0)
    save_position   = Method(position_cache.__setitem__, 0)
    save_position_0 = Method(save_position, 0)


    def line(format = none, *arguments):
        if format is none:
            assert length(arguments) is 0

            write_standard_output('\n')
        else:
            if position() != 0:
                write_standard_output(' ' + (format % arguments   if arguments else   format) + '\n')
            else:
                write_standard_output((format % arguments   if arguments else   format) + '\n')

        flush_standard_output()
        save_position_0()



    def partial(format, *arguments):
        s = (format % arguments   if arguments else   format)

        write_standard_output(s)
        flush_standard_output()

        save_position(position() + length(s))


    #
    #   PrintHeader_and_PrintAndIgnoreExceptions
    #
    class PrintHeader_and_PrintAndIgnoreExceptions():
        __slots__ = ((
            'header',               #   String
        ))


        def __init__(t, header):
            t.header = header


        def __enter__(t):
            partial('%s ...', t.header)

            return t


        def __exit__(t, e_type, e, e_traceback):
            with exit_clause(e_type, e, e_traceback):
                if (e is None) or (e_type is SystemExit):
                    return

                if position() != 0:
                    line()

                print_exception_chain(e)

                #
                #   Swallow exception
                #
                return false


    def safe(header):
        return PrintHeader_and_PrintAndIgnoreExceptions(header)


    @privileged
    def import_PythonPlatform():
        import platform as PythonPlatform

        return PythonPlatform


    import sys      as PythonSystem

    PythonPlatform = import_PythonPlatform()



    #
    #   python_version
    #
    def python_version():
        version_information = PythonSystem.version_info
        build_information   = PythonPlatform.python_build()

        assert (type(build_information) is Tuple) and (length(build_information) == 2)

        return arrange('%d%s%s%s (%s %s)',
                       version_information.major,
                       (
                           ''   if version_information.minor == version_information.micro == 0 else
                           arrange('.%d', version_information.micro)
                       ),
                       (
                           ''   if version_information.micro == 0 else
                           arrange('.%d', version_information.micro)
                       ),
                       (
                           ''   if version_information.serial == 0 else
                           arrange('.%d', version_information.serial)
                       ),
                       build_information[0],
                       build_information[1])



    #
    #   Main
    #
    @share
    def main(arguments):
        #
        #   Version
        #
        with safe('Python version'):
            line(python_version())


        #
        #   Executable
        #
        with safe('Python executable'):
            lookup_PythonSystem = PythonSystem.__dict__.get
            executable          = lookup_PythonSystem('executable')

            line('unknown'   if executable is none else   portray(executable))
