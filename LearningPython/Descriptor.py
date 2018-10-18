#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Descriptor')
def module():
    import sys

    Python_BuiltIn   = __import__('__builtin__'  if is_python_2 else   'builtins')

    object = Object
    absent = Object()
    hasattr = Python_BuiltIn.hasattr


    def _PyType_Lookup(model, name):
        '''Based on `_PyType_Lookup` in "Objects/typeobject.c"'''

        mro = model.__mro__

        if mro is none:
            return absent

        for m in mro:
            symbol_table = m.__dict__

            if name in symbol_table:
                return symbol_table[name]

        return absent


    def lookup__tp_descr_get(model):
        tp_descr_get = _PyType_Lookup(model, '__get__')

        return tp_descr_get


    def has__tp_descr_set(model):
        tp_descr_set = _PyType_Lookup(model, '__set__')

        return tp_descr_set is not absent


    #
    #   Reproduction of `object.__getattribute__`
    #
    def PyObject_GenericGetAttr(instance, name):
        '''Based on `PyObject_GenericGetAttr` in "Objects/object.c"'''

        instance_type = type(instance)

        descriptor = _PyType_Lookup(instance_type, name)

        if descriptor is absent:
            get = absent
        else:
            descriptor_type = type(descriptor)

            get = lookup__tp_descr_get(descriptor_type)

            if (get is not absent) and (has__tp_descr_set(descriptor_type)):
                #
                #   "Data Descriptor" (a `__set__` method exists) has precedence.
                #
                return get(descriptor, instance, instance_type)

        if instance_type.__dictoffset__:
            instance__mapping = instance.__dict__

            if name in instance__mapping:
                return instance__mapping[name]

        if get is not absent:
            return get(descriptor, instance, instance_type)

        raise AttributeError("cannot find attribute `{}` in instance of `{}`".format(name, instance_type.__name__))


    #
    #   Reproduction of `type.__getattribute__`
    #
    def type_getattro(model, name):
        '''Based on `type_getattro` in "Objects/type_object.c"'''

        metatype = type(model)

        descriptor = _PyType_Lookup(metatype, name)

        if descriptor is absent:
            get = absent
        else:
            descriptor_type = type(descriptor)

            get = lookup__tp_descr_get(descriptor_type)

            if (get is not absent) and (has__tp_descr_set(descriptor_type)):
                #
                #   "Data Descriptor" (a `__set__` method exists) has precedence.
                #
                return get(descriptor, instance, instance_type)

        symbol = _PyType_Lookup(model, name)

        if symbol is not absent:
            #
            #   Implement descriptor functionality, if any
            #
            symbol_type = type(symbol)

            symbol_get = lookup__tp_descr_get(symbol_type)

            if symbol_get is not absent:
                #
                #   None 2nd argument indicates the descriptor was
                #   found on the target object itself (or a base)
                #
                return symbol_get(symbol, None, model)

            return symbol

        if get is not absent:
            return get(descriptor, instance, instance_type)

        raise AttributeError("cannot find attribute `{}` in class `{}`".format(name, instance_type.__name__))


    @share
    def show_descriptor():
        print('=== Object example  ===')
        class Readonly_Descriptor(Object):
            __slots__ = ((
                'value',
            ))


            def __init__(self, value):
                self.value = value


            def __get__(self, object, object_type):
                return self.value


        class Data_Descriptor(Object):
            __slots__ = ((
                'value',
            ))


            def __init__(self, value):
                self.value = value


            def __get__(self, object, object_type):
                return self.value


            def __set__(self, object, value):
                self.value = value


        class Point(Object):
            __slots__ = ((
                '__dict__',
                '_y',
            ))

            def __init__(self, x, y):
                self.x = x
                self.y = y
                self._y = 1


        p23 = Point(2, 3)


        Point.x = Readonly_Descriptor(4)
        Point.y = Data_Descriptor(5)
        Point.z = Readonly_Descriptor(6)

        p23.y = 7       #   Uses the Data_Descriptor

        print("p23.x: %d   #   p23.__dict__['x']; *IGNORES* ReadOnly_Descriptor" % p23.x)
        print("p23.y: %d   #   type(p23).__dict__['y'].__get__(p23, Point)" % p23.y)
        print("p23.z: %d   #   type(p23).__dict__['z'].__get__(p23, Point)" % p23.z)
        print('')
        print("PyObject_GenericGetAttr(p23, 'x'):  %d" % PyObject_GenericGetAttr(p23, 'x'))
        print("PyObject_GenericGetAttr(p23, 'y'):  %d" % PyObject_GenericGetAttr(p23, 'y'))
        print("PyObject_GenericGetAttr(p23, 'z'):  %d" % PyObject_GenericGetAttr(p23, 'z'))


        print('')
        print('=== Type example  ===')

        def get_1(self, a, b):
            return 1

        def get_2(a, b):
            return 2

        class Descriptor(object):
            __get__ = get_1

        class Not_A_Descriptor(object):
            def __init__(self):
                self.__get__ = get_2

            def __repr__(self):
                return '<Not_A_Descriptor instance>'

        class Parent(object):
            __slots__ = (())

            x = Descriptor()
            y = Not_A_Descriptor()

        class Child(Parent):
            __slots__ = (())

        #
        #   Copied from https://docs.python.org/3/howto/descriptor.html
        #
        def __getattribute__(self, key):
            "Emulate type_getattro() in Objects/typeobject.c"
            v = object.__getattribute__(self, key)
            if hasattr(v, '__get__'):
                return v.__get__(None, self)
            return v


        print('Child.x: %s' % Child.x)
        print('Child.y: %s' % Child.y)

        print("type.__getattribute__(Child, 'x'): %s" % type.__getattribute__(Child, 'x'))
        print("type.__getattribute__(Child, 'y'): %s" % type.__getattribute__(Child, 'y'))

        try:
            print("__getattribute__(Child, 'x'): %s" % __getattribute__(Child, 'x'))
            print("__getattribute__(Child, 'y'): %s  ***WRONG***" % __getattribute__(Child, 'y'))
        except AttributeError as e:
            #
            #   Catch `AttributeError: 'type' object has no attribute 'x'`
            #
            pass

        print("type_getattro(Child, 'x'): %s" % type_getattro(Child, 'x'))
        print("type_getattro(Child, 'y'): %s  ***CORRECT***" % type_getattro(Child, 'y'))
