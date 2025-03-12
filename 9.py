old_message = ""


def print_without_duplicates(mes):
    global old_message
    if mes != old_message:
        print(mes)
        old_message = mes


for i in range(5):
    print_without_duplicates(input())
