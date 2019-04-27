#
#   convert_none
#
#       Convert `None` to `None`.
#
#   FUTURE:
#       Will convert `None` to `SyntaxTree_None`.
#
#       For now, we are not doing any translations of native python types, so just "converting" `None` as `None`.
#
def convert_none(self):
    assert fact_is_native_none(self)

    return None
import _ast
for k in dir(_ast):
    if k not in ['PyCF_ONLY_AST', '__doc__', '__name__', '__package__', '__version__']:
        print '{}: {}, {}'.format(k, getattr(_ast, k), getattr(_ast, k).__bases__)

