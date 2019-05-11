#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Test_Integer - Test the `Integer` interface.
#


from    Capital.Core                    import  trace
from    Capital.Integer                 import  conjure_integer


def command_test_integer():
    seven = conjure_integer(7)

    trace('Passed: Integer Test')
