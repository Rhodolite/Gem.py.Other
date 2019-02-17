@module
def module():
    class PackageStatement(Python_Object):
        __slots__ = ((
            'name',                     #   ActualString
        ))


        def __init__(self, name):
            self.name = name


        def __repr__(self):
            return arrange('<PackageStatement {!r}>', self.name)


    class Z_Package(Python_Object):
        __slots__ = (())


        @property
        def Crystal(self):
            return z_package__Crystal


    class Z_Mode(Python_Object):
        __slots__ = (())


        @property
        def copyright(self):
            self.append_line(statement_copyright)


        @property
        def package(self):
            return z_package


    Z = Z_Mode()


    main_module  = python_find_loaded_module('__main__')
    main_symbols = main_module.__dict__

    lookup_main_symbol = main_symbols.get
    stash_main_symbol  = main_symbols.__setitem__


    assert lookup_main_symbol('Z') is none

    stash_main_symbol(intern_python_string('Z'), Z)

    trace('main_module: {}', main_module)
