first = [1, 2, 3]
second = [4, 5, 6]

first_content = first[:]
second_content = second[:]

def swap(first, second):
    first[:], second[:] = second[:], first[:]
    
swap(first, second)

print(first, second)