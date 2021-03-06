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
    module_path.insert(2, path_absolute(path_join(path_0, '../../UnitTest')))


    import Gem


@gem('Marble.Main')
def gem():
    require_gem('Marble.Core')
    require_gem('Marble.NestedConjure')


    @share
    def command_generate_ascii():
        require_gem("Marble.GenerateAscii");

        generate_ascii();


    @share
    def command_generate_test_portray_string():
        require_gem("Marble.GenerateTestPortrayString");

        generate_test_portray_string();


    def command_development():
        command_generate_test_portray_string()


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return create_nested_conjure('2017-2018', 'Joy Diamond')

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'ascii':
                return command_generate_ascii()

            if option == 'dev':
                return command_development()

            raise_runtime_error('unknown option: %r', option)
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
