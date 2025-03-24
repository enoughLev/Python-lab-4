one = int(input())
two = int(input())
three = 0

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def roman():
    global three

    three = one + two

    roman_one = int_to_roman(one)
    roman_two = int_to_roman(two)
    roman_three = int_to_roman(three)
    
    print(f"{roman_one} + {roman_two} = {roman_three}")

roman()
