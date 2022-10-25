'''
    Task:
        Square Every Digit
'''

# Variables
str_1 = 'abracadabra'   # 5
str_2 = 'python'        # 1
str_3 = 'woff'          # 1
str_4 = 'door'          # 2
str_5 = 'nymph'         # 0
str_6 = 'rhythm'        # 0

# First solution
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in string:
        if char in vowels: count += 1

    return count

# Second solution
def count_vowels_2(string):
    # return sum(1 for let in string if let in "aeiouAEIOU")
    return sum(char in 'aeiouAEIOU' for char in string)

# Output
print(count_vowels(str_1))
print(count_vowels(str_2))
print(count_vowels(str_3))
print(count_vowels(str_4))
print(count_vowels(str_5))
print(count_vowels(str_6))

print(count_vowels_2(str_1))
print(count_vowels_2(str_2))
print(count_vowels_2(str_3))
print(count_vowels_2(str_4))
print(count_vowels_2(str_5))
print(count_vowels_2(str_6))
