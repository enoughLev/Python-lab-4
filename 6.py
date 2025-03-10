test_string = str(input())


def check_brackets(brack):
    stack = []

    for char in brack:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "NO"
            stack.pop()

    if not stack:
        return "YES"
    else:
        return "NO"


print(check_brackets(test_string))
