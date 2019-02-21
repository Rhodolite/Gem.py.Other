#
#   The following program will print:
#
#       I am constructing: <Build_Point vacant vacant> ...
#       ... continuing to construct: <Build_Point 7 vacant> ...
#       ... done constructing: <Build_Point 7 1>
#       seventy_one: <Immutable_Point 7 1>
#       I am destroying: <Destroy_Point 7 1> ...
#       ... continuing to destroy: <Destroy_Point vacant 1> ...
#       ... done destroying: <Destroy_Point vacant vacant>
#
#   Showing the various states any normal object in python goes through (during construction & destruction).
#
#   In the code below by using `Build_Point` and `Destroy_Point` we can gaurentee that `Immutable_Point` only
#   has one state (it exists) and all it's members are immutable (and never vacant).
#
#   This means that `Immutable_Point.__repr__` can *SAFETLY* access `self.x` and `self.y` without worrying
#   about `AttributeError` being throw due to `self.x` and/or `self.y` being vacant during construction or
#   destruction.
#
#   On the other hand `Build_Point.__repr__` and `Destroy_Point.__repr__` do have to worry about
#   about `AttributeError` being throw due to `self.x` and/or `self.y` being vacant during construction or
#   destruction.
#
#   They do this, via the alternate routine `portray_possibly_vacant_point` which carefully tests for this
#   condition.
# 
def module(f):
    f()


@module
def example():
    Python_Object = object
    none          = None


    def arrange(message, *arguments):
        return message.format(*arguments)

    def trace(message, *arguments):
        if arguments:
            message = message.format(*arguments)

        print(message)

    def portray_possibly_vacant_point(self):
        try:
            x_value = self.x
        except AttributeError as e:
            x_value = "vacant"
        try:
            y_value = self.y
        except AttributeError as e:
            y_value = "vacant"

        return arrange('<{} {} {}>', self.__class__.__name__, x_value, y_value)


    class Build_Point(Python_Object):
        __slots__ = ((
            'x',
            'y',
        ))

        def __init__(self, x, y):
            trace("I am constructing: {!r} ...", self)
            self.x = x
            trace("... continuing to construct: {!r} ...", self)
            self.y = y
            trace("... done constructing: {!r}", self)

        __repr__ = portray_possibly_vacant_point


    class Destroy_Point(Python_Object):
        __slots__ = ((
            'x',
            'y',
        ))

        def __init__(self, x, y):
            runtime_error = RuntimeError("Instances of `Destroy_Point`` may not be constructed, only destroyed")
            raise runtime_error

        def __del__(self):
            trace("I am destroying: {!r} ...", self)
            del self.x
            trace("... continuing to destroy: {!r} ...", self)
            del self.y
            trace("... done destroying: {!r}", self)

        __repr__ = portray_possibly_vacant_point


    class Immutable_Point(Python_Object):
        __slots__ = ((
            'x',
            'y',
        ))

        def __init__(self, x, y):
            runtime_error = RuntimeError("Instances of `Immutable_Point` may not be constructed, only transformed")
            raise runtime_error

        def __del__(self):
            #
            #   Transform myself to a `Destroy_point` before destructing ...
            #
            self.__class__ = Destroy_Point
            self.__del__()

        def __repr__(self):
            return arrange('<Immutable_Point {} {}>', self.x, self.y)


    def create_immutable_point(x, y):
        r = Build_Point(x, y)
        #   Now that `r` is fully built, and has no vacant slots, we can transform it to a `Immutable_Point`
        r.__class__ = Immutable_Point
        return r

    seventy_one = create_immutable_point(7, 1)
    trace('seventy_one: {!r}', seventy_one)
    seventy_one = none
