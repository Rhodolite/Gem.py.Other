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
    module_path.insert(1, path_absolute(path_join(path_0, '../../Capital')))


    import Capital


@module('LearningPython.Main')
def module():
    require_module('LearningPython.Color_1')
    require_module('LearningPython.Color_2')
    require_module('LearningPython.Color_3')
    require_module('LearningPython.Color_4')
    require_module('LearningPython.Color_5')
    require_module('LearningPython.Descriptor')
    require_module('LearningPython.Development')
    require_module('LearningPython.Metaclass')
    require_module('LearningPython.Meta_Metaclass')
    require_module('LearningPython.Show')
    require_module('LearningPython.ObjectParts')
    require_module('LearningPython.TypeParts')


    @share
    def main(arguments):
        show()
        line()

        #show_object_parts()
        #show_type_parts()

        #show_color_1()
        #show_color_2()
        #show_color_3()
        #show_color_4()
        #show_color_5()

        show_metaclass()
        #show_meta_metaclass()
        #show_descriptor()

        #show_development()
