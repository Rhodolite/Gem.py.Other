#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Show')
def module():
    #
    #   See Capital.Output
    #
    #       flush_standard_output = sys.stdout.flush
    #       write_standard_output = sys.stdout.write
    #
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'false')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'Method')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'portray')
    transport('Capital.Core',                       'privileged')
    transport('Capital.Core',                       'true')
    transport('Capital.Core',                       'Tuple')
    transport('Capital.Core',                       'type')
    transport('Capital.Exception',                  'exit_clause')
    transport('Capital.Exception',                  'SystemExit')
    transport('Capital.Output',                     'flush_standard_output')
    transport('Capital.Output',                     'write_standard_output')
    transport('Capital.Traceback',                  'print_exception_chain')


    #
    #   NOTE:
    #       A version of `line` also exists in `Capital.Core`, however the code is reproduced here for learning
    #       purposes.
    #
    #       Also this version is slightly different, in that `line` after `partial` outputs an extra space.
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
    def import_Python_Platform():
        import platform as Python_Platform

        return Python_Platform


    import sys      as Python_System

    Python_Platform = import_Python_Platform()



    #
    #   python_version
    #
    def python_version():
        version_information = Python_System.version_info
        build_information   = Python_Platform.python_build()

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
    #   show
    #
    @share
    def show():
        #
        #   Version
        #
        with safe('Python version'):
            line(python_version())


        #
        #   Executable
        #
        with safe('Python executable'):
            lookup_Python_System = Python_System.__dict__.get
            executable           = lookup_Python_System('executable')

            line('unknown'   if executable is none else   portray(executable))
