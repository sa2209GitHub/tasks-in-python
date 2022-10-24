'''
    Task:
        Check Same Case
'''

# Variables
pair1 = ['z', 'o']  #  1
pair2 = ['W', 'G']  #  1
pair3 = ['f', 'A']  #  0
pair4 = ['K', 'w']  #  0
pair5 = ['a', '#']  # -1
pair6 = ['F', '3']  # -1
pair7 = ['@', '$']  # -1

# First solution
def is_same_case(pair):
    char1, char2 = pair

    lowerChars = 'abcdefghijklmnopqrstuvwxyz'
    upperChars = lowerChars.upper()
    
    if char1 in lowerChars and char2 in lowerChars or char1 in upperChars and char2 in upperChars:
        return 1
    
    if char1 in upperChars and char2 in lowerChars or char1 in lowerChars and char2 in upperChars:
        return 0

    return -1

# Second solution
def is_same_case_2(pair):
    ch1, ch2 = pair

    if not ch1.isalpha() or not ch2.isalpha():
        return -1

    if ch1.islower() != ch2.islower():
        return 0

    if ch1.islower() and ch2.islower() or ch1.isupper() and ch2.isupper():
        return 1

# Third solution
def is_same_case_3(pair):
    c1, c2, = pair

    return int(c1.isupper() == c2.isupper()) if c1.isalpha() and c2.isalpha() else -1

# Fourth solution
def is_same_case_4(pair):
    a, b = pair

    return -1 * int((not(a + b).isalpha()) or not a.islower() ^ b.islower())


# Output
print(is_same_case(pair1))
print(is_same_case(pair2))
print(is_same_case(pair3))
print(is_same_case(pair4))
print(is_same_case(pair5))
print(is_same_case(pair6))
print(is_same_case(pair7))

print(is_same_case_2(pair1))
print(is_same_case_2(pair2))
print(is_same_case_2(pair3))
print(is_same_case_2(pair4))
print(is_same_case_2(pair5))
print(is_same_case_2(pair6))
print(is_same_case_2(pair7))

print(is_same_case_3(pair1))
print(is_same_case_3(pair2))
print(is_same_case_3(pair3))
print(is_same_case_3(pair4))
print(is_same_case_3(pair5))
print(is_same_case_3(pair6))
print(is_same_case_3(pair7))

print(is_same_case_4(pair1))
print(is_same_case_4(pair2))
print(is_same_case_4(pair3))
print(is_same_case_4(pair4))
print(is_same_case_4(pair5))
print(is_same_case_4(pair6))
print(is_same_case_4(pair7))