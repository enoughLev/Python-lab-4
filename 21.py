fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)

def defractalize(lst, parent=None):

    i = 0
    while i < len(lst):
        item = lst[i]
        if isinstance(item, list):
            if parent is not None and item == parent:
                lst.pop(i)
                continue
            else:
                defractalize(item, lst)
        i += 1

print(fractal)
defractalize(fractal)
print(fractal)