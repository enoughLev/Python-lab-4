def partial_sums(*args):
    result = []
    current_sum = 0
    for num in args:
        current_sum += num
        result.append(current_sum)
    return result



print(partial_sums(1, 2, 3, 4))
print(partial_sums(5, 10, -2))

print(partial_sums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(partial_sums(10,10,10,10,10,10,10))