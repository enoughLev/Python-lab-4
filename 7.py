input_word = input()


def palindrome(word):
    if len(word) % 2 == 0:
        i = int(len(word) / 2)
        if word[:i] == word[:i - 1:-1]: return "Палиндром"
    else:
        i = int(len(word) / 2)
        if word[:i] == word[:i:-1]: return "Палиндром"

    return "Не палиндром"


print(palindrome(input_word))
