#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module
def module():
    #
    #   Python Proxy Members
    #
    #       python_object_proxy_members     - A proxy mapping to symbol table of `Python_Object`
    #
    #           In python, when accssing the `.__dict__` of a class, it returns a `dict-proxy`, which give a read-only
    #           view of the mapping.
    #
    #   ALSO:
    #       Each time you use `.__dict__` it creates a *NEW* proxy.
    #
    #       Hence, we save the proxy it creates, and only create it once.
    #
    python_object_proxy_members = Python_Object.__dict__


    #
    #   Python_Object members
    #
    #       python_object_class_attribute   - See long explanation below
    #
    python_object_class_attribute            = python_object_proxy_members['__class__']
    python_object_operator_delete_attribute  = python_object_proxy_members['__delattr__']
   #python_object_documentation_member       = python_object_proxy_members['__doc__']
   #python_object_operator_format            = python_object_proxy_members['__format__']
    python_object_operator_get_attribute     = python_object_proxy_members['__getattribute__']
   #python_object_operator_hash              = python_object_proxy_members['__hash__']
    python_object_constructor                = python_object_proxy_members['__init__']
    python_object_operator_new               = python_object_proxy_members['__new__']
   #python_object_operator_reduce            = python_object_proxy_members['__reduce__']
   #python_object_operator_reduce_extended   = python_object_proxy_members['__reduce_ex__']
    python_object_operator_representation    = python_object_proxy_members['__repr__']
    python_object_operator_set_attribute     = python_object_proxy_members['__setattr__']
    python_object_operator_sizeof            = python_object_proxy_members['__sizeof__']
    python_object_operator_convert_to_string = python_object_proxy_members['__str__']
   #python_object_operator_subclass_hook     = python_object_proxy_members['__subclasshook__']

    if is_python_3:
        python_object_operator_introspection = python_object_proxy_members['__dir__']

   #if is_python_3:
   #    python_object_operator_equal                 = python_object_proxy_members['__eq__']
   #    python_object_operator_greater_than          = python_object_proxy_members['__gt__']
   #    python_object_operator_greater_than_or_equal = python_object_proxy_members['__ge__']
   #    python_object_operator_less_than             = python_object_proxy_members['__lt__']
   #    python_object_operator_less_than_or_equal    = python_object_proxy_members['__le__']
   #    python_object_operator_not_equal             = python_object_proxy_members['__ne__']


    if false:
        #
        #   When enabled, prints the followng:
        #
        #   % Crystal.py: ===  python_object_*  ===
        #   % Crystal.py:               class_attribute: <attribute '__class__' of 'object' objects>
        #   % Crystal.py:     operator_delete_attribute: <slot wrapper '__delattr__' of 'object' objects>
        #   % Crystal.py:          documentation_member: 'The most base type'
        #   % Crystal.py:               operator_format: <method '__format__' of 'object' objects>
        #   % Crystal.py:        operator_get_attribute: <slot wrapper '__getattribute__' of 'object' objects>
        #   % Crystal.py:                 operator_hash: <slot wrapper '__hash__' of 'object' objects>
        #   % Crystal.py:                   constructor: <slot wrapper '__init__' of 'object' objects>
        #   % Crystal.py:                  operator_new: <built-in method __new__ of type object at 0x8f8740>
        #   % Crystal.py:               operator_reduce: <method '__reduce__' of 'object' objects>
        #   % Crystal.py:      operator_reduce_extended: <method '__reduce_ex__' of 'object' objects>
        #   % Crystal.py:       operator_representation: <slot wrapper '__repr__' of 'object' objects>
        #   % Crystal.py:        operator_set_attribute: <slot wrapper '__setattr__' of 'object' objects>
        #   % Crystal.py:               operator_sizeof: <method '__sizeof__' of 'object' objects>
        #   % Crystal.py:    operator_convert_to_string: <slot wrapper '__str__' of 'object' objects>
        #   % Crystal.py:        operator_subclass_hook: <method '__subclasshook__' of 'object' objects>
        #   % Crystal.py: ===  Done  ===
        #
        trace('===  python_object_*  ===')
        trace('               class_attribute: {!r}', python_object_class_attribute)
        trace('     operator_delete_attribute: {!r}', python_object_operator_delete_attribute)
        trace('          documentation_member: {!r}', python_object_documentation_member)
        trace('               operator_format: {!r}', python_object_operator_format)
        trace('        operator_get_attribute: {!r}', python_object_operator_get_attribute)
        trace('                 operator_hash: {!r}', python_object_operator_hash)
        trace('                   constructor: {!r}', python_object_constructor)
        trace('                  operator_new: {!r}', python_object_operator_new)
        trace('               operator_reduce: {!r}', python_object_operator_reduce)
        trace('      operator_reduce_extended: {!r}', python_object_operator_reduce_extended)
        trace('       operator_representation: {!r}', python_object_operator_representation)
        trace('        operator_set_attribute: {!r}', python_object_operator_set_attribute)
        trace('               operator_sizeof: {!r}', python_object_operator_sizeof)
        trace('    operator_convert_to_string: {!r}', python_object_operator_convert_to_string)
        trace('        operator_subclass_hook: {!r}', python_object_operator_subclass_hook)
        trace(' object_operator_introspection: {!r}', python_object_operator_introspection)

        if is_python_3:
            trace('  object_operator_introspection: {!r}', python_object_operator_introspection)

        if is_python_3:
            trace('                operator_equal: {!r}', python_object_operator_equal)
            trace('         operator_greater_than: {!r}', python_object_operator_greater_than)
            trace('operator_greater_than_or_equal: {!r}', python_object_operator_greater_than_or_equal)
            trace('            operator_less_than: {!r}', python_object_operator_less_than)
            trace('   operator_less_than_or_equal: {!r}', python_object_operator_less_than_or_equal)
            trace('            operator_not_equal: {!r}', python_object_operator_not_equal)

        trace('===  Done  ===')


    #
    #<Python_Object::__class__>
    #

    #
    #   python_object_class_attribute  - The attribute descriptor stored in `Python_Object::__class__`.
    #
    #       NOTE:
    #           By "::" we mean the symbol stored in `Python_Object.__dict__`
    #
    #           We cannot use `Python_Object.__class__` since this is overriden by the descriptor
    #           in metaclass of `Python_Object` (i.e.: `Python_Type`) and returns the type of `Python_Object
    #           (i.e.: The metaclass of `Python_Object` which is `Python_Type).
    #
    #       Confusing NOTE:
    #           Of course, the actual descriptor in `Python_Type::__class__` is inherited from
    #           `Python_Object::__class__`, and is the exact descriptor we are trying to get.
    #
    #           However, again, `Python_Object.__class__` will *actually* call this descriptor,
    #           and retreive the type of `Python_Object` (which again is `Python_Type`).
    #
    #           All this can be seen in the asserts below.
    #
    #python_object_class_attribute = python_object_proxy_members['__class__']       #   Done above


    #
    #   The following:
    #
    #       `Python_Object.__class__`
    #
    #   Means:
    #
    #       `python_type(Python_Object)::__class__.__get__(Python_Object)`
    #
    #
    assert Python_Object.__class__ is Python_Type


    #
    #   As above:
    #
    #       `python_object_class_attribute`    IS      `Python_Object::__class__`
    #       `python_object_class_attribute`    IS      `Python_Type  ::__class__`  (inherited from `Python_Object`).
    #
    #   Here we use the descriptor, and call its `.__get__` method to emulate the query `Python_Object.__class__`
    #
    #   Hence:
    #
    #       `Python_Object.__class__`
    #
    #   Means:
    #
    #       `Python_Type::__class__.__get__(Python_Object)`
    #
    #   Which is (due to `Python_Type::__class__` being inherited from `Python_Object::__class__`):
    #
    #       `Python_Object::__class__.__get__(Python_Object)`
    #
    #   Means:
    #
    #       `python_object_proxy_members['__class__'].__get__(Python_Object)`
    #
    #   Means:
    #
    #       `python_object_class_attribute.__get__(Python_Object)`
    #
    assert python_object_proxy_members['__class__'].__get__(Python_Object) is Python_Type
    assert python_object_class_attribute           .__get__(Python_Object) is Python_Type


    #
    #   python_query_class_attribute    - Same as using `.__class__` in a query context (get context).
    #
    #   python_stash_class_attribute    - Same as using `.__class__` in a set context
    #                                     (i.e.: change the "class" of an instance, transforming the instance to
    #                                     a different class).
    #
    python_query_class_attribute = python_object_class_attribute.__get__
    python_stash_class_attribute = python_object_class_attribute.__set__

    #</Python_Object::__class__>


    #
    #   Share
    #
    share(
            python_query_class_attribute = python_query_class_attribute,
            python_stash_class_attribute = python_stash_class_attribute,
        )
