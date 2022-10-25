'''
    Task:
        Square Every Digit
'''

# Variables
number_1 = 3212     # 9414
number_2 = 2112     # 4114
number_3 = 0        # 0

# First solution
def square_every_digit(number):
    number_str = str(number)
    result_str = ''

    for digit in number_str:
        square = int(digit) ** 2
        result_str += str(square)

    return int(result_str)

# Second solution
def square_every_digit_2(number):
    return int(''.join(str(int(d) ** 2) for d in str(number)))

# Output
print(square_every_digit(number_1))
print(square_every_digit(number_2))
print(square_every_digit(number_3))

print(square_every_digit_2(number_1))
print(square_every_digit_2(number_2))
print(square_every_digit_2(number_3))