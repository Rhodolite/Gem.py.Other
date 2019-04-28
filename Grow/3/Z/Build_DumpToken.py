#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Build_DumpToken - Build lines of text from `.dump_*_token`
#


from    Capital.Build_Lines_of_NativeString     import  Build_Lines_of_NativeString
from    Capital.Core                            import  creator

if __debug__:
    from    Capital.SimpleContextLifecycle  import  fact_is_lifecycle_entered



#
#   Build_DumpToken - Build lines of text from `.dump_*_token`
#
#       Derived from `Build_Lines_of_NativeString` -- adds a few methods:
#
#           .greater_than_sign  - Write a '>' (no newline).
#           .space              - Write a ' ' (no newline).
#
class Build_DumpToken(Build_Lines_of_NativeString):
    __slots_ = (())


    def greater_than_sign(self):
        position = self.position

        if position:
            assert fact_is_lifecycle_entered(self.lifecycle)

            self.position = position + 1

            self._f__write('>')
            return

        self.write('>')


    def space(self):
        position = self.position

        if position:
            assert fact_is_lifecycle_entered(self.lifecycle)

            self.position = position + 1

            self._f__write(' ')
            return

        self.write(' ')


@creator
def build_dump_token():
    return Build_DumpToken()
