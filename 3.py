def triangle(a, b, c):
    if (a + b > c) & (b + c > a) & (a + c > b):

        print("Это треугольник")
    else:
        print("Это не треугольник")


inp = input("Введите стороны треугольника через пробел: ").split()

triangle(int(inp[0]), int(inp[1]), int(inp[2]))
