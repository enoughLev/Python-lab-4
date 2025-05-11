def matrix(n=1, m=None, a=0):
    if m is None:
        return [[0] * n for _ in range(n)]
    else:
        if a == 0:
            return [[0] * m for _ in range(n)]
        else:
            return [[a] * m for _ in range(n)]

rows1 = matrix(3)
rows2 = matrix(3, 2)
rows3 = matrix(2, 3, 8)

for row in rows1:
    print(*row)
print()

for row in rows2:
    print(*row)
print()

for row in rows3:
    print(*row)
print()