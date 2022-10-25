'''
    Task:
        Check Same Case
'''

# Variables
pair_1 = ['z', 'o']  #  1
pair_2 = ['W', 'G']  #  1
pair_3 = ['f', 'A']  #  0
pair_4 = ['K', 'w']  #  0
pair_5 = ['a', '#']  # -1
pair_6 = ['F', '3']  # -1
pair_7 = ['@', '$']  # -1

# First solution
def is_same_case(pair):
    char_1, char_2 = pair

    lower_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = lower_chars.upper()
    
    if char_1 in lower_chars and char_2 in lower_chars or char_1 in upper_chars and char_2 in upper_chars:
        return 1
    
    if char_1 in upper_chars and char_2 in lower_chars or char_1 in lower_chars and char_2 in upper_chars:
        return 0

    return -1

# Second solution
def is_same_case_2(pair):
    ch_1, ch_2 = pair

    if not ch_1.isalpha() or not ch_2.isalpha():
        return -1

    if ch_1.islower() != ch_2.islower():
        return 0

    if ch_1.islower() and ch_2.islower() or ch_1.isupper() and ch_2.isupper():
        return 1

# Third solution
def is_same_case_3(pair):
    c_1, c_2, = pair

    return int(c_1.isupper() == c_2.isupper()) if c_1.isalpha() and c_2.isalpha() else -1

# Fourth solution
def is_same_case_4(pair):
    a, b = pair

    return -1 * int((not(a + b).isalpha()) or not a.islower() ^ b.islower())


# Output
print(is_same_case(pair_1))
print(is_same_case(pair_2))
print(is_same_case(pair_3))
print(is_same_case(pair_4))
print(is_same_case(pair_5))
print(is_same_case(pair_6))
print(is_same_case(pair_7))

print(is_same_case_2(pair_1))
print(is_same_case_2(pair_2))
print(is_same_case_2(pair_3))
print(is_same_case_2(pair_4))
print(is_same_case_2(pair_5))
print(is_same_case_2(pair_6))
print(is_same_case_2(pair_7))

print(is_same_case_3(pair_1))
print(is_same_case_3(pair_2))
print(is_same_case_3(pair_3))
print(is_same_case_3(pair_4))
print(is_same_case_3(pair_5))
print(is_same_case_3(pair_6))
print(is_same_case_3(pair_7))

print(is_same_case_4(pair_1))
print(is_same_case_4(pair_2))
print(is_same_case_4(pair_3))
print(is_same_case_4(pair_4))
print(is_same_case_4(pair_5))
print(is_same_case_4(pair_6))
print(is_same_case_4(pair_7))