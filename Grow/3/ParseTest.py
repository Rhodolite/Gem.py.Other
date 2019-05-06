import a, b.c, d as e, g.h as i
from j.k import l, m as n

try:
    a = b = [x  for x in [1,2]] or c or d[1,...]
except X:
    a < b < c
except:
    pass

def f(): pass

@f
def g(): pass

@f
@g(2)
def h(): pass

class A(): pass
