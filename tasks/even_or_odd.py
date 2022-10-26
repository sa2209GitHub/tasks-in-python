'''
    Task:
        Even or Odd
'''

# Variables
num_1 = 1   # 'Odd'
num_2 = 6   # 'Even'
num_3 = 9   # 'Odd'
num_4 = 18  # 'Even'
num_5 = 24  # 'Even'
num_6 = 33  # 'Odd'
num_7 = 64  # 'Even'
num_8 = 87  # 'Odd'
num_9 = 99  # 'Odd'

# Solution
def is_even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

# Output
print(is_even_or_odd(num_1))
print(is_even_or_odd(num_2))
print(is_even_or_odd(num_3))
print(is_even_or_odd(num_4))
print(is_even_or_odd(num_5))
print(is_even_or_odd(num_6))
print(is_even_or_odd(num_7))
print(is_even_or_odd(num_8))
print(is_even_or_odd(num_9))
