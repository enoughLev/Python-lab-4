matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(matr):
    matr = list(map(list, zip(*matr)))
    return matr

print(matrix)
print(transpose(matrix))
print(matrix)

