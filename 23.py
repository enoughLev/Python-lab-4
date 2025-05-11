def matrix(n=None, m=None, a=None):
    matr = []
    if n == None:
        matr.append("0")
        return matr
    elif n > 0:
        for s in range(n):
            i = n
            row = []
            while i > 0:
                row.append("0")
                i = i - 1
            matr.append(row)
        return matr
    elif n > 0 and m > 0:
        for s in range(n):
              
            
rows = matrix(3)
#print(rows)
for row in rows:
    print(*row)