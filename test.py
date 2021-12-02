c = 0
with open('test.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    for r in range(0, len(lines)):
        a = lines[c]
        if a == 'create file':
            print('CF')
        elif a == 'name = "hello.txt"':
            print('N+"h.t"')
        elif a == 'edit file':
            print('EF')
        elif a == 'text = "hello"':
            print('t+"h"')
        if c < len(lines):
            c += 1