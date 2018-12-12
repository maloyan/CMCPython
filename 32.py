import fileinput
v = dict()
for line in fileinput.input():
    if line != '\n' and line[0] != '#':
        try:
            eq = line.find('=')
            if eq != -1:
                left = line[:eq]
                if not left.isidentifier():
                    raise Exception(f"invalid identifier '{left}'")

                right = line[eq + 1:]
                if right.find('=') != -1:
                    raise Exception(f"invalid assignment '{line[:-1]}'")

                v[left] = eval(right, v)
            else:
                print(eval(line, v))
            
        except Exception as e: print(e)
