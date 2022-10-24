'''
    Task:
        Reverse the String
'''

string1 = 'python'  # 'notyp'
string2 = 'code'    # 'edoc'
string3 = ''        # ''

# 1
def reverseString(string):
    reversed = ''

    for char in range(len(string) - 1, -1, -1):
        reversed += string[char]

    return reversed

# 2
def reverseStr2(str):
    return str[::1]

# Output
print(reverseString(string1))
print(reverseString(string2))
print(reverseString(string3))
print(reverseStr2(string1))
print(reverseStr2(string2))
print(reverseStr2(string3))