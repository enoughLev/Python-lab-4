friends = {"Arina": ["Marina", "Arthur"], "Marina": ["Arina", "Mark"]}


def add_friends(name_of_person, list_of_friends):
    if name_of_person in friends:
        [friends[name_of_person].append(elem) for elem in list_of_friends]
    else:
        friends.setdefault(name_of_person, list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    if name_of_person1 in friends:
        return name_of_person2 in friends[name_of_person1]
    return False


def print_friends(name_of_person):
    print(" ".join(sorted(*[value for key, value in friends.items() if key == name_of_person])))


print_friends("Arina")
print_friends("Marina")
print(are_friends("Arina", "Marina"))
print(are_friends("Arina", "Mark"))
add_friends("Arina", ["Mark"])
add_friends("Marina", ["Arthur"])
print(are_friends("Arina", "Mark"))
print_friends("Arina")
print_friends("Marina")
