#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Z.BuiltIn                       import  Python_String


#
#   AN ENUMERATION.
#
#       In this file we are creating an enumeration with three enumerators.
#
#       We really want to say something like the following:
#
#           enumeration TreeContext
#               delete
#               load
#               store
#
#   HOWEVER:
#
#       python does not support enumerations directly.
#
#   INSTEAD:
#
#       So instead we create a `TreeContext` class (which is our enumeration).
#
#       Then we create three instances of this class (which is our three
#       enumerators).
#
#           `.delete`  - The enumerator "delete"
#           `.load`    - The enumerator "load"
#           `.store`   - The enumerator "store".
#
#   FUTURE:
#
#       In the future we our code generator will support enumreators directly.
#
#       When translating to python, it will translate to code similiar to
#       what is below.
#
#       When translating to other languages, that have direct support for
#       enumerations, it will translate to code that uses the language support
#       for enumerations.
#


#
#   enumeration - When used as an annotation, does nothing!
#
#       The annotation `@enumeration` is only used for clarity, to mark a class
#       as *NOT* really, but an enumeration.
#
def enumeration(classification):
    return classification


#
#   Tree Context - Tells the context in which to interpret an expression.
#
#       tree_context_delete     - Save context (i.e.: "delete" a value).
#       tree_context_load       - Load context (i.e.: "get" a value).
#       tree_context_save       - Save context (i.e.: "SET" a value).
#
#   Consider the following statements being turned into a parse tree:
#
#       a.b = c.d
#       del e.f
#
#   In the parse tree, we will have the following tree contexts:
#
#       `a`     - tree context_load   (because we need to "get" `a` to "SET" `a.b`)
#       `a.b`   - tree context_save   (because we need to "SET" `a.b`)
#       `c`     - tree context_load   (because we need to "get" `c` to "get" `c.d`)
#       `c.d`   - tree context_load   (because we need to "get" `c.d`)
#       `e`     - tree context_load   (because we need to "get" `e` to "delete" `e.f`)
#       `e.f`   - tree context_delete (because we need to "delete" `e.f`)
#
#   These are named `*_load` and `*save` since that matches what they are called in
#   `_ast` (the python abstract syntax tree module).
#
#   Also they are not called `*_get` and `*_set` since these have a hamming
#   distance of one (i.e.: differ by one character) -- and are thus too
#   easy to confuse with each other.
#
#   (NOTE: For the same reason we use "SET" in the comment above to make
#   it differ by three characters from "get").
#
#   The following is how we convert `_ast` instances:
#
#       _ast instance of        converted to
#       ----------------        ------------
#       _ast.Delete             tree_context_delete
#       _ast.Load               tree_context_load
#       _ast.Store              tree_context_store
#
#   NOTE:
#       Here we fake a `.name` member, by *NOT* using a real member,
#       but instead inheriting from `Python_String` (i.e.: `str`).
#
#       Whenever we want to access our [fake] `.name` member, we instead
#       use `self`.
#
#       For example, below in `TreeContext.__repr__`, we refer to our [fake]
#       `.name` member as `self` (since `self` is both our own instance and also
#       our own [fake] `.name` member).
#
#   NOTE:
#       Later we'll turn this back into a normal class (with one member
#       named `.name`) -- and our code generator will either:
#
#           1.  Leave it as a class with one member; OR
#           2.  "Optimize" it to a class inherited from `Python_String`
#
#       Depending on the code generation option we use.
#
#       For now we demonstrate this as a "optimized" class inherited from
#       `Python_String` for educational purposes -- as a simple example
#       of how a class can inherit from `Python_String`.
#
if 0:
    #
    #   DISABLED CODE:
    #
    #       Here is how the `TreeContext` class would look if we were
    #       declaring it normally with a normal `.name` member.
    #
    from    Z.BuiltIn                   import  Python_Object


    @enumeration
    class TreeContext(Python_Object):
        __slots__ = ((
            'name',                         #   Python_String
        ))


        def __init__(self, name):
            self.name = name


        def __repr__(self):
            return arrange('<TreeContext {}>', self.name)
else:
    #
    #   ACTUAL CODE:
    #
    #       Here is the actual `TreeContext` class, where we inherit from
    #       `Python_String`, and our [fake] `.name` member does not exist.
    #
    #       As explain above, we simply use `self` when we want to access
    #       our [non-existent] [fake] `.name` member.
    #
    @enumeration
    class TreeContext(Python_String):
        __slots__ = (())


        #__init__ - inherited from `Python_String.__init__` (i.e.: `str.__init__`).


        def __repr__(self):
            #
            #   NOTE:
            #       `self` is *ALSO* our `.name` member -- stored internally as
            #       a Python String.
            #
            #       See comments above, for a more complete explanation.
            #
            #       Compare this version of `TreeContext.__repr__` to
            #       the `.__repr__` version in the DISABLED code above.
            #
            return arrange('<TreeContext {}>', self)


        if 0:
            #
            #   DISABLED CODE:
            #
            #       Here is how we would create a `.name` attribute, that emulates
            #       a `.name` member.
            #
            #       We just say the `.name` attribute is actually `self`.
            #
            #       Since no code actually uses the `.name` member, we don't
            #       actually have to declare a `.name` attribute!
            #
            @property
            def name(self):
                return self


#
#   Now we declare our three enumerators.
#
#       (In python, we have to declare them outside of the class, since they
#       use the class constructor to construct themselves).
#
TreeContext.delete = TreeContext('delete')
TreeContext.load   = TreeContext('load')
TreeContext.store  = TreeContext('store')
