import math

def solve(*coefficients):
    n = len(coefficients)
    if n == 0 or n > 3:
        return None

    if n == 3:
        a, b, c = coefficients
    elif n == 2:
        a = 0
        b, c = coefficients
    else:
        a = 0
        b = 0
        c = coefficients[0]

    if a == 0 and b == 0 and c == 0:
        return ["all"]

    if a == 0:
        if b == 0:
            if c == 0:
                return ["all"]
            else:
                return []
        else:
            return [-c / b]

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return [x1, x2]

print(solve())
print(solve(0))
print(solve(5))
print(solve(0, 0))
print(solve(0, 5))
print(solve(1, -3, 2))
print(solve(0, 0, 0))
print(solve(0, 0, 5))
print(solve(1, 2, 5))
print(solve(1, 0, -4))
