my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#1
list_1 = [element for element in my_list if element < 5]
print("1.", list_1)

#2
list_2 = [element for element in my_list if element % 2 == 0]
print("2.", list_2)

#3
list_3 = [element*2 for element in my_list if element > 17]
print("3.", list_3)

#4
print("4.", end=' ')
last_number_4 = int(input())
list_4 = [(element + 1)**2 for element in range (last_number_4)]
print(list_4)

#5
print("5.", end=' ')
list_5 = [int(num) for num in input().split()]
print(' '.join([str(element**2) for element in list_5]))

#6
print("6.", end=' ')


