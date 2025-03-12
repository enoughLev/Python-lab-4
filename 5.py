def number_to_words(num):
    output = []
    decimal = num // 10
    if decimal > 1:
        if decimal == 1 and num % 10 == 0:
            output = ["десять"]
        if decimal == 2:
            output = ["двадцать"]
        if decimal == 3:
            output = ["тридцать"]
        if decimal == 4:
            output = ["сорок"]
        if decimal == 5:
            output = ["пятьдесят"]
        if decimal == 6:
            output = ["шестьдесят"]
        if decimal == 7:
            output = ["семьдесят"]
        if decimal == 8:
            output = ["восемьдесят"]
        if decimal == 9:
            output = ["девяносто"]

    if num%10 != 0:
        if num % 10 == 1:
            output.append("один")
        if num % 10 == 2:
            output.append("два")
        if num % 10 == 3:
            output.append("три")
        if num % 10 == 4:
            output.append("четыре")
        if num % 10 == 5:
            output.append("пять")
        if num % 10 == 6:
            output.append("шесть")
        if num % 10 == 7:
            output.append("семь")
        if num % 10 == 8:
            output.append("восемь")
        if num % 10 == 9:
            output.append("девять")

    if decimal == 1:
        if num % 10 == 1:
            output = ["одиннадцать"]
        if num % 10 == 2:
            output = ["двенадцать"]
        if num % 10 == 3:
            output = ["тринадцать"]
        if num % 10 == 4:
            output = ["четырнадцать"]
        if num % 10 == 5:
            output = ["пятнадцать"]
        if num % 10 == 6:
            output = ["шестнадцать"]
        if num % 10 == 7:
            output = ["семнадцать"]
        if num % 10 == 8:
            output = ["восемнадцать"]
        if num % 10 == 9:
            output = ["девятнадцать"]

    return output


while True:
    inp = int(input())
    if inp != 0:
        print(' '.join(number_to_words(inp)))
    else:
        break