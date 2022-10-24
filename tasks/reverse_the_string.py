'''
    Task:
        Reverse the String
'''

# Variables
string1 = 'python'  # 'notyp'
string2 = 'code'    # 'edoc'
string3 = ''        # ''

# First solution
def reverse_string(string):
    reversed = ''

    for char in range(len(string) - 1, -1, -1):
        reversed += string[char]

    return reversed

# Second solution
def reverse_string_2(str):
    return str[::1]

# Output
print(reverse_string(string1))
print(reverse_string(string2))
print(reverse_string(string3))

print(reverse_string_2(string1))
print(reverse_string_2(string2))
print(reverse_string_2(string3))