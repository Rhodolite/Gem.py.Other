import types


def line(message, *arguments):
    print(message.format(*arguments))


for k in dir(types):
    if k == '__builtins__':     continue
    if k == '__dict__':         continue

    line('{}: {}', k, types.__dict__[k])
