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

print
print
print '#'
print '#  Singletons'
print '#'
for [name, operator] in [
    [   'add',                   '{+}',    ],
    [   'binary-and',            '{&}'     ],
    [   'binary-exclusive-or',   '{^}'     ],
    [   'different',             '{is-not}'],
    [   'equal',                 '{==}'    ],
    [   'greater-than',          '{>}'     ],
    [   'greater-than-or-equal', '{>=}'    ],
    [   'identity',              '{is}'    ],
    [   'less-than',             '{<}'     ],
    [   'less-than-or-equal',    '{<=}'    ],
    [   'not-equal',             '{!=}'    ],
    [   'in',                    '{in}'    ],
    [   'divide',                '{/}'     ],
    [   'not-in',                '{not-in}'],
    [   'floor-divide',          '{//}'    ],
    [   'invert',                '{~}'     ],
    [   'left-shift',            '{<<}'    ],
    [   'and',                   '{and}'   ],
    [   'or',                    '{or}'    ],
    [   'modify-subtract',       '{-=}'    ],
    [   'modulus',               '{%}'     ],
    [   'multiply',              '{*}'     ],
    [   'negative',              '{-}'     ],
    [   'not',                   '{not}'   ],
    [   'positive',              '{+}'     ],
    [   'power',                 '{**}'    ],
    [   'right-shift',           '{>>}'    ],
    [   'subtract',              '{-}'     ],
]:
    MetaName = 'Tree_{}_Operator' .format('_'.join(s.capitalize()   for s in name.split('-')))
    variable = 'tree_{}_operator'.format(name)

    display_MetaName = repr(MetaName) + ','
    display_operator = repr(operator)

    print '{} = create_TOE({} {})'.format(variable.ljust(35), display_MetaName.ljust(38), display_operator.ljust(10))
#
#       "_Leaf" is used:
#
#           1)  Indicate this is a leaf node (nothing derived from it); but
#
#           2)  *Mostly* so as to have a different name than interface `Tree_Suite`.
