================  Build_DumpToken  ================
#
#   Z.Build_DumpToken - Build lines of text from `.dump_token`
#


from    Capital.Build_Lines_of_NativeString     import  Build_Lines_of_NativeString
from    Capital.Core                            import  creator


#
#   Build_DumpToken - Build lines of text from `.dump_token`
#
#       Derived from `Build_Lines_of_NativeString` -- adds two methods:
#
#           .token_result        - Output the closing '>' (sometimes with a newline)
#           .token_result__brace - Output the closing '}' (sometimes with a newline)
#
class Build_DumpToken(Build_Lines_of_NativeString):
    __slots_ = (())


    def token_result(f, r, newline):
        if (r) and (newline):
            f.line('>')
            return False

        f.write('>')
        return r


    def token_result__brace(f, r, newline):
        if (r) and (newline):
            #{
            f.line('}')
            return False

        #{
        f.write('}')
        return r


@creator
def build_dump_token():
    return Build_DumpToken()

================

#
#   Empty Tuple of SyntaxTree
#
class EmptyTuple_of_SyntaxTree(tuple):
    __slots__ = (())


    def __repr__(self):
        return '<EmptyTuple_of_SyntaxTree>'


empty_tuple_of_syntax_tree = EmptyTuple_of_SyntaxTree()

#
#   SyntaxTree_None
#
class SyntaxTree_None(object):
    __slots__ = (())


    def __bool__(self):
        return False


    def __repr__(self):
        return '<SyntaxTree.None>'


    def dump_token(self, f):
        f.write('<none>')


syntax_tree_none = SyntaxTree_None()
