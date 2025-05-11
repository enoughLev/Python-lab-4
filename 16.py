seq = [1, 1]
def continue_fibonacci_squence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence += [next_element]
    return sequence

# В исходной программе использовался метод __add__, который не меняется исходный массив, а создает новый

continue_fibonacci_squence(seq, 5)
print(*seq)

