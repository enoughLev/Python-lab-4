arr = [1, 2, 3, 4, 5, 6]

# Метод reverse() - изменяет исходный список, метод reversed() - возвращает новый объект
# Исходя из постановки задачи, необходимо использовать reversed()
def mirror(arr):
    mirrored_part = reversed(arr)
    arr += mirrored_part
    return arr

mirror(arr)
print(*arr)

