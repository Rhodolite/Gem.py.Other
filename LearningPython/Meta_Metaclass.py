#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Meta_Metaclass')
def module():
    show_hidden = 0


    transport('Capital.Meta_Metaclass',             'Meta_Metaclass')


    @share
    def show_meta_metaclass():
        blank()

        with indent('show_meta_metaclass:', prefix = 2):
            with indent(arrange('%s:', Meta_Metaclass.__name__), prefix = 2):
                line('Meta_Metaclass:  %s', Meta_Metaclass)
                line('Meta_Metaclass.inspect: %s', Meta_Metaclass.inspect)

            blank()

            show_class_members(Meta_Metaclass, show_hidden = show_hidden)
