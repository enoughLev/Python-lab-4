num_list = [1, 2, 3]
str_num = "4 5 6 7"


def from_string_to_list(string, container):
    for i in range(len(string.split())):
        container += [int(string.split()[i])]
    return container


from_string_to_list(str_num, num_list)
print(*num_list)
