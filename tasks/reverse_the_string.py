'''
    Task:
        Reverse the String
'''

# Variables
string_1 = 'python'  # 'notyp'
string_2 = 'code'    # 'edoc'
string_3 = ''        # ''

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
print(reverse_string(string_1))
print(reverse_string(string_2))
print(reverse_string(string_3))

print(reverse_string_2(string_1))
print(reverse_string_2(string_2))
print(reverse_string_2(string_3))